<template>
    <div id="app">
      <div id="chart1">
        <apexchart type="line" height="230" :options="chartOptionsArea" :series="series" />
      </div>
      <div id="chart2">
        <apexchart type="area" height="130" :options="chartOptionsBrush" :series="series" />
      </div>
    </div>
</template>

<script>

import VueApexCharts from "vue-apexcharts";
import apiAutomate from '../api/automate';
import axios from 'axios';

export default {
    name: 'ChartBrush',
    components: {
        apexchart: VueApexCharts
    },
    data: function () {
    return {
        series: [
            {
                name: "Automate n°1",
                data: []
            },
            {
                name: "Automate n°2",
                data: []
            },
            {
                name: "Automate n°3",
                data: []
            },
            {
                name: "Automate n°4",
                data: []
            },
            {
                name: "Automate n°5",
                data: []
            },
            {
                name: "Automate n°6",
                data: []
            },
            {
                name: "Automate n°7",
                data: []
            },
            {
                name: "Automate n°8",
                data: []
            },
            {
                name: "Automate n°9",
                data: []
            },
            {
                name: "Automate n°10",
                data: []
            }
        ],
        chartOptionsArea: {
            legend: {
                position: "top",
                horizontalAlign: "left",
                offsetX: 25
            },
            yaxis: [
                {
                axisTicks: {
                    show: true
                },
                axisBorder: {
                    show: false,
                    color: "#1E74FF"
                },
                labels: {
                    style: {
                    color: "#1E74FF"
                    }
                },
                title: {
                    text: "Degrés Celsius (°C)",
                    style: {
                    color: "#1E74FF"
                    }
                },
                tooltip: {
                    enabled: true
                }
            }
            ],
            chart: {
                id: 'chartArea',
                toolbar: {
                    tools: {
                        download: true,
                        selection: true,
                        zoom: true,
                        zoomin: true,
                        zoomout: true,
                        pan: true,
                    },
                    autoSelected: 'pan',
                    show: true,
                    offsetX: 25
                }
            },
            colors: ['#F23D5E', '#F23D5E', '#0477BF', '#0477BF', '#049DD9', '#049DD9', '#F2C335', '#F2C335', '#F2856D', '#F2856D'],
            stroke: {
                width: 2,
                curve: 'smooth'
            },
            dataLabels: {
                enabled: false
            },
            fill: {
                opacity: 1,
            },
            markers: {
                size: 0
            },
            xaxis: {
                type: 'datetime'
            }
        },
        chartOptionsBrush: {
            legend: {
                position: "top",
                horizontalAlign: "left",
                offsetX: 25
            },
            chart: {
                id: 'chartBrush',
                brush: {
                target: 'chartArea',
                enabled: true
                },
                selection: {
                enabled: true,
                xaxis: {
                    min: new Date().setHours(new Date().getHours() - 1 ),
                    max: new Date().getTime()
                }
                },
            },
            colors: ['#F23D5E', '#F23D5E', '#0477BF', '#0477BF', '#049DD9', '#049DD9', '#F2C335', '#F2C335', '#F2856D', '#F2856D'],
            stroke: {
                width: 2,
                curve: 'smooth'
            },
            fill: {
                type: 'gradient',
                gradient: {
                opacityFrom: 0.91,
                opacityTo: 0.1,
                }
            },
            xaxis: {                
                min: new Date().setHours(new Date().getHours() - 4 ),
                max: new Date().getTime(),
                type: 'datetime',
                tooltip: {
                    enabled: false
                }
            },
            yaxis: [
                {
                axisTicks: {
                    show: true
                },
                tickAmount: 2,
                axisBorder: {
                    show: false,
                    color: "#1E74FF"
                },
                labels: {
                    style: {
                    color: "#1E74FF"
                    }
                },
                title: {
                    text: "(°C)",
                    style: {
                    color: "#1E74FF"
                    }
                },
                tooltip: {
                    enabled: true
                }
            }]
        },
        
    }
    },

    methods: {
        getData() {
            let url = 'http://localhost:3000/automates/get'
            axios.get(url).then(res=>{
                res.data.forEach(element => {
                    this.series[element.automate_number - 1].data.push([new Date(element.timestamp).getTime() / 1000, element.temp_cuve])
                });
                console.log(this.series)
            })
        }
    },
    mounted() {
        this.getData();
        let currentTime = new Date().getTime();
        console.log(currentTime);
        console.log(new Date().setHours(new Date().getHours() - 1 ));
    }
}

</script>

<style>
.svg_select_points_l, .svg_select_points_r {
    fill: #1e74ff !important;
}
.apexcharts-selection-rect{
    fill: #1e74ff !important;
    stroke: #1e74ff !important;
    opacity: 1 !important;
    fill-opacity: 0.4 !important;
}
.apexcharts-toolbar {
    top: -30px;
}
.con-vs-tabs, .con-vs-tabs .con-slot-tabs {
    overflow: visible !important;
}
</style>
