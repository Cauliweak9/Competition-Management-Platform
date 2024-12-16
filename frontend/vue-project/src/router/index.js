import { createRouter, createWebHistory } from 'vue-router'
import login from '../views/login.vue';
import hello from '../views/AboutView.vue';
import user from '../views/user.vue';

// 路由配置
const routes = [
  { path: '/', component: hello },
  { path: '/login', component: login },
  { 
    path: '/user', 
    component: user, 
    meta: { requiresAuth: true } 
  },
  { 
    name: 'UserInfo',
    path: '/user/:id',
    component: user,
    meta: { requiresAuth: true } 
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

// 路由守卫
router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('token'); // 获取 token
  if (to.matched.some(record => record.meta.requiresAuth) && !token) {
    next('/login'); // 如果没有 token，跳转到登录页面
  } else {
    next(); // 否则允许访问
  }
});


export default router
