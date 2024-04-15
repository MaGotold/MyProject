var lastScrollTop = 0;
var scrollCooldown = false;

$(window).scroll(function() {
    if (scrollCooldown) {
        // Exit if we're still within the cooldown period
        return;
    }

    // Prevent new scroll handling until cooldown is over
    scrollCooldown = true;
    setTimeout(function() {
        scrollCooldown = false;
    }, 100); // Cooldown period in milliseconds

    var currentScroll = $(window).scrollTop();

    if (currentScroll > lastScrollTop) {
        // Scrolling down
        $('#main-navigation').addClass('hidden');
    } else {
        // Scrolling up
        $('#main-navigation').removeClass('hidden');
    }
    lastScrollTop = currentScroll;
});