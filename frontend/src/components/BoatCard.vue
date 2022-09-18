<script setup>
import BoatModal from './BoatModal.vue'
import { ref, computed } from "vue"
const props = defineProps({
  boat: {
    required: true,
    type: Object,
  }
})
const emit = defineEmits(['update:boat'])
const boat = computed({
  get: () => props.boat,
  set: value => emit('update:boat', value)
})
const showEditBoatModal = ref(false)
const showDeleteBoatConfirm = ref(false)

const removeBoat = () => {
  return fetch(`${import.meta.env.VITE_API_BASE_URL}/boats/${boat.value.id}/`, {
    method: 'delete',
  }).then( data => boat.value = undefined )
    // suppress errors for now
    .catch( (error) => console.error(error) )
}
const onSubmit = (event) => {
  event.preventDefault()
  saveBoat()
}
</script>

<template>
  <div>
    <div class="list-group-item list-group-item-action">
      <div class="d-flex justify-content-between align-items-center">
        <h6 class="mb-1">{{ boat.name }}</h6>
        <b-dropdown right size="sm" variant="secondary" no-caret>
          <template #button-content>
            <font-awesome-icon icon="fa-solid fa-bars" />
          </template>
          <b-dropdown-item-button @click="showEditBoatModal = true">Update</b-dropdown-item-button>
          <b-dropdown-divider></b-dropdown-divider>
          <b-dropdown-item-button variant="danger" @click="showDeleteBoatConfirm = true">Remove</b-dropdown-item-button>
        </b-dropdown>
      </div>
      <small class="text-muted">
        updated <timeago :datetime="boat.modified" :autoUpdate="true"/>
      </small>
    </div>
    <boat-modal v-model:showModal="showEditBoatModal" v-model:boat="boat"></boat-modal>
    <b-modal
      v-model="showDeleteBoatConfirm"
      title="Are you sure?"
      ok-title="Remove"
      ok-variant="danger"
      @ok="removeBoat"
      body-class="p-0"
      hide-header-close="true"
      size="sm"
    ></b-modal>
  </div>
</template>

<style scoped>
</style>
