//retrieve node in DOM via ID 
var c = document.getElementById("slate");

//instantiate a CanvasRenderingContext2D object
var ctx = c.getContext("2d");

//init global state var 
var mode = "rect";

//var toggleMode = function(e) { 
var toggleMode = (e) => {
    console.log("toggling...");
    if (mode == "rect") {
        mode = "circ";
    }
    else {
        mode = "rect";
    }
}

var drawRect = function(e) { 
    var mouseX = event.clientX;
    var mouseY = event.clientY;
    console.log("mouseclick registered at ", mouseX, mouseY);
    ctx.fillRect(mouseX-8, mouseY-128, 50, 100);
}

//var drawCircle= function(e) { 
var drawCircle = (e) => {
    var mouseX = event.clientX;
    var mouseY = event.clientY;
    console.log("mouseclick registered at ", mouseX, mouseY);
    ctx.beginPath();
    ctx.arc(mouseX-8, mouseY-128, 50, 0, 360);
    ctx.fill();
}

//var draw = function(e) {
var draw = (e) => {
    if (mode == "rect") {
        drawRect();
    }
    else {
        drawCircle();
    }
}

//var wipeCanvas = function() { 
var wipeCanvas = (e) => {
    ctx.clearRect(0, 0, c.width, c.height)
}

c.addEventListener("click", draw); 
var bToggler = document.getElementById("buttonToggle");
bToggler.addEventListener("click", toggleMode); 
var clearB = document.getElementById("buttonClear"); 
clearB.addEventListener("click", wipeCanvas); 