<template>
  <div class="container mx-auto" >
    <div class="flex justify-center">
      <button
        @click="isOpen = true"
        class="px-6 py-2 text-white bg-blue-600 rounded shadow"
        type="button"
        title="Сортировка и фильтр по книгам"
      >
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
  <path stroke-linecap="round" stroke-linejoin="round" d="M10.5 6h9.75M10.5 6a1.5 1.5 0 1 1-3 0m3 0a1.5 1.5 0 1 0-3 0M3.75 6H7.5m3 12h9.75m-9.75 0a1.5 1.5 0 0 1-3 0m3 0a1.5 1.5 0 0 0-3 0m-3.75 0H7.5m9-6h3.75m-3.75 0a1.5 1.5 0 0 1-3 0m3 0a1.5 1.5 0 0 0-3 0m-9.75 0h9.75" />
</svg>

      </button>

      <div
        v-show="isOpen"
        class="overflow-hidden
          absolute
          inset-0
          flex
          items-center
          justify-center
          bg-gray-700 bg-opacity-50
        "
      >
        <div class="max-w-2xl p-6 bg-white rounded-md shadow-xl">
          <div class="flex items-center justify-between">
            <h3 class="text-2xl">Сортировка и фильтрация книг</h3>
            <svg
              @click="isOpen = false"
              xmlns="http://www.w3.org/2000/svg"
              class="w-8 ml-4 h-8 text-red-900 cursor-pointer"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z"
              />
            </svg>
          </div>
          <div class="mt-4">
              <select v-model="sortOrder" class="flex flex-col max-w-sm rounded-lg py-4 m-4 p-4 overflow-hidden bg-gray-200 shadow-lg focus:outline-none focus:shadow-outline">
                <option value="Без сортировки">Без сортировки</option>
                <option value="cost_per_one">По цене</option>
                <option value="rating">По рейтингу</option>
              </select>


    <div class="card flex p-6">
        <div class="flex flex-col gap-3">
            <div v-for="genre of genres" :key="genre.id" class="flex items-center">
                <Checkbox v-model="selectedGenres" :inputId="genre.id" name="genre" :value="genre.id" />
                <label class="p-2" :for="genre.id">{{ genre.text }}</label>
            </div>
        </div>
    </div>


            <button
              @click="isOpen = false"
              class="px-6 py-2 text-blue-800 border border-blue-600 rounded"
            >
              Отменить
            </button>
            <button @click="saveOptions()" class="px-6 py-2 ml-2 text-blue-100 bg-blue-600 rounded">
              Сохранить
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>

