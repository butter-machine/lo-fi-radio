function update() {
    $.ajax({
        url: "sign_update",
        cache: false,
        success: function(data) {
            $("#sign").html(data);
        }
    });
}

$(document).ready(function() {
    update();
    setInterval('update()', 2000);
});