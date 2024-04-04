<template>
    <div class="max-w-7xl mx-auto">
        <div class="main-center col-span-3 space-y-4">
          <div class="text-center mb-2 text-black py-4 px-6">
              <h1 class="text-4xl font-bold">ЛУЧШИЕ ИЗ ЛУЧШИХ</h1>
          </div>
        </div>
    </div>
    <swiper
        v-if="books.length > 0"
        :spaceBetween="30"
        :slidesPerView="5"
        :autoplay="{
          delay: 3000,
          disableOnInteraction: false,
        }"
        @autoplayTimeLeft="onAutoplayTimeLeft"
        :modules="modules"
        class="mySwiper"
      >
        <swiper-slide v-for="book in books"
                :key="book.id" class="rounded-2xl">
          <div class="flex flex-col">
            <div class="max-w-sm w-full lg:max-w-full lg:flex">
                    <div class="h-48 lg:h-auto lg: flex-none bg-cover rounded-t lg:rounded-t-none lg:rounded-l text-center overflow-hidden" title="Перейти на книгу">
                          <div @click="goToBook(book.id)" class="hover:bg-gray-100 duration-200 cursor-pointer bg-white rounded-lg m-2 p-8 flex flex-col justify-between leading-normal">
                            <p class="text-sm text-gray-600 flex items-center">
                                  <svg class="fill-current text-gray-500 w-3 h-3 mr-2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                                    <path d="M4 8V6a6 6 0 1 1 12 0v2h1a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-8c0-1.1.9-2 2-2h1zm5 6.73V17h2v-2.27a2 2 0 1 0-2 0zM7 6v2h6V6a3 3 0 0 0-6 0z" />
                                  </svg>
                                   {{ book.author.text }}, {{book.additional_genre.text_genre.text}}
                                </p>
                                <img class="p-2" src="https://api.lorem.space/image/book?w=200&h=200" alt="Book cover">
                                <div class="text-gray-900 font-medium text-xl mb-2">{{book.name}}</div>
                                  <span class=" flex items-center px-3 text-xl font-semibold text-gray-500">{{ book.cost_per_one }} ₽</span>
                                  <div class=" flex items-center px-3 text-sm">
                                      <span class="inline-block bg-gray-200 rounded-full mt-4 px-3 py-1 text-sm font-semibold text-gray-700">Рейтинг: {{book.rating}}</span>
                                  </div>
                              </div>

                          </div>
                    </div>
                    <div class="mb-4" >
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
                            <svg xmlns="http://www.w3.org/2000/svg" fill="#60a5fa" stroke="white"  viewBox="0 0 24 24" stroke-width="1.5" class="w-6 h-6">
                              <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 8.25h19.5M2.25 9h19.5m-16.5 5.25h6m-6 2.25h3m-3.75 3h15a2.25 2.25 0 0 0 2.25-2.25V6.75A2.25 2.25 0 0 0 19.5 4.5h-15a2.25 2.25 0 0 0-2.25 2.25v10.5A2.25 2.25 0 0 0 4.5 19.5Z" />
                            </svg>
                        </button>
                        <button v-else @click="addBookToBasket(book.id)" class="py-4 px-6 text-white rounded-lg hover:bg-gray-100 hover:rounded-full  duration-200" title="Добавить в корзину">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" stroke="#60a5fa" viewBox="0 0 24 24" stroke-width="1.5"  class="w-6 h-6 hover:stroke-red-600 duration-200">
                              <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 8.25h19.5M2.25 9h19.5m-16.5 5.25h6m-6 2.25h3m-3.75 3h15a2.25 2.25 0 0 0 2.25-2.25V6.75A2.25 2.25 0 0 0 19.5 4.5h-15a2.25 2.25 0 0 0-2.25 2.25v10.5A2.25 2.25 0 0 0 4.5 19.5Z" />
                            </svg>
                        </button>
                    </div>
            </div>
        </swiper-slide>
        <template #container-end>
          <div class="autoplay-progress">
            <svg viewBox="0 0 48 48" ref="progressCircle">
              <circle cx="24" cy="24" r="20"></circle>
            </svg>
            <span ref="progressContent"></span>
          </div>
        </template>
      </swiper>


      <div class="max-w-7xl mx-auto">
        <div class="main-center col-span-3 space-y-4">
          <div class="text-center m-2  text-black py-4 px-6">
              <h1 class="text-4xl font-bold">НОВИНКИ В ЛИТЕРАТУРЕ</h1>
          </div>
        </div>
    </div>

    <swiper
        v-if="books.length > 0"
        :spaceBetween="30"
        :slidesPerView="5"
        :autoplay="{
          delay: 3000,
          disableOnInteraction: false,
        }"
        @autoplayTimeLeft="onAutoplayTimeLeft"
        :modules="modules"
        class="mySwiper"
      >
        <swiper-slide v-for="book in books"
                :key="book.id" class="rounded-2xl">
          <div class="flex flex-col">
            <div class="max-w-sm w-full lg:max-w-full lg:flex">
                    <div class="h-48 lg:h-auto lg: flex-none bg-cover rounded-t lg:rounded-t-none lg:rounded-l text-center overflow-hidden" title="Перейти на книгу">
                          <div @click="goToBook(book.id)" class="hover:bg-gray-100 duration-200 cursor-pointer bg-white rounded-lg m-2 p-8 flex flex-col justify-between leading-normal">
                            <p class="text-sm text-gray-600 flex items-center">
                                  <svg class="fill-current text-gray-500 w-3 h-3 mr-2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                                    <path d="M4 8V6a6 6 0 1 1 12 0v2h1a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-8c0-1.1.9-2 2-2h1zm5 6.73V17h2v-2.27a2 2 0 1 0-2 0zM7 6v2h6V6a3 3 0 0 0-6 0z" />
                                  </svg>
                                   {{ book.author.text }}, {{book.additional_genre.text_genre.text}}
                                </p>
                                <img class="p-2" src="https://api.lorem.space/image/book?w=200&h=200" alt="Book cover">
                                <div class="text-gray-900 font-medium text-xl mb-2">{{book.name}}</div>
                                  <span class=" flex items-center px-3 text-xl font-semibold text-gray-500">{{ book.cost_per_one }} ₽</span>
                                  <div class=" flex items-center px-3 text-sm">
                                      <span class="inline-block bg-gray-200 rounded-full mt-4 px-3 py-1 text-sm font-semibold text-gray-700">Рейтинг: {{book.rating}}</span>
                                  </div>
                              </div>

                          </div>
                    </div>
                    <div class="mb-4" >
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
                            <svg xmlns="http://www.w3.org/2000/svg" fill="#60a5fa" stroke="white"  viewBox="0 0 24 24" stroke-width="1.5" class="w-6 h-6">
                              <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 8.25h19.5M2.25 9h19.5m-16.5 5.25h6m-6 2.25h3m-3.75 3h15a2.25 2.25 0 0 0 2.25-2.25V6.75A2.25 2.25 0 0 0 19.5 4.5h-15a2.25 2.25 0 0 0-2.25 2.25v10.5A2.25 2.25 0 0 0 4.5 19.5Z" />
                            </svg>
                        </button>
                        <button v-else @click="addBookToBasket(book.id)" class="py-4 px-6 text-white rounded-lg hover:bg-gray-100 hover:rounded-full  duration-200" title="Добавить в корзину">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" stroke="#60a5fa" viewBox="0 0 24 24" stroke-width="1.5"  class="w-6 h-6 hover:stroke-red-600 duration-200">
                              <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 8.25h19.5M2.25 9h19.5m-16.5 5.25h6m-6 2.25h3m-3.75 3h15a2.25 2.25 0 0 0 2.25-2.25V6.75A2.25 2.25 0 0 0 19.5 4.5h-15a2.25 2.25 0 0 0-2.25 2.25v10.5A2.25 2.25 0 0 0 4.5 19.5Z" />
                            </svg>
                        </button>
                    </div>
            </div>
        </swiper-slide>
        <template #container-end>
          <div class="autoplay-progress">
            <svg viewBox="0 0 48 48" ref="progressCircle">
              <circle cx="24" cy="24" r="20"></circle>
            </svg>
            <span ref="progressContent"></span>
          </div>
        </template>
      </swiper>


      <div class="max-w-7xl mx-auto">
        <div class="main-center col-span-3 space-y-4">
          <div class="text-center m-2 text-black py-4 px-6">
              <h1 class="text-4xl font-bold">САМЫЕ ПОПУЛЯРНЫЕ КНИГИ 2024 ГОДА</h1>
          </div>
        </div>
    </div>

    <swiper
        v-if="books.length > 0"
        :spaceBetween="30"
        :slidesPerView="5"
        :autoplay="{
          delay: 3000,
          disableOnInteraction: false,
        }"
        @autoplayTimeLeft="onAutoplayTimeLeft"
        :modules="modules"
        class="mySwiper"
      >
        <swiper-slide v-for="book in books"
                :key="book.id" class="rounded-2xl">
          <div class="flex flex-col">
            <div class="max-w-sm w-full lg:max-w-full lg:flex">
                    <div class="h-48 lg:h-auto lg: flex-none bg-cover rounded-t lg:rounded-t-none lg:rounded-l text-center overflow-hidden" title="Перейти на книгу">
                          <div @click="goToBook(book.id)" class="hover:bg-gray-100 duration-200 cursor-pointer bg-white rounded-lg m-2 p-8 flex flex-col justify-between leading-normal">
                            <p class="text-sm text-gray-600 flex items-center">
                                  <svg class="fill-current text-gray-500 w-3 h-3 mr-2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                                    <path d="M4 8V6a6 6 0 1 1 12 0v2h1a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-8c0-1.1.9-2 2-2h1zm5 6.73V17h2v-2.27a2 2 0 1 0-2 0zM7 6v2h6V6a3 3 0 0 0-6 0z" />
                                  </svg>
                                   {{ book.author.text }}, {{book.additional_genre.text_genre.text}}
                                </p>
                                <img class="p-2" src="https://api.lorem.space/image/book?w=200&h=200" alt="Book cover">
                                <div class="text-gray-900 font-medium text-xl mb-2">{{book.name}}</div>
                                  <span class=" flex items-center px-3 text-xl font-semibold text-gray-500">{{ book.cost_per_one }} ₽</span>
                                  <div class=" flex items-center px-3 text-sm">
                                      <span class="inline-block bg-gray-200 rounded-full mt-4 px-3 py-1 text-sm font-semibold text-gray-700">Рейтинг: {{book.rating}}</span>
                                  </div>
                              </div>

                          </div>
                    </div>
                    <div class="mb-4" >
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
                            <svg xmlns="http://www.w3.org/2000/svg" fill="#60a5fa" stroke="white"  viewBox="0 0 24 24" stroke-width="1.5" class="w-6 h-6">
                              <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 8.25h19.5M2.25 9h19.5m-16.5 5.25h6m-6 2.25h3m-3.75 3h15a2.25 2.25 0 0 0 2.25-2.25V6.75A2.25 2.25 0 0 0 19.5 4.5h-15a2.25 2.25 0 0 0-2.25 2.25v10.5A2.25 2.25 0 0 0 4.5 19.5Z" />
                            </svg>
                        </button>
                        <button v-else @click="addBookToBasket(book.id)" class="py-4 px-6 text-white rounded-lg hover:bg-gray-100 hover:rounded-full  duration-200" title="Добавить в корзину">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" stroke="#60a5fa" viewBox="0 0 24 24" stroke-width="1.5"  class="w-6 h-6 hover:stroke-red-600 duration-200">
                              <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 8.25h19.5M2.25 9h19.5m-16.5 5.25h6m-6 2.25h3m-3.75 3h15a2.25 2.25 0 0 0 2.25-2.25V6.75A2.25 2.25 0 0 0 19.5 4.5h-15a2.25 2.25 0 0 0-2.25 2.25v10.5A2.25 2.25 0 0 0 4.5 19.5Z" />
                            </svg>
                        </button>
                    </div>
            </div>
        </swiper-slide>
        <template #container-end>
          <div class="autoplay-progress">
            <svg viewBox="0 0 48 48" ref="progressCircle">
              <circle cx="24" cy="24" r="20"></circle>
            </svg>
            <span ref="progressContent"></span>
          </div>
        </template>
      </swiper>
