

function time (HOUR , MINUTE, PERIOD) {
if (MINUTE>30) {
var open = "It's almost ";
var ref_hour = HOUR+1;
}
else {
var open = "It's just after ";
var ref_hour = HOUR;
}
if (ref_hour==13) {
    ref_hour==1;
}
if ( (HOUR===11 && MINUTE>30 && PERIOD==="AM") ||  (HOUR===12 && MINUTE<=30 && PERIOD==="PM")  ) {
    console.log(open, "noon" );
}
else if ( (HOUR===11 && MINUTE>30 && PERIOD==="PM") ||  (HOUR===12 && MINUTE<=30 && PERIOD==="AM")  ) {
    console.log(open, "midnight" );
}
else if ( (ref_hour>=10 && ref_hour<=11 && PERIOD=="PM") || (ref_hour>=1 && ref_hour<=3 && PERIOD=="AM")    ) {
    console.log(open, ref_hour, "at night" );
}
else if ( (ref_hour>=4 && ref_hour<=11 && PERIOD=="AM")   ) {
    console.log(open, ref_hour, "in the morning" );
}
else if ( (ref_hour>=1 && ref_hour<=5 && PERIOD=="PM")   ) {
    console.log(open, ref_hour, "afternoon" );
}
else if ( (ref_hour>=6 && ref_hour<=9 && PERIOD=="PM")   ) {
    console.log(open, ref_hour, "in the evening" );
}
else {
    console.log('  Please enter hour (1 to 12) , minute (0-59), period ("AM" or "PM") ');
}
}


time(10, 45, "ASS");
