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
        series: [{
        data: this.generateDayWiseTimeSeries(new Date('11 Feb 2017').getTime(), 185, {
            min: 30,
            max: 90
            })
        }],
        chartOptionsArea: {
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
                show: false
            }
        },
        colors: ['#546E7A'],
        stroke: {
            width: 3
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
        colors: ['#008FFB'],
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
        yaxis: {
            tickAmount: 2
        }
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

