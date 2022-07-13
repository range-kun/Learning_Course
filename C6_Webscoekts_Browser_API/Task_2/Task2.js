const btn = document.querySelector('.btn')

btn.addEventListener('click', ()=>{
    alert(`Ширина вашего экрана ${window.screen.width}px\nВысота ващего экрана ${window.screen.height}px`)
})