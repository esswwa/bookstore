<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
        <div class="main-left col-span-1">
            <div class="p-4 bg-white border border-gray-200 text-center rounded-lg">

                <p><strong>{{ user.name }}</strong></p>
                    <RouterLink
                        class="inline-block mr-2 py-4 px-3 bg-blue-400 text-xs text-white rounded-lg"
                        to="/profile/edit"
                        v-if="userStore.user.id == user.id">
                        Edit profile
                    </RouterLink>

                    <button
                        class="inline-block py-4 px-3 bg-blue-400 text-xs text-white rounded-lg"
                        @click="logout"
                        v-if="userStore.user.id == user.id">
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
    }
}
</script>