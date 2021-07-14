import useFetch from "./UseFetch";

const MainContent = () => {
    const {data, isPending, error} = useFetch("http://127.0.0.1:8000/api/question/");
    return ( 
        <div className="main-content">
            {error && <div>{error}</div>}
            {isPending && <div>Loading...</div>}
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