<template>
  <div id="app">
    <h1>Frontend is Running</h1>
    <p>Status: {{ status }}</p>
    <button @click="checkBackend">Check Backend</button>
    <p v-if="backendMessage">{{ backendMessage }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      status: 'Ready',
      backendMessage: ''
    }
  },
  methods: {
    async checkBackend() {
      try {
        const response = await fetch('/api/health')
        const data = await response.json()
        this.backendMessage = `Backend: ${data.message}`
      } catch (error) {
        this.backendMessage = 'Backend connection failed'
      }
    }
  }
}
</script>

<style>
#app {
  font-family: Arial, sans-serif;
  text-align: center;
  margin-top: 60px;
}
button {
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
}
</style>
