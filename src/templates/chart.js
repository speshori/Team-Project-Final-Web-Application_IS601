var obj;
fetch('/chart/dataset').then(res => res.json()).then(data => obj = data);
console.log(obj);
const mean = obj.mean;
const median = obj.median;
const mode = obj.mode;
const ctx = document.getElementById('chart').getContext('2d');
const chart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['mean', 'median', 'mode'],
        datasets: [{
            label: 'Mean, Median, and Mode',
            data: [mean, median, mode],
            backgroundColor: [
                'red',
                'green',
                'blue'
            ],
            borderColor: [
                'red',
                'green',
                'blue'
            ],
            borderWidth: 0.5
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});