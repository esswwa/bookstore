<!--<template>-->
<!--    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">-->
<!--        <div class="main-center col-span-3 space-y-4">-->

<!--          <div class="bg-blue-500 text-white py-4 px-6 text-center">-->
<!--              <h1 class="text-4xl font-bold">ЛУЧШИЕ ИЗ ЛУЧШИХ</h1>-->
<!--          </div>-->

<!--          <div-->
<!--                class="p-4 bg-white border border-gray-200 rounded-lg"-->
<!--                v-for="book in books"-->
<!--                :key="book.id">-->
<!--                <div class="max-w-sm w-full lg:max-w-full lg:flex">-->
<!--                    <div class="h-48 lg:h-auto lg:w-0 flex-none bg-cover rounded-t lg:rounded-t-none lg:rounded-l text-center overflow-hidden" title="Woman holding a mug">-->
<!--                      </div>-->
<!--                          <div class="border-r border-b border-l border-gray-400 lg:border-t lg:border-gray-400 bg-white rounded-b lg:rounded-b-none lg:rounded-r p-4 flex flex-col justify-between leading-normal">-->
<!--                              <div class="mb-8">-->
<!--                                <p class="text-sm text-gray-600 flex items-center">-->
<!--                                  <svg class="fill-current text-gray-500 w-3 h-3 mr-2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">-->
<!--                                    <path d="M4 8V6a6 6 0 1 1 12 0v2h1a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-8c0-1.1.9-2 2-2h1zm5 6.73V17h2v-2.27a2 2 0 1 0-2 0zM7 6v2h6V6a3 3 0 0 0-6 0z" />-->
<!--                                  </svg>-->
<!--                                  Жанр-->
<!--                                </p>-->
<!--                                <div class="text-gray-900 font-bold text-xl mb-2">{{book.name}}</div>-->
<!--                                <p class="text-gray-700 text-base">{{book.description}}</p>-->
<!--                              </div>-->
<!--                              <div class="flex items-center">-->
<!--                                <div class="text-sm">-->
<!--                                  <p class="text-gray-900 leading-none">{{ book.cost_per_one }}₽</p>-->
<!--                                  <p class="text-gray-600">{{book.rating}}</p>-->
<!--                                </div>-->
<!--                            </div>-->
<!--                        </div>-->
<!--                  </div>-->
<!--            </div>-->

<!--                    <div class="bg-blue-500 text-white py-4 px-6 text-center">-->
<!--              <h1 class="text-4xl font-bold">НОВИНКИ В ЛИТЕРАТУРЕ</h1>-->
<!--          </div>-->

<!--          <div-->
<!--                class="p-4 bg-white border border-gray-200 rounded-lg"-->
<!--                v-for="book in books"-->
<!--                :key="book.id">-->
<!--                <div class="max-w-sm w-full lg:max-w-full lg:flex">-->
<!--                    <div class="h-48 lg:h-auto lg:w-0 flex-none bg-cover rounded-t lg:rounded-t-none lg:rounded-l text-center overflow-hidden" title="Woman holding a mug">-->
<!--                      </div>-->
<!--                          <div class="border-r border-b border-l border-gray-400 lg:border-t lg:border-gray-400 bg-white rounded-b lg:rounded-b-none lg:rounded-r p-4 flex flex-col justify-between leading-normal">-->
<!--                              <div class="mb-8">-->
<!--                                <p class="text-sm text-gray-600 flex items-center">-->
<!--                                  <svg class="fill-current text-gray-500 w-3 h-3 mr-2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">-->
<!--                                    <path d="M4 8V6a6 6 0 1 1 12 0v2h1a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-8c0-1.1.9-2 2-2h1zm5 6.73V17h2v-2.27a2 2 0 1 0-2 0zM7 6v2h6V6a3 3 0 0 0-6 0z" />-->
<!--                                  </svg>-->
<!--                                  Жанр-->
<!--                                </p>-->
<!--                                <div class="text-gray-900 font-bold text-xl mb-2">{{book.name}}</div>-->
<!--                                <p class="text-gray-700 text-base">{{book.description}}</p>-->
<!--                              </div>-->
<!--                              <div class="flex items-center">-->
<!--                                <div class="text-sm">-->
<!--                                  <p class="text-gray-900 leading-none">{{ book.cost_per_one }}₽</p>-->
<!--                                  <p class="text-gray-600">{{book.rating}}</p>-->
<!--                                </div>-->
<!--                            </div>-->
<!--                        </div>-->
<!--                  </div>-->
<!--            </div>-->

