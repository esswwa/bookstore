<template>
  <div class="flex flex-wrap">
                     <div v-for="helperOrder in helperOrders" :key="helperOrder.id" class="w-1/5 p-2">



                           <div class="max-w-s rounded-2xl overflow-hidden bg-white shadow-lg text-center">

  <div class="flex justify-center text-center">
                    <div class="h-48 lg:h-auto lg: flex-none bg-cover rounded-t lg:rounded-t-none lg:rounded-l text-center overflow-hidden" title="Перейти на книгу">
                          <div class="bg-white rounded-lg m-2 p-8 flex flex-col justify-between leading-normal">
                            <p class="text-sm text-gray-600 flex items-center">
                                  <svg class="fill-current text-gray-500 w-3 h-3 mr-2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                                    <path d="M4 8V6a6 6 0 1 1 12 0v2h1a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-8c0-1.1.9-2 2-2h1zm5 6.73V17h2v-2.27a2 2 0 1 0-2 0zM7 6v2h6V6a3 3 0 0 0-6 0z" />
                                  </svg>
                                   {{ helperOrder.book.author.text }},
                                </p>
                                <img class="p-2" src="https://api.lorem.space/image/book?w=200&h=200" alt="Book cover">
                                <div class="text-gray-900 font-medium text-xl mb-2">{{helperOrder.book.name.slice(0, 15) + (helperOrder.book.name.length > 15 ? '...' : '')}}</div>
                                  <span class=" flex items-center px-3 text-xl font-semibold text-gray-500">{{ helperOrder.book.cost_per_one }} ₽</span>

                                    <div class="flex flex-col mt-2">
                                        <span class="text-sm mb-2 font-semibold text-gray-700">Количество: {{ helperOrder.count }}</span>
                                        <span class="text-sm mb-2 font-semibold text-gray-700">Цена за все: {{ helperOrder.all_price }}</span>
                                    </div>

                            <div class="flex items-center justify-center text-center mb-4 mt-4">
                                          <svg class="w-4 h-4 text-yellow-300 me-1" v-if="helperOrder.book.rating > 0" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 22 20">
                                              <path d="M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z"/>
                                          </svg>
                                        <svg v-else class="w-4 h-4 ms-1 text-gray-300 dark:text-gray-500" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 22 20">
                                            <path d="M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z"/>
                                        </svg>
                                          <p class="ms-2 text-sm font-bold text-gray-900 dark:text-white">{{helperOrder.book.rating}}</p>
                                          <span class="w-1 h-1 mx-1.5 bg-gray-500 rounded-full dark:bg-gray-400"></span>
                                          <a :href="`http://localhost:5173/book/${helperOrder.book.id}/1/`" class="text-sm font-medium text-gray-900 underline hover:no-underline dark:text-white">{{helperOrder.book.count_rating}} отзывов</a>
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
            helperOrders: [],
        }
    },

    mounted() {
        this.getHelperOrder();
    },

    methods: {
      getHelperOrder(){
                axios.post(`/api/order/get_helper_order/`, {'order': this.$route.params.id})
                    .then(response => {
                      this.helperOrders = response.data.activeOrders
                      console.log('helperOrders', this.helperOrders)
                    })
                    .catch(error => {
                      console.log('error', error)
                    })
      }
    }
}
</script>
