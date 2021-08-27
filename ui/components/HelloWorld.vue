<template>
  <div class="hello">
    <h1>{{ message }}</h1>
    <form method="POST">
      <div class="row">
        <div class="col">
          <input type="text" v-model="input" class="form-control">
        </div>
        <div class="col-auto">
          <button @click="onClick" class="btn btn-primary">Send</button>
        </div>
      </div>
    </form>
    <div>{{ response }}</div>
  </div>
</template>

<script>
export default {
  name: "HelloWorld",
  data() {
    return {
      message: "",
      input: "",
      response: ""
    };
  },
  mounted() {
    eel.T("app.hello")(value => this.message = value);
  },
  methods: {
    onClick(e) {
      e.preventDefault();
      eel.communicate(this.input)(value => this.response = value);
    }
  }
}
</script>
