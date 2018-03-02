
//********* AMOUNT ACCUMULATED AFTER X TIME
function amount_given_time (LAST_DAY) {
    var total=0
    for (var day = 1; day <= LAST_DAY; day++) {
        if (day===1) {
            var daily_amount = 0.01    
        } 
        else {
            daily_amount *=2
        }
        total +=daily_amount;
    }
console.log("after "+ LAST_DAY + " days, the servant recived total of "+ total.toFixed(2)+ " dollars");    
}
amount_given_time (40)

//********* TIME REQUIRED TO ACCUMULATE X 
function time_given_amount (AMOUNT_DESIRED) { 
    var total=0.01
    var day=1
    var daily_amount=0.01
    while (total<AMOUNT_DESIRED) {
        daily_amount *=2;
        total +=daily_amount;
        day++
    }
    console.log("at the end of day "+ day + ", the servfant will surpass the total of " + AMOUNT_DESIRED + " dollars");   
}
time_given_amount (10000);
time_given_amount (1000000000);
time_given_amount (Infinity);
