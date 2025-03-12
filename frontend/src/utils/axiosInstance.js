import axios from 'axios'

const axiosInstance = axios.create({
  baseURL: 'http://127.0.0.1:8000'
})

// 🔴 Prevent Axios from logging 403/404 errors
axiosInstance.interceptors.response.use(
  response => response,
  error => {
    if (error.response?.status === 404 || error.response?.status === 403) {
      return Promise.reject(error) // UI handles this, no console log
    }
    
    console.error("Unhandled error:", error) // Only log critical errors
    return Promise.reject(error)
  }
)

export default axiosInstance