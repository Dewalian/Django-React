import Cookies from "js-cookie";

const CSRFToken = () => {
    const csrf = Cookies.get("csrftoken")

    return ( 
        <input type="hidden" name="csrfmiddlewaretoken" value={csrf} />
     );
}
 
export default CSRFToken;
