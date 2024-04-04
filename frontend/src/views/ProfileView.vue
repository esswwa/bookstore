<template>
     <div class="p-4 m-4 mx-auto grid grid-cols-4 gap-4 flex items-center">
        <div class="main-center">
            <div class="p-4 bg-white border border-gray-200 rounded-lg">
                    <RouterLink :to="{name: 'profile', params:{'id': userStore.user.id}}">
                      <img src="https://i.pravatar.cc/40?img=70" class="w-16 rounded-full">
                      <p class="p-4"><strong>{{ user.name }}</strong></p>
                    </RouterLink>
                    <button
                        class="inline-block py-4 px-3 bg-blue-400 text-xs text-white rounded-lg"
                        @click="logout"
                        v-if="userStore.user.id == user.id">
                        Выйти из аккаунта
                    </button>
<!--              <div class="container mt-2" >-->
<!--    <div class="flex">-->
<!--      <button-->
<!--        @click="isOpen = true"-->
<!--        class="inline-block py-4 px-3 bg-blue-400 text-xs text-white rounded-lg"-->
<!--        type="button"-->
<!--        title="Редактировать профиль"-->
<!--      >Редактировать профиль</button>-->

<!--      <div-->
<!--        v-show="isOpen"-->
<!--        class="overflow-hidden-->
<!--          absolute-->
<!--          inset-0-->
<!--          flex-->
<!--          items-center-->
<!--          justify-center-->
<!--          bg-gray-700 bg-opacity-50-->
<!--        "-->
<!--      >-->
<!--        <div class="max-w-2xl p-6 bg-white rounded-md shadow-xl">-->
<!--          <div class="flex items-center justify-between">-->
<!--            <h3 class="text-2xl">Редактирование профиля</h3>-->
<!--            <svg-->
<!--              @click="isOpen = false"-->
<!--              xmlns="http://www.w3.org/2000/svg"-->
<!--              class="w-8 ml-4 h-8 text-red-900 cursor-pointer"-->
<!--              fill="none"-->
<!--              viewBox="0 0 24 24"-->
<!--              stroke="currentColor"-->
<!--            >-->
<!--              <path-->
<!--                stroke-linecap="round"-->
<!--                stroke-linejoin="round"-->
<!--                stroke-width="2"-->
<!--                d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z"-->
<!--              />-->
<!--            </svg>-->
<!--          </div>-->
<!--          <div class="mt-4">-->


<!--                    <div>-->
<!--                        <label>Пароль</label><br>-->
<!--                        <input type="password" v-model="password1" value="password1" placeholder="Введите ваш новый пароль" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">-->
<!--                    </div>-->

<!--                    <div>-->
<!--                        <label>Подтвердите пароль</label><br>-->
<!--                        <input type="password" v-model="password2" value="password2" placeholder="Введите ваш новый пароль еще раз" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">-->
<!--                    </div>-->


<!--            <button-->
<!--              @click="isOpen = false"-->
<!--              class="px-6 py-2 mt-2 text-blue-800 border border-blue-600 rounded"-->
<!--            >-->
<!--              Отменить-->
<!--            </button>-->
<!--            <button @click="editProfile()" class="px-6 py-2 ml-2 text-blue-100 bg-blue-600 rounded">-->
<!--              Сохранить-->
<!--            </button>-->
<!--          </div>-->
<!--        </div>-->
<!--      </div>-->
<!--    </div>-->
<!--  </div>-->
                </div>
            </div>
        </div>

    <div class=" p-4 m-4 bg-white border border-gray-200 text-center rounded-lg">

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
                      <button
                        class="inline-block py-4 px-3 bg-blue-400 text-xs text-white rounded-lg"
                        @click="checkCompositionOrder(order.id)">
                        Посмотреть состав заказа
                    </button>
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
                    <button
                        class="inline-block py-4 px-3 bg-blue-400 text-xs text-white rounded-lg"
                        @click="checkCompositionOrder(order.id)">
                        Посмотреть состав заказа
                    </button>
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
                      <button
                        class="inline-block py-4 px-3 bg-blue-400 text-xs text-white rounded-lg"
                        @click="checkCompositionOrder(order.id)">
                        Посмотреть состав заказа
                    </button>
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
            activeOrders: [],
            canceledOrders:[],
            archiveOrders: [],
            helperOrders: [],
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
                  this.activeOrders = response.data.activeOrders
                  this.canceledOrders = response.data.canceledOrders
                  this.archiveOrders = response.data.archiveOrders

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
      // editProfile(){
      //           axios.
      //                 post('/api/edit_profile/', {'user': this.userStore.user.id, 'password1': this.password1, 'password2': this.password2, 'email': this.email})
      //               .then(response => {
      //
      //                   this.getUser()
      //               })
      //               .catch(error => {
      //                 console.log('error', error)
      //               })
      // }
    }
}
</script>