const output = document.getElementsByClassName('output')[0]
const btn = document.querySelector('button')


function processClick(cb){
    let value = Number(document.querySelector('input').value);
    if (typeof(value) === 'number'  && !isNaN(value)){
        if (value > 0 && value <= 10){
            cb(value)
        }
        else{
            output.innerText  = 'Введите число в диапазоне от 1 до 10'
        }
    }
    else{
        output.innerText = 'Введите числовое значение'
    }
}

function makeRequest(numb){
    const url = `https://picsum.photos/v2/list?limit=${numb}`
    const xhr = new XMLHttpRequest()
    let result = ''
    xhr.open('get', url)
    xhr.onload = function() {
        if (xhr.status != 200) {
            output.innerText = 'Неудалось соедениться с сервером'
        } else {
            const response = JSON.parse(xhr.response)
            for(let item in response){
                result += `<div class="card-board">
                               <img src="${response[item].download_url}" 
                               class="card">
                           </div>`
            }
            output.innerHTML = result;
        }
    }
    xhr.send()

}

btn.addEventListener('click', () => processClick(makeRequest))
