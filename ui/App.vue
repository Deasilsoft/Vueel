<template>
  <div id="app">
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <div class="container">
        <router-link to="/" class="navbar-brand">Home</router-link>
        <ul class="navbar-nav mr-auto">
          <li class="nav-item active">
            <router-link to="/" class="nav-link">Home <span class="sr-only">(current)</span></router-link>
          </li>
          <li class="nav-item">
            <router-link to="/about" class="nav-link">About</router-link>
          </li>
        </ul>
      </div>
    </nav>
    <div class="container">
      <breadcrumbs/>
      <router-view/>
    </div>
  </div>
</template>


<script>
import Breadcrumbs from "./components/Breadcrumbs.vue"

export default {
  components: {Breadcrumbs}
}
</script>

<style lang="scss">
@import "../resources/sass/main.scss";
</style>
