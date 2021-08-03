import axios from "axios";
import Cookies from "js-cookie";

const csrftoken = Cookies.get("csrftoken")

const axiosInstance = axios.create({
    baseURL: "http://127.0.0.1:8000/api",
    timeout: 5000,
    headers: {
        "Content-Type": "application/json",
        accept: "application/json",
        "X-CSRFToken": csrftoken
    }
});

export default axiosInstance