

function time (HOUR , MINUTE, PERIOD) {


if (MINUTE>30) {
var open = "It's almost ";
var ref_hour = HOUR+1;
}
else {
var opem = "It's just after ";
var ref_hour = HOUR;
}

if (ref_hour==13 ) {
    ref_hour==1
}

if (ref_hour==12 && MINUTE>30 && PERIOD==AM ) ||  (ref_hour==12 && MINUTE>30 && PERIOD==AM ) {

console.log(open, "noon" )
}




time (1, 23, AM)

