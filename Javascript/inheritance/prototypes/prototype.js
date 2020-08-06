// Declaring a new instance of an object.
var o = new Foo();
// How JavaScript declares a new object under the hood.
var o = new Object();
o.[[Prototype]] = Foo.prototype;
Foo.call(o);