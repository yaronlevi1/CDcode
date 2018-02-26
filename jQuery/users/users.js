$(document).ready(function(){  
    $('input').click(function(){
        $(this).val('')
    })     
    $('#submit').click(function(){
        var FN = document.getElementById('first_name').value
        var LN = document.getElementById('last_name').value
        var EM = document.getElementById('email').value
        var NO = document.getElementById('contactno').value
        $('table').append("<tr><td>"+FN+"</td><td>"+LN+"</td><td>"+EM+"</td><td>"+NO+"</td></tr>")
        return false;
    })
})








