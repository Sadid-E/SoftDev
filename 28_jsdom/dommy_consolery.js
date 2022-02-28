

// Team Twizzy: Sadid Ethun, Theo Fahey
// SoftDev pd0
// K28 -- Getting more comfortable with the dev console and the DOM
// 2022-02-08
// --------------------------------------------------


//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)
console.log("AYO");

var i = "hello";
var j = 20;


//assign an anonymous fxn to a var
var f = function(x) {
  var j=30;
  return j+x;
};


//instantiate an object
var o = { 'name' : 'Thluffy',
          age : 15,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) {
            return x+30;
          }
        };


var addItem = function(text) {
  var list = document.getElementById("thelist");
  var newitem = document.createElement("li");
  newitem.innerHTML = text;
  list.appendChild(newitem);
};

//
var removeItem = function(n) {
  var listitems = document.getElementsByTagName('li');
  listitems[n].remove();
};


var red = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    items[i].classList.add('red');
  }
};


var stripe = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    if (i%2==0){
      items[i].classList.add('red');
    } else {
      items[i].classList.add('blue');
    }
  }
};

let fib = function(x) {
    if (x <= 1) {
        return x;
    }
    return fib(x-1) + fib(x-2);
}

let fac = function(x) {
    if (x == 0) {
        return 1;
    }
    return x * fac(x-1);
}
let gcd = function(x,y){
  if (x>=y){
    a = x;
    b = y;
  }
  else{
    a = y;
    b = x;
  }
  if (a === 0){
    return b;
  }
  if (b === 0){
    return a
  }
  return (gcd(b,a%b));
}