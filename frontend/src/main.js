// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App.vue'
// 引用路由
import router from './config/router'

// 引用API文件
import {post,fetch,patch,put,del} from './config/api'
//定义全局变量
Vue.prototype.$fetch=fetch;
Vue.prototype.$post=post;
Vue.prototype.$patch=patch;
Vue.prototype.$put=put;
Vue.prototype.$del=del;

import {setToken,getToken,clearToken} from './config/localStorage'
Vue.prototype.$setToken=setToken;
Vue.prototype.$getToken=getToken;
Vue.prototype.$clearToken=clearToken;


import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import 'font-awesome/css/font-awesome.min.css'

Vue.use(ElementUI)


// Vue.config.productionTip = false

// Vue.prototype.$api = api

/* eslint-disable no-new */
new Vue({
    router,
    el: '#app',
    render: (h) => h(App)
})
