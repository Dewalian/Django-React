import {useForm} from "react-hook-form";
import {useHistory} from "react-router-dom";
import CSRFToken from "./CSRFToken";
import axiosInstance from "./AxiosInstance";
import { useAxios } from "use-axios-client";

const Register = () => {
    const history = useHistory();
    const {data} = useAxios({url: "http://127.0.0.1:8000/api/user/"});
    const {register, watch, handleSubmit, formState: {errors}} = useForm();
    const watchPassword = watch("password");

    const submit = (data) => {
        axiosInstance.post("/user/", {
            username: data.username,
            email: data.email,
            password: data.password
        })
        .then((res) => {
            history.push("/login");
        })
        .catch((err) => {
            console.error(err);
        })
    };

    const classToggle = (errorName) => {
        if (errorName) {
            return "error";
        } else {
            return null;
        };
    };

    return (
        <form onSubmit={handleSubmit(submit)} className="acc-form">
            <h2>REGISTER</h2>
            <CSRFToken />
            <input className={classToggle(errors.username)} type="text" placeholder="Username" autoComplete="off"
            {...register("username", {
                required: "username required",
                minLength: {value: 4, message: "must be at least 4 characters"},
                maxLength: {value: 12, message: "cannot be more than 12 characters"},
                validate: (v) => !data.find((user) => user.username === v) || "username already exist"
            })}/>
            {errors.username && <div>{errors.username.message}</div>}

            <input className={classToggle(errors.email)} type="text" placeholder="Email" autoComplete="off"
            {...register("email", {
                required: "email required",
                pattern: {value: /^(\w{1,}([-.]\w{1,})*)@\w{1,}(\.\w{2,}){1,}$/, message: "email is invalid"},
                validate: (v) => !data.find((user) => user.email.toLowerCase() === v.toLowerCase()) || "email already exist"
            })}/>
            {errors.email && <div>{errors.email.message}</div>}

            <input className={classToggle(errors.password)} type="password" placeholder="Password"
            {...register("password", {
                required: "password required",
                minLength: {value: 6, message: "must be at least 6 characters"},
                validate: {
                    upper: (v) => /[A-Z]/.test(v) || "must have upper letter(s)",
                    numerical: (v) => /[0-9]/.test(v) || "must have numerical character(s)"
                }
            })}/>
            {errors.password && <div>{errors.password.message}</div>}

            <input className={classToggle(errors.password2)} type="password" placeholder="Re-enter Password" 
            {...register("password2", {
                required: "password confirmation required",
                validate: (v) => v === watchPassword || "password do not match"
            })}/>
            {errors.password2 && <div>{errors.password2.message}</div>}

            <input type="submit" value="Register" />
        </form>      
     );
}
 
export default Register;