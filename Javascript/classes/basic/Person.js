class Person {
  constructor(name) {
    this.name = name;
  }

  sayHello() {
      console.log('Hello ' + this.name)
  }
}

let Person1 = new Person('Austin')
Person1.sayHello()