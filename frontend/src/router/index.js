import { createRouter, createWebHistory } from 'vue-router'
import SignupView from '@/views/SignupView.vue'
import SigninView from "@/views/SigninView.vue";
// import FeedView from "@/views/FeedView.vue";
// import MessagesView from "@/views/MessagesView.vue";
// import SearchView from "@/views/SearchView.vue";



const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/signup',
      name: 'signup',
      component: SignupView
    },
    {
      path: '/signin',
      name: 'signin',
      component: SigninView
    },
    // {
    //   path: '/feed',
    //   name: 'feed',
    //   component: FeedView
    // },
    // {
    //   path: '/messages',
    //   name: 'messages',
    //   component: MessagesView
    // },
    // {
    //   path: '/search',
    //   name: 'search',
    //   component: SearchView
    // },
  ]
})

export default router
