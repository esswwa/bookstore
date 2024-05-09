<template>
<div class="max-w-7xl mx-auto rounded-lg overflow-hidden bg-white shadow-lg flex flex-col items-center w-1/2 p-2" v-if="book">

      <div class="px-6 py-4 flex flex-col items-center">
        <div  v-if="book.genre">
           <p class="text-sm text-gray-600 flex items-center" v-if="book.additional_genre">
                                  <svg class="fill-current text-gray-500 w-3 h-3 mr-2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                                    <path d="M4 8V6a6 6 0 1 1 12 0v2h1a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-8c0-1.1.9-2 2-2h1zm5 6.73V17h2v-2.27a2 2 0 1 0-2 0zM7 6v2h6V6a3 3 0 0 0-6 0z" />
                                  </svg>
                                  {{book.genre.text}}, {{book.additional_genre.text_additional}}, {{book.author.text}}
         </p>
        <p class="text-sm text-gray-600 flex items-center" v-else>
                                  <svg class="fill-current text-gray-500 w-3 h-3 mr-2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                                    <path d="M4 8V6a6 6 0 1 1 12 0v2h1a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-8c0-1.1.9-2 2-2h1zm5 6.73V17h2v-2.27a2 2 0 1 0-2 0zM7 6v2h6V6a3 3 0 0 0-6 0z" />
                                  </svg>
                                  {{book.genre.text}}, {{book.author.text}}
         </p>
        </div>


        <div class="font-bold text-xl mb-2">{{ book.name }}</div>
        <div class="flex">
          <img class="p-2 rounded" height="300px" width="400px" src="@/assets/preview.jpg" alt="Book cover">
          <div class="flex flex-col items-center p-2">
                <p class="text-gray-700 text-base" v-if="book.description">{{book.description.slice(0, 700) + (book.description.length > 700 ? '...' : '')}}</p>
                </div>

                    <div class="px-2 flex flex-col">
                      <span class="flex px-3 text-2xl font-semibold text-gray-500">{{ book.cost_per_one }}₽</span>
                      <div class="mt-4">
                                  <button v-if="favourites.includes(book.id)" @click="deleteFavourite(book.id)" title="Удалить из избранных" class="py-4 px-6 text-white rounded-lg hover:bg-gray-100 hover:rounded-full  duration-200">
                                     <svg xmlns="http://www.w3.org/2000/svg" fill="#60a5fa" stroke="isCurrent" viewBox="0 0 24 24" stroke-width="1.5" class="w-6 h-6">
                                          <path stroke-linecap="round" stroke-linejoin="round" d="M17.593 3.322c1.1.128 1.907 1.077 1.907 2.185V21L12 17.25 4.5 21V5.507c0-1.108.806-2.057 1.907-2.185a48.507 48.507 0 0 1 11.186 0Z" />
                                     </svg>
                                  </button>
                                  <button v-else @click="addBookToFavourite(book.id)" class="py-4 px-6 text-white rounded-lg hover:bg-gray-100 hover:rounded-full  duration-200" title="Добавить в избранные">
                                      <svg xmlns="http://www.w3.org/2000/svg" fill="none" stroke="#60a5fa" viewBox="0 0 24 24" stroke-width="1.5" class="w-6 h-6 hover:stroke-red-600 duration-200">
                                           <path stroke-linecap="round" stroke-linejoin="round" d="M17.593 3.322c1.1.128 1.907 1.077 1.907 2.185V21L12 17.25 4.5 21V5.507c0-1.108.806-2.057 1.907-2.185a48.507 48.507 0 0 1 11.186 0Z" />
                                      </svg>
                                    </button>
                               <button v-if="baskets.includes(book.id)" @click="deleteBookFromBasket(book.id)" class="py-4 px-6 text-white rounded-lg hover:bg-gray-100 hover:rounded-full duration-200" title="Удалить из корзины">
                                    <svg xmlns="http://www.w3.org/2000/svg" fill="#60a5fa" viewBox="0 0 24 24" stroke-width="1.5" class="w-6 h-6">
                                      <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 3h1.386c.51 0 .955.343 1.087.835l.383 1.437M7.5 14.25a3 3 0 0 0-3 3h15.75m-12.75-3h11.218c1.121-2.3 2.1-4.684 2.924-7.138a60.114 60.114 0 0 0-16.536-1.84M7.5 14.25 5.106 5.272M6 20.25a.75.75 0 1 1-1.5 0 .75.75 0 0 1 1.5 0Zm12.75 0a.75.75 0 1 1-1.5 0 .75.75 0 0 1 1.5 0Z" />
                                    </svg>
                                  </button>
                                  <button v-else @click="addBookToBasket(book.id)" class="py-4 px-6 text-white rounded-lg hover:bg-gray-100 hover:rounded-full  duration-200" title="Добавить в корзину">
                                      <svg xmlns="http://www.w3.org/2000/svg" fill="none" stroke="#60a5fa" viewBox="0 0 24 24" stroke-width="1.5" class="w-6 h-6 hover:stroke-red-600 duration-200">
                                        <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 3h1.386c.51 0 .955.343 1.087.835l.383 1.437M7.5 14.25a3 3 0 0 0-3 3h15.75m-12.75-3h11.218c1.121-2.3 2.1-4.684 2.924-7.138a60.114 60.114 0 0 0-16.536-1.84M7.5 14.25 5.106 5.272M6 20.25a.75.75 0 1 1-1.5 0 .75.75 0 0 1 1.5 0Zm12.75 0a.75.75 0 1 1-1.5 0 .75.75 0 0 1 1.5 0Z" />
                                      </svg>
                                  </button>
                </div>
                    </div>
                </div>
                <div class="">
                    <p class="text-sm text-gray-600 flex items-center">Год издания:    {{book.date_of_create}}</p>
                    <p class="text-sm text-gray-600 flex items-center mt-2">ISBN:    {{book.isbn}}</p>
                    <p class="text-sm text-gray-600 flex items-center mt-2">Количество страниц:    {{book.count_of_pages}}</p>
                    <p class="text-sm text-gray-600 flex items-center mt-2">Размер:   {{book.size}}</p>
                    <p class="text-sm text-gray-600 flex items-center mt-2">Тип обложки:    {{book.type_cover}}</p>
                    <p class="text-sm text-gray-600 flex items-center mt-2">Вес, г:     {{book.weight}}</p>
                    <p class="text-sm text-gray-600 flex items-center mt-2" v-if="book.age_restrictions">Возрастные ограничения:     {{book.age_restrictions}}</p>
                </div>
                        <div class="mx-auto flex items-center px-3 text-sm mt-4">
                                      <div class="flex items-center">
                                          <svg class="w-4 h-4 text-yellow-300 me-1" v-if="book.rating > 0" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 22 20">
                                              <path d="M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z"/>
                                          </svg>
                                        <svg v-else class="w-4 h-4 ms-1 text-gray-300 dark:text-gray-500" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 22 20">
                                            <path d="M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z"/>
                                        </svg>
                                          <p class="ms-2 text-sm font-bold text-gray-900 dark:text-white">{{book.rating}}</p>
                                          <span class="w-1 h-1 mx-1.5 bg-gray-500 rounded-full dark:bg-gray-400"></span>
