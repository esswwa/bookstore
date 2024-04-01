<template>
<div class="flex flex-wrap">
  <div v-for="book in books" :key="book.id" v-if="books.length > 0" class="w-1/3 p-2">
    <div class="max-w-sm rounded overflow-hidden shadow-lg">
      <div class="px-6 py-4">
        <div class="font-bold text-xl mb-2">{{ book.name }}</div>
        <p class="text-gray-700 text-base">{{ book.description }}</p>
      </div>
      <div class="px-6 py-4">
        <span class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2">{{ book.genre }}</span>
        <span class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700">{{ book.rating }}</span>
      </div>
      <div class="px-6 py-4">
        <button @click="goToBook(book.id)" class="py-2 px-4 bg-blue-500 text-white rounded-lg">Перейти</button>
      </div>
    </div>
  </div>
</div>

<VuePagination
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
    }
  },
  data() {
    return {
      books: [],
      total: 0, // Устанавливаем начальное значение total
      perPage: 3,
      currentPage: 1
    };
  },
  created() {
    this.total = this.initialTotal; // Устанавливаем total после получения данных
    this.getBook();
  },
  methods: {
    getBook() {
      if (this.$route.params.page) {
        axios
          .get(`/api/book/get_pagination/${this.$route.params.page}/`)
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
      this.$router.push({ path: '/book/' + bookId + '/' });
      console.log("Переход к книге с ID:", bookId);
    },
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



<!--<script>-->
<!--import axios from 'axios';-->
<!--import { useUserStore } from "@/stores/user.js";-->
<!--export default {-->
<!--  props: {-->
<!--    initialTotal: {-->
<!--      type: Number,-->
<!--      required: true-->
<!--    }-->
<!--  },-->
<!--  data() {-->
<!--    return {-->
<!--      books: [],-->
<!--      total: this.initialTotal,-->
<!--      perPage: 3,-->
<!--      currentPage: 1-->
<!--    };-->
<!--  },-->
<!--  created() {-->
<!--    this.getBook();-->
<!--  },-->
<!--  methods: {-->
<!--    getBook() {-->
<!--      if (this.$route.params.page) {-->
<!--        axios-->
<!--            .get(`/api/book/get_pagination/${this.$route.params.page}/`)-->
<!--            .then(response => {-->
<!--              console.log('data', response.data.books);-->
<!--              this.books = response.data.books;-->
<!--              this.total = response.data.count;-->
<!--            })-->
<!--            .catch(error => {-->
<!--              console.log('error', error);-->
<!--            });-->
<!--      }-->
<!--    },-->
<!--    changePage(page) {-->
<!--      this.$router.push({ path: `/all_books/${page}/` });-->
<!--    },-->
<!--    goToBook(bookId) {-->
<!--      this.$router.push({ path: '/book/' + bookId + '/' });-->
<!--      console.log("Переход к книге с ID:", bookId);-->
<!--    },-->
<!--  },-->
<!--  watch: {-->
<!--    '$route': function(newRoute, oldRoute) {-->
<!--    axios-->
<!--        .get(`/api/book/get_pagination/${this.$route.params.page}/`)-->
<!--        .then(response => {-->
<!--          console.log('data', response.data.books);-->
<!--          this.books = response.data.books;-->
<!--        })-->
<!--        .catch(error => {-->
<!--          console.log('error', error);-->
<!--        });-->
<!--    },-->
<!--  },-->
<!--};-->
<!--</script>-->


<!--<script>-->
<!--import axios from 'axios';-->
<!--import { useUserStore } from "@/stores/user.js";-->
<!--export default {-->
<!--  props: {-->
<!--    initialTotal: {-->
<!--      type: Number,-->
<!--      required: true-->
<!--    },-->
<!--    initialPerPage: {-->
<!--      type: Number,-->
<!--      required: true-->
<!--    }-->
<!--  },-->
<!--  data() {-->
<!--    return {-->
<!--      books: [],-->
<!--      total: this.initialTotal,-->
<!--      perPage: 3,-->
<!--      currentPage: 1,-->
<!--      paginatedBooks: [],-->
<!--    };-->
<!--  },-->
<!--  created() {-->
<!--        this.getBook()-->

<!--    },-->
<!--  methods: {-->
<!--    changePage(page) {-->
<!--      this.$route.params.page = page-->
<!--      this.getBook()-->
<!--    },-->
<!--    getBook() {-->
<!--            axios-->
<!--                .get(`/api/book/get_pagination/${this.$route.params.page}/`)-->
<!--                .then(response => {-->
<!--                    console.log('data', response.data.books)-->

<!--                    this.books = response.data.books-->
<!--                  this.total = response.data.count;-->
<!--                    this.changePage(1)-->
<!--                })-->
<!--                .catch(error => {-->
<!--                    console.log('error', error)-->
<!--                })-->
<!--        },-->
<!--      goToBook(bookId) {-->
<!--          this.$router.push({ path: '/book/' + bookId + '/'});-->
<!--          console.log("Переход к книге с ID:", bookId);-->
<!--    },-->
<!--  },-->
<!--};-->
<!--</script>-->

<!--<script >-->
<!--import axios from 'axios';-->
<!--import { useUserStore } from "@/stores/user.js";-->
<!--export default {-->
<!--  data() {-->
<!--    return {-->
<!--      books: [],-->
<!--      total: 30,-->
<!--      perPage: 3,-->
<!--      currentPage: 1,-->
<!--      paginatedBooks: [],-->
<!--    };-->
<!--  },-->
<!--  created() {-->
<!--    this.getBook();-->
<!--  },-->
<!--  methods: {-->
<!--    changePage(page) {-->
<!--      const startIndex = (page - 1) * this.perPage;-->
<!--      const endIndex = startIndex + this.perPage;-->
<!--      this.paginatedBooks = this.books.slice(startIndex, endIndex);-->
<!--    },-->
<!--    getBook() {-->
<!--      axios-->
<!--        .get(`/api/book/`)-->
<!--        .then(response => {-->
<!--          this.books = response.data.books;-->
<!--          this.changePage(this.currentPage);-->
<!--        })-->
<!--        .catch(error => {-->
<!--          console.log('error', error);-->
<!--        });-->
<!--    },-->
<!--  },-->
<!--};-->
<!--</script>-->