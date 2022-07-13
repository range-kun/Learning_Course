const output = document.querySelector(".output");
const inp = document.querySelector('.inp-text')
const sendBtn = document.getElementById('send_message')
const locationBtn = document.getElementById('get_location')
const websocket = new WebSocket('wss://echo.websocket.org/');


// Получение гео-локации //

locationBtn.addEventListener('click', ()=>{
    navigator.geolocation.getCurrentPosition(success, error);
})

const success = (position) => {
    const latitude  = position.coords.latitude;
    const longitude = position.coords.longitude;

    addMessage('Гео-локация', true,
        `https://www.openstreetmap.org/#map=18/${latitude}/${longitude}`)
    websocket.send(position)
    websocket.onmessage = function (evt) {
        const response = evt.data
        console.log('Отправили серверу свою позицию ' + response)
    }
}

const error = () => {
    addMessage('Отказано пользователем в доступе к гео-локации')
}

// Отправка просытх сообщений //

sendBtn.addEventListener('click', ()=>{
    const inputText = inp.value;
    if (inputText) {
        inp.value = ''
        addMessage(inputText)
        websocket.send(inputText)
        websocket.onmessage = function (evt) {
            const response = `Эхо - сервер: ${evt.data}`
            addMessage(response, false)
        }
    }
})

function addMessage (inputText, isHuman=true, link){
    let messageBlock
    if (link){
        messageBlock = document.createElement('a')
        messageBlock.href = link
        messageBlock.classList.add('geo_link')
    } else {
        messageBlock = document.createElement('p')
    }
    messageBlock.innerText = inputText
    messageBlock.classList.add('message_field')
    if (isHuman){
        messageBlock.setAttribute("style", 'margin-left: auto;  margin-right: 0;')
    }
    output.appendChild(messageBlock)
}