<template>
  <div class="min-h-screen bg-gradient-to-b from-indigo-50 to-white flex flex-col">
    <Navbar />

    <div class="flex-1 flex items-center justify-center px-4">
      <div class="max-w-md w-full mx-auto">
        <div class="bg-white rounded-2xl shadow-lg p-8 mb-6">
          <h2 class="text-3xl font-bold text-gray-800 mb-4 text-center">Create Account</h2>
          
          <form @submit.prevent="registerUser" class="space-y-6">
            <!-- Username -->
            <div>
              <label 
                for="username" 
                class="block text-sm font-medium text-gray-700 mb-1"
              >
                Username
              </label>
              <input
                v-model="username"
                type="text"
                id="username"
                class="w-full px-4 py-3 rounded-lg border border-gray-200 
                       focus:ring-2 focus:ring-indigo-500
                       focus:border-indigo-500 transition-all
                       placeholder-gray-400"
                :class="{ 'border-red-500': usernameError }"
                placeholder="Your username"
                required
              />
              <p 
                v-if="usernameError" 
                class="text-red-500 text-sm mt-1"
              >
                {{ usernameError }}
              </p>
            </div>

            <!-- Email -->
            <div>
              <label 
                for="email"
                class="block text-sm font-medium text-gray-700 mb-1"
              >
                Email
              </label>
              <input
                v-model="email"
                type="email"
                id="email"
                class="w-full px-4 py-3 rounded-lg border border-gray-200 
                       focus:ring-2 focus:ring-indigo-500
                       focus:border-indigo-500 transition-all
                       placeholder-gray-400"
                :class="{ 'border-red-500': emailError }"
                placeholder="you@example.com"
                required
              />
              <p 
                v-if="emailError" 
                class="text-red-500 text-sm mt-1"
              >
                {{ emailError }}
              </p>
            </div>

            <!-- Password -->
            <div>
              <label 
                for="password"
                class="block text-sm font-medium text-gray-700 mb-1"
              >
                Password
              </label>
              <input
                v-model="password"
                type="password"
                id="password"
                class="w-full px-4 py-3 rounded-lg border border-gray-200 
                       focus:ring-2 focus:ring-indigo-500
                       focus:border-indigo-500 transition-all
                       placeholder-gray-400"
                :class="{ 'border-red-500': passwordError }"
                placeholder="••••••••"
                required
              />
              <p 
                v-if="passwordError" 
                class="text-red-500 text-sm mt-1"
              >
                {{ passwordError }}
              </p>
            </div>

            <!-- Submit -->
            <button 
              type="submit" 
              class="w-full bg-indigo-600 hover:bg-indigo-700
                     text-white font-medium py-3 rounded-lg
                     transition-all duration-300"
            >
              Register
            </button>
          </form>

          <!-- Error / Success Messages -->
          <div v-if="generalError" class="mt-4 text-center">
            <p class="text-red-500 text-sm">{{ generalError }}</p>
          </div>
          <div v-if="successMessage" class="mt-4 text-center">
            <p class="text-green-500 text-sm">{{ successMessage }}</p>
          </div>

          <!-- Login Link -->
          <p class="mt-4 text-center text-gray-600">
            Already have an account?
            <router-link 
              to="/login" 
              class="text-indigo-600 hover:text-indigo-700 font-medium transition-colors"
            >
              Login here
            </router-link>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'
import Navbar from './Navbar.vue'

const username = ref('')
const email = ref('')
const password = ref('')
const usernameError = ref(null)
const emailError = ref(null)
const passwordError = ref(null)
const generalError = ref(null)
const successMessage = ref(null)

const router = useRouter()

const registerUser = async () => {
  // Clear old errors
  usernameError.value = null
  emailError.value = null
  passwordError.value = null
  generalError.value = null
  successMessage.value = null

  try {
    await axios.post('http://127.0.0.1:8000/auth/register', {
      username: username.value,
      email: email.value,
      password: password.value
    })
    successMessage.value = "Registration successful! Redirecting..."
    
    // Simple auto-redirect after 1.5s
    setTimeout(() => {
      router.push('/login')
    }, 1500)
  } catch (error) {
    generalError.value = 
      error.response?.data?.detail || 
      "Error registering. Please try again."
  }
}
</script>

<style scoped>
.slide-fade-enter-active,
.slide-fade-leave-active {
  transition: all 0.3s ease;
}
.slide-fade-enter-from,
.slide-fade-leave-to {
  opacity: 0;
  transform: translateX(20px);
}
</style>