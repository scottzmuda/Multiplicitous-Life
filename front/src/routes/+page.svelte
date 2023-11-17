<script>
  export let data;
  const { items } = data;
</script>

<article class="article-grid">
  <div class="top" style="text-align: center;">
    <h1>Multiplicitous</h1>
          <!--<nav>
              {% if "creator_id" in session %}
              <a class="nav-create" href="/l/create-living_thing">&#x2295;&#xFE00;</a>
              {% endif %}
          </nav>
          -->
  </div>
    {#each items as item (item.id)}
  <a class="content" href='../{item.time_s}'>
    <div class="content-image-container">
      <img class="content-image" src={`/i/${item.image}`} alt={item.image} />
    </div>
    <div class="content-name">{item.common_kinds[0]}
    </div>
  </a>
    {/each}
</article>

<svelte:head>
  <title>Multiplicitous</title>
  <meta name="description" content="Partial to life.">
  <meta property="og:title" content="Multiplicitous">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://multiplicitous.com/">
  <meta property="og:image" content="https://multiplicitous.com/icon.png">
  <link rel="stylesheet" href="/index.css">
  <link rel="stylesheet" href="/app.css">
</svelte:head>