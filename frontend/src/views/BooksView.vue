<template>
    <div class="max-w-7xl mx-auto">
        <div class="main-center col-span-3 space-y-4">
          <div class="bg-blue-500 text-white py-4 px-6 text-center">
              <h1 class="text-4xl font-bold">ЛУЧШИЕ ИЗ ЛУЧШИХ</h1>
          </div>
        </div>
    </div>
    <swiper
        v-if="books.length > 0"
        :spaceBetween="30"
        :slidesPerView="3"
        :autoplay="{
          delay: 5000,
          disableOnInteraction: false,
        }"
        :pagination="{
          clickable: true,
        }"
        :navigation="true"
        :modules="modules"
        @autoplayTimeLeft="onAutoplayTimeLeft"
        class="mySwiper m-4"
      >
        <swiper-slide v-for="book in books"
                :key="book.id">
<div class="max-w-sm w-full lg:max-w-full lg:flex">
                    <div class="h-48 lg:h-auto lg:w-24 flex-none bg-cover rounded-t lg:rounded-t-none lg:rounded-l text-center overflow-hidden" title="Woman holding a mug">
                      </div>
                          <div class="border-r border-b border-l border-gray-400 lg:border-t lg:border-gray-400 bg-white rounded-b lg:rounded-b-none lg:rounded-r m-2 p-8 flex flex-col justify-between leading-normal">
                              <div class="mb-8">
                                <p class="text-sm text-gray-600 flex items-center">
                                  <svg class="fill-current text-gray-500 w-3 h-3 mr-2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                                    <path d="M4 8V6a6 6 0 1 1 12 0v2h1a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-8c0-1.1.9-2 2-2h1zm5 6.73V17h2v-2.27a2 2 0 1 0-2 0zM7 6v2h6V6a3 3 0 0 0-6 0z" />
                                  </svg>
                                  {{book.additional_genre.text_genre.text}}
                                </p>
                                <div class="text-gray-900 font-bold text-xl mb-2">{{book.name}}</div>
                                <p class="text-gray-700 text-base">{{book.description}}</p>
                              </div>
                              <div class="flex items-center">
                                <div class="text-sm">
                                              <span class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2">Автор: {{ book.author.text }}</span>
                                              <span class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2">Издательство: {{ book.publishing_house.text }}</span>
                                <div class="px-6 py-4">
                                              <span class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700">Цена: {{ book.cost_per_one }}₽</span>
                                              <span class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 ml-2">Рейтинг: {{book.rating}}</span>
                                </div>
                                        <div class="px-6 py-4" >
                                          <button @click="goToBook(book.id)" class="py-4 px-6 bg-blue-400 text-white rounded-lg">Перейти</button>
                                          <button v-if="favourites.includes(book.id)" @click="deleteFavourite(book.id)" class="py-4 px-6 m-2 bg-blue-400 text-white rounded-lg">Удалить из избранных</button>
                                          <button v-else  @click="addBookToFavourite(book.id)" class="py-4 px-6 bg-blue-400 m-2 text-white rounded-lg">Добавить в избранное</button>
                                        </div>
                                </div>
                            </div>
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

          <div class="bg-blue-500 text-white py-4 px-6 text-center">
              <h1 class="text-4xl font-bold">НОВИНКИ В ЛИТЕРАТУРЕ</h1>
          </div>
        </div>
    </div>
<swiper
    v-if="books.length > 0"
        :spaceBetween="30"
        :slidesPerView="3"
    :autoplay="{
      delay: 5000,
      disableOnInteraction: false,
    }"
    :pagination="{
      clickable: true,
    }"
    :navigation="true"
    :modules="modules"
    @autoplayTimeLeft="onAutoplayTimeLeft"
    class="mySwiper m-4"
  >
    <swiper-slide v-for="book in books"
            :key="book.id">
