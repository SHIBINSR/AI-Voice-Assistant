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

    // siri wave
    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 800,
        height: 200,
        style: "ios9",
        amlitude: "1",
        speed:"0.30"
      });

    //   siri message animation
    $(".siri-message").textillate({
        in: { effect: "fadeIn", delay: 50 },
        out: { effect: "fadeOut", delay: 50 },
        loop: true,
        sync: true,
        in:{
            effect: "fadeInUp",
            sync : true
        },
        out:{
            effect: "fadeOutUp",
            sync : true
        }
    })

    // mic button click event
    $("#MicBtn").click(function(){
        eel.playAssistantSound()
        $("#Oval").attr("hidden",true)
        $("#SiriWave").attr("hidden",false)
        eel.allCommands()()
    })

    // shortkey
    function doc_keyUp(e) {
        // this would test for whichever key is 40 (down arrow) and the ctrl key at the same time

        if (e.key === 'j' && e.metaKey) {
            eel.playAssistantSound()
            $("#Oval").attr("hidden", true);
            $("#SiriWave").attr("hidden", false);
            eel.allCommands()()
        }
    }
    document.addEventListener('keyup', doc_keyUp, false);
})