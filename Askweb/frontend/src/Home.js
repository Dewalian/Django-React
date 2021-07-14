import MainContent from "./MainContent"
import Navbar from "./Navbar";
import Sidebar from "./Sidebar";

const Home = () => {
    return ( 
        <div className="App">
            <Navbar/>
            <div className="home">
                <MainContent />
                <Sidebar />
            </div>
        </div>
     );
}
 
export default Home;