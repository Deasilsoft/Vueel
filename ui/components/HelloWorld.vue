<template>
  <div class="hello">
    <h1>{{ this.message }}</h1>
    <form method="POST">
      <div class="row">
        <div class="col">
          <input type="text" v-model="inputValue" class="form-control">
        </div>
        <div class="col-auto">
          <button @click="onClick" class="btn btn-primary">Send</button>
        </div>
      </div>
    </form>
    <div>
      {{ response }}
    </div>
  </div>
</template>

<script>
export default {
  name: "HelloWorld",
  data: function () {
    return {
      message: "",
      inputValue: "",
      response: ""
    }
  },
  mounted: function () {
    eel.hello_world_python()(value => {
      this.message = value
    })
  },
  methods: {
    onClick(e) {
      e.preventDefault();

      eel.print_string(this.inputValue)(value => {
        this.response = value
      })
    }
  }
}
</script>
