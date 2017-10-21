var getUrl = "http://ec2-54-242-86-211.compute-1.amazonaws.com:3000/?get/";
var insertUrl = "http://ec2-54-242-86-211.compute-1.amazonaws.com:3000/?insert/";

$(document).ready(function() {
    $.getScript(getUrl);

    $("#about-button").click(function() {
        $('html,body').animate({
            scrollTop: $("#about").offset().top},
            'slow');
        });
        $("#portfolio-button").click(function() {
        $('html,body').animate({
            scrollTop: $("#portfolio").offset().top},
            'slow');
        });
        $("#contact-button").click(function() {
        $('html,body').animate({
            scrollTop: $("#contact").offset().top},
            'slow');
    });
});

var formSubmit = function() {
    var userName = document.getElementById("name").value.replace(" ", "%20");
    $.getScript(insertUrl + userName);
}

var callback = function(data) {
    $('#currentlyServing').html("<h1>" + data + "</h1>");
}

var insertStatus(data) {
    $('#status').html(data);
}
