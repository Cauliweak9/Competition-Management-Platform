<script setup>
import { userstore } from '../stores/user';
import { ref } from 'vue';
import axios from 'axios';
import Cookies from 'js-cookie';
import router from '../router/index.js'
const user=userstore()

// 登录表单信息
const info = ref({
  email: '',
  password: ''
});
const loginform = () =>{
  axios.post('http://127.0.0.1:5173/login', {
        email: info.value.email,
        password: info.value.password
      }).then(res => {
        if (res.data.code === 1) {
          console.log(res.data.data);
          user.login({
            info: res.data.data,
            token: res.data.token
          });
          
          // 保存 Token 到 Cookies 和 localStorage
          Cookies.set('token', res.data.token, { secure: true, sameSite: 'Strict' });
          console.log(res.data.token);
          localStorage.setItem('token', res.data.token);
          // 跳转到用户页面
          router.push({ name: 'UserInfo', params: { id: res.data.data.id } });
        } else {
          alert("用户名或密码错误");
          user.info.password.value = '';
        }
      }).catch(err => {
        alert("登录失败，请稍后再试！");
        console.error(err);
        user.info.password.value = '';
      });
}
</script>
<template id="login">
  <div class="login">
  <div class="login-container" id="app">
    <div class="login-title">
      <img src="../assets/images/logo.png" alt="" id="logo">
      <span v-if="!islogged">登录到本科生竞赛交流平台</span>
      <span v-else>欢迎回来，用户ID: {{ info.id }}</span>
      <button id="back_to_index" v-if="islogged" @click="goHome">返回首页</button>
    </div>

    <!-- 登录表单 -->
    <form @submit.prevent="loginform" v-if="!islogged">
      <div class="form-group">
        <label for="email" v-if="email">请输入邮箱</label>
        <input 
          type="email" 
          id="email" 
          v-model="info.email" 
          @focus="onfocus('email')" 
          @blur="onblur('email')" 
          style="font-size: 20px;" 
          required
        >
      </div>
      <div class="form-group">
        <label for="password" v-if="password">请输入密码</label>
        <input 
          type="password" 
          id="password" 
          v-model="info.password" 
          @focus="onfocus('password')" 
          @blur="onblur('password')" 
          style="font-size: 20px;" 
          required
        >
      </div>
      <button type="submit" class="btn-login">登录</button>
    </form>

    <!-- 链接部分 -->
    <div class="links" v-if="!islogged">
      <p id="signin" @click="goToRegister">用户注册</p>
      <p id="forget_password" @click="goToForgotPassword">忘记密码</p>
    </div>
  </div>
  </div>
</template>

<script>
import axios from 'axios';
import { ref } from 'vue';
import Cookies from 'js-cookie';


export default {
  data() {
    return {
      email: true,
      password: true,
      islogged: false,
      info: {
        email: '',
        id: ''
      }
    };
  },
  methods: {
    onfocus(id) {
      if (id === "email") this.email = false;
      if (id === "password") this.password = false;
    },
    onblur(id) {
      if (id === "email") this.email = !this.info.email;
      if (id === "password") this.password = !this.info.password;
    },
    loginform() {
      axios.post('http://127.0.0.1:5173/login', {
        email: this.info.email,
        password: this.info.password
      }).then(res => {
        if (res.data.code === 1) {
          this.islogged = true;
          this.info = { ...res.data.data };
          // 保存 Token 到 Cookies 和 localStorage
          Cookies.set('token', res.data.token, { secure: true, sameSite: 'Strict' });
          console.log(res.data.token);
          localStorage.setItem('token', res.data.token);
          // 跳转到用户页面
          this.$router.push({ name: 'UserInfo', params: { id: res.data.data.id } });
        } else {
          alert("用户名或密码错误");
          this.info.password = '';
        }
      }).catch(err => {
        alert("登录失败，请稍后再试！");
        console.error(err);
        this.info.password = '';
      });
    },
    goHome() {
      this.$router.push('/');
    },
    goToRegister() {
      this.$router.push('/register'); // 假设你有注册页面
    },
    goToForgotPassword() {
      this.$router.push('/forgot-password'); // 假设你有找回密码页面
    },

  }
};
</script>

<style>
.login{
  height:519px;
}
/* 样式保持一致 */
.login-title {
  text-align: center;
  font-size: 18px;
  font-weight: bold;
  margin-bottom: 25px;
  margin-right: 20px;
}
#logo {
  width: 40px; 
  height: auto; 
  margin-bottom: -20px;
}
#back_to_index {
  width: 100%;
  padding: 12px;
  background-color: #333;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
  margin-top: 25px;
  margin-left: 10px;
}
.login-container {
  width: 500px;
  padding: 30px;
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  margin-top: 170px;
  margin-left:auto;
  margin-right:auto;
  justify-content: center;
  align-items: center;
}
.form-group {
  position: relative;
  margin-bottom: 10px;
  justify-content: center;
  align-items: center;
  margin-left:auto;
  margin-right:auto;
}
.form-group label {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  left: 10px;
  color: #999;
}
.form-group input {
  width: calc(100% - 22px);
  padding: 12px 6px 12px 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  outline: none;
}
.btn-login {
  width: 100%;
  padding: 12px;
  background-color: #333;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
}
.links {
  display: flex;
  justify-content: space-between;
  text-decoration: none;
  margin-top: 10px;
  gap: 40px;
  font-size: 14px;
  color: #666;
}
.links p {
  cursor: pointer;
}
#signin:hover, #forget_password:hover {
  text-decoration: underline;
}
</style>