<!--                    <div class="bg-blue-500 text-white py-4 px-6 text-center">-->
<!--              <h1 class="text-4xl font-bold">САМЫЕ ПОПУЛЯРНЫЕ КНИГИ 2024 ГОДА</h1>-->
<!--          </div>-->

<!--          <div-->
<!--                class="p-4 bg-white border border-gray-200 rounded-lg"-->
<!--                v-for="book in books"-->
<!--                :key="book.id">-->
<!--                <div class="max-w-sm w-full lg:max-w-full lg:flex">-->
<!--                    <div class="h-48 lg:h-auto lg:w-0 flex-none bg-cover rounded-t lg:rounded-t-none lg:rounded-l text-center overflow-hidden" title="Woman holding a mug">-->
<!--                      </div>-->
<!--                          <div class="border-r border-b border-l border-gray-400 lg:border-t lg:border-gray-400 bg-white rounded-b lg:rounded-b-none lg:rounded-r p-4 flex flex-col justify-between leading-normal">-->
<!--                              <div class="mb-8">-->
<!--                                <p class="text-sm text-gray-600 flex items-center">-->
<!--                                  <svg class="fill-current text-gray-500 w-3 h-3 mr-2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">-->
<!--                                    <path d="M4 8V6a6 6 0 1 1 12 0v2h1a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-8c0-1.1.9-2 2-2h1zm5 6.73V17h2v-2.27a2 2 0 1 0-2 0zM7 6v2h6V6a3 3 0 0 0-6 0z" />-->
<!--                                  </svg>-->
<!--                                  Жанр-->
<!--                                </p>-->
<!--                                <div class="text-gray-900 font-bold text-xl mb-2">{{book.name}}</div>-->
<!--                                <p class="text-gray-700 text-base">{{book.description}}</p>-->
<!--                              </div>-->
<!--                              <div class="flex items-center">-->
<!--                                <div class="text-sm">-->
<!--                                  <p class="text-gray-900 leading-none">{{ book.cost_per_one }}₽</p>-->
<!--                                  <p class="text-gray-600">{{book.rating}}</p>-->
<!--                                </div>-->
<!--                            </div>-->
<!--                        </div>-->
<!--                  </div>-->
<!--            </div>-->
<!--        </div>-->
<!--    </div>-->


<!--<div class="swiper-container">-->
<!--    <div class="swiper-wrapper">-->
<!--        &lt;!&ndash; Используйте v-for для создания слайдов &ndash;&gt;-->
<!--        <div-->
<!--            class="swiper-slide p-4 bg-white border border-gray-200 rounded-lg"-->
<!--            v-for="(book, index) in books"-->
<!--            :key="book.id"-->
<!--            :class="{ 'swiper-slide-hidden': index !== 0 }"-->
<!--        >-->
<!--            &lt;!&ndash; Ваш контент книги &ndash;&gt;-->
<!--            <div class="max-w-sm w-full lg:max-w-full lg:flex">-->
<!--                    <div class="h-48 lg:h-auto lg:w-24 flex-none bg-cover rounded-t lg:rounded-t-none lg:rounded-l text-center overflow-hidden" title="Woman holding a mug">-->
<!--                      </div>-->
<!--                          <div class="border-r border-b border-l border-gray-400 lg:border-t lg:border-gray-400 bg-white rounded-b lg:rounded-b-none lg:rounded-r p-4 flex flex-col justify-between leading-normal">-->
<!--                              <div class="mb-8">-->
<!--                                <p class="text-sm text-gray-600 flex items-center">-->
<!--                                  <svg class="fill-current text-gray-500 w-3 h-3 mr-2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">-->
<!--                                    <path d="M4 8V6a6 6 0 1 1 12 0v2h1a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-8c0-1.1.9-2 2-2h1zm5 6.73V17h2v-2.27a2 2 0 1 0-2 0zM7 6v2h6V6a3 3 0 0 0-6 0z" />-->
<!--                                  </svg>-->
<!--                                  Жанр-->
<!--                                </p>-->
<!--                                <div class="text-gray-900 font-bold text-xl mb-2">{{book.name}}</div>-->
<!--                                <p class="text-gray-700 text-base">{{book.description}}</p>-->
<!--                              </div>-->
<!--                              <div class="flex items-center">-->
<!--                                <div class="text-sm">-->
<!--                                  <p class="text-gray-900 leading-none">{{ book.cost_per_one }}₽</p>-->
<!--                                  <p class="text-gray-600">{{book.rating}}</p>-->
<!--                                </div>-->
<!--                            </div>-->
<!--                        </div>-->
<!--                  </div>-->

<!--   &lt;!&ndash; Добавьте навигацию для слайдера &ndash;&gt;-->
<!--    <div class="swiper-button-next"></div>-->
<!--    <div class="swiper-button-prev"></div>-->
<!--        </div>-->


