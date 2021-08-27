<template>
  <nav v-if="breadcrumbs.length > 0" class="container" aria-label="breadcrumb">
    <ol class="breadcrumb bg-light">
      <li v-for="breadcrumb in breadcrumbs" v-if="!breadcrumb.active" class="breadcrumb-item">
        <router-link v-bind:to="breadcrumb.link">{{ breadcrumb.text }}</router-link>
      </li>
      <li v-for="breadcrumb in breadcrumbs" v-if="breadcrumb.active" class="breadcrumb-item active" aria-current="page">{{ breadcrumb.text }}</li>
    </ol>
  </nav>
</template>

<script>
export default {
  data() {
    return {
      breadcrumbs: Array
    };
  }
}
</script>
