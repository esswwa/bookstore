<template>
   <div class="max-w-7xl mx-auto grid grid-cols-2 gap-4">
        <div class="main-left">
            <div class="p-12 bg-white border border-gray-200 rounded-lg">
                <h1 class="mb-6 text-2xl">Регистрация</h1>

                <p class="mb-6 text-gray-500">
                    Регистрация.Авторизация.Регистрация.Регистрация.Авторизация.
                    Регистрация.Авторизация.Регистрация.Регистрация.Авторизация.
                </p>

                <p class="font-bold">
                    Уже есть аккаунт? <RouterLink :to="{'name': 'signin'}" class="underline">Перейди сюда</RouterLink>, чтобы авторизоваться!
                </p>
            </div>
        </div>

        <div class="main-right">
            <div class="p-12 bg-white border border-gray-200 rounded-lg">
                <form class="space-y-6" v-on:submit.prevent="submitForm">
                    <div>
                        <label>Имя</label><br>
                        <input type="text" v-model="form.name" placeholder="Ваше полное имя" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>

                    <div>
                        <label>E-mail</label><br>
                        <input type="email" v-model="form.email" placeholder="Ваш e-mail адрес" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>

                    <div>
                        <label>Пароль</label><br>
                        <input type="password" v-model="form.password1" placeholder="Ваш пароль" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>

                    <div>
                        <label>Подтвердите пароль</label><br>
                        <input type="password" v-model="form.password2" placeholder="Повторите ваш пароль" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>

                    <template v-if="errors.length > 0">
                      <div class="bg-red-300 text-white rounded-lg p-6">
                        <p v-for="error in errors" v-bind:key="error">{{error}}</p>
                      </div>
                    </template>

                    <div>
                        <button class="py-4 px-6 bg-blue-400 text-white rounded-lg">Зарегистрироваться</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import {useToastStore} from "@/stores/toast";

export default {
  setup() {
    const toastStore = useToastStore()

    return{toastStore}
  },

  data() {

    return{
      form:{
        email: '',
        name: '',
        password1: '',
        password2: '',

        },
      errors: []
      }
    },
      methods: {
        submitForm() {
          this.errors = []

           if(this.form.email === ''){
            this.errors.push('Your email is missing')
          }

          if(this.form.name === ''){
            this.errors.push('Your name is missing')
          }

          if(this.form.password1 === ''){
            this.errors.push('Your password is missing')
          }

          if(this.form.password1 !== this.form.password2){
            this.errors.push('Your password does not match')
          }


            if (this.errors.length === 0) {
                axios
                    .post('/api/signup/', this.form)
                    .then(response => {
                        if (response.data.message === 'success') {
                            this.toastStore.showToast(5000, 'The user is registered. Please activate your account by clicking your email link.', 'bg-emerald-500')

                            this.form.email = ''
                            this.form.name = ''
                            this.form.password1 = ''
                            this.form.password2 = ''
                        } else {
                           const data = JSON.parse(response.data.message)
                            for (const key in data){
                                this.errors.push(data[key][0].message)
                            }

                            this.toastStore.showToast(5000, 'Something went wrong. Please try again', 'bg-red-300')
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