<!--    </div>-->
<!--</div>-->

<!--</template>-->
<!--<script>-->
<!--import axios from 'axios'-->
<!--import Swiper from 'swiper';-->
<!--import 'swiper/swiper-bundle.css';-->
<!--export default {-->
<!--    name: 'BookView',-->


<!--    data() {-->
<!--        return {-->
<!--            books: {-->
<!--                id: null-->
<!--            },-->
<!--            body: ''-->
<!--        }-->
<!--    },-->

<!--    created() {-->
<!--        this.getBook()-->
<!--    },-->
<!--    mounted() {-->
<!--          const mySwiper = new Swiper('.swiper-container', {-->
<!--            slidesPerView: 'auto',-->
<!--            spaceBetween: 20,-->
<!--            centeredSlides: true,-->
<!--            navigation: {-->
<!--              nextEl: '.swiper-button-next',-->
<!--              prevEl: '.swiper-button-prev',-->
<!--            },-->
<!--          });-->
<!--    },-->
<!--    methods: {-->
<!--        getBook() {-->
<!--            axios-->
<!--                .get(`/api/book/`)-->
<!--                .then(response => {-->
<!--                    console.log('data', response.data.books)-->

<!--                    this.books = response.data.books-->
<!--                })-->
<!--                .catch(error => {-->
<!--                    console.log('error', error)-->
<!--                })-->
<!--        },-->
<!--       getBestBooks() {-->
<!--            axios-->
<!--                .get(`/api/book/books_the_best/`)-->
<!--                .then(response => {-->
<!--                    console.log('data', response.data.books)-->

<!--                    this.books_the_best = response.data.books_the_best-->
<!--                })-->
<!--                .catch(error => {-->
<!--                    console.log('error', error)-->
<!--                })-->
<!--        },-->
<!--       getNewBooks() {-->
<!--            axios-->
<!--                .get(`/api/book/books_new_items/`)-->
<!--                .then(response => {-->
<!--                    console.log('data', response.data.books)-->

<!--                    this.books_new_items = response.data.books_new_items-->
<!--                })-->
<!--                .catch(error => {-->
<!--                    console.log('error', error)-->
<!--                })-->
<!--        },-->
<!--       getPopularBook() {-->
<!--            axios-->
<!--                .get(`/api/book/books_popular/`)-->
<!--                .then(response => {-->
<!--                    console.log('data', response.data.books)-->

<!--                    this.books_popular = response.data.books_popular-->
<!--                })-->
<!--                .catch(error => {-->
<!--                    console.log('error', error)-->
<!--                })-->
<!--        },-->

<!--        // submitForm() {-->
<!--        //     console.log('submitForm', this.body)-->
<!--        //-->
<!--        //     axios-->
<!--        //         .post(`/api/books/${this.$route.params.id}/comment/`, {-->
<!--        //             'body': this.body-->
<!--        //         })-->
<!--        //         .then(response => {-->
<!--        //             console.log('data', response.data)-->
<!--        //-->
<!--        //             this.book.comments.push(response.data)-->
<!--        //             this.book.comments_count += 1-->
<!--        //             this.body = ''-->
<!--        //         })-->
<!--        //         .catch(error => {-->
<!--        //             console.log('error', error)-->
<!--        //         })-->
<!--        // }-->
<!--    }-->
<!--}-->
<!--</script>-->



<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
        <div class="main-center col-span-3 space-y-4">
          <div class="bg-blue-500 text-white py-4 px-6 text-center">
              <h1 class="text-4xl font-bold">ЛУЧШИЕ ИЗ ЛУЧШИХ</h1>
          </div>
        </div>
    </div>
<div class="swiper-container">
    <div class="swiper-wrapper">
        <!-- Используйте v-for для создания слайдов -->
        <div
            class="swiper-slide p-4 bg-white border border-gray-200 rounded-lg"
            v-for="(book, index) in books"
            :key="book.id"
        >
            <!-- Ваш контент книги -->
            <div class="max-w-sm w-full lg:max-w-full lg:flex">
                    <div class="h-48 lg:h-auto lg:w-24 flex-none bg-cover rounded-t lg:rounded-t-none lg:rounded-l text-center overflow-hidden" title="Woman holding a mug">
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


    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
        <div class="main-center col-span-3 space-y-4">

          <div class="bg-blue-500 text-white py-4 px-6 text-center">
              <h1 class="text-4xl font-bold">НОВИНКИ В ЛИТЕРАТУРЕ</h1>
          </div>
</div>
    </div>
