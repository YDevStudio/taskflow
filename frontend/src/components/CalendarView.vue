<template>
  <div class="min-h-screen bg-gray-50">
    <Navbar />

    <div class="max-w-4xl mx-auto px-4 py-8">
      <!-- Header & Month Navigation -->
      <div class="flex flex-col md:flex-row md:items-center justify-between mb-6">
        <div>
          <h1 class="text-3xl font-bold text-gray-800">Calendar View</h1>
          <p class="text-gray-500 text-sm">Your tasks at a glance</p>
        </div>
        <div class="mt-4 md:mt-0 space-x-2">
          <button
            @click="prevMonth"
            class="px-4 py-2 rounded-lg border border-gray-300 text-gray-600 hover:bg-gray-100 transition-colors duration-200"
          >
            &larr; Prev
          </button>
          <button
            @click="nextMonth"
            class="px-4 py-2 rounded-lg border border-gray-300 text-gray-600 hover:bg-gray-100 transition-colors duration-200"
          >
            Next &rarr;
          </button>
        </div>
      </div>

      <!-- Current Month Display -->
      <h2 class="text-xl font-semibold text-gray-700 text-center mb-2">
        {{ currentMonthName }} {{ currentYear }}
      </h2>

      <!-- Day Names Row (not offset) -->
      <div class="grid grid-cols-7 gap-2 text-xs font-medium text-gray-500 uppercase tracking-wide mb-3">
        <div v-for="(dayName, i) in dayNames" :key="i" class="text-center">
          {{ dayName }}
        </div>
      </div>

      <!-- Actual Calendar Grid -->
      <div class="grid grid-cols-1 sm:grid-cols-7 gap-2">
        <div
          v-for="day in daysInMonth"
          :key="day.date"
          class="bg-white rounded-lg shadow-sm p-3 text-center flex flex-col hover:shadow-md transition-all duration-300"
          :class="{
            'ring-2 ring-red-300': isToday(day.date),
          }"
        >
          <!-- Day Number -->
          <div
            class="text-lg font-bold mb-2"
            :class="{ 'text-red-500': isToday(day.date) }"
          >
            {{ formatDay(day.date) }}
          </div>

          <!-- Task List -->
          <ul class="text-xs text-left space-y-1">
            <li
              v-for="task in day.tasks"
              :key="task.id"
              class="truncate text-gray-600"
            >
              • {{ task.title }}
            </li>
            <!-- If you want to show a "No tasks" placeholder:
            <li 
              v-if="!day.tasks.length" 
              class="text-gray-400 italic"
            >
              No tasks
            </li>
            -->
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import Navbar from './Navbar.vue'
import dayjs from 'dayjs'
import axios from 'axios'
import { useAuthStore } from '../store/index.js'

const authStore = useAuthStore()

const tasks = ref([])
const currentMonth = ref(dayjs().startOf('month'))
const daysInMonth = ref([])

// For the day-name headers across the top
const dayNames = [
  'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'
]

/* ---------------- FETCH TASKS ---------------- */
const fetchTasks = async () => {
  if (!authStore.token) return
  try {
    const res = await axios.get('http://127.0.0.1:8000/tasks', {
      headers: {
        Authorization: `Bearer ${authStore.token}`
      }
    })
    tasks.value = res.data
    buildCalendar()
  } catch (error) {
    console.error('Error fetching tasks:', error)
  }
}

/* ---------------- BUILD CALENDAR ----------------
   For simplicity, we are simply iterating from 
   day 1..N in the current month. (No offset.)
------------------------------------------------- */
const buildCalendar = () => {
  const startOfMonth = currentMonth.value.startOf('month')
  const endOfMonth = currentMonth.value.endOf('month')
  const totalDays = endOfMonth.date()

  const daysArray = []
  for (let i = 1; i <= totalDays; i++) {
    const date = startOfMonth.date(i)
    const dayTasks = tasks.value.filter(task => {
      if (!task.due_date) return false
      return dayjs(task.due_date).isSame(date, 'day')
    })
    daysArray.push({
      date: date.toDate(),
      tasks: dayTasks
    })
  }
  daysInMonth.value = daysArray
}

/* ---------------- NAVIGATION ---------------- */
const prevMonth = () => {
  currentMonth.value = currentMonth.value.subtract(1, 'month')
  buildCalendar()
}
const nextMonth = () => {
  currentMonth.value = currentMonth.value.add(1, 'month')
  buildCalendar()
}

/* ---------------- HELPERS ---------------- */
const currentMonthName = computed(() => {
  return currentMonth.value.format('MMMM')
})
const currentYear = computed(() => {
  return currentMonth.value.format('YYYY')
})

const formatDay = (date) => {
  return dayjs(date).format('D')
}

const isToday = (date) => {
  return dayjs().isSame(date, 'day')
}

/* ---------------- ON MOUNT ---------------- */
onMounted(() => {
  fetchTasks()
})
</script>