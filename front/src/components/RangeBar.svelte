<script>
    export let name;
    export let max;
    export let min;
    export let current;
</script>

<div class="main">
    <div class="legend">
        <span class="l">L</span>
        <span class="title">{name}</span>
        <span class="h">H</span>
    </div>
    <div class="bar" style={`--pos: ${(current - min) / (max - min)}`}></div>
    <div class="values">
        <span class="min">{min}</span>
        <span class="max">{max}</span>
    </div>
</div>

<style>
    :root{
        --bar-w: 35vw;
        --bar-h: 1em;
        --pointer-w: .1em;
    }
    .legend{
        display: grid;
        justify-content: space-between;
        grid-template-columns: 1fr 1fr 1fr;
    }
    .bar{
        height: var(--bar-h);
        width: var(--bar-w);
        background-color: rgb(151, 238, 255);
        position: relative;
    }
    .title{
        text-align: center;
    }
    .h{
        text-align: right;
    }
    .bar::before{
        display: block;
        content: " ";
        position: absolute;
        left: calc(var(--bar-w) * var(--pos) - var(--pointer-w) / 2);
        height: calc(var(--bar-h));
        width: var(--pointer-w);
        background-color: black;
    }
    .values{
        display: grid;
        justify-content: space-between;
        grid-template-columns: 1fr 1fr;
    }
    .max{
        text-align: right;
    }
    @media (max-width: 1350px) {
        .bar{
            --bar-w: 20em;
        }
    }
</style>