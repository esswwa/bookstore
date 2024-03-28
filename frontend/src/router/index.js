import { createRouter, createWebHistory } from 'vue-router'
import SignupView from '@/views/SignupView.vue'
import SigninView from "@/views/SigninView.vue";
import BasketView from "@/views/BasketView.vue";
import BooksView from "@/views/BooksView.vue";
import FavouriteView from "@/views/FavouriteView.vue";
import OrderView from "@/views/OrdersView.vue";
import ProfileView from "@/views/ProfileView.vue";



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
    {
      path: '/basket',
      name: 'basket',
      component: BasketView
    },
    {
      path: '/books',
      name: 'books',
      component: BooksView
    },
    {
      path: '/favourite',
      name: 'favourite',
      component: FavouriteView
    },
    {
      path: '/order',
      name: 'order',
      component: OrderView
    },
    {
      path: '/profile/:id',
      name: 'profile',
      component: ProfileView
    },
  ]
})

export default router
