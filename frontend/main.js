const TokenArr = [

]

const ENDPOINT = 'http://localhost:8000/';
const createToken = 'api/token/';
const sendBtn = document.querySelector('.sendBtn');




const sendPost = () => {
    
for (let i = 0; i < TokenArr.length; i++ ){

            fToken = TokenArr[i];
            let data = {
                token: fToken,
            };
            fetch(ENDPOINT+createToken, {
                method: 'POST', // или 'PUT'
                body: JSON.stringify(data), 
                headers: {
                        'Content-Type': 'application/json'
                }
            })
            .then(response => response.json())

    console.log(i);
}


};

sendBtn.addEventListener('click', sendPost)