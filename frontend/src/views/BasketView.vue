<template>
<!--    <div class="flex">-->
<!--    <div class="flex flex-col">-->
<!--      <div v-for="book in books" :key="book.id" v-if="books.length > 0">-->
<!--       <div class="flex flex-col rounded mt-4 p-4 overflow-hidden bg-white shadow-lg">-->
<!--      <div>-->
<!--         <div class="px-6 py-4">-->
<!--         <p class="text-sm text-gray-600 flex items-center">-->
<!--                                  <svg class="fill-current text-gray-500 w-3 h-3 mr-2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">-->
<!--                                    <path d="M4 8V6a6 6 0 1 1 12 0v2h1a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-8c0-1.1.9-2 2-2h1zm5 6.73V17h2v-2.27a2 2 0 1 0-2 0zM7 6v2h6V6a3 3 0 0 0-6 0z" />-->
<!--                                  </svg>-->
<!--                                  {{book.additional_genre.text_genre.text}}, {{book.author.text}}-->
<!--                                </p>-->
<!--        <div class="font-bold text-xl mb-2">{{ book.name }}</div>-->
<!--        <p class="text-gray-700 text-base">{{ book.description }}</p>-->
<!--      </div>-->
<!--      <div class="px-6 py-4">-->
<!--        <span class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700">Цена: {{ book.cost_per_one }}₽</span>-->
<!--        <span class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 ml-2">Рейтинг: {{book.rating}}</span>-->

<!--      </div>-->

<!--      <div class="px-6 " >-->
<!--        <button @click="goToBook(book.id)" class="py-4 px-6 bg-blue-400 text-white rounded-lg">Перейти</button>-->
<!--      </div>-->
<!--      </div>-->


<!--    </div>-->
<!--      </div>-->
<!--    </div>-->

<!--    <div class="flex flex-col">-->
<!--            <div v-for="additional in basket_additionals" :key="additional.id" v-if="basket_additionals.length > 0">-->
<!--               <div class="flex flex-col ml-4 mt-4 p-4 overflow-hidden bg-white shadow-lg">-->
<!--                      <div class="px-6 py-4 mt-4" >-->
<!--                      <div class="font-bold text-xl mb-2">Количество: {{ additional.count }}</div>-->
<!--                      <div class="font-bold text-xl mb-2">Цена за книги: {{ additional.all_price }}</div>-->
<!--               </div>-->
<!--            </div>-->
<!--    </div>-->
<!--    </div>-->

<!--    <div class="w-full">-->
<!--      <div class="flex flex-col max-w-sm rounded mt-4 p-4 overflow-hidden bg-white shadow-lg">-->
<!--        Общая стоимость всей корзины:-->
<!--      {{ all_price }}-->
<!--      </div>-->
<!--    </div>-->
<!--  </div>-->

  <div class="flex">
  <div class="flex flex-col">
    <div v-for="book in books" :key="book.id" v-if="books.length > 0">
      <div class="card rounded mt-4 p-4 overflow-hidden bg-white shadow-lg">
        <div class="card-content">
          <div class="px-6 py-4">
            <p class="text-sm text-gray-600 flex items-center">
              <svg class="fill-current text-gray-500 w-3 h-3 mr-2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                <path d="M4 8V6a6 6 0 1 1 12 0v2h1a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-8c0-1.1.9-2 2-2h1zm5 6.73V17h2v-2.27a2 2 0 1 0-2 0zM7 6v2h6V6a3 3 0 0 0-6 0z" />
              </svg>
              {{book.additional_genre.text_genre.text}}, {{book.author.text}}
            </p>
            <div class="font-bold text-xl mb-2">{{ book.name }}</div>
            <p class="text-gray-700 text-base">{{ book.description }}</p>
          </div>
          <div class="px-6 py-4">
            <span class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700">Цена: {{ book.cost_per_one }}₽</span>
            <span class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 ml-2">Рейтинг: {{book.rating}}</span>
          </div>
        </div>
        <div class="card-footer px-6">
          <button @click="goToBook(book.id)" class="card-button py-4 px-6 bg-blue-400 text-white rounded-lg">Перейти</button>
        </div>
            <button @click="addOneMore(book.id)" title="Добавить еще одну штуку" class="py-4 m-6 px-6 text-black rounded-lg border border-black">
              <svg xmlns="http://www.w3.org/2000/svg" fill="#60a5fa" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round" d="M12 4.5v15m7.5-7.5h-15" />
              </svg>
            </button>
              {{count}}
           <button @click="deleteOneMore(book.id)" class="py-4 px-6 text-black rounded-lg  border border-black" title="Добавить в избранные">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M5 12h14" />
                </svg>
           </button>
      </div>
    </div>
  </div>

  <div class="flex flex-col">
    <div v-for="additional in basket_additionals" :key="additional.id" v-if="basket_additionals.length > 0">
      <div class="card ml-4 mt-4 p-4 overflow-hidden bg-white shadow-lg">
        <div class="card-content">
          <div class="px-6 py-4 mt-4">
            <div class="font-bold text-xl mb-2">Количество: {{ additional.count }}</div>
            <div class="font-bold text-xl mb-2">Цена за книги: {{ additional.all_price }}</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
      <div class="w-full">
      <div class="flex flex-col max-w-sm rounded mt-4 p-4 overflow-hidden bg-white shadow-lg">
        Общая стоимость всей корзины:
      {{ all_price }}
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
            body: ''
        }
    },
    created() {
        this.getBasket()
    },
    methods:{
        goToBook(bookId) {
          this.$router.push({ path: '/book/' + bookId + '/'});
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
    }
  }
</script>