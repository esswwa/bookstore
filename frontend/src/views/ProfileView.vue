<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
        <div class="main-left col-span-1">
            <div class="p-4 bg-white border border-gray-200 text-center rounded-lg">

                <p><strong>{{ user.name }}</strong></p>
                    <RouterLink
                        class="inline-block mr-2 py-4 px-3 bg-purple-600 text-xs text-white rounded-lg"
                        to="/profile/edit"
                        v-if="userStore.user.id === this.user.id">
                        Edit profile
                    </RouterLink>

                    <button
                        class="inline-block py-4 px-3 bg-red-600 text-xs text-white rounded-lg"
                        @click="logout"
                        v-if="userStore.user.id === this.user.id">
                        Log out
                    </button>
                </div>
            </div>
        </div>

</template>

<script>
import axios from 'axios'

import { useUserStore } from '@/stores/user'
import { useToastStore } from '@/stores/toast'

export default {
    name: 'FeedView',

    setup() {
        const userStore = useUserStore()
        const toastStore = useToastStore()

        return {
            userStore,
            toastStore
        }
    },
    data() {
        return {
            posts: [],
            user: {
                id: ''
            },
            can_send_friendship_request: null,
        }
    },

    mounted() {
        this.getUser()
    },

    methods: {
              getUser() {
            axios
                .get(`/api/profile/${this.$route.params.id}/`)
                .then(response => {
                    console.log('data', response.data)
                    this.user = response.data.user
                })
                .catch(error => {
                    console.log('error', error)
                })
        },
        logout() {
            console.log('Log out')

            this.userStore.removeToken()

            this.$router.push('/signin')
        }
        // deletePost(id) {
        //     this.posts = this.posts.filter(post => post.id !== id)
        // },
        //
        // sendDirectMessage() {
        //     console.log('sendDirectMessage')
        //
        //     axios
        //         .get(`/api/chat/${this.$route.params.id}/get-or-create/`)
        //         .then(response => {
        //             console.log(response.data)
        //
        //             this.$router.push('/chat')
        //         })
        //         .catch(error => {
        //             console.log('error', error)
        //         })
        // },
        //
        // sendFriendshipRequest() {
        //     axios
        //         .post(`/api/friends/${this.$route.params.id}/request/`)
        //         .then(response => {
        //             console.log('data', response.data)
        //
        //             this.can_send_friendship_request = false
        //
        //             if (response.data.message == 'request already sent') {
        //                 this.toastStore.showToast(5000, 'The request has already been sent!', 'bg-red-300')
        //             } else {
        //                 this.toastStore.showToast(5000, 'The request was sent!', 'bg-emerald-300')
        //             }
        //         })
        //         .catch(error => {
        //             console.log('error', error)
        //         })
        // },
        //
        // getFeed() {
        //     axios
        //         .get(`/api/posts/profile/${this.$route.params.id}/`)
        //         .then(response => {
        //             console.log('data', response.data)
        //
        //             this.posts = response.data.posts
        //             this.user = response.data.user
        //             this.can_send_friendship_request = response.data.can_send_friendship_request
        //         })
        //         .catch(error => {
        //             console.log('error', error)
        //         })
        // },

    }
}
</script>