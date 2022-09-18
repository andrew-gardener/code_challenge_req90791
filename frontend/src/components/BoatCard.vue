<script setup>
const props = defineProps({
  boat: {
    required: true,
    type: Object,
  }
})
</script>

<template>
  <div class="list-group-item list-group-item-action">
    <div class="d-flex justify-content-between align-items-center">
      <h6 class="mb-1">{{ boat.name }}</h6>
      <b-button @click="" size="sm" variant="success">
        <font-awesome-icon icon="fa-solid fa-plus" />
      </b-button>
    </div>
    <small class="text-muted">
      updated <timeago :datetime="boat.modified" :autoUpdate="true"/>
    </small>
  </div>
</template>

<style scoped>
</style>
