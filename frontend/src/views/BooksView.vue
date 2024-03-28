<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
        <div class="main-center col-span-3 space-y-4">
            <div
                class="p-4 bg-white border border-gray-200 rounded-lg"
                v-if="book.id"
            >
<!--                <FeedItem v-bind:book="book" />-->
            </div>

<!--            <div-->
<!--                class="p-4 ml-6 bg-white border border-gray-200 rounded-lg"-->
<!--                v-for="comment in book.comments"-->
<!--                v-bind:key="comment.id"-->
<!--            >-->
            </div>

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
            </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'PostView',

    // components: {
    // },

    data() {
        return {
            book: {
                id: null
            },
            body: ''
        }
    },

    // mounted() {
    //     this.getBook()
    // },

    methods: {
        // getBook() {
        //     axios
        //         .get(`/api/books/${this.$route.params.id}/`)
        //         .then(response => {
        //             console.log('data', response.data)
        //
        //             this.book = response.data.book
        //         })
        //         .catch(error => {
        //             console.log('error', error)
        //         })
        // },

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