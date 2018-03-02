
$(document).ready(function(){

    $('img').click(function() {
        if ($(this).attr('src') == $(this).attr('cat')) {
            $(this).attr('src', $(this).attr('ninja'))    
        } else {
            $(this).attr('src', $(this).attr('cat'))    
        }
      })    
})










