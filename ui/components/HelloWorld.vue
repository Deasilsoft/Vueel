<template>
  <div>
    <h1>{{ hello_text }}</h1>
    <form method="POST">
      <b-row>
        <b-col>
          <b-form-input trim v-model="input"/>
        </b-col>
        <b-col cols="auto">
          <b-button type="submit" variant="primary" @click="onClick">{{ button_text }}</b-button>
        </b-col>
      </b-row>
    </form>
    <div>{{ response_text }}</div>
  </div>
</template>

<script>
import Vueel from "../mixins/Vueel";

export default {
  mixins: [
    Vueel
  ],

  data()
  {
    return {
      hello_text: "",
      button_text: "",
      response_text: "",
      input: "",
      timeout: null,
    };
  },

  async mounted()
  {
    this.hello_text  = await this.T("app.hello");
    this.button_text = await this.T("app.send");
  },

  methods: {
    onClick(e)
    {
      e.preventDefault();

      window.eel.communicate(this.input)(value => this.response_text = value);

      if (this.timeout !== null)
      {
        clearTimeout(this.timeout);
      }

      this.timeout = setTimeout(() => this.response_text = "", 5000);
    }
  }
};
</script>
