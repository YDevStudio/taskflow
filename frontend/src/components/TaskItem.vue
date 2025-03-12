<template>
  <div class="p-4">
    <!-- Editing Mode -->
    <template v-if="editing">
      <div class="space-y-4">
        <input 
          v-model="editedTask.title" 
          placeholder="Task Title"
          class="w-full px-4 py-2 rounded-lg border border-gray-200 focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500"
        />

        <textarea
          v-model="editedTask.description"
          placeholder="Description"
          class="w-full px-4 py-2 rounded-lg border border-gray-200 focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500"
          rows="3"
        ></textarea>

        <div class="grid grid-cols-2 gap-4">
          <select 
            v-model="editedTask.priority" 
            class="px-4 py-2 rounded-lg border border-gray-200 focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500"
          >
            <option value="High">High Priority</option>
            <option value="Medium">Medium Priority</option>
            <option value="Low">Low Priority</option>
          </select>
          <input
            v-model="editedTask.category"
            placeholder="Category"
            class="px-4 py-2 rounded-lg border border-gray-200 focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500"
          />
        </div>

        <input
          v-model="editedTask.due_date"
          type="datetime-local"
          class="w-full px-4 py-2 rounded-lg border border-gray-200 focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500"
        />

        <div class="flex justify-end space-x-3">
          <button
            @click="$emit('cancel')"
            class="px-4 py-2 text-gray-600 hover:text-gray-800 transition-colors"
          >
            Cancel
          </button>
          <button
            @click="$emit('save', task.id)"
            class="px-4 py-2 bg-indigo-600 hover:bg-indigo-700 text-white rounded-lg transition-colors"
          >
            Save Changes
          </button>
        </div>
      </div>
    </template>

    <!-- Read-Only Mode -->
    <template v-else>
      <div class="flex items-start justify-between">
        <div class="flex items-start space-x-4 flex-1">
          <!-- Completed Toggle -->
          <button 
            @click="$emit('toggle', task)"
            class="mt-1 flex-shrink-0"
          >
            <div 
              :class="[
                'w-5 h-5 rounded-full border-2 flex items-center justify-center',
                task.completed ? 'border-emerald-500 bg-emerald-500' : 'border-gray-300'
              ]"
            >
              <svg 
                v-if="task.completed" 
                class="w-3 h-3 text-white" 
                fill="none" 
                stroke="currentColor" 
                viewBox="0 0 24 24"
              >
                <path 
                  stroke-linecap="round" 
                  stroke-linejoin="round" 
                  stroke-width="2" 
                  d="M5 13l4 4L19 7"
                />
              </svg>
            </div>
          </button>

          <!-- Task Details -->
          <div class="flex-1 min-w-0">
            <h3 
              :class="[
                'text-lg font-medium',
                task.completed ? 'text-gray-400 line-through' : 'text-gray-800'
              ]"
            >
              {{ task.title }}
            </h3>

            <p 
              v-if="task.description" 
              class="text-gray-500 text-sm mt-1"
            >
              {{ task.description }}
            </p>

            <div class="flex items-center space-x-3 mt-2">
              <span 
                v-if="task.category"
                class="px-2 py-1 bg-indigo-100 text-indigo-800 text-xs rounded-full"
              >
                {{ task.category }}
              </span>
              <span 
                class="flex items-center text-gray-400 text-sm"
              >
                <svg 
                  class="w-4 h-4 mr-1" 
                  fill="none" 
                  stroke="currentColor" 
                  viewBox="0 0 24 24"
                >
                  <path 
                    stroke-linecap="round" 
                    stroke-linejoin="round" 
                    stroke-width="2" 
                    d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"
                  />
                </svg>
                {{ formatDate(task.due_date) }}
              </span>
            </div>
          </div>
        </div>

        <!-- Edit / Delete Controls -->
        <div class="flex space-x-2 mt-2 ml-auto sm:mt-0 sm:ml-0">
          <button 
            @click="$emit('edit', task)"
            class="px-3 py-1 text-sm text-gray-500 hover:text-gray-700 transition-colors"
          >
            Edit
          </button>
          <button 
            @click="$emit('delete', task)"
            class="px-3 py-1 text-sm text-red-500 hover:text-red-700 transition-colors"
          >
            Delete
          </button>
        </div>
      </div>
    </template>
  </div>
</template>

<script>
import dayjs from 'dayjs'

export default {
  name: 'TaskItem',
  props: {
    task: {
      type: Object,
      required: true
    },
    editing: {
      type: Boolean,
      default: false
    },
    // This is the v-model binding for the parent’s "editedTask"
    editedTask: {
      type: Object,
      default: () => ({})
    }
  },
  emits: [
    'edit',
    'delete',
    'toggle',
    'save',
    'cancel',
    'update:editedTask' // For v-model on 'editedTask' (if you need to use it programmatically)
  ],
  setup() {
    const formatDate = (dateStr) => {
      if (!dateStr) return ''
      return dayjs(dateStr).format('MMM D, YYYY h:mm A')
    }

    return {
      formatDate
    }
  }
}
</script>