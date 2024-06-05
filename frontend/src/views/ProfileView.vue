<template>
     <div class="p-4 m-4 mx-auto grid grid-cols-4 gap-4 flex items-center">
        <div class="main-center">
            <div class="p-4 bg-white border border-gray-200 rounded-lg flex flex-col items-center">
              <div class="flex items-center">
                   <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-16 rounded-full">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M17.982 18.725A7.488 7.488 0 0 0 12 15.75a7.488 7.488 0 0 0-5.982 2.975m11.963 0a9 9 0 1 0-11.963 0m11.963 0A8.966 8.966 0 0 1 12 21a8.966 8.966 0 0 1-5.982-2.275M15 9.75a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
                    </svg>
                  <p class="p-4" v-if="user.name"><strong>{{ user.name }}</strong></p>
              </div>
              <p class="p-4" v-if="user.email">{{ user.email }}</p>
            </div>
        </div>
     </div>

    <div class=" p-4 m-4 bg-white border border-gray-200 text-center rounded-lg" v-if="userStore.user.superuser !== true">
    <fwb-tabs v-model="activeTab" class="p-5">
       <fwb-tab name="all" title="Все заказы">
          <div class="flex flex-wrap" v-if="allOrders.length > 0 && this.isLoading === false">
              <div v-for="order in allOrders" :key="order.id" class="w-1/4 p-2">
                <div @click="checkCompositionOrder(order.id)" title="Перейти на заказ" class="hover:bg-gray-100 duration-200 cursor-pointer max-w-sm rounded overflow-hidden bg-white shadow-lg">
                  <h1 class="text-xl">
                    Номер заказа: {{order.id}}
                  </h1>
                  <div class="px-6 py-4" v-if="order.status === 'Оформлен' || order.status ==='В пути' || order.status ==='В пункте выдачи'">
                     <p class="text-sm text-gray-600 flex items-center">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                                    <path stroke-linecap="round" stroke-linejoin="round" d="M2.036 12.322a1.012 1.012 0 0 1 0-.639C3.423 7.51 7.36 4.5 12 4.5c4.638 0 8.573 3.007 9.963 7.178.07.207.07.431 0 .639C20.577 16.49 16.64 19.5 12 19.5c-4.638 0-8.573-3.007-9.963-7.178Z" />
                                    <path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
                                  </svg>
                       <div class="inline-block bg-red-200 px-3 py-1 rounded-full" v-if="order.status ==='Оформлен'">{{order.status}}</div>
                       <div class="inline-block bg-yellow-200 px-3 py-1 rounded-full" v-else-if="order.status ==='В пути'">{{order.status}}</div>
                       <div class="inline-block bg-green-200 px-3 py-1 rounded-full" v-else>{{order.status}}</div>
                     </p>
                    <div class="text-gray-700 text-base mb-2">Пункт выдачи: {{order.address.text}}</div>
                    <p class="text-gray-700 text-base">Дата оформления заказа: {{new Date(order.date_order).toLocaleString('ru-RU', { day: '2-digit', month: '2-digit', year: 'numeric' })}}</p>
                    <p class="text-gray-700 text-base" v-if="order.status === 'Оформлен' || order.status ==='В пути'">Планируемая дата выдачи: {{new Date(new Date(order.date_order).getTime() + 10 * 24 * 60 * 60 * 1000).toLocaleString('ru-RU', { day: '2-digit', month: '2-digit', year: 'numeric' })}}</p>

                    <p class="text-gray-700 text-base">Общая стоимость заказа: {{ order.all_price }} ₽</p>
                  </div>
                  <div class="px-6 py-4" v-else-if="order.status === 'Завершен'">
                      <p class="text-sm text-gray-600 flex items-center">
                         <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                                    <path stroke-linecap="round" stroke-linejoin="round" d="M2.036 12.322a1.012 1.012 0 0 1 0-.639C3.423 7.51 7.36 4.5 12 4.5c4.638 0 8.573 3.007 9.963 7.178.07.207.07.431 0 .639C20.577 16.49 16.64 19.5 12 19.5c-4.638 0-8.573-3.007-9.963-7.178Z" />
                                    <path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
                                  </svg>
                        <div class="inline-block bg-green-200 px-3 py-1 rounded-full">{{order.status}}</div>
                     </p>
                    <div class="text-gray-700 text-base mb-2">Пункт выдачи: {{ order.address.text }}</div>
                    <p class="text-gray-700 text-base">Общая стоимость заказа: {{ order.all_price }} ₽</p>
                    <p class="text-gray-700 text-base">Дата оформления заказа: {{new Date(order.date_order).toLocaleString('ru-RU', { day: '2-digit', month: '2-digit', year: 'numeric' })}}</p>
                    <p class="text-gray-700 text-base">Заказ был получен: {{new Date(order.date_of_receiving).toLocaleString('ru-RU', { day: '2-digit', month: '2-digit', year: 'numeric' })}}</p>
                  </div>
                  <div class="px-6 py-4" v-else-if="order.status === 'Отменен' || order.status === 'Не выкуплен'">
                      <p class="text-sm text-gray-600 flex items-center">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                                    <path stroke-linecap="round" stroke-linejoin="round" d="M2.036 12.322a1.012 1.012 0 0 1 0-.639C3.423 7.51 7.36 4.5 12 4.5c4.638 0 8.573 3.007 9.963 7.178.07.207.07.431 0 .639C20.577 16.49 16.64 19.5 12 19.5c-4.638 0-8.573-3.007-9.963-7.178Z" />
                                    <path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
                                  </svg>
                        <div class="inline-block bg-gray-200 px-3 py-1 rounded-full">{{order.status}}</div>
                     </p>
                    <div class="text-gray-700 text-base mb-2">Пункт выдачи: {{ order.address.text }}</div>
                    <p class="text-gray-700 text-base">Общая стоимость заказа: {{ order.all_price }} ₽</p>
                    <p class="text-gray-700 text-base">Дата оформления заказа: {{new Date(order.date_order).toLocaleString('ru-RU', { day: '2-digit', month: '2-digit', year: 'numeric' })}}</p>
                  </div>
                </div>
              </div>
          </div>
         <div v-else-if="allOrders.length > 0 && this.isLoading === false">
            Все заказы отсутствуют
         </div>
         <div v-else class="grid grid-cols-4 gap-4">
         <div v-for="index in 12" :key="index" class="border border-gray-300 shadow rounded-md max-w-sm mx-auto">
           <div class="animate-pulse flex space-x-4 ml-4 mr-4">
            <div class="rounded-full bg-slate-200 h-20 w-20"></div>
            <div class="flex-1 space-y-6 py-1">
              <div class="h-4 w-8 bg-slate-200 rounded"></div>
              <div class="space-y-3">
                <div class="grid grid-cols-3 gap-4">
                  <div class="h-4 w-8 bg-slate-200 rounded col-span-2"></div>
                  <div class="h-4 w-8 bg-slate-200 rounded col-span-1"></div>
                </div>
                <div class="h-4 w-8 bg-slate-200 rounded"></div>
              </div>
            </div>
          </div>

          </div>
        </div>
        </fwb-tab>

        <fwb-tab name="first" title="Активные заказы" >
          <div class="flex flex-wrap" v-if="activeOrders.length > 0 && this.isLoading === false">
              <div v-for="order in activeOrders" :key="order.id" class="w-1/4 p-2">
                <div @click="checkCompositionOrder(order.id)" title="Перейти на заказ" class="hover:bg-gray-100 duration-200 cursor-pointer max-w-sm rounded overflow-hidden bg-white shadow-lg">
                  <h1 class="text-xl">
                    Номер заказа: {{order.id}}
                  </h1>
                  <div class="px-6 py-4">
                     <p class="text-sm text-gray-600 flex items-center">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                                    <path stroke-linecap="round" stroke-linejoin="round" d="M2.036 12.322a1.012 1.012 0 0 1 0-.639C3.423 7.51 7.36 4.5 12 4.5c4.638 0 8.573 3.007 9.963 7.178.07.207.07.431 0 .639C20.577 16.49 16.64 19.5 12 19.5c-4.638 0-8.573-3.007-9.963-7.178Z" />
                                    <path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
                                  </svg>
                       <div class="inline-block bg-red-200 px-3 py-1 rounded-full" v-if="order.status ==='Оформлен'">{{order.status}}</div>
                       <div class="inline-block bg-yellow-200 px-3 py-1 rounded-full" v-else-if="order.status ==='В пути'">{{order.status}}</div>
                       <div class="inline-block bg-green-200 px-3 py-1 rounded-full" v-else>{{order.status}}</div>
                     </p>
                    <div class="text-gray-700 text-base mb-2">Пункт выдачи: {{ order.address.text }}</div>
                    <p class="text-gray-700 text-base">Дата оформления заказа: {{new Date(order.date_order).toLocaleString('ru-RU', { day: '2-digit', month: '2-digit', year: 'numeric' })}}</p>
                    <p class="text-gray-700 text-base" v-if="order.status === 'Оформлен' || order.status ==='В пути'">Планируемая дата выдачи: {{new Date(new Date(order.date_order).getTime() + 10 * 24 * 60 * 60 * 1000).toLocaleString('ru-RU', { day: '2-digit', month: '2-digit', year: 'numeric' })}}</p>
                    <p class="text-gray-700 text-base">Общая стоимость заказа: {{ order.all_price }} ₽</p>
                  </div>
                </div>
              </div>
          </div>
           <div v-else-if="activeOrders.length > 0 && this.isLoading === false">

          Активные заказы отсутствуют
         </div>
         <div v-else class="grid grid-cols-4 gap-4">
         <div v-for="index in 12" :key="index" class="border border-gray-300 shadow rounded-md max-w-sm mx-auto">
           <div class="animate-pulse flex space-x-4 ml-4 mr-4">
            <div class="rounded-full bg-slate-200 h-20 w-20"></div>
            <div class="flex-1 space-y-6 py-1">
              <div class="h-4 w-8 bg-slate-200 rounded"></div>
              <div class="space-y-3">
                <div class="grid grid-cols-3 gap-4">
                  <div class="h-4 w-8 bg-slate-200 rounded col-span-2"></div>
                  <div class="h-4 w-8 bg-slate-200 rounded col-span-1"></div>
                </div>
                <div class="h-4 w-8 bg-slate-200 rounded"></div>
              </div>
            </div>
          </div>

          </div>
        </div>
        </fwb-tab>

        <fwb-tab name="second" title="Архив заказов">
           <div class="flex flex-wrap" v-if="archiveOrders.length > 0 && this.isLoading === false">
              <div v-for="order in archiveOrders" :key="order.id" class="w-1/4 p-2">
                <div @click="checkCompositionOrder(order.id)" title="Перейти на заказ" class="hover:bg-gray-100 duration-200 cursor-pointer max-w-sm rounded overflow-hidden bg-white shadow-lg">
                  <h1 class="text-xl">
                    Номер заказа: {{order.id}}
                  </h1>
                  <div class="px-6 py-4">
                     <p class="text-sm text-gray-600 flex items-center">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                                    <path stroke-linecap="round" stroke-linejoin="round" d="M2.036 12.322a1.012 1.012 0 0 1 0-.639C3.423 7.51 7.36 4.5 12 4.5c4.638 0 8.573 3.007 9.963 7.178.07.207.07.431 0 .639C20.577 16.49 16.64 19.5 12 19.5c-4.638 0-8.573-3.007-9.963-7.178Z" />
                                    <path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
                                  </svg>
                        <div class="inline-block bg-green-200 px-3 py-1 rounded-full">{{order.status}}</div>
                     </p>
                    <div class="text-gray-700 text-base mb-2">Пункт выдачи: {{ order.address.text }}</div>
                    <p class="text-gray-700 text-base">Общая стоимость заказа: {{ order.all_price }} ₽</p>
                    <p class="text-gray-700 text-base">Дата оформления заказа: {{new Date(order.date_order).toLocaleString('ru-RU', { day: '2-digit', month: '2-digit', year: 'numeric' })}}</p>
                    <p class="text-gray-700 text-base">Заказ был получен: {{new Date(order.date_of_receiving).toLocaleString('ru-RU', { day: '2-digit', month: '2-digit', year: 'numeric' })}}</p>
                  </div>
                </div>
              </div>
          </div>
              <div v-else-if="archiveOrders.length > 0 && this.isLoading === false">

          Архив заказов пуст. Самое время это исправить:)
         </div>
         <div v-else class="grid grid-cols-4 gap-4">
         <div v-for="index in 12" :key="index" class="border border-gray-300 shadow rounded-md max-w-sm mx-auto">
           <div class="animate-pulse flex space-x-4 ml-4 mr-4">
            <div class="rounded-full bg-slate-200 h-20 w-20"></div>
            <div class="flex-1 space-y-6 py-1">
              <div class="h-4 w-8 bg-slate-200 rounded"></div>
              <div class="space-y-3">
                <div class="grid grid-cols-3 gap-4">
                  <div class="h-4 w-8 bg-slate-200 rounded col-span-2"></div>
                  <div class="h-4 w-8 bg-slate-200 rounded col-span-1"></div>
                </div>
                <div class="h-4 w-8 bg-slate-200 rounded"></div>
              </div>
            </div>
          </div>

          </div>
        </div>
        </fwb-tab>

        <fwb-tab name="third"  title="Отмененные заказы">
            <div class="flex flex-wrap" v-if="canceledOrders.length > 0 && this.isLoading === false">
              <div v-for="order in canceledOrders" :key="order.id" class="w-1/4 p-2">
                <div @click="checkCompositionOrder(order.id)" title="Перейти на заказ" class="hover:bg-gray-100 duration-200 cursor-pointer max-w-sm rounded overflow-hidden bg-white shadow-lg">
                  <h1 class="text-xl">
                    Номер заказа: {{order.id}}
                  </h1>
                  <div class="px-6 py-4">
                     <p class="text-sm text-gray-600 flex items-center">
                         <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                           <path stroke-linecap="round" stroke-linejoin="round" d="M2.036 12.322a1.012 1.012 0 0 1 0-.639C3.423 7.51 7.36 4.5 12 4.5c4.638 0 8.573 3.007 9.963 7.178.07.207.07.431 0 .639C20.577 16.49 16.64 19.5 12 19.5c-4.638 0-8.573-3.007-9.963-7.178Z" />
                           <path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
                         </svg>
                        <div class="inline-block bg-red-200 px-3 py-1 rounded-full">{{order.status}}</div>
                     </p>
                    <div class="text-gray-700 text-base mb-2">Пункт выдачи: {{ order.address.text }}</div>
                    <p class="text-gray-700 text-base">Общая стоимость заказа: {{ order.all_price }} ₽</p>
                    <p class="text-gray-700 text-base">Дата оформления заказа: {{new Date(order.date_order).toLocaleString('ru-RU', { day: '2-digit', month: '2-digit', year: 'numeric' })}}</p>
                  </div>
                </div>
              </div>
          </div>
             <div v-else-if="archiveOrders.length > 0 && this.isLoading === false">

          Отмененных заказов нет. Спасибо за доверие:)
         </div>
         <div v-else class="grid grid-cols-4 gap-4">
         <div v-for="index in 12" :key="index" class="border border-gray-300 shadow rounded-md max-w-sm mx-auto">
           <div class="animate-pulse flex space-x-4 ml-4 mr-4">
            <div class="rounded-full bg-slate-200 h-20 w-20"></div>
            <div class="flex-1 space-y-6 py-1">
              <div class="h-4 w-8 bg-slate-200 rounded"></div>
              <div class="space-y-3">
                <div class="grid grid-cols-3 gap-4">
                  <div class="h-4 w-8 bg-slate-200 rounded col-span-2"></div>
                  <div class="h-4 w-8 bg-slate-200 rounded col-span-1"></div>
                </div>
                <div class="h-4 w-8 bg-slate-200 rounded"></div>
              </div>
            </div>
          </div>

          </div>
        </div>
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
      isLoading: false,
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
                this.isLoading = true;
        axios
            .post('/api/order/', {'user': this.userStore.user.id})
            .then(response => {

                  this.allOrders = response.data.allOrders
                  this.activeOrders = response.data.activeOrders
                  this.canceledOrders = response.data.canceledOrders
                  this.archiveOrders = response.data.archiveOrders
                this.isLoading = false;

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