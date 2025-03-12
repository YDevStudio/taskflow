<template>
  <div class="min-h-screen bg-gray-50">
    <Navbar />
    <div class="max-w-4xl mx-auto px-4 py-8">
      <!-- Header Section -->
      <div class="flex flex-col md:flex-row justify-between items-start md:items-center mb-8">
        <div class="mb-4 md:mb-0">
          <h1 class="text-3xl font-bold text-gray-800">Task Manager</h1>
          <p class="text-gray-500 mt-1">Stay organized and productive</p>
        </div>
        <button 
          @click="toggleForm"
          class="flex items-center bg-indigo-600 hover:bg-indigo-700 text-white px-6 py-3 rounded-lg transition-all duration-300 shadow-sm"
        >
          <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6"/>
          </svg>
          {{ showForm ? 'Close' : 'New Task' }}
        </button>
      </div>

      <TaskForm v-if="showForm" @task-created="handleTaskCreated" />

      <!-- Controls Section -->
      <div class="bg-white rounded-lg shadow-sm p-4 mb-6">
        <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center">
          <div class="flex items-center mb-2 sm:mb-0">
            <span class="text-gray-600 mr-3">Sort by:</span>
            <div class="relative">
              <select 
                v-model="sortBy" 
                @change="sortTasks" 
                class="appearance-none bg-white pl-4 pr-8 py-2 rounded-md border border-gray-200 text-gray-700 focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500"
              >
                <option value="date">Due Date</option>
                <option value="priority">Priority</option>
                <option value="category">Category</option>
                <option value="name">Task Name</option>
              </select>
              <div class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2">
                <svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                </svg>
              </div>
            </div>
          </div>
          <div class="flex items-center space-x-4">
            <div class="flex items-center">
              <span class="text-sm text-gray-600 mr-2">Pending:</span>
              <span class="bg-blue-100 text-blue-800 text-sm px-2 py-1 rounded">{{ pendingTasks.length }}</span>
            </div>
            <div class="flex items-center">
              <span class="text-sm text-gray-600 mr-2">Completed:</span>
              <span class="bg-green-100 text-green-800 text-sm px-2 py-1 rounded">{{ completedTasks.length }}</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Tasks Container -->
      <div class="space-y-6">
        <!-- Pending Tasks -->
        <div>
          <div class="flex items-center mb-4">
            <h2 class="text-xl font-semibold text-gray-800">Pending Tasks</h2>
            <span class="ml-2 bg-indigo-100 text-indigo-800 text-sm px-2 py-1 rounded-full">{{ pendingTasks.length }}</span>
          </div>
          <transition-group name="list" tag="div" class="space-y-3">
            <div 
              v-for="task in pendingTasks" 
              :key="task.id" 
              :class="[
                'group bg-white rounded-lg shadow-sm border-l-4 hover:shadow-md transition-all duration-300',
                { 'border-red-500': task.priority === 'High', 
                  'border-orange-400': task.priority === 'Medium', 
                  'border-blue-400': task.priority === 'Low' }
              ]"
            >
              <TaskItem 
                :task="task" 
                :editing="editingTaskId === task.id"
                @edit="editTask" 
                @delete="confirmDelete" 
                @toggle="toggleCompleted" 
                @save="saveTask"
                @cancel="cancelEdit"
                v-model:edited-task="editedTask"
              />
            </div>
          </transition-group>
        </div>

        <!-- Completed Tasks -->
        <div class="pt-6 border-t border-gray-100">
          <div class="flex items-center mb-4">
            <h2 class="text-xl font-semibold text-gray-800">Completed Tasks</h2>
            <span class="ml-2 bg-green-100 text-green-800 text-sm px-2 py-1 rounded-full">{{ completedTasks.length }}</span>
          </div>
          <transition-group name="list" tag="div" class="space-y-3">
            <div 
              v-for="task in completedTasks" 
              :key="task.id" 
              class="group bg-white rounded-lg shadow-sm border-l-4 border-emerald-500 opacity-75 hover:opacity-100 hover:shadow-md transition-all duration-300"
            >
              <TaskItem 
                :task="task" 
                :editing="editingTaskId === task.id"
                @edit="editTask" 
                @delete="confirmDelete" 
                @toggle="toggleCompleted" 
                @save="saveTask"
                @cancel="cancelEdit"
                v-model:edited-task="editedTask"
              />
            </div>
          </transition-group>
        </div>
      </div>

      <!-- Delete Confirmation Modal -->
      <transition name="modal">
        <div v-if="confirmingDelete" class="fixed inset-0 bg-black bg-opacity-30 flex items-center justify-center p-4">
          <div class="bg-white rounded-xl shadow-2xl max-w-md w-full p-6">
            <div class="flex items-center mb-4">
              <div class="flex-shrink-0 bg-red-100 p-2 rounded-lg">
                <svg class="w-6 h-6 text-red-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/>
                </svg>
              </div>
              <div class="ml-4">
                <h3 class="text-lg font-semibold text-gray-900">Delete Task</h3>
                <p class="text-gray-500">Are you sure you want to delete this task? This action cannot be undone.</p>
              </div>
            </div>
            <div class="flex justify-end space-x-3">
              <button 
                @click="confirmingDelete = false"
                class="px-4 py-2 text-gray-700 hover:text-gray-900 transition-colors duration-200"
              >
                Cancel
              </button>
              <button 
                @click="deleteTask"
                class="px-4 py-2 bg-red-600 hover:bg-red-700 text-white rounded-lg transition-colors duration-200"
              >
                Delete Task
              </button>
            </div>
          </div>
        </div>
      </transition>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import Navbar from './Navbar.vue'
