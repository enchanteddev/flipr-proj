<script>
    export let change;
    export let value = 100;
</script>

<div class={"change " + (change >= 0 ? "plus": "minus")}>
    {change > 0 ? "▲ +": "▼ "}{(change.toFixed(2))} ({(change * 100 / value).toFixed(2)}%)
</div>

<style>
    .change{
        font-size: inherit;
        display: inline;
    }
    .plus{
        color: green;
    }
    .minus{
        color: red;
    }
</style>