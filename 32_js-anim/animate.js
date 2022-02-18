// Team Phantom Tollbooth :: Clyde Sinclair, Fierce Dragon
// SoftDev pd0
// K31 -- canvas based JS animation
// 2022-02-15t

// model for HTML5 canvas-based animation

// SKEELTON


//access canvas and buttons via DOM
var c = document.getElementById("playground");
var dotButton = document.getElementById("buttonCircle");
var stopButton = document.getElementById("buttonStop");
var logoButton = document.getElementById("buttonLogo");

//prepare to interact with canvas in 2D
var ctx = c.getContext("2d");

//set fill color to team color
ctx.fillStyle = "purple";

var requestID;  //init global var for use with animation frames

//var clear = function(e) {
var clear = (e) => {
  console.log("clear invoked...")

  // YOUR CODE HERE
  ctx.clearRect(0, 0, c.width, c.height);
}


var radius = 0;
var growing = true;

//var drawDot = function() {
var drawDot = () => {
    console.log("drawDot invoked...");
    clear();
  // YOUR CODE HERE

    if (growing){


      if (radius > c.width/2-1) {
        growing = false;
      }
      radius++;
    }
    else {
      if (radius <= 1){
        growing = true;
      }
      radius--;
    }
    ctx.beginPath();
    ctx.arc(c.width/2, c.height/2, radius, 0, 360);
    ctx.fill();



      //window.cancelAnimationFrame(requestID);

        requestID = window.requestAnimationFrame(drawDot);


  /*
    ...to
    Wipe the canvas,
    Repaint the circle,
    ...and somewhere (where/when is the right time?)
    Update requestID to propagate the animation.
    You will need
    window.cancelAnimationFrame()
    window.requestAnimationFrame()
   */
}

var xGrowing = true;
var yGrowing = true;
var imgX = Math.random() * (c.width/2 +100);
var imgY = Math.random() * (c.height/2 +100);
var logo = document.getElementById("dvd");

var drawLogo = () => {
    clear();
    if (imgX >= c.width-75 || imgX <= 0) {
        xGrowing = !xGrowing;
    }
    if (imgY >= c.height-50 || imgY <= 0) {
        yGrowing = !yGrowing;
    }
    if (xGrowing) {
        imgX++;
    }
    else {
        imgX--;
    }
    if (yGrowing) {
        imgY++;
    } 
    else {
        imgY--;
    }
    ctx.drawImage(logo, imgX, imgY, 75, 50);
    requestID = window.requestAnimationFrame(drawLogo);
}

//var stopIt = function() {
var stopIt = () => {
  console.log("stopIt invoked...");
  //console.log( requestID );

  // YOUR CODE HERE
  /*
    ...to
    Stop the animation
    You will need
    window.cancelAnimationFrame()
  */
  window.cancelAnimationFrame(requestID);
}


dotButton.addEventListener( "click", drawDot );
stopButton.addEventListener( "click",  stopIt );
logoButton.addEventListener( "click",  drawLogo );
