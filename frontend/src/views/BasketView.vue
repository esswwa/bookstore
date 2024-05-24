<template>
  <div v-if="showCard === false">


  <div class="flex items-center" >

    <div>
      <div class="flex flex-col max-w-sm rounded-lg py-4 p-4 overflow-hidden bg-white shadow-lg focus:outline-none focus:shadow-outline">
        <label for="delivery-points" class="mb-2 font-bold">Пункты выдачи</label>
        <select class="flex flex-col max-w-sm rounded-lg py-4 p-4 overflow-hidden bg-white focus:outline-none focus:shadow-outline hover:bg-gray-100 duration-200 cursor-pointer" v-model="selectedItem" title="Пункты выдачи">
          <option v-for="item in address" :key="item.id" :value="item.id">{{ item.text }}</option>
        </select>
      </div>
    </div>
        <div class="ml-2">
      <div class="flex flex-col max-w-sm rounded-lg p-4 overflow-hidden bg-green-200 shadow-lg">
        Общая стоимость всей корзины:
      {{ all_price }} ₽
      </div>
    </div>
    <div class="flex items-center">
       <button @click="goToOrder()" v-if="check" disabled class="card-button py-4 px-6 ml-4 bg-blue-400 text-white rounded-lg">Оформить заказ</button>
       <button @click="goToOrder()" v-else class="card-button py-4 px-6 ml-4 bg-blue-400 text-white rounded-lg">Оформить заказ</button>
        <div class="ml-4 flex flex-col max-w-sm rounded-lg p-4 overflow-hidden bg-red-200 shadow-lg" v-if="check">
        Заказ невозможно оформить т.к. у вас добавлена книга, которой нет в наличии
      </div>

    </div>
  </div>

 <div class="flex">
  <div class="flex flex-col">
    <div v-for="book in books" :key="book.id" v-if="books.length > 0">
      <div class="card rounded mt-4 p-4 overflow-hidden shadow-lg" :class="{'bg-red-200': book.count_on_stock === 0, 'bg-white': book.count_on_stock > 0 }">
        <div @click="goToBook(book.id)" class="flex hover:bg-gray-100 duration-200 cursor-pointer rounded-lg card-content">
                           <div>
                             <img class="p-2" style="height: 150px; width: 150px;" src="@/assets/preview.jpg" alt="Book cover">
                           </div>
                            <div class="px-6 flex flex-col">
                              <div>
                                 <p class="text-sm text-gray-600 flex items-center" v-if="book.author">
                                <svg v-if="!viewedBooks.includes(book.id)" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                                  <path stroke-linecap="round" stroke-linejoin="round" d="M3.98 8.223A10.477 10.477 0 0 0 1.934 12C3.226 16.338 7.244 19.5 12 19.5c.993 0 1.953-.138 2.863-.395M6.228 6.228A10.451 10.451 0 0 1 12 4.5c4.756 0 8.773 3.162 10.065 7.498a10.522 10.522 0 0 1-4.293 5.774M6.228 6.228 3 3m3.228 3.228 3.65 3.65m7.894 7.894L21 21m-3.228-3.228-3.65-3.65m0 0a3 3 0 1 0-4.243-4.243m4.242 4.242L9.88 9.88" />
                                </svg>
                                <svg v-else xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                                  <path stroke-linecap="round" stroke-linejoin="round" d="M2.036 12.322a1.012 1.012 0 0 1 0-.639C3.423 7.51 7.36 4.5 12 4.5c4.638 0 8.573 3.007 9.963 7.178.07.207.07.431 0 .639C20.577 16.49 16.64 19.5 12 19.5c-4.638 0-8.573-3.007-9.963-7.178Z" />
                                  <path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
                                </svg>
                                {{ book.author.text.split(',')[0] }}
                                </p>
                                <div class="font-bold text-xl mb-2" v-if="book.name">{{book.name.slice(0,50) + (book.name.length > 50 ? '...' : '')}}</div>
                                  <p class="text-gray-700 text-base" v-if="book.description">{{ book.description.slice(0, 200) + (book.name.length > 200 ? '...' : '') }}</p><p class=" rounded-full py-4 text-sm font-semibold">На складе {{ book.count_on_stock}} штук(и)</p>
                                </div>
                              </div>

                                <div class="px-6 py-4">
                                  <span class="px-2 py-1 text-2xl font-semibold text-gray-700" v-if="book.cost_per_one">{{ book.cost_per_one }}₽</span>

                                </div>
                            </div>
  <div class="mx-auto flex items-center px-3 text-sm">
                                      <div class="flex items-center ml-4" v-if="book.rating >= 0">
                                          <svg class="w-4 h-4 text-yellow-300 me-1" v-if="book.rating > 0" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 22 20">
                                              <path d="M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z"/>
                                          </svg>
                                        <svg v-else class="w-4 h-4 ms-1 text-gray-300 dark:text-gray-500" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 22 20">
                                            <path d="M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z"/>
                                        </svg>
                                          <p class="ms-2 text-sm font-bold text-gray-900 dark:text-white">{{book.rating.toFixed(2)}}</p>
                                          <span class="w-1 h-1 mx-1.5 bg-gray-500 rounded-full dark:bg-gray-400"></span>
                                          <RouterLink :to="`/book/${book.id}/1/`" class="text-sm font-medium text-gray-900 underline hover:no-underline dark:text-white">
                                                   {{book.count_rating}} отзывов
                                          </RouterLink>
                                      </div>
                                  </div>
         <div v-for="additional in basket_additionals" :key="additional.id" v-if="basket_additionals.length > 0" >

           <div v-if="additional.book.id === book.id" class="flex items-center text-center">
                  <button @click="addOneMore(book.id)" v-if="additional.count < additional.book.count_on_stock" title="Добавить еще одну штуку" class="py-4 px-6 rounded-lg hover:bg-gray-100 hover:rounded-full duration-200">
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" stroke="#60a5fa" viewBox="0 0 24 24" stroke-width="1.5" class="w-6 h-6 hover:stroke-red-600 duration-200">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M12 4.5v15m7.5-7.5h-15" />
                  </svg>
                </button>
                <button @click="addOneMore(book.id)" v-else disabled title="Добавить еще одну штуку" class="py-4 px-6 rounded-lg hover:bg-gray-100 hover:rounded-full duration-200">
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
      <RouterLink to="/books/" class="hover:underline text-gray-900 text-xl mb-2">
           Ваша корзина пуста, самое время это исправить!
      </RouterLink>
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
          <RouterLink :to="`/composition_order/${orderId}/`" class="text-white no-underline">
                                                   Перейти на страницу заказа
                                          </RouterLink>
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
      viewedBooks: [],
      viewed: [],
            books: {
                id: null
            },
          basket_additionals:[],
          all_price: 0,
          address: [],
          orderId: 0,
          addressOrder: '',
          check:false,
          showCard: false,
          selectedItem: null,
            body: ''
        }
    },
    created() {
      this.getViewedBooks();
        this.getBasket();
      this.getAddress();
    },
    methods:{
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
               getBasket() {
                 console.log("ASDAS", this.userStore.user.id)
                      axios
                          .post(`/api/basket/`, {"user": this.userStore.user.id})
                          .then(response => {
                              console.log('data', response.data.books)

                            this.books = response.data.books
                            this.check = false;
                             for (var i in this.books) {
                                  if (this.books[i].count_on_stock === 0) {
                                      this.check = true;
                                      break; // Exit the loop once a book with count_on_stock 0 is found
                                  }
                              }
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