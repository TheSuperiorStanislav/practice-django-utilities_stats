$('document').ready(() => {
    $(".nav-item:first-child .nav-link").toggleClass("active")
    $(".tab-pane:first-child").toggleClass("active")
    $(".tab-pane:first-child").toggleClass("fade")

    const months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
        ]

    const capitalize = (s) => {
        return s[0].toUpperCase() + s.slice(1);
    }

    const normalizeField = (field) => {
        return capitalize(field.replace(/_/g, ' ').replace('hws', 'HWS'))
    }

    const drawGraph = (ctx, data) => {
        new Chart(ctx, {
            type: 'line',
            data: { 
                labels: months,
                datasets: [{
                    label: normalizeField(field),
                    data: data,
                    borderColor: '#FFF',
                    backgroundColor: 'rgba(0,102,204,0.25)',
                    fill: true,
                }],
            },
            options: {
                responsive: true,
                tooltips: {
                    mode: 'index',
                    intersect: false,
                    callbacks: {
                        label: function(tooltipItem, data) {
                            const value = tooltipItem.yLabel
                            if (value == 0){
                                return "No data"
                            }
                            var label = data.datasets[tooltipItem.datasetIndex].label || '';

                            if (label) {
                                label += ': ';
                            }
                            label += Math.round(value * 100) / 100;
                            return label;
                        }
                    }
                },
                hover: {
                    mode: 'nearest',
                    intersect: true
                },
                scales: {
                    xAxes: [{
                        display: true,
                        scaleLabel: {
                            display: true,
                            labelString: 'Month'
                        },
                        ticks: {
                            min: 1,
                            max: 12,
                        }
            
                    }],
                    yAxes: [{
                        display: true,
                        ticks: {
                            suggestedMin: 0,
                        }
                    }]
                }
            },
        })
    }

    let drawFieldGraph = (field, data) => {
        return new Promise ((resolve, reject) => {
            for (year in data){
                values = data[year]["values"]
                var graphItems = new Array(12).fill(0) 
                for (var key in data[year]["values"]){
                    graphItems[values[key][0] - 1] = values[key][1]

                }
                var ctx = document.getElementById(`${field}_${year}_visualization`).getContext('2d')
                drawGraph(ctx, graphItems)
            }
        })
    }

    const promiseArray = []
    for (var field in stat_data) {
        promiseArray.push(drawFieldGraph(field,stat_data[field]))
    }
    const drawGraphs = async() => {
        await Promise.all(promiseArray)
    }
    drawGraphs()
})