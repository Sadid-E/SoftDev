// Team Phantom Tollbooth :: Clyde Sinclair, Fierce Dragon 
// SoftDev pd0
// K27 -- Basic functions in JavaScript
// 2022-02-03r
// --------------------------------------------------


// as a duo...
// pair programming style,
// implement a fact and fib fxn


//Do whatever you think is needed. Think: S I M P L E.   Think: S M A R T.

var fib = function(x) {
    if (x <= 1) {
        return x; 
    }
    return fib(x-1) + fib(x-2);
}

var fac = function(x) {
    if (x == 0) {
        return 1;
    }
    return x * fac(x-1);
}