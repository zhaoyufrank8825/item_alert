// $(document).ready(function(){
//     $('.footer').fadeOut(2000).delay(2000).fadeIn(2000).delay(2000).fadeOut(2000).delay(2000).fadeIn(2000)
// });

$(function(){
    // $('.footer').fadeOut(3000).fadeIn(3000).fadeOut(3000).fadeIn(3000).fadeOut(3000).fadeIn(3000)

    $('.footer').click(function(){
        alert("You clicked the footer.")
    })

    $('.jumbotron').hover(function(){
        $(this).css("border","3px solid black")
    },
    function(){
        $(this).css("border","0px solid black")
    })

    // $('.jumbotron').on("click", function(){
    //     alert("You clicked the Jumbotron")
    // })

});