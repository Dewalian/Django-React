import {useAxios} from "use-axios-client";

const MainContent = () => {
    const {data, error, loading} = useAxios({url: "http://127.0.0.1:8000/api/question/"});
    return ( 
        <div className="main-content">
            {error && <div>{error.message}</div>}
            {loading && <div>Loading...</div>}
            {data && data.map(question => (
                <div className="question-post" key={question.id}>
                    <h1>{question.title}</h1>
                    <hr/>
                    <p className="user">by {question.user}</p>
                    <p className="ask">{question.ask_post}</p>
                </div>
            ))}
        </div>
     );
};
 
export default MainContent;