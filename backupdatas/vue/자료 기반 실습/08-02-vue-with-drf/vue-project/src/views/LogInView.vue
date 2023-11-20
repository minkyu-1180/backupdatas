<template>
  <div>
    <h1>LogIn</h1>
    <form @submit.prevent="logIn">
      <div>
        <input type="username" v-model.trim="username">
      </div>
      <div>
        <input type="password" v-model.trim="password">
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
const password = ref(null)

const logIn = function () {
  const payload = {
    username: username.value,
    password: password.value,
  }
  store.logIn(payload)
}
</script>

<style>

</style>
