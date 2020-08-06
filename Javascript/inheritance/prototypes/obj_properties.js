let f = function () {
  this.a = 1;
  this.b = 2;
};

let o = new f();

f.prototype.b = 3;
f.prototype.c = 4;

console.log(o.a);
console.log(o.b);
console.log(o.c);
console.log(o);

var o = {
  a: 2,
  m: function () {
    return this.a + 1;
  },
};

console.log(o.m());