import TaskForm from './TaskForm.vue'
import TaskItem from './TaskItem.vue'
import { onMounted, ref, computed } from 'vue'
import { useAuthStore } from '../store/index.js'
import dayjs from 'dayjs'

export default {
  components: {
    Navbar,
    TaskForm,
    TaskItem
  },
  setup() {
    const tasks = ref([])
    const showForm = ref(false)
    const errorMessage = ref('')
    const authStore = useAuthStore()
    const sortBy = ref('date')
    const confirmingDelete = ref(false)
    const taskToDelete = ref(null)
    const editingTaskId = ref(null)
    const editedTask = ref({})

    const fetchTasks = async () => {
      errorMessage.value = ''
      if (!authStore.token) return
      try {
        const res = await axios.get('http://127.0.0.1:8000/tasks', {
          headers: { Authorization: `Bearer ${authStore.token}` }
        })
        tasks.value = res.data.map(t => ({ ...t, new: false }))
      } catch (error) {
        errorMessage.value = 'Error fetching tasks. Please try again.'
      }
    }

    const toggleCompleted = async (task) => {
      if (!authStore.token) return
      try {
        await axios.put(`http://127.0.0.1:8000/tasks/${task.id}`,
          { completed: !task.completed },
          { headers: { Authorization: `Bearer ${authStore.token}` } }
        )
        fetchTasks()
      } catch (error) {
        errorMessage.value = 'Error updating task. Please try again.'
      }
    }

    const confirmDelete = (task) => {
      confirmingDelete.value = true
      taskToDelete.value = task.id
    }

    const deleteTask = async () => {
      if (!authStore.token || !taskToDelete.value) return
      try {
        await axios.delete(`http://127.0.0.1:8000/tasks/${taskToDelete.value}`, {
          headers: { Authorization: `Bearer ${authStore.token}` }
        })
        confirmingDelete.value = false
        taskToDelete.value = null
        fetchTasks()
      } catch (error) {
        errorMessage.value = 'Error deleting task. Please try again.'
      }
    }

    const editTask = (task) => {
      editingTaskId.value = task.id
      editedTask.value = { ...task }
    }

    const cancelEdit = () => {
      editingTaskId.value = null
      editedTask.value = {}
    }

    const saveTask = async (taskId) => {
      if (!authStore.token) return
      try {
        await axios.put(`http://127.0.0.1:8000/tasks/${taskId}`,
          editedTask.value,
          { headers: { Authorization: `Bearer ${authStore.token}` } }
        )
        cancelEdit()
        fetchTasks()
      } catch (error) {
        errorMessage.value = 'Error saving task. Please try again.'
      }
    }

    const handleTaskCreated = () => {
      showForm.value = false
      fetchTasks().then(() => {
        tasks.value[0].new = true
        setTimeout(() => { tasks.value[0].new = false }, 1000)
      })
    }

    const toggleForm = () => {
      showForm.value = !showForm.value
    }

    const sortTasks = () => {
      if (sortBy.value === 'date') {
        tasks.value.sort((a, b) => new Date(a.due_date) - new Date(b.due_date))
      } else if (sortBy.value === 'priority') {
        const priorityOrder = { 'High': 1, 'Medium': 2, 'Low': 3 }
        tasks.value.sort((a, b) => priorityOrder[a.priority] - priorityOrder[b.priority])
      } else if (sortBy.value === 'category') {
        tasks.value.sort((a, b) => a.category.localeCompare(b.category))
      } else if (sortBy.value === 'name') {
        tasks.value.sort((a, b) => a.title.localeCompare(b.title))
      }
    }

    const pendingTasks = computed(() => tasks.value.filter(task => !task.completed))
    const completedTasks = computed(() => tasks.value.filter(task => task.completed))

    onMounted(fetchTasks)

    return {
      tasks, showForm, fetchTasks, toggleCompleted, confirmDelete, deleteTask, handleTaskCreated, toggleForm,
      confirmingDelete, taskToDelete, sortBy, sortTasks, pendingTasks, completedTasks,
      editingTaskId, editedTask, editTask, saveTask, cancelEdit
    }
  }
}
</script>

<style scoped>
.list-enter-active,
.list-leave-active {
  transition: all 0.3s ease;
}
.list-enter-from,
.list-leave-to {
  opacity: 0;
  transform: translateY(30px);
}

.modal-enter-active,
.modal-leave-active {
  transition: opacity 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}
.modal-enter-from,
.modal-leave-to {
  opacity: 0;
}

@keyframes highlight {
  0% { background-color: rgba(99, 102, 241, 0.1); }
  100% { background-color: transparent; }
}

.new-task-effect {
  animation: highlight 1.5s ease-out;
}
</style>