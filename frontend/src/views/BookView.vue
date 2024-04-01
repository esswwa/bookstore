<template>
  <div class="max-w-sm w-full lg:max-w-full lg:flex">
                    <div class="h-48 lg:h-auto lg:w-24 flex-none bg-cover rounded-t lg:rounded-t-none lg:rounded-l text-center overflow-hidden" title="Woman holding a mug">
                      </div>
                          <div class="border-r border-b border-l border-gray-400 lg:border-t lg:border-gray-400 bg-white rounded-b lg:rounded-b-none lg:rounded-r m-2 p-8 flex flex-col justify-between leading-normal">
                              <div class="mb-8">
                                <p class="text-sm text-gray-600 flex items-center">
                                  <svg class="fill-current text-gray-500 w-3 h-3 mr-2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                                    <path d="M4 8V6a6 6 0 1 1 12 0v2h1a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-8c0-1.1.9-2 2-2h1zm5 6.73V17h2v-2.27a2 2 0 1 0-2 0zM7 6v2h6V6a3 3 0 0 0-6 0z" />
                                  </svg>
                                  Жанр
                                </p>
                                <div class="text-gray-900 font-bold text-xl mb-2">{{book.name}}</div>
                                <p class="text-gray-700 text-base">{{book.description}}</p>
                              </div>
                              <div class="flex items-center">
                                <div class="text-sm">
                                  <p class="text-gray-900 leading-none">{{ book.author }}</p>
                                  <p class="text-gray-900 leading-none">{{ book.cost_per_one }}₽</p>
                                  <p class="text-gray-600">{{book.rating}}</p>
                                  <div>
                                        <button @click="addBookToFavourite(book.id)" class="py-4 m-4 px-6 bg-blue-400 text-white rounded-lg">Добавить в избранное</button>
                                  </div>
                                </div>
                            </div>
                        </div>
      </div>
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
            body: ''
        }
    },
    created() {
        this.getBook()
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

              },   addBookToFavourite(bookId){
          axios.post('/api/favourite/add_to_favourite/',{
                "book_id": bookId,
                "user_id": localStorage.getItem('user.id')
              })
              .then(response => {
                console.log("book_id", response.data.book_id)
                console.log("user_id", response.data.user_id)
                console.log("message", response.data.message)
                console.log("fav", response.data.favourite)

              })
              .catch(error => {
                console.log("error", error)

              })

      },
    }
  }
</script>