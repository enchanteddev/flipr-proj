<script>
// @ts-nocheck

    import Companies from "./components/Companies.svelte";
    import MarketIndex from "./components/MarketIndex.svelte";
    import Signin from "./components/Signin.svelte";
    let page = 'index';
    let signedin = false;
    let username = '';
    const base_url = 'http://127.0.0.1:5000';
    const signin = (usrname, pwd) => {
      signedin = true;
      username = usrname;
      page = 'index'
    }

</script>
<svelte:head>
  <link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,400;0,700;1,400;1,700&display=swap" rel="stylesheet">
</svelte:head>
<div class="header">
  <div class="container">
    <div class="main">
        <div class="title">Helllo</div>
        <div class="right">
          <div class="link" on:click={() => {page = "index"}}>Index</div>
          <div class="link" on:click={() => {page = "companies"}}>Companies</div>
          <div class="link" on:click={() => {page = "signin"}}>{signedin ? `Sign Out ${username}` : "Sign In"}</div>
        </div>
    </div>

</div>
</div>
<div class="content">
  {#if page === 'index'}
  	<MarketIndex base_url = {base_url}/>
  {/if}
  
  {#if page === 'companies'}
    <Companies base_url = {base_url}/>
  {/if}

  {#if page === 'signin'}
    <Signin login = {signin}/>
  {/if}
</div>

<style>
  :root{
    --header-h: 13vh;
    --inline-margin: 2em;
  }
  .header{
    height: var(--header-h);
    position: fixed;
    z-index: 2;
    width: 100%;
    font-size: larger;
  }
  .content{
    display: grid;
    padding-top: var(--header-h);
    z-index: 1;
    place-items: center;
    height: 100%;
  }
  .container{
    height: 100%;
    display: grid;
    place-items: center;
  }
  .main{
      display: flex;
      width: 98%;
      background-color: aqua;
      height: 70%;
      border-radius: 2vh;
      place-items: center;
      position: relative;
  }
  .title{
      margin-left: var(--inline-margin);
  }
  .right{
      display: flex;
      position: absolute;
      right: var(--inline-margin);
  }
  .link{
      margin: 2em;
      cursor: pointer;
  }
  @media (max-width: 1350px) {
        .link{
            margin: 0.1em;
        }
        .link::after{
          content:  ' |';
        }
        :root{
          --inline-margin: 0.4em;
        }
    }
</style>