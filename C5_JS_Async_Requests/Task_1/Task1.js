prostoStroka = `
<list>
    <student>
        <name lang="en">
            <first>Ivan</first>
            <second>Ivanov</second>
        </name>
        <age>35</age>
        <prof>teacher</prof>
    </student>
    <student>
        <name lang="ru">
            <first>Петр</first>
            <second>Петров</second>
        </name>
        <age>58</age>
        <prof>driver</prof>
    </student>
</list>`
const parser = new DOMParser();
XMLDom = parser.parseFromString(prostoStroka, 'text/xml')

listNode = XMLDom.querySelector('list')

firstStudent = listNode.querySelector('student')
studentFirstName = firstStudent.querySelector('first')
studentSecondName = firstStudent.querySelector('second')
studentAge = Number(firstStudent.querySelector('age').textContent)
studentProf = firstStudent.querySelector('prof').textContent
studentLang = firstStudent.querySelector('name').getAttribute('lang')

secondStudent = listNode.querySelectorAll('student')[1]
secondStudentFirstName = secondStudent.querySelector('first')
secondStudentSecondName = secondStudent.querySelector('second')
secondStudentAge = Number(secondStudent.querySelector('age').textContent)
secondStudentProf = secondStudent.querySelector('prof').textContent
secondStudentLang = secondStudent.querySelector('name').getAttribute('lang')

obj = {
    list:[
        {name: `${studentFirstName.textContent} ${studentSecondName.textContent}`, age: studentAge,
            prof: studentProf, lang: studentLang},
        {name: `${secondStudentFirstName.textContent} ${secondStudentSecondName.textContent}`,
            age: secondStudentAge, prof: secondStudentProf, lang: secondStudentLang}
    ]
}
console.log(obj)