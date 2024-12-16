<template>
    <div class="login-container" id="app">
        <div class="login-title">
            <img src="static/images/shark.png" alt="" id="logo">
            <span v-show="!islogged">登录到本科生竞赛交流平台</span>
            <span v-show="islogged" v-text="'欢迎回来，' + info.id"></span>
            <button id="back_to_index" v-show="islogged" @click="goHome">返回首页</button>
        </div>
        <form @submit.prevent="loginform" v-show="!islogged">
            <div class="form-group">
                <label for="email" v-if="email">请输入邮箱</label>
                <input type="email" id="email" v-model="info.email" @focus="onfocus('email')" @blur="onblur('email')">
            </div>
            <div class="form-group">
                <label for="password" v-if="password">请输入密码</label>
                <input type="password" id="password" v-model="info.password" @focus="onfocus('password')" @blur="onblur('password')">
            </div>
            <button type="submit" class="btn-login">登录</button>
        </form>
        <div class="links" v-show="!islogged">
            <p id="signin">用户注册</p>
            <p id="forget_password">忘记密码</p>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            email: true,
            password: true,
            islogged: false,
            info: {
                email: '',
                password: '',
                id: ''
            }
        };
    },
    methods: {
        onfocus(id) {
            if (id === "email") {
                this.email = false;
            } else if (id === "password") {
                this.password = false;
            }
        },
        onblur(id) {
            if (id === "email") {
                this.email = this.info.email === "";
            } else if (id === "password") {
                this.password = this.info.password === "";
            }
        },
        loginform() {
            const that = this;
            axios.post('/login', {
                email: this.info.email,
                password: this.info.password
            }).then(res => {
                if (res.data.code === 1) {
                    that.islogged = true;
                    that.info = { ...res.data.data };
                    localStorage.setItem('token', res.data.access_token);
                    localStorage.setItem('user', JSON.stringify(res.data.data));
                    that.$router.push('/dashboard'); // 跳转到受保护页面
                } else {
                    alert("用户名或密码错误");
                    that.info.password = '';
                }
            }).catch(err => {
                alert("登录失败，请稍后再试！");
                console.error(err);
                that.info.password = '';
            });
        }
    }
};
</script>