<div class="swiper-container1">
    <div class="swiper-wrapper">
        <!-- Используйте v-for для создания слайдов -->
        <div
            class="swiper-slide1 p-4 bg-white border border-gray-200 rounded-lg"
            v-for="(book, index) in books"
            :key="book.id"
        >
            <!-- Ваш контент книги -->
            <div class="max-w-sm w-full lg:max-w-full lg:flex">
                    <div class="h-48 lg:h-auto lg:w-24 flex-none bg-cover rounded-t lg:rounded-t-none lg:rounded-l text-center overflow-hidden" title="Woman holding a mug">
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
            <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
        <div class="main-center col-span-3 space-y-4">

          <div class="bg-blue-500 text-white py-4 px-6 text-center">
              <h1 class="text-4xl font-bold">САМЫЕ ПОПУЛЯРНЫЕ КНИГИ 2024 ГОДА</h1>
          </div>
</div>
    </div>

<div class="swiper-container2">
    <div class="swiper-wrapper">
        <!-- Используйте v-for для создания слайдов -->
        <div
            class="swiper-slide2 p-4 bg-white border border-gray-200 rounded-lg"
            v-for="(book, index) in books"
            :key="book.id"
        >
            <!-- Ваш контент книги -->
            <div class="max-w-sm w-full lg:max-w-full lg:flex">
                    <div class="h-48 lg:h-auto lg:w-24 flex-none bg-cover rounded-t lg:rounded-t-none lg:rounded-l text-center overflow-hidden" title="Woman holding a mug">
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
</template>

<style>
.swiper-slide-hidden {
    display: none;
}

.swiper-slide-active {
    display: block;
}
.swiper-slide-hidden1 {
    display: none;
}

.swiper-slide-active1 {
    display: block;
}
.swiper-slide-hidden2 {
    display: none;
}

.swiper-slide-active2 {
    display: block;
}
</style>
<script>
import axios from 'axios'
import Swiper from 'swiper';
import 'swiper/swiper-bundle.css';
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
    mounted() {
          const mySwiper = new Swiper('.swiper-container', {
            slidesPerView: 'auto',
            spaceBetween: 20,
            centeredSlides: true,
            on: {
                init: function () {
                    // Скрыть все элементы, кроме первого
                    document.querySelectorAll('.swiper-slide').forEach((slide, index) => {
                        if (index !== 0) {
                            slide.classList.add('swiper-slide-hidden');
                        }
                    });
                },
                slideChange: function () {
                    // Скрыть предыдущий слайд
                    document.querySelectorAll('.swiper-slide').forEach(slide => {
                        slide.classList.remove('swiper-slide-active');
                        slide.classList.add('swiper-slide-hidden')
                    });
                    console.log("id", mySwiper.activeIndex)
                    mySwiper.slides[mySwiper.activeIndex].classList.remove('swiper-slide-hidden');
                    mySwiper.slides[mySwiper.activeIndex].classList.add('swiper-slide-active');
                  console.log(mySwiper.slides)
                },
            }
        });
        const mySwiper1 = new Swiper('.swiper-container1', {
            slidesPerView: 'auto',
            spaceBetween: 20,
            centeredSlides: true,
            on: {
                init: function () {
                    // Скрыть все элементы, кроме первого
                    document.querySelectorAll('.swiper-slide1').forEach((slide, index) => {
                        if (index !== 0) {
                            slide.classList.add('swiper-slide-hidden1');
                        }
                    });
                },
                slideChange: function () {
                    // Скрыть предыдущий слайд
                    document.querySelectorAll('.swiper-slide1').forEach(slide => {
                        slide.classList.remove('swiper-slide-active1');
                    });
                    mySwiper1.slides[mySwiper1.activeIndex].classList.add('swiper-slide-active1');
                },
            }
        });
        const mySwiper2 = new Swiper('.swiper-container2', {
            slidesPerView: 'auto',
            spaceBetween: 20,
            centeredSlides: true,
            navigation: {
              nextEl: '.swiper-button-next',
              prevEl: '.swiper-button-prev',
            },
            on: {
                init: function () {
                    // Скрыть все элементы, кроме первого
                    document.querySelectorAll('.swiper-slide2').forEach((slide, index) => {
                        if (index !== 0) {
                            slide.classList.add('swiper-slide-hidden2');
                        }
                    });
                },
                slideChange: function () {
                    // Скрыть предыдущий слайд
                    document.querySelectorAll('.swiper-slide2').forEach(slide => {
                        slide.classList.remove('swiper-slide-active2');
                    });
                    mySwiper2.slides[mySwiper2.activeIndex].classList.add('swiper-slide-active2');
                },
            }
        });
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