import Home from "./Home";
import Register from "./Register";
import Login from "./Login";
import {BrowserRouter as Router, Route, Switch} from "react-router-dom";

function App() {
  return (
    <Router>
        <div>
            <Switch>
                <Route exact path={["/", "/home"]} component={Home} />
                <Route path="/register" component={Register} />
                <Route path="/login" component={Login} />
            </Switch>
        </div>
    </Router>
  );
}

export default App;
