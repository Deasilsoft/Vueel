<template>
  <div>
    <div class="text-center">
      <img alt="Vue Logo" src="../../resources/images/vue-logo.png">
    </div>
    <HelloWorld/>
  </div>
</template>

<script>
import HelloWorld from "../components/HelloWorld.vue";

export default {
  name: "home",
  components: {
    HelloWorld
  },
  data() {
    return {
      breadcrumbs: [
        {
          active: true,
          link: "/",
          text: "Home"
        }
      ]
    };
  },
  mounted() {
    eel.T("app.home")(value => this.breadcrumbs[0].text = value);
  }
};
</script>
