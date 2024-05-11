<template>

<!--  -->


<div class="flex">
  <div class="max-w-s rounded-2xl overflow-hidden bg-white shadow-lg m-2 min-w-max" v-if="order">
          <div class="text-gray-900 font-medium text-xl mb-2">

            <div class="px-6 py-4">

              <p class="text-sm text-gray-600 flex items-center" v-if="order.status">
                        <svg class="fill-current text-gray-500 w-3 h-3 mr-2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                          <path d="M4 8V6a6 6 0 1 1 12 0v2h1a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-8c0-1.1.9-2 2-2h1zm5 6.73V17h2v-2.27a2 2 0 1 0-2 0zM7 6v2h6V6a3 3 0 0 0-6 0z" />
                        </svg>
                       <div class="inline-block bg-red-200 px-3 py-1 rounded-full" v-if="order.status ==='Оформлен'">{{order.status}}</div>
                       <div class="inline-block bg-yellow-200 px-3 py-1 rounded-full" v-else-if="order.status ==='В пути'">{{order.status}}</div>
                       <div class="inline-block bg-green-200 px-3 py-1 rounded-full" v-else>{{order.status}}</div>
                     </p>
               <h1 class="text-xl">
                    Номер заказа: {{order.id}}
                  </h1>
                    <div class="text-gray-700 text-xl mb-2" v-if="order.address">Пункт выдачи: {{ order.address.text }}</div>
                    <p class="text-gray-700 text-base" v-if="order.date_order">Дата оформления заказа: {{new Date(order.date_order).toLocaleString('ru-RU', { day: '2-digit', month: '2-digit', year: 'numeric' })}}</p>
                    <p class="text-gray-700 text-base" v-if="order.status === 'В пункте выдачи'">Дата прибытия в пункт выдачи: {{new Date(order.date_delivered).toLocaleString('ru-RU', { day: '2-digit', month: '2-digit', year: 'numeric' })}}</p>
                    <p class="text-gray-700 text-base" v-if="order.status === 'Завершен'">Заказ был получен: {{new Date(order.date_of_receiving).toLocaleString('ru-RU', { day: '2-digit', month: '2-digit', year: 'numeric' })}}</p>

                    <p class="text-gray-700 text-base">Общая стоимость заказа: {{ order.all_price }} ₽</p>
                    <button @click="cancelOrder()" v-if="userStore.user.superuser !== true && order.status !== 'Отменен' && order.status !== 'Завершен' && order.status !== 'Не выкуплен'" class="card-button py-4 px-6 mt-4 bg-blue-400 text-white rounded-lg">Отменить заказ</button>
                    <div v-if="order.status === 'В пункте выдачи'" class="m-4 whitespace-normal text-m text-gray-900 flex justify-center text-center items-center">
                      Ваш заказ прибыл в пункт выдачи,<br>
                      если вы не заберете заказ в течении<br>
                      2-х недель, то он будет автоматически отменен!<br>
                      Спасибо за покупку!
                    </div>
                  </div>
          </div>
  </div>
  <div class="flex flex-wrap">
                     <div v-for="helperOrder in helperOrders" :key="helperOrder.id" class="w-1/3 p-2 min-w-max">
                           <div class="max-w-s rounded-2xl overflow-hidden bg-white shadow-lg text-center min-w-max">
                              <div class="flex justify-center text-center">
                    <div class="h-48 lg:h-auto lg: flex-none bg-cover rounded-t lg:rounded-t-none lg:rounded-l text-center overflow-hidden" title="Перейти на книгу">
                          <div @click="goToBook(helperOrder.book.id)" class="hover:bg-gray-100 duration-200 cursor-pointer bg-white rounded-lg m-2 p-8 flex flex-col justify-between leading-normal">
                            <p class="text-sm text-gray-600 flex items-center" v-if="helperOrder.book.author">
                                   <svg v-if="!viewedBooks.includes(helperOrder.book.id)" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                                    <path stroke-linecap="round" stroke-linejoin="round" d="M3.98 8.223A10.477 10.477 0 0 0 1.934 12C3.226 16.338 7.244 19.5 12 19.5c.993 0 1.953-.138 2.863-.395M6.228 6.228A10.451 10.451 0 0 1 12 4.5c4.756 0 8.773 3.162 10.065 7.498a10.522 10.522 0 0 1-4.293 5.774M6.228 6.228 3 3m3.228 3.228 3.65 3.65m7.894 7.894L21 21m-3.228-3.228-3.65-3.65m0 0a3 3 0 1 0-4.243-4.243m4.242 4.242L9.88 9.88" />
                                  </svg>
                                  <svg v-else xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                                    <path stroke-linecap="round" stroke-linejoin="round" d="M2.036 12.322a1.012 1.012 0 0 1 0-.639C3.423 7.51 7.36 4.5 12 4.5c4.638 0 8.573 3.007 9.963 7.178.07.207.07.431 0 .639C20.577 16.49 16.64 19.5 12 19.5c-4.638 0-8.573-3.007-9.963-7.178Z" />
                                    <path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
                                  </svg>
                                   {{ helperOrder.book.author.text.split(',')[0] }}
                                </p>
                                <img class="p-2" height="200px" width="200px" src="@/assets/preview.jpg" alt="Book cover">
                                <div class="text-gray-900 font-medium text-xl mb-2" v-if="helperOrder.book.name">{{helperOrder.book.name.slice(0, 15) + (helperOrder.book.name.length > 15 ? '...' : '')}}</div>
                                  <span class=" flex items-center px-3 text-xl font-semibold text-gray-500" v-if="helperOrder.book.cost_per_one">{{ helperOrder.book.cost_per_one }} ₽</span>

                                    <div class="flex flex-col mt-2">
                                        <span class="text-sm mb-2 font-semibold text-gray-700" v-if="helperOrder.count">Количество: {{ helperOrder.count }}</span>
                                        <span class="text-sm mb-2 font-semibold text-gray-700" v-if="helperOrder.all_price">Цена за все: {{ helperOrder.all_price }}</span>
                                    </div>



                          </div>
                      <div class="flex items-center justify-center text-center mb-8 mt-4" v-if="helperOrder.book.rating >= 0">
                                          <svg class="w-4 h-4 text-yellow-300 me-1" v-if="helperOrder.book.rating > 0" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 22 20">
                                              <path d="M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z"/>
                                          </svg>
                                        <svg v-else class="w-4 h-4 ms-1 text-gray-300 dark:text-gray-500" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 22 20">
                                            <path d="M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z"/>
                                        </svg>
                                          <p class="ms-2 text-sm font-bold text-gray-900 dark:text-white">{{helperOrder.book.rating.toFixed(2)}}</p>
                                          <span class="w-1 h-1 mx-1.5 bg-gray-500 rounded-full dark:bg-gray-400"></span>
                                          <RouterLink :to="`/book/${helperOrder.book.id}/1/`" class="text-sm font-medium text-gray-900 underline hover:no-underline dark:text-white">
                                                   {{helperOrder.book.count_rating}} отзывов
                                            </RouterLink>
                                      </div>
                              </div>
                    </div>




  </div>

