/*

Tinkering around with a fixed nav bar, and changing it based on scroll


*/

$(document).ready(function(){
  $(window).scroll(function(){
    var scrollTop = $(window).scrollTop();
    if (scrollTop > 49) {
        $('body').addClass('header-fixed');
    } else {
        $('body').removeClass('header-fixed');
    }
    // change the style of the navbar when the user scrolls into the next zone.
    // get the distance of the 2nd section from the top of the page - height of header.
    if (scrollTop > 1) {
        $('#topnav').addClass('alt-header');
    } else {
        $('#topnav').removeClass('alt-header');
    }
  });
});
