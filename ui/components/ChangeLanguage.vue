<template>
  <div>
    <form method="POST">
      <b-row>
        <b-col>
          <b-form-select v-model="locale">
            <b-form-select-option value="en">English</b-form-select-option>
            <b-form-select-option value="no">Norsk</b-form-select-option>
          </b-form-select>
        </b-col>
        <b-col cols="auto">
          <b-button type="submit" variant="primary" @click="onClick">{{ button_text }}</b-button>
        </b-col>
      </b-row>
    </form>
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
      locale: "",
      button_text: "",
    };
  },

  async mounted()
  {
    this.locale      = await this.C("language");
    this.button_text = await this.T("app.change language");
  },

  methods: {
    onClick(e)
    {
      e.preventDefault();

      window.eel.change_language(this.locale)();

      location.reload();
    }
  }
};
</script>