</div>

  </div>
  </div>
</template>

<script>

import axios from 'axios'
import { useUserStore } from '@/stores/user'
import {FwbTab, FwbTabs} from "flowbite-vue";
import {useToastStore} from "@/stores/toast.js";
import {ref} from "vue";
export default {
    name: 'FeedView',
  components: {
    FwbTab,
    FwbTabs
  },

    setup() {
        const userStore = useUserStore()
        const toastStore = useToastStore()
        return {
            userStore,
            toastStore,
        }
    },
    data() {
        return {
      viewedBooks: [],
      viewed: [],
            order: null,
            helperOrders: [],
        }
    },
    mounted() {
        this.getViewedBooks();
        this.getOrder();
        this.getHelperOrder();
    },

    methods: {
      getOrder(){
        axios
            .post('/api/order/get_order_only/', {'order': this.$route.params.id})
            .then(response => {
                  this.order = response.data.order
            })
            .catch(error => {
                      console.log('error', error)
                    })
      },
    goToBook(bookId) {
     axios
           .post(`/api/book/add_view/`, {"bookId":bookId,"user": this.userStore.user.id})
           .then(response => {
             this.$router.push({ path: `/book/${bookId}/1/` });
             console.log("Переход к книге с ID:", bookId);
           })
           .catch(error => {
               console.log('error', error)
           })
    },
      getHelperOrder(){
                axios.post(`/api/order/get_helper_order/`, {'order': this.$route.params.id})
                    .then(response => {
                      this.helperOrders = response.data.activeOrders
                      console.log('helperOrders', this.helperOrders)
                    })
                    .catch(error => {
                      console.log('error', error)
                    })
      },
      cancelOrder(){
             axios.post(`/api/order/cancel_order/`, {'order': this.$route.params.id})
                    .then(response => {
                      this.helperOrders = response.data.activeOrders
                      console.log('helperOrders', this.helperOrders)
                      this.$router.push({ path: `/profile/${this.userStore.id}/` });
                    })
                    .catch(error => {
                      console.log('error', error)
                    })
      },
      applyOrder(){
             axios.post(`/api/order/apply_order/`, {'order': this.$route.params.id})
                    .then(response => {
                      this.helperOrders = response.data.activeOrders
                      console.log('helperOrders', this.helperOrders)
                      this.$router.push({ path: `/profile/${this.userStore.id}/` });
                    })
                    .catch(error => {
                      console.log('error', error)
                    })
      },
    getViewedBooks(){
      axios
          .post('/api/book/get_viewed_books/', {"user_id": this.userStore.user.id})
          .then(response => {
            this.viewed = response.data.viewedBooks
            this.viewedBooks = this.viewed.map(item => item.id)
            console.log("viewedBooks", this.viewedBooks)
          })
          .catch(error =>{
            console.log("error", error)
          })
    }
    }
}
</script>
