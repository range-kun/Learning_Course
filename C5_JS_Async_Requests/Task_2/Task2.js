prostoJSON = `
{
 "list": [
  {
   "name": "Petr",
   "age": "20",
   "prof": "mechanic"
  },
  {
   "name": "Vova",
   "age": "60",
   "prof": "pilot"
  }
 ]
}
`;
const data = JSON.parse(prostoJSON);
const students = data.list

const firstStudent = students[0]
const secondStudent = students[1]

obj = {
    list:[
        firstStudent,
        secondStudent
    ]
}

console.log(obj)