import axios, { AxiosResponse, AxiosError } from 'axios';

const http = axios.create();

const onSuccess = (response: AxiosResponse) => response;

const onError = (error: AxiosError) => {
  if (axios.isCancel(error)) {
    console.log("request cancelled!");
    return;
  }
  if (error.message === "Network Error") {
    window.location.href = "/503";
    return;
  }
  if (typeof error.response === "undefined") {
    alert("予期せぬエラーが発生したよ。ぴえん");
    return Promise.reject(error);
  }
  switch (error.response.status) {
    case 500:
      window.location.href = "/500";
      return;
    default:
      alert("予期せぬエラーが発生したよ。ぴえん");
      return Promise.reject(error);
  }
};

http.interceptors.response.use(onSuccess, onError);

export default http;
