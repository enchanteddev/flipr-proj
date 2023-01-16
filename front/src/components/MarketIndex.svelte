<script>
    import ChangeIndicator from "./ChangeIndicator.svelte";
    import CurrentValue from "./CurrentValue.svelte";
    import RangeBar from "./RangeBar.svelte";
    import Chart from "chart.js/auto";
    import { onMount } from "svelte";

    export let base_url;

    let selected_index = 'nse';
    let selected_time = 'ytd';

    const indices = {
        nse: {name: 'NIFTY 50', code: 'INDEXNSE: NIFTY_50', value: 12425, change: 345},
        bse: {name: 'SENSEX', code: 'INDEXBOM: SENSEX', value: 12425, change: -312},
    }

    let returns = {
        ytd: 2,
        m1: 3.4,
        m3: 12.5,
        m6: 122,
        y1: 1039.32,
        y5: 232,
        y10: 232.23,
    }

    let last_update_at = Date.now();
    let readable_date = new Date(last_update_at).toLocaleString().toUpperCase();


    let ranges = [[0, 100], [0, 100]];
    let current = 0;
    let change = 0;
    let chartData = [[], []];
    let open = 0;
    let prevClose = 0;
    const get_data = (stockname) => {
        
        fetch(`${base_url}/maxmin/${stockname}:0`).then(r => r.json()).then(r => {
            ranges[0][0] = r.min;
            ranges[0][1] = r.max;
        })
        fetch(`${base_url}/maxmin/${stockname}:364`).then(r => r.json()).then(r => {
            ranges[1][0] = r.min;
            ranges[1][1] = r.max;
        })
        
        fetch(`${base_url}/close/${stockname}:1000`).then(r => r.json()).then(r => {
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
            prevClose = chartData[1][chartData[1].length - 2];
        })
    
        fetch(`${base_url}/openclose/${stockname}:0`).then(r => r.json()).then(r => {
            current = r.close;
            change = current - r.open;
            open = r.open;
        })
    }
    
    
    let myChart;
    $: get_data(selected_index);
    const chart = () => {
        console.log('chrting', chartData)
        const labels = chartData[0];
        const data = {
            labels: labels,
            datasets: [{
                label: 'INDEX VALUE',
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
    <select name="index-selector" id="ind" class="selector" bind:value={selected_index}>
        <option value="nse">NSE</option>
        <option value="bse">BSE</option>
    </select>
    <div class="title">
        {indices[selected_index].name}
    </div>
    <div class="subtitle">
        <div class="left">{indices[selected_index].code}</div>
        <div class="right">Last Updated: {readable_date}</div>
    </div>
    <div class="brk"></div>
    <div class="info">
        <CurrentValue value = {current} change = {change}/>
        <div class="ranges">
            <RangeBar name="Day Range" current = {current} max = {ranges[0][1]} min = {ranges[0][0]}/>
            <RangeBar name="52 Week Range" current = {current} max = {ranges[1][1]} min = {ranges[1][0]}/>
        </div>
        <div class="container">
            <div class="returns">
                Returns in 
                <select name="time-selector" id="return-time" class="selector" bind:value={selected_time}>
                    <option value="ytd">YTD</option>
                    <option value="m1">1 Month</option>
                    <option value="m3">3 Month</option>
                    <option value="m6">6 Month</option>
                    <option value="y1">1 Year</option>
                    <option value="y5">5 Year</option>
                    <option value="y10">10 Year</option>
                </select>
                = <ChangeIndicator change = {returns[selected_time]}/>
            </div>
            <div class="graph">
                <canvas id="graph"></canvas>
            </div>
        </div>
    </div>
    <div class="overview">
        <div class="overhead">Overview</div>
        <hr>
        <div class="overwrapper">

            <div class="overviewcontent">
                <div class="overviewitem">Open: <span class="overviewvalue">{open}</span></div>
                <div class="overviewitem">Previous Close: <span class="overviewvalue">{prevClose}</span></div>
                <div class="overviewitem">Day High: <span class="overviewvalue">{ranges[0][1]}</span></div>
                <div class="overviewitem">Day Low: <span class="overviewvalue">{ranges[0][0]}</span></div>
                <div class="overviewitem">52 Week High: <span class="overviewvalue">{ranges[1][1]}</span></div>
                <div class="overviewitem">52 Week Low: <span class="overviewvalue">{ranges[1][0]}</span></div>
            </div>
        </div>
    </div>

    <div class="moreinfo">
        
    </div>
</div>

<style>
    .main{
        width: 96%;
    }
    .selector{
        background-color: white;
        outline: none;
        border: 3px aqua solid;
        font-size: large;
        padding-inline: 1em;
    }
    .title{
        font-size: 50px;
    }
    .brk{
        width: 100%;
        height: 0.2em;
        background-color: black;
    }
    .subtitle{
        display: flex;
        position: relative;
    }
    .right{
        position: absolute;
        right: 0;
    }
    .info{
        display: flex;
        margin-top: 2em;
        place-items: center;
    }
    .ranges{
        margin-inline: 2em;
        display: grid;
        place-content: center;
        gap: 5vh;
    }
    .container{
        display: grid;
        place-items: center;
    }
    .ranges{
        margin-inline: 6vw;
    }
    
    .overviewcontent{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 0 10vw;
        width: 60%;
        font-size: x-large;
    }
    .overviewitem{
        position: relative;
        border: 3px dashed rgb(83, 83, 83);
        border-inline: 0px;
        border-top: 0px;
        margin-bottom: 10px;
    }
    .overviewvalue{
        position: absolute;
        right: 0;
    }
    .overwrapper{
        display: grid;
        place-items: center;
    }
    @media (max-width: 1350px) {
        .info{
            flex-direction: column;
        }
    }
    @media (max-width: 500px){
        .subtitle{
            display: block;
        }
    }

</style>
