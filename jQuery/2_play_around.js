$(document).ready(function() {

    $('button#hide').click(function(){
        $('p#hide').hide();
     })
     $('button#show').click(function(){
        $('p#show').show();
     })
     $('button#toggle').click(function(){
        $('p#toggle').toggle();
     })
     $('button#slideUp').click(function(){
        $('p#slideUp').slideUp();
     })
     $('button#slideDown').click(function(){
        $('p#slideDown').slideDown();
     })
     $('button#slideToggle').click(function(){
        $('p#slideToggle').slideToggle();
     })

     $('button#fadeOut').click(function(){
        $('p#fadeOut').fadeOut();
     })
     $('button#fadeIn').click(function(){
        $('p#fadeIn').fadeIn();
     })


     $('button#addClass').click(function(){
        $('p#addClass').addClass("green");
     })
     $('button#removeClass').click(function(){
        $('p#removeClass').removeClass("yellow");
     })

     $('button#css').click(function(){
        $('p#css').css("font-weight","bolder");
     })

     


     



})


