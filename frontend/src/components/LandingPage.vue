<template>
  <!-- Added flex and flex-col classes to the outer container -->
  <div class="flex flex-col min-h-screen bg-gradient-to-br from-indigo-50 via-white to-indigo-50">
    <Navbar />

    <!-- Make main section flex-1 so that it takes up remaining space -->
    <main class="flex-1">
      <!-- Hero Section -->
      <section class="container mx-auto px-4 py-24 lg:py-32">
        <div class="max-w-7xl mx-auto text-center">
          <template v-if="!isAuthenticated">
            <div class="space-y-8">
              <h1 class="text-5xl md:text-6xl font-extrabold text-gray-900 leading-tight">
                Transform Your
                <span class="bg-clip-text text-transparent bg-gradient-to-r from-indigo-600 to-purple-600">
                  Productivity
                </span>
              </h1>
              <p class="text-xl md:text-2xl text-gray-600 max-w-3xl mx-auto leading-relaxed">
                Collaborate, organize, and achieve your goals with our intuitive work management platform.
              </p>
              <div class="flex flex-col sm:flex-row justify-center gap-4 mt-12">
                <router-link 
                  to="/register" 
                  class="inline-flex items-center justify-center px-8 py-4 text-lg font-semibold text-white 
                         bg-gradient-to-r from-indigo-600 to-purple-600 rounded-xl shadow-lg hover:shadow-xl 
                         transition-all duration-300 hover:scale-[1.02]"
                >
                  Start Free Trial
                  <ArrowRightIcon class="w-5 h-5 ml-2 -mr-1" />
                </router-link>
                <router-link 
                  to="/login" 
                  class="inline-flex items-center justify-center px-8 py-4 text-lg font-semibold text-indigo-600 
                         bg-white border-2 border-indigo-100 rounded-xl hover:border-indigo-200 
                         transition-all duration-300 hover:scale-[1.02]"
                >
                  Explore Features
                </router-link>
              </div>
            </div>
            <div class="mt-16 lg:mt-24">
              <div class="relative mx-auto bg-gradient-to-r from-indigo-600 to-purple-600 rounded-3xl shadow-2xl 
                         overflow-hidden max-w-6xl aspect-video">
                <div class="absolute inset-0 bg-gradient-to-t from-black/20 to-transparent"></div>
                <img src="https://cdn.dribbble.com/users/879147/screenshots/15494726/media/9a6e3d8c5a3a5b3c2c3f3e4e4f3e4e4.png" 
                     class="w-full h-full object-cover" 
                     alt="Dashboard Preview">
              </div>
            </div>
          </template>

          <!-- Authenticated State -->
          <template v-else>
            <div class="space-y-8">
              <div class="inline-flex items-center bg-indigo-100 text-indigo-800 px-6 py-2 rounded-full 
                          text-sm font-medium mb-8">
                <UserCircleIcon class="w-5 h-5 mr-2" />
                Welcome back , {{ authStore.user }}!
              </div>
              <h2 class="text-4xl md:text-5xl font-extrabold text-gray-900">
                Ready to Conquer Your Day?
              </h2>
              <div class="flex flex-col sm:flex-row justify-center gap-4 mt-12">
                <router-link 
                  to="/tasks" 
                  class="inline-flex items-center justify-center px-8 py-4 text-lg font-semibold text-white 
                         bg-gradient-to-r from-indigo-600 to-purple-600 rounded-xl shadow-lg hover:shadow-xl 
                         transition-all duration-300 hover:scale-[1.02]"
                >
                  Go to Tasks
                  <CheckCircleIcon class="w-5 h-5 ml-2 -mr-1" />
                </router-link>
                <router-link 
                  to="/calendar" 
                  class="inline-flex items-center justify-center px-8 py-4 text-lg font-semibold text-indigo-600 
                         bg-white border-2 border-indigo-100 rounded-xl hover:border-indigo-200 
                         transition-all duration-300 hover:scale-[1.02]"
                >
                  View Calendar
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
              <h2 class="text-4xl font-extrabold text-gray-900 mb-6">Everything You Need to Succeed</h2>
              <p class="text-xl text-gray-600">Integrated tools that work seamlessly together</p>
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
        <div class="flex flex-col md:flex-row justify-between items-center">
          <router-link to="/" class="text-2xl font-bold text-indigo-600 mb-6 md:mb-0">
            TaskFlow
          </router-link>
          <div class="flex space-x-8">
            <a href="#" class="text-gray-600 hover:text-indigo-600 transition-colors">Privacy</a>
            <a href="#" class="text-gray-600 hover:text-indigo-600 transition-colors">Terms</a>
            <a href="#" class="text-gray-600 hover:text-indigo-600 transition-colors">Contact</a>
          </div>
        </div>
        <p class="text-center text-gray-600 mt-8">&copy; 2024 TaskFlow. All rights reserved.</p>
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
    title: "Smart Task Management",
    description: "Prioritize, categorize, and track tasks with intelligent automation and reminders."
  },
  {
    icon: CalendarIcon,
    title: "Team Calendar",
    description: "Sync deadlines, meetings, and milestones across your entire organization."
  },
  {
    icon: ChartBarIcon,
    title: "Advanced Analytics",
    description: "Real-time insights into team performance and project progress."
  }
]
</script>
