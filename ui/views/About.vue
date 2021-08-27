<template>
  <div class="py-5">
    <h1>{{ about }}</h1>
  </div>
</template>

<script>
export default {
  name: "about",
  data() {
    return {
      about: "",
      breadcrumbs: [
        {
          active: false,
          link: "/",
          text: "Home"
        },
        {
          active: true,
          link: "/about",
          text: "About"
        }
      ]
    };
  },
  mounted() {
    eel.T("app.home")(value => this.breadcrumbs[0].text = value);
    eel.T("app.about")(value => this.breadcrumbs[1].text = value);
    eel.T("app.about message")(value => this.about = value);
  }
};
</script>
