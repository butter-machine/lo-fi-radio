function sign_update() {
    $.ajax({
        url: "sign_update",
        cache: false,
        success: function(data) {
            $("#sign").html(data);
        }
    });
}

$(document).ready(function() {
    sign_update();
    setInterval('sign_update()', 3000);
});