<RouterLink :to="`/book/${book.id}/1/`" class="text-sm font-medium text-gray-900 underline hover:no-underline dark:text-white">
                                                   {{book.count_rating}} отзывов
                                            </RouterLink>                                      </div>
                                  </div>

        </div>

      </div>


  <div class="max-w-7xl mx-auto rounded overflow-hidden bg-white shadow-lg mt-4 flex flex-col  w-1/3 p-2">

    <div class="flex flex-col items-center justify-center text-center" >
            <div class="px-6 py-4 flex flex-col items-center">
        <div class="font-bold text-xl mb-2">Отзывы</div>
        <span class="inline-block px-3 py-1 text-sm font-semibold text-gray-700 ml-2">Рейтинг: {{book.rating}}</span>
      </div>
      <div class="flex flex-row items-center">
        <div v-if="check === false" class="flex flex-col items-center">
          <input v-model="review" class="bg-white shadow-md m-2 rounded-lg p-3 focus:outline-none focus:ring focus:ring-blue-400" type="text" placeholder="Введите отзыв">
          <input v-model="rating" class="bg-white shadow-md m-2 rounded-lg p-3 focus:outline-none focus:ring focus:ring-blue-400" type="number" min="0" max="5" placeholder="Введите рейтинг">

          <button @click="addReview(book.id)" class="inline-block py-4 px-3 bg-blue-400 text-xs text-white rounded-lg" title="Добавить отзыв">
            Добавить отзыв
          </button>
          <div v-if="showReview === true">
                Заполните отзыв и указывайте корректный рейтинг
          </div>

        </div >

      </div>
    </div>




  <div class="flex flex-col">
              <div v-for="review1 in reviews" :key="review1.id" class="p-2">
                <div class="rounded overflow-hidden bg-gray-200 shadow-lg">
                  <div class="px-6 py-4">
                     <p class="text-sm text-gray-600 flex items-center">
                        <svg class="fill-current text-gray-500 w-3 h-3 mr-2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                          <path d="M4 8V6a6 6 0 1 1 12 0v2h1a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-8c0-1.1.9-2 2-2h1zm5 6.73V17h2v-2.27a2 2 0 1 0-2 0zM7 6v2h6V6a3 3 0 0 0-6 0z" />
                        </svg>
                        {{review1.user.name}}, {{new Date(review1.date_review).getDay()}}.{{new Date(review1.date_review).getMonth()}}.{{new Date(review1.date_review).getFullYear()}}
                     </p>
                    <div class="font-bold text-xl mb-2">Рейтинг: {{ review1.rating }}</div>
                    <p class="text-gray-700 text-base">Отзыв: {{ review1.review }}</p>
                  </div>
                </div>
              </div>
          </div>

    </div>

  <VuePagination

    v-if="reviews.length > 0"
        :total="total"
      v-model:value="currentPage"
      :perPage="perPage"
      @set="changePage" />
