import './assets/main.css'
import { createRouter, createWebHistory } from 'vue-router'
import { autoAnimatePlugin } from '@formkit/auto-animate/vue'
import { createApp } from 'vue'
import App from './App.vue'
 
import Registration from './pages/Registration.vue'
import Profile from './pages/Profile.vue'
import ProfessorTable from './pages/ProfessorTable.vue'
import ProfessorCourse from './pages/ProfessorCourse.vue'
import StudentCourse from './pages/StudentCourse.vue'
import StudentMarks from './pages/StudentMarks.vue'
import NotFound from './pages/NotFound.vue'

const app = createApp(App)

const routes = [
  { path: '/', name: 'Registration', component: Registration },
  { path: '/studprofile/:userId', name: 'StudProfile', component: Profile },
  { path: '/profprofile/:userId', name: 'ProfProfile', component: Profile },
  { path: '/table/:userId', name: 'ProfessorTable', component: ProfessorTable },
  { path: '/makecourse/:userId', name: 'ProfessorCourse', component: ProfessorCourse },
  { path: '/courses/:userId', name: 'StudentCourses', component: StudentCourse },
  { path: '/marks/:userId', name: 'StudentMarks', component: StudentMarks },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

app.use(autoAnimatePlugin)
app.use(router)
app.mount('#app')
