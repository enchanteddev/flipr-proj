<script>
    import { Chart } from "chart.js";
    import { onMount } from "svelte";

    export let base_url;

    let selected_company = 'RELIANCE';
    let time_frame = 1
    const time_frames = [{name: 'D', days: 1}, 
                        {name: 'W', days: 7}, 
                        {name: 'M1', days: 30}, 
                        {name: 'M3', days: 90}, 
                        {name: 'M6', days: 180}, 
                        {name: 'Y', days: 365}, 
                        {name: 'MAX', days: 10000}]
    let chartData = [[], []];

    const get_data = (selected_company, time_frame) => {
        fetch(`${base_url}/close/${selected_company}:${time_frames[time_frame].days}`).then(r => r.json()).then(r => {
            while(chartData[0].length > 0) {
                chartData[0].pop();
            }
            while(chartData[1].length > 0) {
                chartData[1].pop();
            }
            r.forEach(element => {

                chartData[0].push(element.date.slice(4, 16));
                chartData[1].push(element.close);
            });
            console.log(chartData, r.json)
            try{
                myChart.update();
                console.log('hi')
            }
            catch(e){chart();console.log('e', e)}
            })
    }
    let myChart;
    $: get_data(selected_company, time_frame);
    const chart = () => {
        console.log('chrting', chartData)
        const labels = chartData[0];
        const data = {
            labels: labels,
            datasets: [{
                label: 'Share Price',
                data: chartData[1],
                fill: false,
                borderColor: 'rgb(75, 192, 192)',
                tension: 0.1
            }]
        };
        myChart = new Chart(document.getElementById("graph"), {
            type: 'line',
        data: data,
        options: {
            scales: {
                x: {
                    ticks: {
                        maxRotation: 0,
                    }
                }
            }
        }
    });}
    
    
    onMount(() => {
        document.getElementById("graph").width = Math.max(400, document.body.clientWidth * 0.35);
        document.getElementById("graph").height = 200;
        
        //chart();
    });
</script>
<div class="main">
    <div class="input">
        <select name="company-selector" id="com" class="selector" bind:value={selected_company}>
            <option value="ASHOKLEY">ASHOKLEY</option>
            <option value="CIPLA">CIPLA</option>
            <option value="EICHERMOT">EICHERMOT</option>
            <option value="RELIANCE">RELIANCE</option>
            <option value="TATASTEEL">TATASTEEL</option>
        </select>
        <div class="time-input">
            <select name="time-selector" id="time" class="selector" bind:value={time_frame}>
            {#each time_frames as time_, i}
                <option value="{i}">{time_.name}</option>
            {/each}
        </div>
        
    </div>
    <div class="graph">
        <canvas id="graph"></canvas>
    </div>
</div>

<style>
    .main{
        width: 96%
    }
    .input{
        display: flex;
        width: 100%;
    }
    .selector{
        background-color: white;
        outline: none;
        border: 3px aqua solid;
        font-size: large;
        padding-inline: 1em;
        margin-right: 1em;
    }
    .time-input{
        display: grid;
        grid-template-columns: 1fr 1fr 1fr 1fr 1fr 1fr 1fr;
        gap: 1em;
    }
</style>