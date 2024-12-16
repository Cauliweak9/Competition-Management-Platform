// src/stores/auth.js
import {ref,computed} from 'vue';
import { defineStore } from 'pinia';

export const userstore = defineStore('auth', () => {
    const token=ref('')
    const islogin=ref(false)
    const info=ref({
        id:'',
        email:'',
        password:''
    })
    function login(data){
        console.log(data)
        info.value.id=data.info.id
        info.value.email=data.info.email
        token.value=data.token
        islogin.value=true
    }
    function logout(){
        token.value=''
        info.name=''
        info.email=''
        info.password=''
        islogin.value=false
    }
    return {
        token,
        info,
        islogin,
        login,
    }
});

