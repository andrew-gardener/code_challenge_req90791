<script setup>
import BoatForm from './BoatForm.vue'
import { computed } from "vue"
const props = defineProps({
  boat: {
    required: true,
    type: Object,
  },
  showModal: {
    required: true,
    type: Boolean,
  }
})
const emit = defineEmits(['update:boat', 'update:showModal'])
const boat = computed({
  get: () => props.boat,
  set: value => emit('update:boat', value)
})
const showModal = computed({
  get: () => props.showModal,
  set: value => emit('update:showModal', value)
})
const isNew = boat.value.id === undefined
const title = isNew ? 'Add new boat' : `Update ${boat.value.name}`
</script>

<template>
  <b-modal v-model="showModal" :title="title" hideFooter="true">
    <boat-form v-if="showModal" v-model:boat="boat" @completed="showModal = false"></boat-form>
  </b-modal>
</template>

<style scoped>
</style>