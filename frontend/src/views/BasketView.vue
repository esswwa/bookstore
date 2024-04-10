<template>
  <div v-if="showCard === false">


  <div class="flex items-center" >
    <div class="">
      <div class="flex flex-col max-w-sm rounded-lg p-4 overflow-hidden bg-white shadow-lg">
        Общая стоимость всей корзины:
      {{ all_price }} ₽
      </div>
    </div>
    <div>
      <select class="flex flex-col max-w-sm rounded-lg py-4 ml-4 p-4 overflow-hidden bg-white shadow-lg focus:outline-none focus:shadow-outline" v-model="selectedItem">
        <option v-for="item in address" :key="item.id" :value="item.id">{{ item.text }}</option>
      </select>
    </div>
    <div class="">
       <button @click="goToOrder()" class="card-button py-4 px-6 ml-4 bg-blue-400 text-white rounded-lg">Оформить заказ</button>
    </div>
  </div>

 <div class="flex">
  <div class="flex flex-col">
    <div v-for="book in books" :key="book.id" v-if="books.length > 0">
      <div class="card rounded mt-4 p-4 overflow-hidden bg-white shadow-lg">
        <div @click="goToBook(book.id)" class="hover:bg-gray-100 duration-200 cursor-pointer rounded-lg card-content">
          <div class="px-6 py-4">
            <p class="text-sm text-gray-600 flex items-center">
              <svg class="fill-current text-gray-500 w-3 h-3 mr-2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                <path d="M4 8V6a6 6 0 1 1 12 0v2h1a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-8c0-1.1.9-2 2-2h1zm5 6.73V17h2v-2.27a2 2 0 1 0-2 0zM7 6v2h6V6a3 3 0 0 0-6 0z" />
              </svg>
                                   {{ book.author.text.split(',')[0] }}
            </p>
            <div class="font-bold text-xl mb-2">{{book.name.slice(0,50) + (book.name.length > 50 ? '...' : '')}}</div>
            <p class="text-gray-700 text-base">{{ book.description.slice(0, 200) + (book.name.length > 200 ? '...' : '') }}</p>
          </div>
          <div class="px-6 py-4">
            <span class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700">Цена: {{ book.cost_per_one }} ₽</span>
          </div>
        </div>
  <div class="mx-auto flex items-center px-3 text-sm">
                                      <div class="flex items-center m-2">
                                          <svg class="w-4 h-4 text-yellow-300 me-1" v-if="book.rating > 0" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 22 20">
                                              <path d="M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z"/>
                                          </svg>
                                        <svg v-else class="w-4 h-4 ms-1 text-gray-300 dark:text-gray-500" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 22 20">
                                            <path d="M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z"/>
                                        </svg>
                                          <p class="ms-2 text-sm font-bold text-gray-900 dark:text-white">{{book.rating}}</p>
                                          <span class="w-1 h-1 mx-1.5 bg-gray-500 rounded-full dark:bg-gray-400"></span>
                                          <a :href="`http://localhost:5173/book/${book.id}/1/`" class="text-sm font-medium text-gray-900 underline hover:no-underline dark:text-white">{{book.count_rating}} отзывов</a>
                                      </div>
                                  </div>
         <div v-for="additional in basket_additionals" :key="additional.id" v-if="basket_additionals.length > 0" >

           <div v-if="additional.book.id === book.id" class="flex items-center text-center">
                  <button @click="addOneMore(book.id)" title="Добавить еще одну штуку" class="py-4 px-6 rounded-lg hover:bg-gray-100 hover:rounded-full duration-200">
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" stroke="#60a5fa" viewBox="0 0 24 24" stroke-width="1.5" class="w-6 h-6 hover:stroke-red-600 duration-200">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M12 4.5v15m7.5-7.5h-15" />
                  </svg>
                </button>
                  <div>{{additional.count}}</div>

               <button @click="deleteOneMore(book.id)" class="py-4 px-6 rounded-lg hover:bg-gray-100 hover:rounded-full duration-200" title="Уменьшить количество или полностью удалить из корзины">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" stroke="#60a5fa" viewBox="0 0 24 24" stroke-width="1.5" class="w-6 h-6 hover:stroke-red-600 duration-200">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M5 12h14" />
                    </svg>
               </button>

               <div class="text-xl mb-2">Цена за все книги: {{ additional.all_price }} ₽</div>

           </div>

        </div>

      </div>
    </div>
    <div v-else>
      <div class="card rounded mt-4 p-8 overflow-hidden bg-white shadow-lg">
           <a href="http://localhost:5173/books/" class="hover:underline text-gray-900 text-xl mb-2">Ваша корзина пуста, самое время это исправить!</a>
      </div>
    </div>
  </div>
