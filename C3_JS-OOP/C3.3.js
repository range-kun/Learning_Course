let car = {
    model: 'ford',
    country: 'usa'
}

let myCar = Object.create(car)
myCar.colour = 'white'
myCar['power'] = '100'

// Задание 1

function checkObject(obj){
    for (let prop in obj){
        if (obj.hasOwnProperty(prop)){
            console.log(prop, obj[prop]);
        }
    }
}
console.log('+++Задание 1+++')
checkObject(myCar)

// Задание 2

function checkProperty(obj, string){
    console.log(string in obj)
}
console.log('+++Задание 2+++')
checkProperty(myCar, 'colour')
checkProperty(myCar, 'wheels')

// Задание 3

function createObj(){
    return Object.create(null)
}
createObj()