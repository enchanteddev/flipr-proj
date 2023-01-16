<script>
    import ChangeIndicator from "./ChangeIndicator.svelte";

    export let value;
    export let change;
    $:{
        console.log(value, change > 0)
    }
</script>

<div class="current-value">
    <div class="value">{value}</div>
    <div class="change">
        <ChangeIndicator change = {change} value = {value}/>
    </div>
</div>

<style>
    .change{
        font-size: larger;
    }
    .value{
        font-size: 80px;
    }
</style>