</template>

<script>

import { ref } from 'vue';
import axios from 'axios'
import { Swiper, SwiperSlide } from 'swiper/vue';
import { useUserStore } from "@/stores/user.js";

  // Import Swiper styles
  import 'swiper/css';
  import "../assets/base.css";
  import 'swiper/css/navigation';
  import 'swiper/css/navigation';


  // import required modules
  import { Autoplay, Pagination, Navigation } from 'swiper/modules';
import BookComponent from "@/components/BookComponent.vue";

export default {
    name: 'BookView',

 components: {
      Swiper,
      SwiperSlide,
   BookComponent
    },
 setup() {
      const progressCircle = ref(null);
      const progressContent = ref(null);

      const onAutoplayTimeLeft = (s, time, progress) => {
        progressCircle.value.style.setProperty('--progress', 1 - progress);
        progressContent.value.textContent = `${Math.ceil(time / 1000)}s`;
      };
      return {
        onAutoplayTimeLeft,
        progressCircle,
        progressContent,
        modules: [Autoplay, Pagination, Navigation],
      };
      },

    data() {
        return {
            books: {
                id: null
            },
            favourite: [],
            favourites: [],
            basket: [],
            baskets: [],
            body: ''
        }
    },

    created() {
    this.userStore = useUserStore()
        this.getBook();
        this.getFavourite();
        this.getBasket();
    },
    methods: {
        goToBook(bookId) {
      this.$router.push({ path: `/book/${bookId}/1/` });
          console.log("Переход к книге с ID:", bookId);
        },
        getBook() {
            axios
                .get(`/api/book/`)
                .then(response => {
                    console.log('data', response.data.books)

                    this.books = response.data.books
                })
                .catch(error => {
                    console.log('error', error)
                })
        },
       getBestBooks() {
            axios
                .get(`/api/book/books_the_best/`)
                .then(response => {
                    console.log('data', response.data.books)

                    this.books_the_best = response.data.books_the_best
                })
                .catch(error => {
                    console.log('error', error)
                })
        },
       getNewBooks() {
            axios
                .get(`/api/book/books_new_items/`)
                .then(response => {
                    console.log('data', response.data.books)

                    this.books_new_items = response.data.books_new_items
                })
                .catch(error => {
                    console.log('error', error)
                })
        },
       getPopularBook() {
            axios
                .get(`/api/book/books_popular/`)
                .then(response => {
                    console.log('data', response.data.books)

                    this.books_popular = response.data.books_popular
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

                }
}
</script>