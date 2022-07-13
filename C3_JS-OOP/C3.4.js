// Задание 4.
function ElectricDevice(device){
    this.device = device
    this.isWorking = false
}
ElectricDevice.prototype.turnOn = function(){
    if (!this.isWorking){
        this.isWorking = true
        console.log('Прибор работает')
    }
    else{
        this.isWorking = false
        console.log('Прибор выключен')
    }
}

function Vacuum (device, brand, volume ){
    this.deviсe = device
    this.brand = brand
    this.volume = volume
    this.makeNoise = function(){
        console.log(`Пылесосы фирмы ${this.brand} делают самое громкое ВЖУУУУУУ`)
    }
}

Vacuum.prototype = new ElectricDevice()

function Fridge(device, brand, power, maxTemperature, minTemperature){
    this.deviсe = device
    this.brand = brand
    this.maxTemperature = maxTemperature
    this.minTemperature = minTemperature
    this.power = power
    this.changeTemp = function (temperature){
        if (this.minTemperature < temperature && temperature < this.maxTemperature){
            console.log(`Установлека температура ${temperature} градусов`)
        }
        else{
            console.log('Указанная темпераутра указана вне доступного диапазона')
        }
    }
}

Fridge.prototype = new ElectricDevice()

const samsungFridge = new Fridge('fridge', 'samsung', '1200 Вт', 7, -20)
samsungFridge.changeTemp(20)
samsungFridge.turnOn()

const tefalXC = new Vacuum('vacuum', 'Tefal', '0,3 литра')
console.log(tefalXC.deviсe)
tefalXC.makeNoise()