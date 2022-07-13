const output = document.getElementsByClassName('output')[0]
const btn = document.querySelector('button')

function verifyNumber(value){
    if (typeof(value) === 'number'  && !isNaN(value)){
        return value >= 100 && value <= 300;
    } else {
        return false
    }
}

async function processClick(func){
    let value1 = Number(document.getElementById('inp1').value);
    let value2 = Number(document.getElementById('inp2').value);
    if (verifyNumber(value1) && verifyNumber(value2)){
        let url = `https://picsum.photos/${value1}/${value2}`;
        const answer = await func(url);
        if (answer){
            const result = `<div class="card-board">
                               <img src="${answer}">
                           </div>`
            output.innerHTML = result;
        } else {
            console.log('Нету ответа')
        }
    }
    else{
        output.innerText = 'Водно из чисел вне диапазона от 100 до 300'
    }
}

retrieveData = url => {
    return fetch(url)
        .then((response) => {
            return response.url;
        })
        .catch((error) => {
            output.innerText = 'Ошибка обращения к серверу'
            return false
            }
        )
}

btn.addEventListener('click', () => processClick(retrieveData))