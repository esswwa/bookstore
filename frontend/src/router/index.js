import { createRouter, createWebHistory } from 'vue-router'
import SignupView from '@/views/SignupView.vue'
import SigninView from "@/views/SigninView.vue";
import BasketView from "@/views/BasketView.vue";
import BooksView from "@/views/BooksView.vue";
import FavouriteView from "@/views/FavouriteView.vue";
import OrdersView from "@/views/OrdersView.vue";
import ProfileView from "@/views/ProfileView.vue";
import BookView from "@/views/BookView.vue";
import AllBooksView from "@/views/AllBooksView.vue";
import CompositionOrderView from "@/views/CompositionOrderView.vue";



const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
      {
      path: '/',
      name: '',
      component: BooksView
    },
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
      path: '/favourite/:page',
      name: 'favourite',
      component: FavouriteView
    },
    {
      path: '/order',
      name: 'order',
      component: OrdersView
    },
    {
      path: '/all_books/:page',
      name: 'all_books',
      component: AllBooksView
    },
    {
      path: '/book/:id/:page/',
      name: 'book',
      component: BookView
    },
    {
      path: '/profile/:id',
      name: 'profile',
      component: ProfileView
    },
    {
      path: '/composition_order/:id',
      name: 'composition_order',
      component: CompositionOrderView
    },
  ]
})

export default router
