<template>
  <div>
    <div class="py-5">
      <h1>{{ about }}</h1>
    </div>
    <ChangeLanguage/>
  </div>
</template>

<script>
import Vueel          from "../mixins/Vueel";
import ChangeLanguage from "../components/ChangeLanguage";

export default {
  components: {
    ChangeLanguage
  },

  mixins: [
    Vueel
  ],

  data()
  {
    return {
      about: "",
    };
  },

  async mounted()
  {
    this.about = await this.T("app.about message");
  }
};
</script>
