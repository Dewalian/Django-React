import {Link} from "react-router-dom";

const Navbar = () => {
    return ( 
        <div className="navbar">
            <div className="nav-left">
                <div className="nav-item nav-title">REACT</div>
                <div className="nav-item"><Link to="/home">Home</Link></div>
            </div>
            <div className="nav-right">
                <div className="nav-item"><Link to="/register">Register</Link></div>
                <div className="nav-item"><Link to="/login">Login</Link></div>
            </div>
        </div>
     );
}

export default Navbar;