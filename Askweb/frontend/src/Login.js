import {useForm} from "react-hook-form";
import { useHistory } from "react-router";
import axiosInstance from "./AxiosInstance";

const Login = () => {
    const history = useHistory();
    const {register, handleSubmit, formState: {errors}} = useForm();

    const submit = (data) => {
        axiosInstance.post("token/", {
            username: data.username,
            password: data.password
        })
        .then((res) => {
            localStorage.setItem("access_token", res.data.access);
            localStorage.setItem("refresh_token", res.data.refresh);
            axiosInstance.defaults.headers["Authorization"] = `JWT ${localStorage.getItem("access_token")}`;
            history.push("/");
        })
    };

    const classToggle = (errorName) => {
        if (errorName) {
            return "error"
        } else {
            return null
        };
    };
    
    return ( 
        <form onSubmit={handleSubmit(submit)} className="acc-form">
            <h2>LOGIN</h2>
            <input className={classToggle(errors.username)} type="text" placeholder="Username" 
            {...register("username", {
                required: "username required",
                minLength: {value: 4, message: "must be at least 4 characters"},
                maxLength: {value: 12, message: "cannot be more than 12 characters"}
            })}/>
            {errors.username && <div>{errors.username.message}</div>}

            <input className={classToggle(errors.password)} type="password" placeholder="Password" 
            {...register("password", {
                required: "password required"
            })}/>
            {errors.password && <div>{errors.password.message}</div>}

            <input type="submit" value="Login" />
        </form>
     );
}
 
export default Login;