</div>
  </div>
<div v-else>
  <div class="card rounded mt-4 p-4 overflow-hidden bg-white shadow-lg">
    <div class="container mx-auto p-5 flex flex-col items-center">

      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="green" class="w-20 h-20">
        <path stroke-linecap="round" stroke-linejoin="round" d="M21 11.25v8.25a1.5 1.5 0 0 1-1.5 1.5H5.25a1.5 1.5 0 0 1-1.5-1.5v-8.25M12 4.875A2.625 2.625 0 1 0 9.375 7.5H12m0-2.625V7.5m0-2.625A2.625 2.625 0 1 1 14.625 7.5H12m0 0V21m-8.625-9.75h18c.621 0 1.125-.504 1.125-1.125v-1.5c0-.621-.504-1.125-1.125-1.125h-18c-.621 0-1.125.504-1.125 1.125v1.5c0 .621.504 1.125 1.125 1.125Z" />
      </svg>

      <h1 class="text-4xl text-center text-gray-800">Спасибо за заказ!</h1>
      <p class="text-xl text-center text-gray-600">Номер вашего заказа: {{orderId}}</p>
      <p class="text-xl text-center text-gray-600">Заказ будет доставлен в пункт выдачи: {{addressOrder}}</p>
      <p class="text-xl text-center text-gray-600">Общая стоимость вашего заказа: {{all_price}} ₽</p>
      <div class="flex justify-center mt-5">
        <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
          <a :href="`http://localhost:5173/composition_order/${orderId}/`"
             class="text-white no-underline">Перейти на страницу заказа</a>
        </button>
      </div>
    </div>
  </div>
</div>
</template>

<script>

import axios from 'axios'
import {useUserStore} from "@/stores/user.js";
export default {
    name: 'BasketView',
    setup(){
       const userStore = useUserStore()
       return{
         userStore
       }
     },
    data() {
        return {
            books: {
                id: null
            },
          basket_additionals:[],
          all_price: 0,
          address: [],
          orderId: 0,
          addressOrder: '',
          showCard: false,
          selectedItem: null,
            body: ''
        }
    },
    created() {
        this.getBasket();
      this.getAddress();
    },
    methods:{
        goToBook(bookId) {
      this.$router.push({ path: `/book/${bookId}/1/` });
          console.log("Переход к книге с ID:", bookId);
    },
               getBasket() {
                 console.log("ASDAS", this.userStore.user.id)
                      axios
                          .post(`/api/basket/`, {"user": this.userStore.user.id})
                          .then(response => {
                              console.log('data', response.data.books)

                            this.books = response.data.books
                            this.basket_additionals = response.data.basket_additionals
                            this.all_price = response.data.all_price
                            console.log('basket', this.books)
                            console.log('basket_additionals',this.basket_additionals )
                          })
                          .catch(error => {
                              console.log('error', error)
                          })

              },
              addOneMore(bookId){
                  axios
                          .post(`/api/basket/add_to_basket/`, {"user": this.userStore.user.id, "book": bookId})
                          .then(response => {

                            this.getBasket()

                          })
                          .catch(error => {
                              console.log('error', error)
                          })


              },
              deleteOneMore(bookId){
                        axios
                          .post(`/api/basket/delete_one_more/`, {"user": this.userStore.user.id, "book": bookId})
                          .then(response => {

                            this.getBasket()

                          })
                          .catch(error => {
                              console.log('error', error)
                          })



              },
      getAddress(){
          axios.get('/api/order/get_address/')
              .then(response => {

                console.log('address', response.data.address)
                this.address = response.data.address
                this.selectedItem = 1
              })
              .catch(error => {

                console.log('error', error)
              })
      },
      goToOrderHelper(basket_additionals_list, order){
          axios.post('/api/order/add_helper_order/', {
            'basket_additionals_list': basket_additionals_list,
            'order': order
          })
              .then(response => {

              })
          .catch(error => {
                              console.log('error', error)
                          })
      },
          goToOrder( ){
          console.log('selected_item', this.selectedItem)
                        axios
                          .post(`/api/order/add_order/`, {"user": this.userStore.user.id, "basket_additionals": this.basket_additionals[0].id, "all_price": this.all_price, 'selected_item': this.selectedItem})
                          .then(response => {
                            this.showCard = true
                            this.orderId = response.data.order.id
                            this.addressOrder = response.data.address
                            this.goToOrderHelper(response.data.basket_additionals_list, response.data.order)
                          })
                          .catch(error => {
                              console.log('error', error)
                          })



              },
    }
  }
</script>