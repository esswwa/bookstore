<template>
                     <div v-for="helperOrder in helperOrders" :key="helperOrder.id">

                                <div class="card rounded mt-4 p-4 overflow-hidden bg-gray-200 shadow-lg">
                                <div class="card-content">
                                  <div class="px-6 py-4">
                                    <p class="text-sm text-gray-600 flex items-center">
                                      <svg class="fill-current text-gray-500 w-3 h-3 mr-2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                                        <path d="M4 8V6a6 6 0 1 1 12 0v2h1a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-8c0-1.1.9-2 2-2h1zm5 6.73V17h2v-2.27a2 2 0 1 0-2 0zM7 6v2h6V6a3 3 0 0 0-6 0z" />
                                      </svg>
                                      {{helperOrder.book.additional_genre.text_genre.text}}, {{helperOrder.book.author.text}}
                                    </p>
                                    <div class="font-bold text-xl mb-2">{{ helperOrder.book.name }}</div>
                                    <p class="text-gray-700 text-base">{{ helperOrder.book.description }}</p>
                                  </div>
                                  <div class="px-6 py-4">
                                    <span class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700">Цена: {{ helperOrder.book.cost_per_one }}₽</span>
                                    <span class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 ml-2">Рейтинг: {{helperOrder.book.rating}}</span>
                                  </div>
                                  <div class="px-6">
                                    <span class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700">Количество: {{ helperOrder.count }}</span>
                                    <span class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700">Цена за все: {{ helperOrder.all_price }}</span>
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
