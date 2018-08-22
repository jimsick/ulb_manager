// 引用模板
import Vue from 'vue'
import VueRouter from 'vue-router'

import Home from '../page/Home.vue'
import Bus from '../page/bus/Bus.vue'
import Login from '../page/Login.vue'
import NotFound from '../page/404Page.vue';
import {clearToken, getToken} from "./localStorage";
Vue.use(VueRouter)

// 配置路由
const routes = [
    {
        path: '/',
        component: Home,
        name: '公交管理配置',
        iconCls: 'fa fa-id-card-o',//图标样式class
        meta: {
          requireAuth: true,
        },
        children: [
            { path: '/bus', component: Bus, name: '公交列表'},
            // { path: '/table', component: Table, name: 'Table' },
        ]
    },
    {
        path: '/login',
        component: Login,
        iconCls: 'el-icon-message',//图标样式class
        name: '登录',
        hidden: true
    },
    {
      path: "/404",
      name: "notFound",
      component: NotFound,

      hidden: true
    },
    {
      path:'*',
      component:NotFound,
      hidden: true
    }
];

// 使用配置文件规则
const router = new VueRouter({
    routes
})

router.beforeEach((to, from, next) => {
//设置延时器让created先执行在进行路由跳转
    // 判断该路由是否需要登录权限
  // let redirect = from.query.redirect//如果来源路由有query
  if ((getToken("token")==null||getToken("token")=="") && to.path != '/login') {
    clearToken()
    // 通过vuex state获取当前的状态是否存在
      next({
        path: '/login',
        query: {
          redirect: to.fullPath
        } // 将跳转的路由path作为参数，登录成功后跳转到该路由
      })
  }else if(to.path == '/login'){
    clearToken()
    next();
  }else {
    next();
  }
})


export default router;
