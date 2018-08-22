import axios from 'axios';
import routes from "./router";
import VueRouter from 'vue-router';

import router from './router';

import {setToken,getToken,clearToken} from './localStorage'

// import { Message } from 'element-ui';

axios.defaults.timeout = 5000;
axios.defaults.baseURL ='';
let base = 'http://127.0.0.1:8000/';

// const router = new VueRouter({
//     routes
// })

//http request 拦截器
axios.interceptors.request.use(
  config => {
    let token = getToken("token");
    config.data = JSON.stringify(config.data);
    config.headers = {
      // 'Content-Type':'application/x-www-form-urlencoded'
      'Content-Type': 'application/json;charset=UTF-8'
    }
    if(token) {
      config.headers.Authorization=`JWT ${token}`
    }
    return config;
  },
  error => {
    return Promise.reject(error);
  }
);


//http response 拦截器
axios.interceptors.response.use(
  response => {
    return response;
  },
  error => {
    switch (error.response.status) {
      case 401:
        // 返回 401 跳转到登录页面
        router.replace({
          path: '/login',
          query: { redirect: router.currentRoute.path },
        })
        error.response.data.detail = "登录信息已过期，请重新登录"
        break
      case 404:
        router.replace({
            path: '/404'
        })
        break
      case 400:
        router.replace({
            path: '/login'
        })
        error.response.data.detail = "用户名或密码错误"
        break
    }
    return Promise.reject(error)
  }
)


/**
 * 封装get方法
 * @param url
 * @param data
 * @returns {Promise}
 */

export function fetch(url,params={}){
  return new Promise((resolve,reject) => {
    axios.get(`${base}${url}`,{params:params})
    .then(response => {
      resolve(response.data);
    },err => {
      reject(err.response)
    })
  })
}


/**
 * 封装post请求
 * @param url
 * @param data
 * @returns {Promise}
 */

 export function post(url,data = {}){
   return new Promise((resolve,reject) => {
     axios.post(`${base}${url}`,data)
        .then(response => {
          resolve(response.data);
        },err => {
          reject(err.response)
        })
   })
 }

 /**
 * 封装patch请求
 * @param url
 * @param data
 * @returns {Promise}
 */

export function patch(url,data = {}){
  return new Promise((resolve,reject) => {
    axios.patch(`${base}${url}`,data)
       .then(response => {
         resolve(response.data);
       },err => {
         reject(err.response.data.detail)
       })
  })
}

 /**
 * 封装put请求
 * @param url
 * @param data
 * @returns {Promise}
 */

export function put(url,data = {}){
  return new Promise((resolve,reject) => {
    axios.put(`${base}${url}`,data)
       .then(response => {
         resolve(response.data);
       },err => {
         reject(err.response.data.detail)
       })
  })
}

 /**
 * 封装delete请求
 * @param url
 * @param data
 * @returns {Promise}
 */
export function del(url,data = {}){
  return new Promise((resolve,reject) => {
    axios.delete(`${base}${url}`,data)
       .then(response => {
         resolve(response.data);
       },err => {
         reject(err.response.data.detail)
       })
  })
}
