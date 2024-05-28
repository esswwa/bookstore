<template>
  <div class="flex items-center">
      <div class="max-w-7xl mx-auto">
          <div class="main-center col-span-3 space-y-4">
              <div class="text-center text-black py-4 px-6">
                  <h1 class="text-4xl font-bold">ВCЕ ЗАКАЗЫ</h1>
              </div>
          </div>
      </div>

      <div class="container flex" >
        <div class="mt-4 ml-2">
              <input v-model="searchInput" placeholder="Поиск" class="flex flex-col max-w-sm rounded-lg py-4 mb-4 p-4 overflow-hidden shadow-lg focus:outline-none focus:shadow-outline"/>
            </div>
         <div class="mt-4 ml-2">
              <select v-model="sortOrder" class="flex flex-col max-w-sm rounded-lg py-4 mb-4 p-4 overflow-hidden shadow-lg focus:outline-none focus:shadow-outline">
                <option value="Без сортировки">Без сортировки</option>
                <option value="all_price">По цене</option>
                <option value="status">По статусу</option>
                <option value="date_order">По дате оформления заказа</option>
              </select>
            </div>
        <div class="flex items-center">
            <button @click="saveOptions()" class="px-6 py-2 ml-2 text-blue-100 bg-blue-400 rounded">
               Сохранить
          </button>
        </div>

        <div class="flex items-center">
             <button v-if="(selectedFilter != '' && selectedFilter != null) || sortOrder !== 'Без сортировки' || searchInput !== ''" @click="resetFilters()" class="px-6 py-2 ml-2 text-blue-100 bg-blue-400 rounded" title="Сбросить фильтры">
              Сбросить сортировку и фильтры
          </button>
        </div>


      </div>
  </div>


<div class="flex">

  <div class="max-w-s rounded-2xl overflow-hidden bg-white shadow-lg m-2 min-w-max">
      <div class="card flex p-6" v-if="genres.length > 0">
        <div class="flex flex-col">
<!--          <div class="text-gray-900 font-medium text-xl mt-4 mb-2">-->
<!--            Поиск по книгам-->
<!--          </div>-->

<!--          <div class="text-gray-900 font-medium text-xl mt-4 mb-2">-->
<!--            Сортировка по цене и рейтингу-->
<!--          </div>-->

          <div class="text-gray-900 font-medium text-xl mb-2">
            Статусы
          </div>
            <div v-for="genre of genres" :key="genre.id" class="flex items-center">

                <Checkbox v-model="selectedFilter" :inputId="genre.id" name="genre" :value="genre.id" />
                <label class="p-2" :for="genre.id">{{ genre.text }}</label>
            </div>
        </div>
    </div>
  </div>

<div class="flex flex-wrap" v-if="orders.length > 0">
        <div v-for="order in orders" :key="order.id" class="w-1/3 p-2 min-w-max">
          <div @contextmenu="onContextMenu($event, order.id, order.status)" @click="checkCompositionOrder(order.id)" title="Перейти на заказ" class="hover:bg-gray-100 duration-200 p-4 cursor-pointer max-w-sm rounded overflow-hidden bg-white shadow-lg">
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
              <div class="text-gray-700 text-xl mb-2">Пункт выдачи: {{ order.address.text }}</div>
              <p class="text-gray-700 text-base">Дата оформления заказа: {{new Date(order.date_order).toLocaleString('ru-RU', { day: '2-digit', month: '2-digit', year: 'numeric' })}}</p>
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
              <div class="text-gray-700 text-xl mb-2">Пункт выдачи: {{ order.address.text }}</div>
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
              <div class="text-gray-700 text-xl mb-2">Пункт выдачи: {{ order.address.text }}</div>
              <p class="text-gray-700 text-base">Общая стоимость заказа: {{ order.all_price }} ₽</p>
              <p class="text-gray-700 text-base">Дата оформления заказа: {{new Date(order.date_order).toLocaleString('ru-RU', { day: '2-digit', month: '2-digit', year: 'numeric' })}}</p>
            </div>
          </div>
        </div>
    </div>
  <div v-else class="flex flex-col items-center p-6">
    Книги с необходимыми вам параметрами отсутствуют
    <button @click="resetFilters()" class="py-4 px-6 m-4 bg-blue-400 text-white rounded-lg" title="Сбросить фильтры">
        Сбросить фильтры
    </button>
  </div>
  </div>

<VuePagination
    v-if="orders.length > 0"
      :total="total"
      v-model:value="currentPage"
      :perPage="perPage"
      @set="changePage" />


</template>


<script>
import axios from 'axios';
import { useUserStore } from "@/stores/user.js";
import {SwiperSlide} from "swiper/vue";

