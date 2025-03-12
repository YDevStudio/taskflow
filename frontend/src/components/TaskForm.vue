<template>
  <div class="bg-white p-6 rounded-lg shadow-sm mb-6">
    <h2 class="text-xl font-bold mb-4">Create a New Task</h2>
    <form @submit.prevent="createTask" class="space-y-4">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <!-- Title -->
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1">Title</label>
          <input 
            v-model="title" 
            type="text" 
            class="w-full border px-3 py-2 rounded-lg 
                   focus:ring-2 focus:ring-indigo-500 
                   focus:border-indigo-500 transition-all" 
            required
          />
        </div>
        <!-- Category -->
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1">Category</label>
          <input 
            v-model="category" 
            type="text" 
            class="w-full border px-3 py-2 rounded-lg 
                   focus:ring-2 focus:ring-indigo-500 
                   focus:border-indigo-500 transition-all"
          />
        </div>
        <!-- Priority -->
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1">Priority</label>
          <select 
            v-model="priority" 
            class="w-full border px-3 py-2 rounded-lg 
                   focus:ring-2 focus:ring-indigo-500 
                   focus:border-indigo-500 transition-all"
          >
            <option disabled value="">-- Select Priority --</option>
            <option>High</option>
            <option>Medium</option>
            <option>Low</option>
          </select>
        </div>
        <!-- Due Date -->
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1">Due Date</label>
          <input 
            v-model="due_date" 
            type="datetime-local" 
            class="w-full border px-3 py-2 rounded-lg 
                   focus:ring-2 focus:ring-indigo-500 
                   focus:border-indigo-500 transition-all"
          />
        </div>
      </div>

      <!-- Description -->
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">Description</label>
        <textarea 
          v-model="description" 
          class="w-full border px-3 py-2 rounded-lg 
                 focus:ring-2 focus:ring-indigo-500 
                 focus:border-indigo-500 transition-all" 
          rows="3"
        ></textarea>
      </div>

      <!-- Submit Button & Error -->
      <button 
        type="submit" 
        class="mt-4 w-full bg-indigo-600 hover:bg-indigo-700 
               text-white font-medium py-2 rounded-lg 
               transition-all duration-300"
      >
        Create Task
      </button>

      <div v-if="errorMessage" class="mt-2 text-center">
        <p class="text-red-500 text-sm">{{ errorMessage }}</p>
      </div>
    </form>
  </div>
</template>

<script>
import { ref } from 'vue'
import axios from 'axios'
import { useAuthStore } from '../store/index.js'

export default {
  props: ['reload'],
  setup(props, { emit }) {
    const title = ref('')
    const description = ref('')
    const category = ref('')
    const priority = ref('')
    const due_date = ref('')
    const errorMessage = ref('')
    const authStore = useAuthStore()

    const createTask = async () => {
      errorMessage.value = ''
      if (!authStore.token) {
        errorMessage.value = 'Authentication token not found. Please login again.'
        return
      }
      try {
        await axios.post(
          'http://127.0.0.1:8000/tasks',
          {
            title: title.value,
            description: description.value,
            category: category.value,
            priority: priority.value,
            due_date: due_date.value 
              ? new Date(due_date.value).toISOString() 
              : null
          },
          {
            headers: { Authorization: `Bearer ${authStore.token}` }
          }
        )
        // Clear form fields
        title.value = ''
        description.value = ''
        category.value = ''
        priority.value = ''
        due_date.value = ''

        // Let the parent know we've created a task:
        emit('task-created')
      } catch (error) {
        errorMessage.value = 
          error.response?.data?.detail || 
          'Error creating task. Please try again.'
      }
    }

    return {
      title,
      description,
      category,
      priority,
      due_date,
      errorMessage,
      createTask
    }
  }
}
</script>