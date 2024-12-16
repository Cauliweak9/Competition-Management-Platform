<script setup>
import { createApp } from 'vue';
import { RouterLink, RouterView } from 'vue-router'
import topnavbar from './components/top-navbar.vue'
import botnavbar from './components/bot_navbar.vue'
import {userstore} from './stores/user';

const store=userstore();
</script>

<template>
  <div id="app">
    <nav>
      <topnavbar style="width: 100vw;" :islogin="islogin"/>
    </nav style="display:block">
    <div class="container" >
      <router-view></router-view>
    </div>
    <footer>
      <botnavbar style="width: 100vw;"/>
    </footer>
  </div>
</template>

<script>
export default {
  data(){
    return{
      islogin: false,
      id:'',
      email:''
    }
  },
}
</script>

<style>
* {
  margin:0;
  padding:0;
}
body{
  background-color: #f5f7fa;
}
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
  }
.container{
}
</style>
