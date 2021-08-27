<template>
  <div id="app" class="d-flex flex-column justify-content-between min-vh-100">
    <div id="from-the-top">
      <header>
        <nav class="navbar navbar-expand navbar-light bg-light mb-2">
          <div class="container">
            <router-link to="/" class="navbar-brand">Vueel</router-link>
            <ul class="navbar-nav mr-auto">
              <li v-for="link in navigation.links" v-bind:class="link.class">
                <router-link v-bind:to="link.link" class="nav-link">
                  <span>{{ link.text }}</span>
                  <span v-if="link.active" class="sr-only">(current)</span>
                </router-link>
              </li>
            </ul>
          </div>
        </nav>
        <breadcrumbs :breadcrumbs="breadcrumbs"/>
      </header>
      <main class="container mb-2">
        <router-view/>
      </main>
    </div>
    <div id="from-the-bottom">
      <footer class="bg-light p-5">
        <div class="container">
          <span>Copyright &copy; Vueel {{ year }}</span>
        </div>
      </footer>
    </div>
  </div>
</template>


<script>
import Breadcrumbs from "./components/Breadcrumbs.vue"

export default {
  components: {
    Breadcrumbs
  },
  data() {
    return {
      year: new Date().getFullYear(),
      breadcrumbs: Array,
      navigation: {
        classes: {
          active: "nav-item active",
          default: "nav-item"
        },
        links: [
          {
            active: true,
            link: "/",
            text: "Home"
          },
          {
            active: false,
            link: "/about",
            text: "About"
          }
        ]
      }
    };
  },
  beforeCreate() {
    eel.C("language")(value => document.documentElement.setAttribute("lang", value));
  },
  mounted() {
    eel.T("app.home")(value => this.navigation.links[0].text = value);
    eel.T("app.about")(value => this.navigation.links[1].text = value);
  },
  methods: {
    loadBreadcrumbs() {
      // TODO: load current view's breadcrumbs
    },
    onNavigation() {
      // TODO: fix active link
    }
  }
}
</script>

<style lang="scss">
@import "../resources/sass/main.scss";
</style>
