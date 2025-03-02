$(document).ready(function(){
    
    $(".text").textillate({
        in: { effect: "fadeIn", delay: 50 },
        out: { effect: "fadeOut", delay: 50 },
        loop: true,
        sync: true,
        in:{
            effect: "bounceIn"
        },
        out:{
            effect: "bounceout"
        }
    })
})