$(document).ready(function() {
    const play = $("#play");
    const volume = $("#volume");
    const audio = $("#audio")[0];

    play.click(function() {
        if (audio.paused) {
            audio.load();
            audio.play();
            play.text("pause");
        } else {
            audio.pause();
            play.text("play");
        }
    });

    volume.on('input', function() {
        audio.volume = volume.val() / 100;
        if (volume.val() == 1) {
            audio.muted = true;
        } else {
            audio.muted = false;
        }
    });

});

function buffering() {
    $("#play").text("connecting with space...");
}

function canPlay() {
    if ($("#audio").prop("paused")) {
        $("#play").text("play");
    } else {
        $("#play").text("pause");
    }
}