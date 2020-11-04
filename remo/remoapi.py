# -*- coding: utf-8 -*-
import subprocess
import json
import sqlite3
import configparser
import os
import pytz

class Remo:
    def __init__(self, path_config="config.ini"):
        if not os.path.exists(path_config):
            self.initConfig(path_config)
        else:
            self.config = configparser.ConfigParser()
            self.config.read(path_config)
            self.timezone = pytz.timezone('Asia/Tokyo')

        if not os.path.exists("./web/data/"):
            os.makedirs("./web/data/")
    
    def getConfig(self):
        return self.config


    def initConfig(self, path_config):
        config = configparser.ConfigParser()

        config.add_section('info')
        config.set('info', 'remo', "token_remo")
        config.set('info', 'discord', "token_discord")
        config.set('info', 'channel', "channel_id")
        config.set('info', 'database', "./web/data/remo_data.db")
        config.set('info', 'timezone', "Asia/Tokyo")
        config.set('info', 'second', "3600")

        with open(path_config, 'w') as file:
            config.write(file)
        
        print("Config file doesn't exist. Please fill information to " + path_config)
        exit(1)


    def get_value(self):
        """
        Get the environment data of home from Nature Remo Web API
        """
        result = subprocess.run(['curl -s -X GET "https://api.nature.global/1/devices" -H "accept: application/json" -k --header "Authorization: Bearer ' + self.config.get('info', 'remo')+ '"'], stdout=subprocess.PIPE, shell=True)
        return result.stdout.decode('utf8')


    def get_message(self, time, save=False):
        """
        Get the message
        """

        value = json.loads(self.get_value())
        events = value[0]['newest_events']
        
        name = value[0]['name']
        temperature = events['te']['val']
        humidity = events['hu']['val']
        illumination = events['il']['val']
        
        if save:
            self._save_values(name, time, temperature, humidity, illumination)
        
        msg = '現在({0})の{1}は\n気温{2:.1f}°C 湿度{3:.0f}%です'.format(time, name, temperature, humidity)
        
        return msg


    def _save_values(self, name, time, temperature, humidity, illumination):
        """
        Save the values to the database
        """
        with sqlite3.connect(self.config.get('info', 'database')) as con:
            cursor = con.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS data_set(name, time, te, hu, il)")

            command = "INSERT INTO data_set VALUES(?, ?, ?, ?, ?)"
            cursor.execute(command, (name, time, temperature, humidity, illumination))
            con.commit()


def main():
    """
    main function
    """
    remo = Remo()
    print(remo.get_message(True))

if __name__ == '__main__':
    main()
