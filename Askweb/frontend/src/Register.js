import {useForm} from "react-hook-form";

const Register = () => {
    const {register, watch, handleSubmit, formState: {errors}} = useForm();
    const watchPassword = watch("password")

    const submit = (data) => {
        console.log(data)
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
            <h2>REGISTER</h2>
            <input className={classToggle(errors.username)} type="text" placeholder="Username"
            {...register("username", {
                required: "username required",
                minLength: {value: 4, message: "must be at least 4 characters"},
                maxLength: {value: 12, message: "cannot be more than 12 characters"}
            })}/>
            {errors.username && <div>{errors.username.message}</div>}

            <input className={classToggle(errors.email)} type="text" placeholder="Email" 
            {...register("email", {
                required: "email required",
                pattern: {value: /^(\w{1,}(([-.]\w{1,})*)?)@\w{1,}(\.\w{2,}){1,}$/, message: "email is invalid"}
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