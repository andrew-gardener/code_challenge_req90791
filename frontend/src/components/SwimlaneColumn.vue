<script setup>
import draggable from 'vuedraggable'
import BoatCard from './BoatCard.vue'
import { computed } from "vue"
const props = defineProps({
  swimlane: {
    required: true,
    type: Object,
  }
})
const emit = defineEmits(['update:swimlane'])
const swimlane = computed({
  get: () => props.swimlane,
  set: value => emit('update:swimlane', value)
})

const reorder = (event) => {
  if (event.added) {
    // update the order of the boats in the backend
    return fetch(`${import.meta.env.VITE_API_BASE_URL}/swimlanes/${swimlane.value.id}/boats/`, {
      method: 'post',
      headers: {
        'content-type': 'application/json'
      },
      body: JSON.stringify({
        boats: swimlane.value.boats.map( boat => boat.id ),
        touch: event.added.element.id,
      })
    }).then( response => response.json() )
      .then( data => swimlane.value = data )
      // suppress errors for now
      .catch( (error) => console.error(error) )
  }
}
const updateBoat = (boat, index) => {
  if (boat) {
    swimlane.value.boats[index] = boat
  } else {
    swimlane.value.boats.splice(index, 1)
  }
}
</script>

<template>
  <div class="col-sm">
    <div class="card border-dark mb-3 swimlane-column">
      <h5 class="card-header">{{ swimlane.name }}</h5>
      <div class="card-body">
        <div class="list-group">
          <draggable v-model="swimlane.boats" item-key="id" group="boats" @change="reorder" ghost-class="ghost-card">
            <template #item="{element, index}">
              <boat-card v-bind:boat="element" @update:boat="updateBoat($event, index)" class="cursor-move"></boat-card>
            </template>
          </draggable>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.swimlane-column {
  min-height: 10rem;
}
.ghost-card {
  opacity: 0.5;
}
.cursor-move {
  cursor: move;
}
</style>