<?php
function getData(){
    try{
        $dsn = 'sqlite:data/remo_data.db';
        $db = new PDO($dsn, "", "");
        # $db->setAttribute( PDO::ATTR_PERSISTENT, TRUE );
        $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        # $query = $db->prepare("SELECT time, te, hu FROM data_set LIMIT (SELECT COUNT(*) FROM data_set)-168, 168");
        $query = $db->prepare("SELECT time, te, hu FROM data_set LIMIT (SELECT COUNT(*) FROM data_set)");
        $query->execute();
        $result = $query->fetchAll();
        
        $len = count($result);
        $str = "";
        # for($i = $len - 1; 0 <= $i; $i--){ 
        for($i = 0; $i < $len; $i++){ 
        
            $str .= $result[$i]['time'].','.$result[$i]['te'].','.$result[$i]['hu'].'<br>';

        }
        echo $str;
        # echo $len;
    }catch(Exception $e){
        echo $e->getMessage();
    }
}
?>