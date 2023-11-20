<template>
  <div>
    <h1>SignUp</h1>
    <form @submit.prevent="signUp">
      <div>
        <input type="text" v-model.trim="username">
      </div>
      <div>
        <input type="password" v-model.trim="password1">
      </div>
      <div>
        <input type="password" v-model.trim="password2">
      </div>
      <input type="submit">

    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()

const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)

const signUp = function () {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
  }
  store.signUp(payload)
}
</script>

<style>

</style>
