<script>
    import {location, querystring} from 'svelte-spa-router'
    let searchParams = new URLSearchParams($querystring);
    console.log(searchParams.get('code'))
</script>

<div>
    <p>code :{searchParams.get('code' )}</p>
</div>