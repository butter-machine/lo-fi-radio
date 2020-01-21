function playlist_update() {
    $.ajax({
        url: "playlist_update",
        cache: false,
        success: function(data) {
            $("#playlist").html(data);
        }
    });
}

$(document).ready(function() {
    playlist_update();
    setInterval('playlist_update()', 2000);
});