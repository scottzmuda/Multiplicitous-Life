<script>
  export let data;
  const { item } = data;
</script>

<svelte:head>
  <title>{item.common_kinds[0]}</title>
  <meta name="description" content={item.note}>
  <link rel="stylesheet" href="/page.css">
</svelte:head>


<article class="article-grid" id="living_things">
    <div class="article-header">
        <nav>
            <a class="close-page" href="/">
                &#x2297;&#xFE00;
            </a>
        </nav>
        <h1>{item.common_kinds[0]}</h1>
    </div> 
    <div class="article-image">
        <img class="feature" src={`/i/${item.image}`} alt={item.image}>
    </div>
    <div class="top-right">
        <em>
          {#each item.formal_kinds as formal_kind}
                    {formal_kind}<br>
          {/each}
        </em>
    </div>
    <div class="bottom-left">
        <!--<em>
            {{living_thing.season}}<br>
            {{living_thing.sun_based_time}}<br>
            {{living_thing.natural_language_latitude}}<br>
        </em>-->
    </div>
    <div class="bottom-right">
        <div id="map"></div>
    </div>
    <div class="bottom">
        @{item.name_id}<br>
        <em>{item.note}</em>
    </div>
</article>