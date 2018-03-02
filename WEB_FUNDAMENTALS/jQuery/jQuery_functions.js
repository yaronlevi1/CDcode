
$(document).ready(function(){
    $('#click button').click(function(){
        alert('you clicked!')
     })
     $('#hide').click(function(){
        $('#hideshow h4').hide()
     })
     $('#show').click(function(){
        $('#hideshow h4').show()
     })
     $('#toggle button').click(function(){
        $('#toggle h4').toggle()
     })
     $('#slideDown').click(function(){
        $('#slideDownUp h4').slideDown()
     })
     $('#slideUp').click(function(){
        $('#slideDownUp h4').slideUp()
     })
     $('#slideToggle button').click(function(){
        $('#slideToggle h4').slideToggle()
     })
     $('#fadeIn').click(function(){
        $('#fadeInOut h4').fadeIn()
     })   
     $('#fadeOut').click(function(){
        $('#fadeInOut h4').fadeOut()
     })
     $('#addClass button').click(function(){
        $('#addClass h4').addClass("red");
     })
     $('#before').click(function(){
        $('#beforeafter h4').before("XXX ");
     })
     $('#after').click(function(){
        $('#beforeafter h4').after("XXX ");
     })    
     $('#append button').click(function(){
        $('#append h4').append("XXX ");
     })
     $('#html button').click(function(){
        $('#html h4').html(" <b> REVISED CONTENT</b> ");
     })
     $('#attr button').click(function(){
        $('#attr h4').attr("id", "green");
     })
     $('#val button').click(function(){
        $('#val input').val("REVISED VALUE");
     })
     $('#text button').click(function(){
        $('#text h4').text("REVISED TEXT");
     })
     $("#data").data( "check", { var1: 16, var2: "pizza!" } );
     $('#data button').click(function(){
         $('#data span:first').text($("#data").data("check" ).var1);
         $('#data span:last').text($("#data").data("check" ).var2);
     })

})








