let object = {
    firstName: "John",
    lastName: "Doe",
    age: 30,
    fullName: function(){
        return this.firstName + " " + this.lastName;
    },
    sayHi: function(){
        console.log("Hi, my name is " + this.fullName());
    }
}

object.sayHi();