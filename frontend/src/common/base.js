Vue.prototype.setToken = function (tokenName, tokenValue) {
    if (window.localStorage) {
      localStorage.setItem(tokenName, tokenValue);
    } else {
      alert('This browser does NOT support localStorage');
    }
};
Vue.prototype.getToken = function (name) {
    var token = localStorage.getItem(name);
    if (token) {
      return token;
    } else {
      return '';
    }
  };
