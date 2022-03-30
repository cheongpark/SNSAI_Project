var index = 1;

$(document).ready(function() {
    var interval = setInterval(slide, 5000);
    $('.slide').hover(
        function() { clearInterval(interval); },
        function() { interval = setInterval(slide, 5000); }
    );
});

function slide () {
    if (index < 4) {
        $('.slideul').animate(
        {
            left: '-=' + 1300
        }, 'slow');
        index++;
    }
    else {
        $('.slideul').animate(
        {
            left: 0
        }, 'slow');
        index = 1;
    }
};