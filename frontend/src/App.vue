<script setup>
import { onMounted, ref } from "vue"
import BoatModal from './components/BoatModal.vue'
import SwimlaneColumn from './components/SwimlaneColumn.vue'
const swimlanes = ref(null)
const loading = ref(true)
const error = ref(null)
const showNewBoatModal = ref(false)

const fetchSwimlanes = () => {
  loading.value = true

  // fetch all swimlanes from backend
  return fetch(`${import.meta.env.VITE_API_BASE_URL}/swimlanes/`, {
    method: 'get',
    headers: {
      'content-type': 'application/json'
    }
  }).then( response => response.json() )
    .then( data => swimlanes.value = data )
    // suppress errors for now
    .catch( (error) => error.value = error )
    .then( () => loading.value = false )
}

const addNewBoat = (newBoat) => swimlanes.value[0].boats.push(newBoat)
onMounted(() => {
  fetchSwimlanes()
})
</script>

<template>
  <div v-if="loading" class="spinner-border text-light spinner" role="status"></div>
  <div v-if="!loading && swimlanes" class="container">
    <b-navbar dark="true" variant="dark">
      <a class="navbar-brand">EchoCatch Tours</a>
      <b-navbar-nav small="true">
        <b-nav-item>
          <b-button @click="showNewBoatModal = true" variant="success">
            New Boat <font-awesome-icon icon="fa-solid fa-plus" />
          </b-button>
        </b-nav-item>
      </b-navbar-nav>
    </b-navbar>
    <p></p>
    <div class="row">
      <swimlane-column v-for="(swimlane, index) in swimlanes" :key="swimlane.id" v-model:swimlane="swimlanes[index]"></swimlane-column>
    </div>
    <boat-modal v-model:showModal="showNewBoatModal" v-bind:boat="{ swimlane_id: swimlanes[0].id }" @update:boat="addNewBoat"></boat-modal>
  </div>
  <p v-if="error">
    error: {{ error }}
  </p>
</template>

<style scoped>
.navbar {
  --bs-navbar-padding-y: 0;
}
.spinner {
  display: block;
  position: fixed;
  z-index: 1031; /* High z-index so it is on top of the page */
  top: 50%;
  right: 50%; /* or: left: 50%; */
  margin-top: -..px; /* half of the elements height */
  margin-right: -..px; /* half of the elements width */
}
</style>
