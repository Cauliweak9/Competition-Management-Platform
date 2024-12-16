import Vue from 'vue';
import VueRouter from 'vue-router';
import axios from 'axios';
import Login from './components/Login.vue'; // 登录页面
import Dashboard from './components/Dashboard.vue'; // 受保护页面

Vue.use(VueRouter);

const routes = [
    { path: '/', redirect: '/login' },
    { path: '/login', component: Login },
    { path: '/dashboard', component: Dashboard, meta: { requiresAuth: true } }
];

const router = new VueRouter({
    routes
});

// 全局路由守卫
router.beforeEach((to, from, next) => {
    const token = localStorage.getItem('token'); // 从 localStorage 获取 Token

    if (to.matched.some(record => record.meta.requiresAuth)) {
        // 需要登录的路由
        if (!token) {
            next('/login'); // 如果没有 Token，跳转到登录页
        } else {
            // 验证 Token 的有效性
            axios.get('/verify-token', {
                headers: { Authorization: `Bearer ${token}` }
            }).then(() => {
                next(); // Token 有效，允许访问
            }).catch(() => {
                localStorage.removeItem('token'); // 移除无效 Token
                localStorage.removeItem('user');
                next('/login'); // Token 无效，跳转到登录页
            });
        }
    } else {
        // 不需要登录的路由直接放行
        next();
    }
});

export default router;