<div class="max-w-sm w-full lg:max-w-full lg:flex">
                    <div class="h-48 lg:h-auto lg:w-24 flex-none bg-cover rounded-t lg:rounded-t-none lg:rounded-l text-center overflow-hidden" title="Woman holding a mug">
                      </div>
                          <div class="border-r border-b border-l border-gray-400 lg:border-t lg:border-gray-400 bg-white rounded-b lg:rounded-b-none lg:rounded-r m-2 p-8 flex flex-col justify-between leading-normal">
                              <div class="mb-8">
                                <p class="text-sm text-gray-600 flex items-center">
                                  <svg class="fill-current text-gray-500 w-3 h-3 mr-2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                                    <path d="M4 8V6a6 6 0 1 1 12 0v2h1a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-8c0-1.1.9-2 2-2h1zm5 6.73V17h2v-2.27a2 2 0 1 0-2 0zM7 6v2h6V6a3 3 0 0 0-6 0z" />
                                  </svg>
                                  {{book.additional_genre.text_genre.text}}
                                </p>
                                <div class="text-gray-900 font-bold text-xl mb-2">{{book.name}}</div>
                                <p class="text-gray-700 text-base">{{book.description}}</p>
                              </div>
                              <div class="flex items-center">
                                <div class="text-sm">
                                              <span class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2">Автор: {{ book.author.text }}</span>
                                              <span class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2">Издательство: {{ book.publishing_house.text }}</span>
                                <div class="px-6 py-4">
                                              <span class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700">Цена: {{ book.cost_per_one }}₽</span>
                                              <span class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 ml-2">Рейтинг: {{book.rating}}</span>
                                </div>
                                        <div class="px-6 py-4" >
                                          <button @click="goToBook(book.id)" class="py-4 px-6 bg-blue-400 text-white rounded-lg">Перейти</button>
                                          <button v-if="favourites.includes(book.id)" @click="deleteFavourite(book.id)" class="py-4 px-6 m-2 bg-blue-400 text-white rounded-lg">Удалить из избранных</button>
                                          <button v-else  @click="addBookToFavourite(book.id)" class="py-4 px-6 bg-blue-400 m-2 text-white rounded-lg">Добавить в избранное</button>
                                        </div>
                                </div>
                            </div>
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

          <div class="bg-blue-500 text-white py-4 px-6 text-center">
              <h1 class="text-4xl font-bold">САМЫЕ ПОПУЛЯРНЫЕ КНИГИ 2024 ГОДА</h1>
          </div>
</div>
    </div>
<swiper
    v-if="books.length > 0"
        :spaceBetween="30"
        :slidesPerView="3"
    :autoplay="{
      delay: 5000,
      disableOnInteraction: false,
    }"
    :pagination="{
      clickable: true,
    }"
    :navigation="true"
    :modules="modules"
    @autoplayTimeLeft="onAutoplayTimeLeft"
    class="mySwiper m-4"
  >
    <swiper-slide v-for="book in books" :key="book.id">
 <div class="max-w-sm w-full lg:max-w-full lg:flex">
                    <div class="h-48 lg:h-auto lg:w-24 flex-none bg-cover rounded-t lg:rounded-t-none lg:rounded-l text-center overflow-hidden" title="Woman holding a mug">
                      </div>
                          <div class="border-r border-b border-l border-gray-400 lg:border-t lg:border-gray-400 bg-white rounded-b lg:rounded-b-none lg:rounded-r m-2 p-8 flex flex-col justify-between leading-normal">
                              <div class="mb-8">
                                <p class="text-sm text-gray-600 flex items-center">
                                  <svg class="fill-current text-gray-500 w-3 h-3 mr-2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                                    <path d="M4 8V6a6 6 0 1 1 12 0v2h1a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-8c0-1.1.9-2 2-2h1zm5 6.73V17h2v-2.27a2 2 0 1 0-2 0zM7 6v2h6V6a3 3 0 0 0-6 0z" />
                                  </svg>
                                  {{book.additional_genre.text_genre.text}}
                                </p>
                                <div class="text-gray-900 font-bold text-xl mb-2">{{book.name}}</div>
                                <p class="text-gray-700 text-base">{{book.description}}</p>
                              </div>
                              <div class="flex items-center">
                                <div class="text-sm">
                                              <span class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2">Автор: {{ book.author.text }}</span>
                                              <span class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2">Издательство: {{ book.publishing_house.text }}</span>
                                <div class="px-6 py-4">
                                              <span class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700">Цена: {{ book.cost_per_one }}₽</span>
                                              <span class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 ml-2">Рейтинг: {{book.rating}}</span>
                                </div>
                                        <div class="px-6 py-4" >
                                          <button @click="goToBook(book.id)" class="py-4 px-6 bg-blue-400 text-white rounded-lg">Перейти</button>
                                          <button v-if="favourites.includes(book.id)" @click="deleteFavourite(book.id)" class="py-4 px-6 m-2 bg-blue-400 text-white rounded-lg">Удалить из избранных</button>
                                          <button v-else  @click="addBookToFavourite(book.id)" class="py-4 px-6 bg-blue-400 m-2 text-white rounded-lg">Добавить в избранное</button>
                                        </div>
                                </div>
                            </div>
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

export default {
    name: 'BookView',

 components: {
      Swiper,
      SwiperSlide,
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
            body: ''
        }
    },

    created() {
    this.userStore = useUserStore()
        this.getBook();
        this.getFavourite();
    },
    methods: {
        goToBook(bookId) {
          this.$router.push({ path: '/book/' + bookId + '/'});
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

    }
}
</script>