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
                data: this.generateDayWiseTimeSeries(new Date('11 Feb 2017').getTime(), 185, {
                    min: 10,
                    max: 90
                })
            },
            {
                name: "Automate n°2",
                data: this.generateDayWiseTimeSeries(new Date('11 Feb 2017').getTime(), 185, {
                    min: 10,
                    max: 90
                })
            },
            {
                name: "Automate n°3",
                data: this.generateDayWiseTimeSeries(new Date('11 Feb 2017').getTime(), 185, {
                    min: 10,
                    max: 90
                })
            },
            {
                name: "Automate n°4",
                data: this.generateDayWiseTimeSeries(new Date('11 Feb 2017').getTime(), 185, {
                    min: 10,
                    max: 90
                })
            },
            {
                name: "Automate n°5",
                data: this.generateDayWiseTimeSeries(new Date('11 Feb 2017').getTime(), 185, {
                    min: 10,
                    max: 90
                })
            },
            {
                name: "Automate n°6",
                data: this.generateDayWiseTimeSeries(new Date('11 Feb 2017').getTime(), 185, {
                    min: 10,
                    max: 90
                })
            },
            {
                name: "Automate n°7",
                data: this.generateDayWiseTimeSeries(new Date('11 Feb 2017').getTime(), 185, {
                    min: 10,
                    max: 90
                })
            },
            {
                name: "Automate n°8",
                data: this.generateDayWiseTimeSeries(new Date('11 Feb 2017').getTime(), 185, {
                    min: 10,
                    max: 90
                })
            },
            {
                name: "Automate n°9",
                data: this.generateDayWiseTimeSeries(new Date('11 Feb 2017').getTime(), 185, {
                    min: 10,
                    max: 90
                })
            },
            {
                name: "Automate n°10",
                data: this.generateDayWiseTimeSeries(new Date('11 Feb 2017').getTime(), 185, {
                    min: 10,
                    max: 90
                })
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
                    min: new Date('19 Jun 2017').getTime(),
                    max: new Date('14 Aug 2017').getTime()
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
        }
    }
    },

    methods: {
        generateDayWiseTimeSeries: function (baseval, count, yrange) {
            var i = 0;
            var series = [];
            while (i < count) {
            var x = baseval;
            var y = Math.floor(Math.random() * (yrange.max - yrange.min + 1)) + yrange.min;

            series.push([x, y]);
            baseval += 86400000;
            i++;
            }

            console.log(series)
            return series;
        }
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
