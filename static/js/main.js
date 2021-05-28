let alert = document.getElementsByClassName("alert");
setTimeout(function () {
    if (alert && alert.length) {
        alert[0].classList.add('d-none');
        alert[1].classList.add('d-none');
    }
}, 3000);

var height = $(window).height();
$(document).ready(function () {
    'use strict';
    // Detect browser for css purpose
    if (navigator.userAgent.toLowerCase().indexOf('firefox') > -1) {
        $('.form form label').addClass('fontSwitch');
    }

    // Form validation
    $('input').blur(function () {
        // label effect
        if ($(this).val().length > 0) {
            $(this).siblings('label').addClass('active');
        } else {
            $(this).siblings('label').removeClass('active');
        }
    });
    // form switch
    $('a.switch').click(function (e) {
        $(this).toggleClass('active');
        e.preventDefault();

        if ($('a.switch').hasClass('active')) {
            $(this).parents('.form-peice').addClass('switched').siblings('.form-peice').removeClass('switched');
        } else {
            $(this).parents('.form-peice').removeClass('switched').siblings('.form-peice').addClass('switched');
        }
    });


// Auto close alerts
    let alert = document.getElementsByClassName("alert");
    setTimeout(function () {
        if (alert && alert.length) {
            alert[0].classList.add('d-none');
        }
    }, 4000);

    $('.brand-slider').owlCarousel({
        loop: true,
        dots: false,
        margin: 20,
        autoplay: true,
        // autoplayHoverPause: true,
        responsive: {
            0: {
                items: 3
            },
            600: {
                items: 4
            },
            1000: {
                items: 5
            }
        }
    })

    const prevIcon = '<i class="fa fa-angle-left fs-3 text-dark" aria-hidden="true"></i>'
    const nextIcon = '<i class="fa fa-angle-right fs-3 text-dark" aria-hidden="true"></i>'
    $('.category-slider').owlCarousel({
        nav: true,
        dots: false,
        navText: [prevIcon, nextIcon],
        responsive: {
            0: {
                items: 2
            },
            600: {
                items: 3
            },
            1000: {
                items: 4
            }
        }
    });
});
