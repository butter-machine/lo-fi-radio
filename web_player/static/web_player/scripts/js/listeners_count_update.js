function listeners_count_update() {
    $.ajax({
        url: "listeners_count_update",
        cache: false,
        success: function(data) {
            $("#listeners-count").html(data);
        }
    });
}

$(document).ready(function() {
    listeners_count_update();
    setInterval('listeners_count_update()', 10000);
});