import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex)

const store = new Vuex.Store({
  // 定义状态
  state: {
    //登录状态，默认为''，当登录成功后自动再更新状态
    isLogin :''
  },
  mutations:{
    isLogin(state,msg){
      state.isLogin = msg;
      this.setToken('isLogin',msg)
    }
  }
})
export default store
