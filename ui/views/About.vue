<template>
  <div class="py-5">
    <h1>{{ about }}</h1>
  </div>
</template>

<script>
import Vueel from "../mixins/Vueel";

export default {
  mixins: [
    Vueel
  ],
  data() {
    return {
      about: "",
    };
  },
  async mounted() {
    this.about = await this.T("app.about message");
  }
};
</script>
