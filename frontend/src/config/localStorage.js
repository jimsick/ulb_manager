export function setToken(tokenName, tokenValue){
    if (window.localStorage) {
      localStorage.setItem(tokenName, tokenValue);
    } else {
      alert('This browser does NOT support localStorage');
    }
}

export function getToken(name){
     var token = localStorage.getItem(name);
    if (token) {
      return token;
    } else {
      return '';
    }
}
export function clearToken(){
     localStorage.clear()
}
