<script>
    export let login;

    let username = '';
    let password = '';
    const login_ = () => {
        login(username, password)
    }
</script>

<div class="wrapper">
    <div class="main">
    <div class="heading">
        <div class="title">LOG IN</div>
    </div>
    <div class="prompt">
        <form on:submit|preventDefault={login_}>
            <div class="label">Username</div>
            <input type="username" id="username" name="username" class="input" bind:value={username}>
            <div class="label">Password</div>
            <input type="password" id="pwd" name="pwd" minlength="8" class="input" bind:value={password}><br><br>
            <input type="submit">
        </form>
    </div>
</div>

</div>

<style>
    .wrapper{
        width: 100%;
        height: 100%;
        display: grid;
        place-items: center;
    }
    .main{
        padding: 1em;
        border-radius: 2vh;
        background: #011CFF;
/* Created with https://www.css-gradient.com */
background: #01B5FF;
background: -webkit-linear-gradient(top, #01B5FF, #01FFF9);
background: -moz-linear-gradient(top, #01B5FF, #01FFF9);
background: linear-gradient(to bottom, #01B5FF, #01FFF9);
        width: 40%;
        margin-top: 20vh;
    }
    .prompt{
        row-gap: 1em;
    }
    .heading{
        height: 10em;
        position: relative;
    }
    .title{
        position: absolute;
        bottom: 0;
        font-size: 60px;
    }
    .input{
        width: 100%;
        font-size: xx-large;
    }

    @media (max-width: 500px) {
        .main{
            width: 90%;
        }
    }
</style>