<script setup>
import { ref, computed } from "vue"
const props = defineProps({
  boat: {
    required: true,
    type: Object,
  }
})
const emit = defineEmits(['update:boat', 'completed'])
const boat = computed({
  get: () => props.boat,
  set: value => emit('update:boat', value)
})
const isNew = boat.value.id === undefined
const submitButton = isNew ? 'Create' : 'Update'
const formUrl = `${import.meta.env.VITE_API_BASE_URL}/boats/` + (isNew ? '' : `${boat.value.id}/`)
const formMethod =  isNew ? 'post' : 'put'

const form = ref({
  name: boat.value.name || '',
})

const saveBoat = () => {
  return fetch(formUrl, {
    method: formMethod,
    headers: {
      'content-type': 'application/json'
    },
    body: JSON.stringify({
      ...boat.value,
      ...form.value,
    })
  }).then( response => response.json() )
    .then( data => boat.value = data )
    // suppress errors for now
    .catch( (error) => console.error(error) )
    .then( () => emit('completed') )
}
const onSubmit = (event) => {
  event.preventDefault()
  saveBoat()
}
</script>

<template>
  <b-form @submit="onSubmit">
    <b-form-group label="Name:" label-for="name">
      <b-form-input id="name" v-model="form.name" placeholder="Enter name" required></b-form-input>
    </b-form-group>
    <b-button type="submit" variant="primary">{{ submitButton }}</b-button>
  </b-form>
</template>

<style scoped>
</style>