</template>


<script>

import axios from 'axios'
import {useUserStore} from "@/stores/user.js";
export default {
    name: 'FavouriteView',
  setup(){
       const userStore = useUserStore()
       return{
         userStore
       }
     },
    data() {
        return {
            book: {
                id: null
            },
          total: 0, // Устанавливаем начальное значение total
          perPage: 5,
          currentPage: 1,
          showReview: false,
      favourite: [],
          reviews: [],
      favourites: [],
            basket: [],
            baskets: [],
          check: false,
          review: '',
          rating: 0,

        }
    },
    created() {
    this.getBook();
    this.getFavourite();
    this.getBasket();
    this.getReview();
    },
    methods:{
               getBook() {
                console.log("id", this.$route.params.id)
                      axios
                          .get(`/api/book/${this.$route.params.id}/`)
                          .then(response => {
                              console.log('data', response.data.book)
                              this.book = response.data.book
                          })
                          .catch(error => {
                              console.log('error', error)
                          })

              },
    getFavourite() {
                 console.log("ASDAS", this.userStore.user.id)
                      axios
                          .post(`/api/favourite/`, {"user": this.userStore.user.id})
                          .then(response => {
                              console.log('data', response.data.favourites)

                              this.favourite = response.data.favourites
                            this.favourites = this.favourite.map(item => item.id)
                            console.log("favourites", this.favourites)
                          })
                          .catch(error => {
                              console.log('error', error)
                          })

              },
               addBookToFavourite(bookId){
          axios.post('/api/favourite/add_to_favourite/',{
                "book_id": bookId,
                "user_id": localStorage.getItem('user.id')
              })
              .then(response => {
                console.log("book_id", response.data.book_id)
                console.log("user_id", response.data.user_id)
                console.log("message", response.data.message)
                console.log("fav", response.data.favourite)
               this.getFavourite()

              })
              .catch(error => {
                console.log("error", error)

              }) },
  deleteFavourite(bookId) {

       axios
           .post(`/api/favourite/delete_favourite/`, {"user": this.userStore.user.id, "book": bookId})
           .then(response => {
               console.log("message", response.data.message);
               this.getFavourite()
           })
           .catch(error => {
               console.log('error', error)
           }) },

          getBasket() {
                console.log("ASDAS", this.userStore.user.id)
                      axios
                          .post(`/api/basket/`, {"user": this.userStore.user.id})
                          .then(response => {
                              console.log('data', response.data.baskets)

                              this.basket = response.data.books
                            this.baskets = this.basket.map(item => item.id)
                            console.log("baskets", this.baskets)
                          })
                          .catch(error => {
                              console.log('error', error)
                          })

          },
               addBookToBasket(bookId){
          axios.post('/api/basket/add_to_basket/',{ "book": bookId, "user": localStorage.getItem('user.id') })
              .then(response => {
                console.log("book_id", response.data.book_id)
                console.log("user_id", response.data.user_id)
                console.log("message", response.data.message)
                console.log("fav", response.data.favourite)
               this.getBasket();

              })
              .catch(error => {
                console.log("error", error)

              }) },
              deleteBookFromBasket(bookId) {

                   axios
                       .post(`/api/basket/delete_basket/`, {"user": this.userStore.user.id, "book": bookId})
                       .then(response => {
                           console.log("message", response.data.message);
                           this.getBasket();
                       })
                       .catch(error => {
                           console.log('error', error)
                       }) },
      getReview() {
                 console.log('id', this.$route.params.id)
                 console.log('page', this.$route.params.page)
        axios
            .post(`/api/review/${this.$route.params.id}/${this.$route.params.page}/`, {
              'user': this.userStore.user.id
            })
            .then(response => {
              this.reviews = response.data.reviews
              this.check = response.data.check
              this.total = response.data.count;

            })

      },
      addReview(bookId){
                 axios.
                     post('/api/review/add_review/', {
                       'user': this.userStore.user.id,
                        'book': bookId,
                        'review': this.review,
                        'rating': this.rating
                 })
                     .then(response => {
                       this.showReview = false
                       this.getReview()
                       this.getBook()
                     })
                     .catch(error=>{
                       this.showReview = true
                       console.log('error', error)
                     })
      },
        changePage(page) {
          this.$router.push({ path: `/book/${this.book.id}/${page}/` });
        },

    },
   watch: {
          '$route': function(newRoute, oldRoute) {
            if (this.$route.params.page) {
              this.getReview();
              console.log('change_page')
            }
          },
        },
  }
</script>