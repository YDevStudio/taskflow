<template>
  <div class="flex flex-col min-h-screen bg-gradient-to-br from-indigo-50 via-white to-indigo-50">
    <Navbar />

    <main class="flex-1">
      <!-- Hero Section -->
      <section class="container mx-auto px-4 py-24 lg:py-32">
        <div class="max-w-7xl mx-auto text-center">
          <template v-if="!isAuthenticated">
            <div class="space-y-8">
              <h1 class="text-5xl md:text-6xl font-extrabold text-gray-900 leading-tight">
                Keep Track of Your  
                <span class="bg-clip-text text-transparent bg-gradient-to-r from-indigo-600 to-purple-600">
                  Tasks & Goals
                </span>
              </h1>
              <p class="text-xl md:text-2xl text-gray-600 max-w-3xl mx-auto leading-relaxed">
                A simple task manager to organize your work and daily activities.
              </p>
              <div class="flex flex-col sm:flex-row justify-center gap-4 mt-12">
                <router-link 
                  to="/register" 
                  class="inline-flex items-center justify-center px-8 py-4 text-lg font-semibold text-white 
                         bg-gradient-to-r from-indigo-600 to-purple-600 rounded-xl shadow-lg hover:shadow-xl 
                         transition-all duration-300 hover:scale-[1.02]"
                >
                  Get Started
                  <ArrowRightIcon class="w-5 h-5 ml-2 -mr-1" />
                </router-link>
                <router-link 
                  to="/login" 
                  class="inline-flex items-center justify-center px-8 py-4 text-lg font-semibold text-indigo-600 
                         bg-white border-2 border-indigo-100 rounded-xl hover:border-indigo-200 
                         transition-all duration-300 hover:scale-[1.02]"
                >
                  Login
                </router-link>
              </div>
            </div>
          </template>

          <!-- Authenticated State -->
          <template v-else>
            <div class="space-y-8">
              <div class="inline-flex items-center bg-indigo-100 text-indigo-800 px-6 py-2 rounded-full 
                          text-sm font-medium mb-8">
                <UserCircleIcon class="w-5 h-5 mr-2" />
                Welcome back, {{ authStore.user }}!
              </div>
              <h2 class="text-4xl md:text-5xl font-extrabold text-gray-900">
                Let's get things done!
              </h2>
              <div class="flex flex-col sm:flex-row justify-center gap-4 mt-12">
                <router-link 
                  to="/tasks" 
                  class="inline-flex items-center justify-center px-8 py-4 text-lg font-semibold text-white 
                         bg-gradient-to-r from-indigo-600 to-purple-600 rounded-xl shadow-lg hover:shadow-xl 
                         transition-all duration-300 hover:scale-[1.02]"
                >
                  Go to My Tasks
                  <CheckCircleIcon class="w-5 h-5 ml-2 -mr-1" />
                </router-link>
                <router-link 
                  to="/calendar" 
                  class="inline-flex items-center justify-center px-8 py-4 text-lg font-semibold text-indigo-600 
                         bg-white border-2 border-indigo-100 rounded-xl hover:border-indigo-200 
                         transition-all duration-300 hover:scale-[1.02]"
                >
                  Open Calendar
                  <CalendarIcon class="w-5 h-5 ml-2 -mr-1" />
                </router-link>
              </div>
            </div>
          </template>
        </div>
      </section>

      <!-- Features Section -->
      <template v-if="!isAuthenticated">
        <section class="bg-white py-24">
          <div class="container mx-auto px-4">
            <div class="max-w-4xl mx-auto text-center mb-20">
              <h2 class="text-4xl font-extrabold text-gray-900 mb-6">What You Can Do</h2>
              <p class="text-xl text-gray-600">Manage tasks, track deadlines, and stay organized.</p>
            </div>
            <div class="grid md:grid-cols-3 gap-12">
              <div 
                v-for="(feature, index) in features"
                :key="index"
                class="group p-8 bg-white rounded-2xl border border-indigo-50 
                       hover:border-transparent hover:shadow-xl transition-all duration-300"
              >
                <div class="w-16 h-16 bg-gradient-to-r from-indigo-600 to-purple-600 rounded-2xl 
                            flex items-center justify-center mb-6 group-hover:scale-110 transition-transform">
                  <component :is="feature.icon" class="w-8 h-8 text-white" />
                </div>
                <h3 class="text-2xl font-bold text-gray-900 mb-4">{{ feature.title }}</h3>
                <p class="text-gray-600 leading-relaxed">{{ feature.description }}</p>
              </div>
            </div>
          </div>
        </section>
      </template>
    </main>

    <footer class="border-t border-indigo-100 bg-white">
      <div class="container mx-auto px-4 py-12">
        <p class="text-center text-gray-600 mt-8">&copy; 2024 TaskFlow. Personal project.</p>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { CheckCircleIcon, CalendarIcon, ChartBarIcon, UserCircleIcon, ArrowRightIcon } from '@heroicons/vue/24/outline'
import Navbar from './Navbar.vue'
import { useAuthStore } from '../store/index.js'

const authStore = useAuthStore()
const isAuthenticated = computed(() => authStore.isAuthenticated)

const features = [
  {
    icon: CheckCircleIcon,
    title: "Task Organization",
    description: "Create, categorize, and prioritize tasks easily."
  },
  {
    icon: CalendarIcon,
    title: "Calendar Integration",
    description: "See all tasks in a structured calendar view."
  },
  {
    icon: ChartBarIcon,
    title: "Progress Tracking",
    description: "Mark tasks as completed and track your progress."
  }
]
</script>