$(document).ready(function() {
    const sidebar = $(".sidebar");
    const cont= $(".content");
    const button = $(".bt_sidebar");
    hiden = false;
    
    button.click(function() {
        if (hiden) {
            sidebar.css({"width": "200px"});
            cont.css({"margin-left": "200px"})
            hiden = false;
        }
        else {
            sidebar.css({"width": "0"});
            cont.css({"margin-left": "0"})
            hiden = true;
        }
    });
});