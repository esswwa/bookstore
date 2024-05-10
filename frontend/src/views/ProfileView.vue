<template>
     <div class="p-4 m-4 mx-auto grid grid-cols-4 gap-4 flex items-center">
        <div class="main-center">
            <div class="p-4 bg-white border border-gray-200 rounded-lg flex flex-col items-center">
              <div class="flex items-center">
                  <img src="https://i.pravatar.cc/40?img=70" class="w-16 rounded-full">
                  <p class="p-4" v-if="user.name"><strong>{{ user.name }}</strong></p>
              </div>
              <p class="p-4" v-if="user.email">{{ user.email }}</p>
            </div>
        </div>
     </div>

    <div class=" p-4 m-4 bg-white border border-gray-200 text-center rounded-lg">
    <fwb-tabs v-model="activeTab" class="p-5">
       <fwb-tab name="all" v-if="allOrders.length > 0" title="Все заказы">
          <div class="flex flex-wrap">
              <div v-for="order in allOrders" :key="order.id" class="w-1/4 p-2">
                <div @click="checkCompositionOrder(order.id)" title="Перейти на заказ" class="hover:bg-gray-100 duration-200 cursor-pointer max-w-sm rounded overflow-hidden bg-white shadow-lg">
                  <h1 class="text-xl">
                    Номер заказа: {{order.id}}
                  </h1>
                  <div class="px-6 py-4" v-if="order.status === 'Оформлен' || order.status ==='В пути' || order.status ==='В пункте выдачи'">
                     <p class="text-sm text-gray-600 flex items-center">
                        <svg class="fill-current text-gray-500 w-3 h-3 mr-2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                          <path d="M4 8V6a6 6 0 1 1 12 0v2h1a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-8c0-1.1.9-2 2-2h1zm5 6.73V17h2v-2.27a2 2 0 1 0-2 0zM7 6v2h6V6a3 3 0 0 0-6 0z" />
                        </svg>
                       <div class="inline-block bg-red-200 px-3 py-1 rounded-full" v-if="order.status ==='Оформлен'">{{order.status}}</div>
                       <div class="inline-block bg-yellow-200 px-3 py-1 rounded-full" v-else-if="order.status ==='В пути'">{{order.status}}</div>
                       <div class="inline-block bg-green-200 px-3 py-1 rounded-full" v-else>{{order.status}}</div>
                     </p>
                    <div class="text-gray-700 text-xl mb-2">Пункт выдачи: {{ order.address.text }}</div>
                    <p class="text-gray-700 text-base">Дата оформления заказа: {{new Date(order.date_order).toLocaleString('ru-RU', { day: '2-digit', month: '2-digit', year: 'numeric' })}}</p>
                    <p class="text-gray-700 text-base">Общая стоимость заказа: {{ order.all_price }} ₽</p>
                  </div>
                  <div class="px-6 py-4" v-else-if="order.status === 'Завершен'">
                      <p class="text-sm text-gray-600 flex items-center">
                        <svg class="fill-current text-gray-500 w-3 h-3 mr-2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                          <path d="M4 8V6a6 6 0 1 1 12 0v2h1a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-8c0-1.1.9-2 2-2h1zm5 6.73V17h2v-2.27a2 2 0 1 0-2 0zM7 6v2h6V6a3 3 0 0 0-6 0z" />
                        </svg>
                        <div class="inline-block bg-green-200 px-3 py-1 rounded-full">{{order.status}}</div>
                     </p>
                    <div class="text-gray-700 text-xl mb-2">Пункт выдачи: {{ order.address.text }}</div>
                    <p class="text-gray-700 text-base">Общая стоимость заказа: {{ order.all_price }} ₽</p>
                    <p class="text-gray-700 text-base">Дата оформления заказа: {{new Date(order.date_order).toLocaleString('ru-RU', { day: '2-digit', month: '2-digit', year: 'numeric' })}}</p>
                    <p class="text-gray-700 text-base">Заказ был получен: {{new Date(order.date_of_receiving).toLocaleString('ru-RU', { day: '2-digit', month: '2-digit', year: 'numeric' })}}</p>
                  </div>
                  <div class="px-6 py-4" v-else-if="order.status === 'Отменен' || order.status === 'Не выкуплен'">
                      <p class="text-sm text-gray-600 flex items-center">
                        <svg class="fill-current text-gray-500 w-3 h-3 mr-2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                          <path d="M4 8V6a6 6 0 1 1 12 0v2h1a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-8c0-1.1.9-2 2-2h1zm5 6.73V17h2v-2.27a2 2 0 1 0-2 0zM7 6v2h6V6a3 3 0 0 0-6 0z" />
                        </svg>
                        <div class="inline-block bg-gray-200 px-3 py-1 rounded-full">{{order.status}}</div>
                     </p>
                    <div class="text-gray-700 text-xl mb-2">Пункт выдачи: {{ order.address.text }}</div>
                    <p class="text-gray-700 text-base">Общая стоимость заказа: {{ order.all_price }} ₽</p>
                    <p class="text-gray-700 text-base">Дата оформления заказа: {{new Date(order.date_order).toLocaleString('ru-RU', { day: '2-digit', month: '2-digit', year: 'numeric' })}}</p>
                  </div>
                </div>
              </div>
          </div>
        </fwb-tab>
        <fwb-tab name="all" v-else title="Все заказы" >
          Все заказы отсутствуют
        </fwb-tab>
        <fwb-tab name="first" v-if="activeOrders.length > 0" title="Активные заказы" >
          <div class="flex flex-wrap">
              <div v-for="order in activeOrders" :key="order.id" class="w-1/4 p-2">
                <div @click="checkCompositionOrder(order.id)" title="Перейти на заказ" class="hover:bg-gray-100 duration-200 cursor-pointer max-w-sm rounded overflow-hidden bg-white shadow-lg">
                  <h1 class="text-xl">
                    Номер заказа: {{order.id}}
                  </h1>
                  <div class="px-6 py-4">
                     <p class="text-sm text-gray-600 flex items-center">
                        <svg class="fill-current text-gray-500 w-3 h-3 mr-2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                          <path d="M4 8V6a6 6 0 1 1 12 0v2h1a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-8c0-1.1.9-2 2-2h1zm5 6.73V17h2v-2.27a2 2 0 1 0-2 0zM7 6v2h6V6a3 3 0 0 0-6 0z" />
                        </svg>
                       <div class="inline-block bg-red-200 px-3 py-1 rounded-full" v-if="order.status ==='Оформлен'">{{order.status}}</div>
                       <div class="inline-block bg-yellow-200 px-3 py-1 rounded-full" v-else-if="order.status ==='В пути'">{{order.status}}</div>
                       <div class="inline-block bg-green-200 px-3 py-1 rounded-full" v-else>{{order.status}}</div>
                     </p>
                    <div class="text-gray-700 text-xl mb-2">Пункт выдачи: {{ order.address.text }}</div>
                    <p class="text-gray-700 text-base">Дата оформления заказа: {{new Date(order.date_order).toLocaleString('ru-RU', { day: '2-digit', month: '2-digit', year: 'numeric' })}}</p>
                    <p class="text-gray-700 text-base">Общая стоимость заказа: {{ order.all_price }} ₽</p>
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
              <div v-for="order in archiveOrders" :key="order.id" class="w-1/4 p-2">
                <div @click="checkCompositionOrder(order.id)" title="Перейти на заказ" class="hover:bg-gray-100 duration-200 cursor-pointer max-w-sm rounded overflow-hidden bg-white shadow-lg">
                  <h1 class="text-xl">
                    Номер заказа: {{order.id}}
                  </h1>
                  <div class="px-6 py-4">
                     <p class="text-sm text-gray-600 flex items-center">
                        <svg class="fill-current text-gray-500 w-3 h-3 mr-2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                          <path d="M4 8V6a6 6 0 1 1 12 0v2h1a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-8c0-1.1.9-2 2-2h1zm5 6.73V17h2v-2.27a2 2 0 1 0-2 0zM7 6v2h6V6a3 3 0 0 0-6 0z" />
                        </svg>
                        <div class="inline-block bg-green-200 px-3 py-1 rounded-full">{{order.status}}</div>
                     </p>
                    <div class="text-gray-700 text-xl mb-2">Пункт выдачи: {{ order.address.text }}</div>
                    <p class="text-gray-700 text-base">Общая стоимость заказа: {{ order.all_price }} ₽</p>
                    <p class="text-gray-700 text-base">Дата оформления заказа: {{new Date(order.date_order).toLocaleString('ru-RU', { day: '2-digit', month: '2-digit', year: 'numeric' })}}</p>
                    <p class="text-gray-700 text-base">Заказ был получен: {{new Date(order.date_of_receiving).toLocaleString('ru-RU', { day: '2-digit', month: '2-digit', year: 'numeric' })}}</p>
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
              <div v-for="order in canceledOrders" :key="order.id" class="w-1/4 p-2">
                <div @click="checkCompositionOrder(order.id)" title="Перейти на заказ" class="hover:bg-gray-100 duration-200 cursor-pointer max-w-sm rounded overflow-hidden bg-white shadow-lg">
                  <h1 class="text-xl">
                    Номер заказа: {{order.id}}
                  </h1>
                  <div class="px-6 py-4">
                     <p class="text-sm text-gray-600 flex items-center">
                        <svg class="fill-current text-gray-500 w-3 h-3 mr-2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                          <path d="M4 8V6a6 6 0 1 1 12 0v2h1a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-8c0-1.1.9-2 2-2h1zm5 6.73V17h2v-2.27a2 2 0 1 0-2 0zM7 6v2h6V6a3 3 0 0 0-6 0z" />
                        </svg>
                        <div class="inline-block bg-red-200 px-3 py-1 rounded-full">{{order.status}}</div>
                     </p>
                    <div class="text-gray-700 text-xl mb-2">Пункт выдачи: {{ order.address.text }}</div>
                    <p class="text-gray-700 text-base">Общая стоимость заказа: {{ order.all_price }} ₽</p>
                    <p class="text-gray-700 text-base">Дата оформления заказа: {{new Date(order.date_order).toLocaleString('ru-RU', { day: '2-digit', month: '2-digit', year: 'numeric' })}}</p>

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
    name: 'ProfileView',
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
            user: {
                id: ''
            },
      isOpen: false,
          password1: null,
          password2: null,
          email: null,
            allOrders: [],
            activeOrders: [],
            canceledOrders:[],
            archiveOrders: [],
            helperOrders: [],
            activeTab: ref('all')
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
                  this.email = response.data.user.email
                  this.password1 = this.user.password1
                  this.password2 = this.user.password2
                  console.log('data_user', this.user)
                })
                .catch(error => {
                    console.log('error', error)
                })
        },
      getOrder(){
        axios
            .post('/api/order/', {'user': this.userStore.user})
            .then(response => {

                  this.allOrders = response.data.allOrders
                  this.activeOrders = response.data.activeOrders
                  this.canceledOrders = response.data.canceledOrders
                  this.archiveOrders = response.data.archiveOrders

              console.log('allOrders', this.allOrders)
              console.log('activeOrders', this.activeOrders)
              console.log('canceledOrders', this.canceledOrders)
              console.log('archiveOrders', this.archiveOrders)
        });
      },
      checkCompositionOrder(orderId){
            this.$router.push(`/composition_order/${orderId}/`)
      },
        logout() {
            console.log('Log out')

            this.userStore.removeToken()

            this.$router.push('/signin')
        },
    }
}
</script>