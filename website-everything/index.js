var getUrl = "http://ec2-54-242-86-211.compute-1.amazonaws.com:3000/?get/";
var insertUrl = "http://ec2-54-242-86-211.compute-1.amazonaws.com:3000/?insert/";

var getUrl = "http://localhost:3000/?get";
var insertUrl = "http://localhost:3000/?insert=";

$(document).ready(function() {
    $.ajaxSetup({
        cache: true
    });
    $.getScript(getUrl);
    //
    // $("#about-button").click(function() {
    //     $('html,body').animate({
    //         scrollTop: $("#about").offset().top},
    //         'slow');
    //     });
    //     $("#portfolio-button").click(function() {
    //     $('html,body').animate({
    //         scrollTop: $("#portfolio").offset().top},
    //         'slow');
    //     });
    //     $("#contact-button").click(function() {
    //     $('html,body').animate({
    //         scrollTop: $("#contact").offset().top},
    //         'slow');
    // });
});

var formSubmit = function(data) {
    console.log('button clicked');
    var userName = document.getElementById("name").value.replace(" ", "%20");
    console.log(insertUrl + userName);
    $.getScript(insertUrl + userName);
}

var callback = function(data) {
    console.log('callback');
    $('#currentlyServing').html("<h1>" + data + "</h1>");
}

var insertStatus = function(data) {
    console.log('insertStatus');
    $('#status').html("<h1>please wait " + data + "</h1>");
}
