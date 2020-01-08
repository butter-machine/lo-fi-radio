$(document).ready(function() {
    const sidebar = $(".sidebar");
    const cont= $(".content");
    const button = $(".bt-sidebar");
    hiden = true;
    
    button.click(function() {
        if (hiden) {
            sidebar.css({"width": "300px"});
            button.css({"margin-left": "252px"})
            button.text("X");
            cont.css({"margin-left": "300px"})
            sidebar.css({"opacity": "0.75"})
            hiden = false;
        }
        else {
            sidebar.css({"width": "0"});
            button.css({"margin-left": "0"})
            button.text("Play list");
            cont.css({"margin-left": "0"})
            sidebar.css({"opacity": "0"})
            hiden = true;
        }
    });
});