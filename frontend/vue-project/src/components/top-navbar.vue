<script setup>
import { computed } from 'vue'; // 确保导入 computed
import { userstore } from '../stores/user'
const user=userstore();
</script>

template:
<template class="top-navbar">
<body>
    <div class="navbar">
        <div class="menu">
            <img src="../assets/images/logo.png" alt="shark" > <!-- Logo占位符 -->
            <span strong>深圳大学本科生竞赛交流平台</span>
            <span class="list">
            <button>首页</button>
            <button>比赛</button>
            <button>论坛</button>
            </span>
        </div>
        <div class="auth-buttons">
            <button class="login-btn" v-show="!user.islogin">登录</button>
            <button id="register-btn" v-show="!user.islogin">注册</button>
            <img v-show="user.islogin" src="../assets/images/shark.jpg" alt="shark" class="id-img">
            <a class="top-id" href="#" v-show="user.islogin">{{ user.info.id }}</a>
        </div>
    </div>
</body>
</template>

style:
<style >
        .top-navbar {
            display: block;
            width: 100%; /* 设置宽度为100% */
            margin: 0; /* 确保没有外边距 */
            padding: 0; /* 如果需要，也可以清除内边距 */
            font-family: Arial, sans-serif;
            background-color: #f5f7fa; /* 淡灰色背景 */
            box-sizing: border-box; /* 确保盒模型的宽度包括padding和border */
        }
        .navbar {
            flex-grow: 1; /* 让顶部栏扩展以填满剩余空间 */
            display: flex;
            align-items: center;
            width:100%;
            justify-content: space-between;
            padding: 10px 20px;
            background-color: white;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            box-sizing: border-box; /* 确保盒模型的宽度包括padding和border */
        }
        .list{
            margin-left: 20px;
        }
        .menu img {
            position:relative;
            height: 40px;
            width:auto;
            margin-bottom: -13px;
            margin-left: 20px;
        }
        .menu a {
            text-decoration: none;
            color: black;
            margin-left: 15px;
        }
        .menu button{
            border: none;
            background-color: transparent;
            cursor: pointer;
            color: black;
            transition: background-color 0.3s; /* 添加过渡效果 */
            font-size: 20px; /* 设置按钮文字的大小 */
            width: 100px; /* 设置按钮的宽度 */
            height: 40px; /* 设置按钮的高度 */
            border-radius: 10px; /* 设置按钮的圆角 */
            margin-right: 10px;

        }
        .menu button:hover {
            background-color: #e9ecef; /* 按钮悬停时的背景颜色 */
        }
        .auth-buttons button {
            border: none;
            background-color: transparent;
            cursor: pointer;
            color: black;
            transition: background-color 0.3s; /* 添加过渡效果 */
            font-size: 15px; /* 设置按钮文字的大小 */
            width: 60px; /* 设置按钮的宽度 */
            height: 40px; /* 设置按钮的高度 */
            border-radius: 10px; /* 设置按钮的圆角 */
            margin-right: 10px;
        }
        .auth-buttons button:hover {
            background-color: #e9ecef; /* 按钮悬停时的背景颜色 */
        }
        .auth-buttons .top-id{
            position:absolute;
            top:20px;
            right:40px;
            font-size:20px;

            text-decoration:none;
            color:rgb(122, 122, 122);
            font-weight:bold;
            transition:color 0.3s;
        }
        .top-id:hover{
            color:black;
        }
        .id-img{
            position:absolute;
            height: 40px;
            top:10px;
            right:80px;
            width:auto;
            margin-right:'30px';
        }
</style>