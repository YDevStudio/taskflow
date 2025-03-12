<template>
  <div class="min-h-screen bg-gradient-to-b from-indigo-50 to-white flex flex-col">
    <Navbar />

    <div class="flex-1 flex items-center justify-center px-4">
      <div class="max-w-md w-full">
        <transition name="slide-fade" mode="out-in">
          <div key="form" class="bg-white rounded-2xl shadow-lg p-8 mb-6">
            <div class="text-center mb-8">
              <h1 class="text-3xl font-bold text-gray-800 mb-2">Welcome Back</h1>
              <p class="text-gray-500">Please sign in to continue</p>
            </div>

            <form @submit.prevent="loginUser" class="space-y-6">
              <!-- Email Field -->
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

              <!-- Password Field -->
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

              <!-- General Error -->
              <p 
                v-if="generalError" 
                class="text-red-500 text-sm mt-1 text-center"
              >
                {{ generalError }}
              </p>

              <!-- Submit Button -->
              <button 
                type="submit"
                class="w-full bg-indigo-600 hover:bg-indigo-700
                       text-white font-medium py-3 rounded-lg
                       transition-all duration-300 flex items-center justify-center"
                :disabled="loading"
              >
                <span v-if="!loading">Sign In</span>
                <svg 
                  v-else
                  class="animate-spin h-5 w-5 text-white" 
                  xmlns="http://www.w3.org/2000/svg" 
                  fill="none"
                  viewBox="0 0 24 24"
                >
                  <circle 
                    class="opacity-25" 
                    cx="12" 
                    cy="12" 
                    r="10" 
                    stroke="currentColor" 
                    stroke-width="4"
                  />
                  <path 
                    class="opacity-75" 
                    fill="currentColor"
                    d="M4 12a8 8 0 018-8V0C5.373 0 0 
                       5.373 0 12h4zm2 5.291A7.962 7.962 0 
                       014 12H0c0 3.042 1.135 5.824 3 
                       7.938l3-2.647z"
                  />
                </svg>
              </button>
            </form>

            <!-- Registration Link -->
            <div class="mt-6 text-center">
              <p class="text-gray-600">
                Don't have an account?
                <router-link 
                  to="/register"
                  class="text-indigo-600 hover:text-indigo-700 font-medium transition-colors"
                >
                  Create account
                </router-link>
              </p>
            </div>
          </div>
        </transition>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'
import Navbar from './Navbar.vue'
import { useAuthStore } from '../store/index.js'

const email = ref('')
const password = ref('')
const loading = ref(false)
const emailError = ref(null)
const passwordError = ref(null)
const generalError = ref(null)

const router = useRouter()
const authStore = useAuthStore()

const loginUser = async () => {
  loading.value = true
  emailError.value = null
  passwordError.value = null
  generalError.value = null

  try {
    const response = await axios.post('http://127.0.0.1:8000/auth/login', {
      email: email.value,
      password: password.value
    })

    if (response.status === 200) {
      authStore.setToken(response.data.access_token)
      authStore.setUser(response.data.username)
      router.push('/tasks')
    }
  } catch (error) {
    if (error.response) {
      if (error.response.status === 404) {
        emailError.value = "No account found with this email."
      } else if (error.response.status === 403) {
        passwordError.value = "Incorrect password. Please try again."
      } else {
        generalError.value = error.response.data.detail || "Login failed. Please try again."
      }
    } else {
      generalError.value = "An unexpected error occurred. Please try again later."
    }
  } finally {
    loading.value = false
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