// Задание 5.
class ElectricDevice{
    constructor(device){
        this.device = device;
        this.isWorking = false;
    }
    turnOn() {
        if (!this.isWorking){
            this.isWorking = true;
            console.log('Прибор работает');
        } else {
            this.isWorking = false;
            console.log('Прибор выключен');
        }
    }
}


class Vacuum extends ElectricDevice{
    constructor(device, brand, volume){
        super(device);
        this.brand = brand;
        this.volume = volume;
    }
    makeNoise(){
        console.log(`Пылесосы фирмы ${this.brand} делают самое громкое ВЖУУУУУУ`)
    }
}


class Fridge extends ElectricDevice{
    constructor(device, brand, power, maxTemperature, minTemperature){
        super(device);
        this.brand = brand;
        this.maxTemperature = maxTemperature;
        this.minTemperature = minTemperature;
        this.power = power;
    }
    changeTemp(temperature){
        if (this.minTemperature < temperature && temperature < this.maxTemperature){
            console.log(`Установлека температура ${temperature} градусов`)
        }
        else{
            console.log('Указанная темпераутра указана вне доступного диапазона')
        }
    }
}


const samsungFridge = new Fridge('fridge', 'samsung', '1200 Вт', 7, -20)
samsungFridge.changeTemp(20)
samsungFridge.turnOn()

const tefalXC = new Vacuum('vacuum', 'Tefal', '0,3 литра')
console.log(tefalXC.device)
tefalXC.makeNoise()