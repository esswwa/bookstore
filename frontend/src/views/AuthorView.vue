<template>
  <div class="flex items-center">
           <div class="max-w-7xl mx-auto">
        <div class="main-center col-span-3 space-y-4">
          <div class="text-center text-black py-4 px-6">
              <h1 class="text-4xl">ВCЕ КНИГИ ПО АВТОРУ:</h1>
              <h1 class="text-4xl font-bold">{{this.author}}</h1>
          </div>
        </div>
    </div>

  <div class="container" >
    <button @click="saveOptions()" class="px-6 py-2 ml-2 text-blue-100 bg-blue-400 rounded">
         Сохранить
    </button>
    <button v-if="(selectedGenres != '' && selectedGenres != null) || sortOrder !== 'Без сортировки' || searchInput !== ''" @click="resetFilters()" class="px-6 py-2 ml-2 text-blue-100 bg-blue-400 rounded" title="Сбросить фильтры">
        Сбросить сортировку и фильтры
    </button>
  </div>
  </div>


<div class="flex">

  <div class="max-w-s rounded-2xl overflow-hidden bg-white shadow-lg m-2 min-w-max">
      <div class="card flex p-6" v-if="genres.length > 0">
        <div class="flex flex-col">
          <div class="text-gray-900 font-medium text-xl mt-4 mb-2">
            Поиск по книгам
          </div>
            <div class="mt-4">
              <input v-model="searchInput" placeholder="Поиск" class="flex flex-col max-w-sm rounded-lg py-4 mb-4 p-4 overflow-hidden bg-gray-200 shadow-lg focus:outline-none focus:shadow-outline"/>
            </div>
          <div class="text-gray-900 font-medium text-xl mt-4 mb-2">
            Сортировка по цене и рейтингу
          </div>
            <div class="mt-4">
              <select v-model="sortOrder" class="flex flex-col max-w-sm rounded-lg py-4 mb-4 p-4 overflow-hidden bg-gray-200 shadow-lg focus:outline-none focus:shadow-outline">
                <option value="Без сортировки">Без сортировки</option>
                <option value="cost_per_one">По цене</option>
                <option value="rating">По рейтингу</option>
              </select>
            </div>
          <div class="text-gray-900 font-medium text-xl mb-2">
            Фильтрация по жанрам
          </div>
            <div v-for="genre of genres" :key="genre.id" class="flex items-center">

                <Checkbox v-model="selectedGenres" :inputId="genre.id" name="genre" :value="genre.id" />
                <label class="p-2" :for="genre.id">{{ genre.text }}</label>
            </div>
        </div>
    </div>
  </div>

<div class="flex flex-wrap max-w-s">
  <div v-for="book in books" :key="book.id" v-if="books.length > 0" class="w-1/4 p-2 min-w-max ">
    <div class="max-w-s rounded-2xl min-w-max overflow-hidden bg-white shadow-lg text-center">
            <div class="flex justify-center text-center">
                    <div class="h-48 lg:h-auto lg: flex-none bg-cover rounded-t lg:rounded-t-none lg:rounded-l text-center overflow-hidden" title="Перейти на книгу">
                          <div @click="goToBook(book.id)" class="hover:bg-gray-100 duration-200 cursor-pointer bg-white rounded-lg m-2 p-8 flex flex-col justify-between leading-normal">
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
                                <img class="p-2" height="200px" width="200px" src="@/assets/preview.jpg" alt="Book cover">
                                <div class="text-gray-900 font-medium text-xl mb-2" v-if="book.name">{{book.name.slice(0, 15) + (book.name.length > 15 ? '...' : '')}}</div>
                                  <span class=" flex items-center px-3 text-xl font-semibold text-gray-500" v-if="book.cost_per_one">{{ book.cost_per_one }} ₽</span>
                                  <span class="px-3 flex items-center text-red-500" v-if="book.count_on_stock === 0">Нет в наличии</span>
                          </div>

                          </div>
                    </div>

                                        <div class="px-3 mt-4 flex items-center justify-center" v-if="book.rating >=0">
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

                    <div class="mb-4" v-if="userStore.user.superuser !== true">
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
  <div v-else class="flex flex-col items-center p-6">
    Книги с необходимыми вам параметрами отсутствуют
    <button @click="resetFilters()" class="py-4 px-6 m-4 bg-blue-400 text-white rounded-lg" title="Сбросить фильтры">
        Сбросить фильтры
    </button>
  </div>
</div>
</div>

<VuePagination
    v-if="books.length > 0"
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
      books: [],
      favourite: [],
      favourites: [],
      author: '',
      searchInput: '',
      total: 0, // Устанавливаем начальное значение total
      perPage: 12,
      currentPage: 1,
      basket: [],
      baskets: [],
      sortOrder: 'Без сортировки',
      isOpen: false,
      pizza: null,
      genres: [],
      selectedGenres: null
    };
  },
  created() {
    this.userStore = useUserStore() // Устанавливаем total после получения данных
    this.getViewedBooks();
    this.getAuthor();
    this.getBook();
    this.getFavourite();
        this.getBasket();
        this.getGenre();
  },
  methods: {
    getBook() {
      if (this.$route.params.page && this.$route.params.author) {
        axios
          .post(`/api/book/get_pagination_author/${this.$route.params.author}/${this.$route.params.page}/`, {'searchInput': this.searchInput, 'selected_genres': this.selectedGenres, 'sort_order': this.sortOrder})
          .then(response => {
            console.log('data', response.data.books);
            this.books = response.data.books;
            this.total = response.data.count;
          })
          .catch(error => {
            console.log('error', error);
          });
      }
    },
    getAuthor() {
      if (this.$route.params.author) {
          axios
            .get(`/api/book/get_author/${this.$route.params.author}/`)
            .then(response => {
              this.author = response.data.author.text;
              console.log("author", response.data.author.text)
            })
            .catch(error => {
              console.log('error', error);
            });
        }
      },
    changePage(page) {
      this.$router.push({ path: `/all_books/${page}/` });
    },
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
                       })
              },
    getGenre(){
      axios
          .get('/api/book/get_genres/')
          .then(response => {
              this.genres = response.data.genres
          })
    },
    saveOptions(){
      console.log('selected', this.selectedGenres)
        this.getBook();
      this.isOpen = false
    },
    resetFilters(){
      this.selectedGenres = null;
      this.sortOrder = 'Без сортировки'
      this.searchInput = ''
      this.getBook();
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
  },

  watch: {
    '$route': function(newRoute, oldRoute) {
      if (this.$route.params.page) {
        this.getBook();
      }
    },
  },
};
</script>

