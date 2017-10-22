$(document).ready(function () {
    var interval = 500;   //number of mili seconds between each call
    var refresh = function() {
        $.ajax({
            url: ,
            cache: false,
            success: function(html) {
                $('#server-name').html(html);
                setTimeout(function() {
                    alert("Refreshed");
                    //refresh();
                }, interval);
            }
        });
    };
    refresh();
});
