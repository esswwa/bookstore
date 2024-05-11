<template>
   <div class="max-w-7xl mx-auto grid grid-cols-2 gap-4">
        <div class="main-left">
            <div class="p-12 bg-white border border-gray-200 rounded-lg">
                <h1 class="mb-6 text-2xl">Авторизация</h1>

                <p class="mb-6 text-gray-500">
                    Авторизация.Регистрация.Авторизация.Регистрация.Авторизация.
                    Авторизация.Регистрация.Авторизация.Регистрация.Авторизация.
                </p>

                <p class="font-bold">
                    Еще нет аккаунта? <RouterLink :to="{'name': 'signup'}" class="underline">Перейди сюда</RouterLink>, чтобы зарегистрироваться!
                </p>
            </div>
        </div>

        <div class="main-right">
            <div class="p-12 bg-white border border-gray-200 rounded-lg">
                <form class="space-y-6" v-on:submit.prevent="submitForm">
                    <div>
                        <label>E-mail</label><br>
                        <input type="email" v-model="form.email" placeholder="Ваш e-mail адрес" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>
                    <div>
                        <label>Пароль</label><br>
                        <input type="password" v-model="form.password" placeholder="Ваш пароль" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>

                     <template v-if="errors.length > 0">
                      <div class="bg-red-300 text-white rounded-lg p-6">
                        <p v-for="error in errors" v-bind:key="error">{{error}}</p>
                      </div>
                    </template>

                    <div>
                        <button class="py-4 px-6 bg-blue-400 text-white rounded-lg">Авторизоваться</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { useUserStore } from "@/stores/user";

export default {

  setup(){
    const userStore = useUserStore()
    return{
      userStore
    }
  },
  data() {
    return{
      form: {
        email:'',
        password:''
      },
      errors: []
    }

  },
      methods: {
        async submitForm() {
          this.errors = []

           if(this.form.email === ''){
            this.errors.push('Your email is missing')
          }

          if(this.form.password === ''){
            this.errors.push('Your password is missing')
          }

            if (this.errors.length === 0) {
                await axios
                    .post('/api/signin/', this.form)
                    .then(response => {
                       this.userStore.setToken(response.data)
                       axios.defaults.headers.common["Authorization"] = "Bearer " + response.data.access

                    })
                    .catch(error => {
                        this.errors.push('The user does not exist or the password is incorrect')
                        console.log('error', error)
                    })
            }
            if (this.errors.length === 0) {
                await axios
                      .get('/api/me/')
                      .then(response => {
                         this.userStore.setUserInfo(response.data)

                          if(!this.userStore.user.superuser){
                            this.$router.push('/books')
                          }
                          else{
                            this.$router.push('/admin_orders')

                          }
                      })
                      .catch(error => {
                          console.log('error', error)
                      })
            }

        }
      }
  }
</script>