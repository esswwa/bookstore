<template>
    <div class="p-4 m-4 mx-auto grid grid-cols-4 gap-4">
        <div class="main-left col-span-1">
            <div class="p-4 bg-white border border-gray-200 rounded-lg">

                <p class="p-4"><strong>{{ user.name }}</strong></p>
                    <RouterLink
                        class="inline-block mr-2 py-4 px-3 bg-blue-400 text-xs text-white rounded-lg"
                        to="/profile/edit"
                        v-if="userStore.user.id == user.id">
                        Edit profile
                    </RouterLink>

                    <button
                        class="inline-block py-4 px-3 bg-blue-400 text-xs text-white rounded-lg"
                        @click="logout"
                        v-if="userStore.user.id == user.id">
                        Log out
                    </button>
                </div>
            </div>
        </div>

    <div class="p-4 m-4 bg-white border border-gray-200 text-center rounded-lg">

    <fwb-tabs v-model="activeTab" class="p-5">
        <fwb-tab name="first" v-if="activeOrders.length > 0" title="Активные заказы" >
          <div class="flex flex-wrap">
              <div v-for="order in activeOrders" :key="order.id" class="w-1/3 p-2">
                <div class="max-w-sm rounded overflow-hidden bg-white shadow-lg">
                  <div class="px-6 py-4">
                     <p class="text-sm text-gray-600 flex items-center">
                        <svg class="fill-current text-gray-500 w-3 h-3 mr-2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                          <path d="M4 8V6a6 6 0 1 1 12 0v2h1a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-8c0-1.1.9-2 2-2h1zm5 6.73V17h2v-2.27a2 2 0 1 0-2 0zM7 6v2h6V6a3 3 0 0 0-6 0z" />
                        </svg>
                        {{order.status}}, {{new Date(order.date_order).getDay()}}.{{new Date(order.date_order).getMonth()}}.{{new Date(order.date_order).getFullYear()}}
                     </p>
                    <div class="font-bold text-xl mb-2">Пункт выдачи: {{ order.address.text }}</div>
                    <p class="text-gray-700 text-base">Общая стоимость заказа: {{ order.all_price }} ₽</p>
                  </div>
                  <div class="px-6 py-4" v-if="order.status === 'В пункте выдачи'">
                    <span class="inline-block px-3 py-1 text-sm font-semibold text-gray-700">Заказ прибыл в пункт выдачи {{ order.date_delivered }} числа, если вы не заберете заказ в течении 2-х недель, то он будет отменен! Спасибо за покупку!</span>
                  </div>
                </div>
              </div>
          </div>
        </fwb-tab>
        <fwb-tab name="first" v-else title="Активные заказы" >
          Активные заказы отсутствуют
        </fwb-tab>
        <fwb-tab name="second" v-if="archiveOrders.length > 0" title="Архив заказов">
           <div class="flex flex-wrap">
              <div v-for="order in archiveOrders" :key="order.id" class="w-1/3 p-2">
                <div class="max-w-sm rounded overflow-hidden bg-white shadow-lg">
                  <div class="px-6 py-4">
                     <p class="text-sm text-gray-600 flex items-center">
                        <svg class="fill-current text-gray-500 w-3 h-3 mr-2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                          <path d="M4 8V6a6 6 0 1 1 12 0v2h1a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-8c0-1.1.9-2 2-2h1zm5 6.73V17h2v-2.27a2 2 0 1 0-2 0zM7 6v2h6V6a3 3 0 0 0-6 0z" />
                        </svg>
                        {{order.status}}, {{new Date(order.date_order).getDay()}}.{{new Date(order.date_order).getMonth()}}.{{new Date(order.date_order).getFullYear()}}
                     </p>
                    <div class="font-bold text-xl mb-2">Пункт выдачи: {{ order.address.text }}</div>
                    <p class="text-gray-700 text-base">Общая стоимость заказа: {{ order.all_price }} ₽</p>
                    <p class="text-gray-700 text-base">Заказ был получен: {{new Date(order.date_of_receiving).getDay()}}.{{new Date(order.date_of_receiving).getMonth()}}.{{new Date(order.date_of_receiving).getFullYear()}}</p>
                      <button
                        class="inline-block py-4 px-3 bg-blue-400 text-xs text-white rounded-lg"
                        @click="logout">
                        Оставить отзыв
                    </button>
                  </div>
                </div>
              </div>
          </div>
        </fwb-tab>
        <fwb-tab name="second" v-else title="Архив заказов">
          Архив заказов пуст. Самое время это исправить:)
        </fwb-tab>
        <fwb-tab name="third" v-if="canceledOrders.length > 0" title="Отмененные заказы">
            <div class="flex flex-wrap">
              <div v-for="order in canceledOrders" :key="order.id" class="w-1/3 p-2">
                <div class="max-w-sm rounded overflow-hidden bg-white shadow-lg">
                  <div class="px-6 py-4">
                     <p class="text-sm text-gray-600 flex items-center">
                        <svg class="fill-current text-gray-500 w-3 h-3 mr-2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                          <path d="M4 8V6a6 6 0 1 1 12 0v2h1a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-8c0-1.1.9-2 2-2h1zm5 6.73V17h2v-2.27a2 2 0 1 0-2 0zM7 6v2h6V6a3 3 0 0 0-6 0z" />
                        </svg>
                        {{order.status}}, {{new Date(order.date_order).getDay()}}.{{new Date(order.date_order).getMonth()}}.{{new Date(order.date_order).getFullYear()}}
                     </p>
                    <div class="font-bold text-xl mb-2">Пункт выдачи: {{ order.address.text }}</div>
                    <p class="text-gray-700 text-base">Общая стоимость заказа: {{ order.all_price }} ₽</p>
                  </div>
                </div>
              </div>
          </div>
        </fwb-tab>
        <fwb-tab name="third" v-else title="Отмененные заказы">
          Отмененных заказов нет. Спасибо за доверие:)
        </fwb-tab>
  </fwb-tabs>

    </div>




</template>

<script>
import axios from 'axios'
import { useUserStore } from '@/stores/user'
import { useToastStore } from '@/stores/toast'

import { ref } from 'vue'
import { FwbTab, FwbTabs } from 'flowbite-vue'

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
            posts: [],
            user: {
                id: ''
            },
            activeOrders: [],
            canceledOrders:[],
            archiveOrders: [],
            can_send_friendship_request: null,
            activeTab: ref('first')
        }
    },

    mounted() {
        this.getUser();
        this.getOrder();
    },

    methods: {
              getUser() {
            axios
                .get(`/api/profile/${this.$route.params.id}/`)
                .then(response => {
                    console.log('data', response.data)
                    this.user = response.data.user
                })
                .catch(error => {
                    console.log('error', error)
                })
        },
      getOrder(){
        axios
            .post('/api/order/', {'user': this.userStore.user})
            .then(response => {
                  this.activeOrders = response.data.activeOrders
                  this.canceledOrders = response.data.canceledOrders
                  this.archiveOrders = response.data.archiveOrders

              console.log('activeOrders', this.activeOrders)
              console.log('canceledOrders', this.canceledOrders)
              console.log('archiveOrders', this.archiveOrders)
        });
      },
        logout() {
            console.log('Log out')

            this.userStore.removeToken()

            this.$router.push('/signin')
        }
    }
}
</script>