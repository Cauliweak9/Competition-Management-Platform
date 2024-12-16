template:
<template>
<body>
    <div class="navbar">
        <div class="menu">
            <img src="/static/images/shark.png" alt="shark" > <!-- Logo占位符 -->
            <span v-show="!islogged" strong>深圳大学本科生竞赛交流平台</span>
            <span class="list">
            <button>首页</button>
            <button>比赛</button>
            <button>论坛</button>
            </span>
        </div>
        <div class="auth-buttons">
            <button class="login-btn">登录</button>
            <button>注册</button>
        </div>
    </div>
</body>
</template>
style:
<style>
  body {
            margin: 0;
            font-family: Arial, sans-serif;
            background-color: #f5f7fa; /* 淡灰色背景 */
        }
        .navbar {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 10px 20px;
            background-color: white;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        .list{
            margin-left: 20px;
        }
        .menu img {
            position:relative;
            height: 40px;
            weight:auto;
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
</style>