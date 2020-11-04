<!DOCTYPE html>
<head>
    <title>Temperature and Humidity</title>
</head>
<html>
    <meta http-equiv="refresh" content="60" >
    <div class="container" style="width:90%; height:90%;">
        <canvas id="myChart"></canvas>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.7.2/Chart.bundle.js"></script>
    <body>
        <script type = "text/javascript">
            var data = '<?php
                include "./drawGraph.php";
                getData()
            ?>';
            data = data.split('<br>');
            // document.write(data)
            var time = new Array();
            var temperature = new Array();
            var humidity = new Array();
            
            
            for(i = 0; i < data.length; i++){
                values = data[i].split(",");
                time.push(values[0]);
                temperature.push(values[1]);
                humidity.push(values[2]);
            }
            var ctx = document.getElementById("myChart");
            ctx.width=window.innerWidth*0.5;
            ctx.height=window.innerHeight*0.5;
            
            // ar last = time.pop()
            // document.write(time.length - 1, time.pop());
            var myChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: time,
                    datasets:[
                        {
                            label : 'temperature',
                            data: temperature,
                            borderColor: "rgba(128,128,255,1)",
                            backgroundColor: "rgba(0,0,0,0)",
                            yAxisID:"y-axis1"
                        },
                        {
                            label : 'humidity',
                            data: humidity,
                            borderColor: "rgba(128,200,128,1)",
                            backgroundColor: "rgba(0,0,0,0)",
                            yAxisID:"y-axis2"
                        }
                    ]
                },
                options: {
                    title: {
                        display: true,
                        text: 'Temperature and humidity (last update : ' + time[time.length - 2]+ ')'
                    },
                    scales: {
                        yAxes: [
                            {
                                id: "y-axis1",
                                position: "left",
                                ticks: {
                                    fontColor:"blue",
                                    suggestedMax: 40,
                                    suggestedMin: 0,
                                    stepSize: 10,
                                    callback: function(value, index, values){
                                        return  value +  '℃'
                                    }
                                }
                            },
                            {
                                id: "y-axis2",
                                position: "right",
                                ticks: {
                                    fontColor:"green",
                                    suggestedMax: 100,
                                    suggestedMin: 0,
                                    stepSize: 10,
                                    callback: function(value, index, values){
                                        return  value +  '%'
                                    }
                                }
                            }
                        ]
                    }
                }
            });
            
        </script>
        <noscript> No running javascript </noscript>
    </body>
</html>