// 配置API接口地址
import axios from 'axios';
import routes from "./router";
import qs from 'qs'

let base = 'http://127.0.0.1:8000/api/bus';

axios.interceptors.request.use(
    config => {
        config.data = qs.stringify(config.data);
        config.headers = {
            'Content-Type':'application/x-www-form-urlencoded'
        }
        return config;
    },
    err => {
        return Promise.reject(err);
    }
);

// export const requestLogin = params => { return axios.post(`${base}/login`, params).then(res => res.data); };
export const getBusList = params => { return axios.get(`${base}/bus/`, { params: params }); };

export const updateList = params => { return axios.post(`${base}/addProFlow/update`,{ params },{headers: {
                                                'Content-Type': 'application/json;',
                                              },
                                              }); };

export default routes;