export default {
  components: {SwiperSlide},
  data() {
    return {
      viewedBooks: [],
      viewed: [],
      orders: [],
      searchInput: '',
      total: 0, // Устанавливаем начальное значение total
      perPage: 12,
      currentPage: 1,
      sortOrder: 'Без сортировки',
      isOpen: false,
      pizza: null,
      genres: [],
      selectedFilter: null

    };
  },
  created() {
    this.userStore = useUserStore() // Устанавливаем total после получения данных
    this.getOrder();
    this.getGenre();
  },
  methods: { onContextMenu(e, orderId, status) {
    //prevent the browser's default menu
    e.preventDefault();
    //show our menu
      console.log('status', status)
      if(status === "В пути" ){

            this.$contextmenu({
        x: e.x,
        y: e.y,
        items: [
          {
            label: "Изменить статус заказа на 'В пункте выдачи'",
            children: [
              { label: "Подтвердить изменение статуса",
                onClick: () => {
                  this.statusChanged("В пункте выдачи", orderId)}
              },
            ]
          },
            {
            label: "Изменить статус заказа на 'Отменен'",
            children: [
              { label: "Подтвердить изменение статуса",
                onClick: () => {
                  this.statusChanged("Отменен", orderId)}
              },
            ]
          },
        ]
    })
      }
      else if(status === "Оформлен" ){
               this.$contextmenu({
        x: e.x,
        y: e.y,
        items: [
          {
            label: "Изменить статус заказа на 'В пути'",
            children: [
              { label: "Подтвердить изменение статуса",
                onClick: () => {
                  this.statusChanged("В пути", orderId)}
              },
            ]
          },
            {
            label: "Изменить статус заказа на 'Отменен'",
            children: [
              { label: "Подтвердить изменение статуса",
                onClick: () => {
                  this.statusChanged("Отменен", orderId)}
              },
            ]
          },
        ]
    })
      }
       else if(status === "В пункте выдачи" ){
               this.$contextmenu({
        x: e.x,
        y: e.y,
        items: [
          {
              label: "Продлить срок хранения",
               children: [
                { label: "Продлить срок хранения на 7 дней.",
                  onClick: () => {
                    this.orderRenewalDate("7", orderId)}
                },
                   { label: "Продлить срок хранения на 14 дней.",
                  onClick: () => {
                    this.orderRenewalDate("14", orderId)}
                },
                   { label: "Продлить срок хранения на 21 день.",
                  onClick: () => {
                    this.orderRenewalDate("21", orderId)}
                },
                   { label: "Продлить срок хранения на 28 дней.",
                  onClick: () => {
                    this.orderRenewalDate("28", orderId)}
                },
            ]
          },
          {
            label: "Изменить статус заказа на 'Завершен'",
            children: [
              { label: "Подтвердить изменение статуса",
                onClick: () => {
                  this.statusChanged("Завершен", orderId)}
              },
            ]
          },
            {
            label: "Изменить статус заказа на 'Не выкуплен'",
            children: [
              { label: "Подтвердить изменение статуса",
                onClick: () => {
                  this.statusChanged("Не выкуплен", orderId)}
              },
            ]
          },
        ]
    })
      }
},
    orderRenewalDate(date, orderId){
        axios
            .post('/api/order/order_renewal_date/', {'date': date, 'order_id': orderId})
            .then(response => {
                this.getOrder()
            })
            .catch(error=>{
              console.log('error', error)
            })
    },

    getOrder(){
        if (this.$route.params.page) {
            axios
                .post(`/api/order/admin_orders/${this.$route.params.page}/`, {'search_input': this.searchInput, 'selected_filter': this.selectedFilter, 'sort_order': this.sortOrder})
                .then(response => {
                  console.log('data', response.data.books);
                  this.orders = response.data.orders;
                  this.total = response.data.count;
                })
                .catch(error => {
                  console.log('error', error);
                });
        }
    },
    statusChanged(status, orderId){
        axios
            .post('/api/order/change_status/', {'status': status, 'order_id': orderId})
            .then(response => {
                this.getOrder()
            })
            .catch(error=>{
              console.log('error', error)
            })
    },
    changePage(page) {
      this.$router.push({ path: `/admin_orders/${page}/` });
    },
    checkCompositionOrder(orderId){
            this.$router.push(`/composition_order/${orderId}/`)
      },
    getGenre(){
      const statusList = [
        { id: 1, text: "Оформлен" },
        { id: 2, text: "В пути" },
        { id: 3, text: "В пункте выдачи" },
        { id: 4, text: "Завершен" },
        { id: 5, text: "Отменен" },
        { id: 6, text: "Не выкуплен" }
      ];
      this.genres = statusList;
    },
    saveOptions(){
      console.log('selected', this.selectedFilter)
        this.getOrder();
      this.isOpen = false
    },
    resetFilters(){
      this.selectedFilter = null;
      this.sortOrder = 'Без сортировки'
      this.searchInput = ''
      this.getOrder();
    },
  },

  watch: {
    '$route': function(newRoute, oldRoute) {
      if (this.$route.params.page) {
        this.getOrder();
      }
    },
  },
};
</script>

