<template>
  <div class="flex flex-col">
  <div v-for="book in books" :key="book.id" v-if="books.length > 0">
    <div class="max-w-sm rounded overflow-hidden bg-white shadow-lg">

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

      <div class="px-6 " >
        <button @click="goToBook(book.id)" class="py-4 px-6 bg-blue-400 text-white rounded-lg">Перейти</button>
      </div>

    </div>
  </div>
</div>

  <div v-for="additional in basket_additionals" :key="additional.id" v-if="basket_additionals.length > 0">
 <div class="px-6 py-4">
        <div class="font-bold text-xl mb-2">{{ additional.count }}</div>
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
                            console.log('basket', this.books)
                            console.log('basket_additionals',this.basket_additionals )
                          })
                          .catch(error => {
                              console.log('error', error)
                          })

              }
    }
  }
</script>