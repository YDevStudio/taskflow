import { defineStore } from 'pinia'
import axios from 'axios'

export const useAuthStore = defineStore('auth', {
  // 1) Initialize from localStorage if present
  state: () => ({
    token: localStorage.getItem('token') || null,
    user: JSON.parse(localStorage.getItem('user') || 'null'),
  }),
  getters: {
    isAuthenticated: (state) => !!state.token,
  },
  actions: {
    // 2) Set token in store + localStorage
    setToken(token) {
      this.token = token
      localStorage.setItem('token', token)
    },
    // 3) Set user in store + localStorage (if you want to store user data)
    setUser(user) {
      this.user = user
      localStorage.setItem('user', JSON.stringify(user))
    },
    // 4) Clear everything on logout
    logout() {
      this.token = null
      this.user = null
      localStorage.removeItem('token')
      localStorage.removeItem('user')
    },
    // 5) (Optional) Restore user data from the server if needed
    //    e.g., fetch user details from /auth/me if your API supports it
    async restore() {
      if (!this.token) return
      try {
        // Example: fetch user info to confirm token is valid
        // const response = await axios.get('http://127.0.0.1:8000/auth/me', {
        //   headers: { Authorization: `Bearer ${this.token}` }
        // })
        // this.setUser(response.data)
      } catch (error) {
        // If token is invalid, log them out
        this.logout()
      }
    },
  },
})

// Example task store (unchanged)
export const useTaskStore = defineStore('tasks', {
  state: () => ({
    tasks: [],
  }),
  actions: {
    async fetchTasks(token) {
      try {
        const res = await axios.get('http://127.0.0.1:8000/tasks', {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        })
        this.tasks = res.data
      } catch (error) {
        console.log(error)
      }
    },
  },
})