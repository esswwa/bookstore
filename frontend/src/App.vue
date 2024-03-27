
<template>
<nav class="py-10 px-8 border-b border-gray-200">
        <div class="max-w-7xl mx-auto">
            <div class="flex items-center justify-between">
                <div class="menu-left">
                    <a href="#" class="text-xl">Магазин книг "Читай-Летай"</a>
                </div>

                <div class="menu-center flex space-x-12" v-if="userStore.user.isAuthenticated">
                    <RouterLink to="/books" class="text-blue-700">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 12l8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25" />
                        </svg>
                    </RouterLink>

                    <RouterLink to="/order">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                          <path stroke-linecap="round" stroke-linejoin="round" d="m20.25 7.5-.625 10.632a2.25 2.25 0 0 1-2.247 2.118H6.622a2.25 2.25 0 0 1-2.247-2.118L3.75 7.5M10 11.25h4M3.375 7.5h17.25c.621 0 1.125-.504 1.125-1.125v-1.5c0-.621-.504-1.125-1.125-1.125H3.375c-.621 0-1.125.504-1.125 1.125v1.5c0 .621.504 1.125 1.125 1.125Z" />
                        </svg>

                    </RouterLink>

                    <RouterLink to="/favourite">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                          <path stroke-linecap="round" stroke-linejoin="round" d="M17.593 3.322c1.1.128 1.907 1.077 1.907 2.185V21L12 17.25 4.5 21V5.507c0-1.108.806-2.057 1.907-2.185a48.507 48.507 0 0 1 11.186 0Z" />
                        </svg>

                    </RouterLink>

                    <RouterLink to="/basket">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                          <path stroke-linecap="round" stroke-linejoin="round" d="M21 12a2.25 2.25 0 0 0-2.25-2.25H15a3 3 0 1 1-6 0H5.25A2.25 2.25 0 0 0 3 12m18 0v6a2.25 2.25 0 0 1-2.25 2.25H5.25A2.25 2.25 0 0 1 3 18v-6m18 0V9M3 12V9m18 0a2.25 2.25 0 0 0-2.25-2.25H5.25A2.25 2.25 0 0 0 3 9m18 0V6a2.25 2.25 0 0 0-2.25-2.25H5.25A2.25 2.25 0 0 0 3 6v3" />
                        </svg>

                    </RouterLink>

                    <RouterLink to="/profile">
                       <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                          <path stroke-linecap="round" stroke-linejoin="round" d="M17.982 18.725A7.488 7.488 0 0 0 12 15.75a7.488 7.488 0 0 0-5.982 2.975m11.963 0a9 9 0 1 0-11.963 0m11.963 0A8.966 8.966 0 0 1 12 21a8.966 8.966 0 0 1-5.982-2.275M15 9.75a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
                       </svg>

                    </RouterLink>
                </div>

                <div class="menu-right">
                  <template  v-if="userStore.user.isAuthenticated">
                    <a href="#">
                      <img src="https://i.pravatar.cc/40?img=70" class="w-12 rounded-full">
                    </a>
                  </template>
                  <template  v-else>
                    <RouterLink to="/signin" class="mr-4 py-4 px-6 bg-gray-600 text-white rounded-lg">Войти</RouterLink>
                    <RouterLink to="/signup" class="py-4 px-6 bg-blue-400 text-white rounded-lg">Зарегистрироваться</RouterLink>
                  </template>
                </div>
            </div>
        </div>
</nav>

    <main class="px-8 py-6 bg-gray-100">
        <RouterView />
    </main>

</template>
<script>
import Toast from '@/components/Toast.vue'
import { useUserStore } from "@/stores/user";
import axios from "axios";

export default {
  setup(){
    const userStore = useUserStore()
    return{
      userStore
    }
  },
  components: {
    Toast
  },
  beforeCreate() {
    this.userStore.initStore()

    const token = this.userStore.user.access

    if(token){
      axios.defaults.headers.common["Authorization"] = "Bearer " + token
    }
    else {
      axios.defaults.headers.common["Authorization"] = ""

    }
  }
}
</script>
