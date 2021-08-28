<template>
  <div>
    <h1>{{ hello }}</h1>
    <form method="POST">
      <b-row>
        <b-col>
          <b-form-input trim v-model="input"/>
        </b-col>
        <b-col cols="auto">
          <b-button type="submit" variant="primary" @click="onClick">{{ send }}</b-button>
        </b-col>
      </b-row>
    </form>
    <div>{{ response }}</div>
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
      hello: "",
      send: "",
      input: "",
      response: ""
    };
  },
  async mounted() {
    this.hello = await this.T("app.hello");
    this.send = await this.T("app.send");
  },
  methods: {
    onClick(e) {
      e.preventDefault();
      eel.communicate(this.input)(value => this.response = value);
    }
  }
};
</script>
