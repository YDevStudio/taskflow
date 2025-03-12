import { createRouter, createWebHistory } from 'vue-router'
import Login from '../components/Login.vue'
import Register from '../components/Register.vue'
import TaskList from '../components/TaskList.vue'
import CalendarView from '../components/CalendarView.vue'
import LandingPage from '../components/LandingPage.vue' 
const routes = [
  { path: '/', name: 'LandingPage', component: LandingPage }, 
  { path: '/login', name: 'Login', component: Login },
  { path: '/register', name: 'Register', component: Register },
  { path: '/tasks', name: 'TaskList', component: TaskList },
  { path: '/calendar', name: 'CalendarView', component: CalendarView },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router