<div class="flex flex-wrap">
  <div v-for="book in books" :key="book.id" v-if="books.length > 0" class="w-1/3 p-2">
    <div class="max-w-s rounded overflow-hidden bg-white shadow-lg">

      <div class="px-6 py-4">
         <p class="text-sm text-gray-600 flex items-center">
                                  <svg class="fill-current text-gray-500 w-3 h-3 mr-2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                                    <path d="M4 8V6a6 6 0 1 1 12 0v2h1a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-8c0-1.1.9-2 2-2h1zm5 6.73V17h2v-2.27a2 2 0 1 0-2 0zM7 6v2h6V6a3 3 0 0 0-6 0z" />
                                  </svg>
                                  {{book.additional_genre.text_genre.text}}, {{book.additional_genre.text_additional}}, {{book.author.text}}
                                </p>
        <div class="font-bold text-xl mb-2">{{ book.name }}</div>
        <p class="text-gray-700 text-base">{{ book.description }}</p>
      </div>
      <div class="px-6 py-4">
        <span class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700">Цена: {{ book.cost_per_one }}₽</span>
        <span class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 ml-2">Рейтинг: {{book.rating}}</span>
      </div>

      <div class="px-6 py-4" >
        <button @click="goToBook(book.id)" class="py-4 px-6 mr-2 bg-blue-400 text-white rounded-lg">Перейти</button>
                                           <button v-if="favourites.includes(book.id)" @click="deleteFavourite(book.id)" title="Удалить из избранных" class="py-4 px-6 text-black rounded-lg border border-blue-400">
                                            <svg xmlns="http://www.w3.org/2000/svg" fill="#60a5fa" stroke="isCurrent" viewBox="0 0 24 24" stroke-width="1.5" class="w-6 h-6">
                                                            <path stroke-linecap="round" stroke-linejoin="round" d="M17.593 3.322c1.1.128 1.907 1.077 1.907 2.185V21L12 17.25 4.5 21V5.507c0-1.108.806-2.057 1.907-2.185a48.507 48.507 0 0 1 11.186 0Z" />
                                            </svg>
                                          </button>

                                        <button v-else @click="addBookToFavourite(book.id)" class="py-4 px-6 m-2 text-white rounded-lg border border-blue-400" title="Добавить в избранные">
                                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" stroke="#60a5fa" viewBox="0 0 24 24" stroke-width="1.5" class="w-6 h-6">
                                                            <path stroke-linecap="round" stroke-linejoin="round" d="M17.593 3.322c1.1.128 1.907 1.077 1.907 2.185V21L12 17.25 4.5 21V5.507c0-1.108.806-2.057 1.907-2.185a48.507 48.507 0 0 1 11.186 0Z" />
                                            </svg>
                                          </button>

                                                <button v-if="baskets.includes(book.id)" @click="deleteBookFromBasket(book.id)" class="py-4 px-6 m-2 text-white rounded-lg border border-blue-400" title="Удалить из корзины">
                                               <svg xmlns="http://www.w3.org/2000/svg" fill="#60a5fa" stroke="isCurrent" viewBox="0 0 24 24" stroke-width="1.5" class="w-6 h-6">
                                                <path stroke-linecap="round" stroke-linejoin="round" d="m14.74 9-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 0 1-2.244 2.077H8.084a2.25 2.25 0 0 1-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 0 0-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 0 1 3.478-.397m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 0 0-3.32 0c-1.18.037-2.09 1.022-2.09 2.201v.916m7.5 0a48.667 48.667 0 0 0-7.5 0" />
                                              </svg>
                                        </button>
                                        <button v-else @click="addBookToBasket(book.id)" class="py-4 px-6 m-2 text-white rounded-lg border border-blue-400" title="Добавить в корзину">
                                               <svg xmlns="http://www.w3.org/2000/svg" fill="none" stroke="#60a5fa" viewBox="0 0 24 24" stroke-width="1.5" class="w-6 h-6">
                                                <path stroke-linecap="round" stroke-linejoin="round" d="m14.74 9-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 0 1-2.244 2.077H8.084a2.25 2.25 0 0 1-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 0 0-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 0 1 3.478-.397m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 0 0-3.32 0c-1.18.037-2.09 1.022-2.09 2.201v.916m7.5 0a48.667 48.667 0 0 0-7.5 0" />
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

export default {

  props: {
    initialTotal: {
      type: Number,
      required: true
    },
  },
  data() {
    return {
      books: [],
      favourite: [],
      favourites: [],
      total: 0, // Устанавливаем начальное значение total
      perPage: 9,
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
    this.userStore = useUserStore()
    this.total = this.initialTotal; // Устанавливаем total после получения данных
    this.getBook();
    this.getFavourite();
        this.getBasket();
        this.getGenre();
  },
  methods: {
    getBook() {
      if (this.$route.params.page) {
        axios
          .post(`/api/book/get_pagination/${this.$route.params.page}/`, {'selected_genres': this.selectedGenres, 'sort_order': this.sortOrder})
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
    changePage(page) {
      this.$router.push({ path: `/all_books/${page}/` });
    },
    goToBook(bookId) {
      this.$router.push({ path: `/book/${bookId}/1/` });
      console.log("Переход к книге с ID:", bookId);
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

      this.getBook();
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

