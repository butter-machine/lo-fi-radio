$(document).ready(function() {
    const sidebar = $(".sidebar");
    const cont= $(".content");
    const button = $(".bt-sidebar");
    const history_cell = $(".history-cell");
    hiden = true;
    
    button.click(function() {
        var sidebar_width = "";
        var button_margin_left = "";
        var content_min_opacity = "1";
        
        if ($(window).width() < 650) {
            sidebar_width = $(window).width().toString();
            button_margin_left = sidebar_width - button.width() - 10;
            content_min_opacity = "0";
        }
        else {
            sidebar_width = "300px";
            button_margin_left = "252px";
        }
        
        if (hiden) {
            sidebar.css({"width": sidebar_width});
            button.css({"margin-left": button_margin_left});
            button.text("X");
            cont.css({"margin-left": sidebar_width});
            cont.css({"opacity": content_min_opacity});
            sidebar.css({"opacity": "0.75"});
            history_cell.css({"opacity": "1"});
            history_cell.css({"transition": "1s"});
            hiden = false;
        }
        else {
            sidebar.css({"width": "0"});
            button.css({"margin-left": "0"});
            button.text("Play list");
            cont.css({"margin-left": "0"});
            cont.css({"opacity": "1"});
            sidebar.css({"opacity": "0"});
            history_cell.css({"opacity": "0"});
            history_cell.css({"transition": "0.1s"});
            hiden = true;
        }
    });
});