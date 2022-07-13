const output = document.getElementsByClassName('output')[0]
const btn = document.querySelector('button')

function verifyNumber(value){
    if (typeof(value) === 'number'  && !isNaN(value)){
        return value >= 1 && value <= 10;
    } else {
        return false
    }
}

async function clickOnMe(func){
    const number1 = Number(document.getElementById('inp1').value)
    const number2 = Number(document.getElementById('inp2').value)
    if (!verifyNumber(number1) && !verifyNumber(number2)){
        output.innerText = 'Номер страницы и лимит вне диапазона от 1 до 10'
    } else if (!verifyNumber(number1)){
        output.innerText = 'Номер страницы вне диапазона от 1 до 10'
    } else if (!verifyNumber(number2)){
        output.innerText = 'Лимит вне диапазона от 1 до 10'
    } else {
        const url = `https://picsum.photos/v2/list?page=${number1}&limit=${number2}`
        let answer = await func(url)
        if (answer){
            localStorage.setItem('previousResponse', answer)
            output.innerHTML = answer
        } else {
            console.log('Нету ответа')
        }

    }
}

makeRequest = url => {
    return fetch(url)
        .then((response) =>{
            return response.json()
        })
        .then((jsonResponse) => {
            let result = ''
            jsonResponse.forEach(item => {
                const oneImage = `<div class="card-board">
                                    <img src="${item.download_url}" 
                                     class="card">
                                  </div>`
                result += oneImage
            });
            return result
        })
        .catch((error) =>{
            output.innerText = `Ошибка обращения к серверу ${error}`
            return false
        })
}

btn.addEventListener('click', () => clickOnMe(makeRequest))

const prevResponse = localStorage.getItem('previousResponse')
if (prevResponse){
    output.innerHTML = prevResponse
}