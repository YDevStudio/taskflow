<template>
  <nav class="sticky top-0 backdrop-blur-sm bg-white/80 border-b border-indigo-50 z-50">
    <div class="container mx-auto px-4">
      <div class="flex items-center justify-between h-20">
        <router-link 
          to="/" 
          class="flex items-center space-x-2 transition-transform hover:scale-105"
        >
          <svg class="w-8 h-8 text-indigo-600" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M16 2L2 16L16 30L30 16L16 2Z" fill="currentColor" stroke="currentColor" stroke-width="2"/>
            <path d="M16 2L22 8L16 14L10 8L16 2Z" fill="white"/>
            <path d="M16 30L22 24L16 18L10 24L16 30Z" fill="white"/>
          </svg>
          <span class="text-2xl font-bold text-gray-900">TaskFlow</span>
        </router-link>

        <div class="hidden lg:flex items-center space-x-10">
          <template v-if="authStore.isAuthenticated">
            <router-link 
              v-for="link in navigationLinks" 
              :key="'auth-' + link.path" 
              :to="link.path"
              class="relative text-gray-600 hover:text-indigo-600 px-3 py-2 transition-colors
                     before:absolute before:-bottom-1 before:left-0 before:w-0 before:h-0.5 
                     before:bg-indigo-600 before:transition-all hover:before:w-full"
              active-class="text-indigo-600 font-semibold"
            >
              {{ link.name }}
            </router-link>
          </template>
        </div>

        <div class="flex items-center space-x-4">
          <button v-if="authStore.isAuthenticated" @click="logout"
            class="flex items-center space-x-2 px-5 py-2.5 text-gray-600 hover:text-red-600 
                   transition-colors rounded-lg group"
          >
            <span class="font-medium">Logout</span>
            <ArrowLeftOnRectangleIcon class="w-5 h-5 transition-transform group-hover:scale-110" />
          </button>
          
          <router-link v-else to="/login"
            class="hidden lg:inline-flex items-center px-6 py-2.5 bg-indigo-600 hover:bg-indigo-700 
                   text-white font-medium rounded-lg transition-all duration-300 hover:shadow-lg"
          >
            Login
          </router-link>

          <button @click="toggleMobileMenu" class="lg:hidden p-2 text-gray-600 hover:text-indigo-600">
            <Bars3Icon class="w-6 h-6" />
          </button>
        </div>
      </div>

      <!-- Mobile Menu -->
      <div v-if="showMobileMenu" class="lg:hidden py-4 space-y-4">
        <template v-if="authStore.isAuthenticated">
          <router-link 
            v-for="link in navigationLinks" 
            :key="'mobile-auth-' + link.path" 
            :to="link.path"
            class="block px-4 py-3 text-gray-600 hover:bg-indigo-50 rounded-lg"
            active-class="bg-indigo-50 text-indigo-600"
          >
            {{ link.name }}
          </router-link>
        </template>
        <div class="border-t border-indigo-100 pt-4">
          <router-link 
            v-if="!authStore.isAuthenticated"
            to="/login" 
            class="block w-full text-center px-4 py-3 bg-indigo-600 text-white rounded-lg 
                   hover:bg-indigo-700 transition-colors"
          >
            Sign In
          </router-link>
        </div>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { ref } from 'vue'
import { useAuthStore } from '../store/index.js'
import { useRouter } from 'vue-router'
import { Bars3Icon, ArrowLeftOnRectangleIcon } from '@heroicons/vue/24/outline'

const authStore = useAuthStore()
const router = useRouter()
const showMobileMenu = ref(false)

const navigationLinks = ref([
  { name: 'Tasks', path: '/tasks' },
  { name: 'Calendar', path: '/calendar' },
  // { name: 'Analytics', path: '/analytics' }
])

const toggleMobileMenu = () => {
  showMobileMenu.value = !showMobileMenu.value
}

const logout = () => {
  authStore.logout()
  router.push('/login')
  showMobileMenu.value = false
}
</script>