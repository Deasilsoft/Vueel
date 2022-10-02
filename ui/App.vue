<template>
  <div id="app" class="d-flex flex-column justify-content-between min-vh-100">
    <div id="from-the-top">
      <header>
        <b-navbar type="light" variant="light" class="mb-2">
          <b-container>
            <b-navbar-brand to="/home">{{ title }}</b-navbar-brand>
            <b-navbar-nav class="mr-auto">
              <b-nav-item v-for="item in navigation" :key="item.order" :to="item.path">
                <span>{{ item.text }}</span>
              </b-nav-item>
            </b-navbar-nav>
          </b-container>
        </b-navbar>
        <b-container v-if="breadcrumbs.length > 0">
          <b-breadcrumb :items="breadcrumbs" class="bg-light mb-2"/>
        </b-container>
      </header>
      <b-container tag="main" class="mb-2">
        <router-view/>
      </b-container>
    </div>
    <div id="from-the-bottom">
      <footer class="bg-light p-5">
        <b-container>
          <span>Copyright &copy; Vueel {{ year }}</span>
        </b-container>
      </footer>
    </div>
  </div>
</template>

<script>
import Breadcrumbs from "./mixins/Breadcrumbs.js"
import Vueel       from "./mixins/Vueel";

export default {
  mixins: [
    Vueel,
    Breadcrumbs
  ],

  data()
  {
    return {
      title: "",
      year: new Date().getFullYear(),
      navigation: []
    };
  },

  async mounted()
  {
    // SET LANG IN HTML
    document.documentElement.setAttribute("lang", await this.C("language"));

    this.title = await this.T("app.vueel");

    // ADD NAVIGATION LINKS
    for (const route of this.$router.options.routes.filter(route => route.navigation.show))
    {
      this.navigation.push({
        order: route.navigation.order,
        text: await this.T("app." + route.name),
        path: route.path,
      });
    }
  },

  watch: {
    $route(to, from)
    {
      // CLEAR OLD BREADCRUMBS
      this.clearBreadcrumbs();

      // ADD BREADCRUMB LINKS
      for (const breadcrumb of this.$router.options.routes.find(route => route.name === to.name).breadcrumbs)
      {
        this.addBreadcrumb(breadcrumb);
      }
    }
  }
};
</script>

<style lang="scss">
@import "../resources/sass/main.scss";
</style>
