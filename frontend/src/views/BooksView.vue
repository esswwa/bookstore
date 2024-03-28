<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
        <div class="main-center col-span-3 space-y-4">

          <div class="bg-blue-500 text-white py-4 px-6 text-center">
              <h1 class="text-4xl font-bold">ЛУЧШИЕ ИЗ ЛУЧШИХ</h1>
          </div>

          <div
                class="p-4 bg-white border border-gray-200 rounded-lg"
                v-for="book in books"
                :key="book.id">
                <div class="max-w-sm w-full lg:max-w-full lg:flex">
                    <div class="h-48 lg:h-auto lg:w-0 flex-none bg-cover rounded-t lg:rounded-t-none lg:rounded-l text-center overflow-hidden" title="Woman holding a mug">
                      </div>
                          <div class="border-r border-b border-l border-gray-400 lg:border-t lg:border-gray-400 bg-white rounded-b lg:rounded-b-none lg:rounded-r p-4 flex flex-col justify-between leading-normal">
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
                                  <p class="text-gray-900 leading-none">{{ book.cost_per_one }}₽</p>
                                  <p class="text-gray-600">{{book.rating}}</p>
                                </div>
                            </div>
                        </div>
                  </div>
            </div>

                    <div class="bg-blue-500 text-white py-4 px-6 text-center">
              <h1 class="text-4xl font-bold">НОВИНКИ В ЛИТЕРАТУРЕ</h1>
          </div>

          <div
                class="p-4 bg-white border border-gray-200 rounded-lg"
                v-for="book in books"
                :key="book.id">
                <div class="max-w-sm w-full lg:max-w-full lg:flex">
                    <div class="h-48 lg:h-auto lg:w-0 flex-none bg-cover rounded-t lg:rounded-t-none lg:rounded-l text-center overflow-hidden" title="Woman holding a mug">
                      </div>
                          <div class="border-r border-b border-l border-gray-400 lg:border-t lg:border-gray-400 bg-white rounded-b lg:rounded-b-none lg:rounded-r p-4 flex flex-col justify-between leading-normal">
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
                                  <p class="text-gray-900 leading-none">{{ book.cost_per_one }}₽</p>
                                  <p class="text-gray-600">{{book.rating}}</p>
                                </div>
                            </div>
                        </div>
                  </div>
            </div>

                    <div class="bg-blue-500 text-white py-4 px-6 text-center">
              <h1 class="text-4xl font-bold">САМЫЕ ПОПУЛЯРНЫЕ КНИГИ 2024 ГОДА</h1>
          </div>

          <div
                class="p-4 bg-white border border-gray-200 rounded-lg"
                v-for="book in books"
                :key="book.id">
                <div class="max-w-sm w-full lg:max-w-full lg:flex">
                    <div class="h-48 lg:h-auto lg:w-0 flex-none bg-cover rounded-t lg:rounded-t-none lg:rounded-l text-center overflow-hidden" title="Woman holding a mug">
                      </div>
                          <div class="border-r border-b border-l border-gray-400 lg:border-t lg:border-gray-400 bg-white rounded-b lg:rounded-b-none lg:rounded-r p-4 flex flex-col justify-between leading-normal">
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
                                  <p class="text-gray-900 leading-none">{{ book.cost_per_one }}₽</p>
                                  <p class="text-gray-600">{{book.rating}}</p>
                                </div>
                            </div>
                        </div>
                  </div>
            </div>
        </div>
    </div>

  <!--            <div-->
<!--                class="p-4 ml-6 bg-white border border-gray-200 rounded-lg"-->
<!--                v-for="comment in book.comments"-->
<!--                v-bind:key="comment.id"-->
<!--            >-->

<!--            <div class="bg-white border border-gray-200 rounded-lg">-->
<!--                <form v-on:submit.prevent="submitForm" method="post">-->
<!--                    <div class="p-4">-->
<!--                        <textarea v-model="body" class="p-4 w-full bg-gray-100 rounded-lg" placeholder="What do you think?"></textarea>-->
<!--                    </div>-->

<!--                    <div class="p-4 border-t border-gray-100">-->
<!--                        <button class="inline-block py-4 px-6 bg-purple-600 text-white rounded-lg">Comment</button>-->
<!--                    </div>-->
<!--                </form>-->
<!--            </div>-->
</template>

<script>
import axios from 'axios'

export default {
    name: 'BookView',


    data() {
        return {
            books: {
                id: null
            },
            body: ''
        }
    },

    created() {
        this.getBook()
    },

    methods: {
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

        // submitForm() {
        //     console.log('submitForm', this.body)
        //
        //     axios
        //         .post(`/api/books/${this.$route.params.id}/comment/`, {
        //             'body': this.body
        //         })
        //         .then(response => {
        //             console.log('data', response.data)
        //
        //             this.book.comments.push(response.data)
        //             this.book.comments_count += 1
        //             this.body = ''
        //         })
        //         .catch(error => {
        //             console.log('error', error)
        //         })
        // }
    }
}
</script>