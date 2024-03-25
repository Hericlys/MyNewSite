// mask
$("#phone").mask("(99) 99999-9999");

// Scroll reveal
ScrollReveal({ reset: true });

var title = {
    distance: '150%',
    origin: 'bottom',
    opacity: null,
};


var sub_title= {
    delay: 300,
}

var button_container = {
    delay: 500,
}

var about_info_lef = {
    duration: 2000,
    rotate: {x: 0, y:80, z:15},
    distance: '50%',
    origin: 'left',
}

var about_info_right = {
    duration: 2000,
    rotate: {x: 0, y:80, z:-15},
    distance: '50%',
    origin: 'right',
}

var about_profile = {
    duration: 2000,
    rotate: {x: 0, y:80, z:0},
}

var service_card = {
    duration: 2000,
    rotate: {x: 0, y:80, z:0},
    delay: 300,
    interval: 100,
    reset: true,
}

var section_header = {
    delay: 300,
}

var slideUp = {
    distance: '150%',
    origin: 'bottom',
    opacity: null
};

ScrollReveal().reveal('.title', title);
ScrollReveal().reveal('.sub-title', sub_title);
ScrollReveal().reveal('.button_container', button_container);
ScrollReveal().reveal('.about_info_lef', about_info_lef);
ScrollReveal().reveal('.about_info_right', about_info_right);
ScrollReveal().reveal('.about-profile', about_profile);
ScrollReveal().reveal('.service-card', service_card);
ScrollReveal().reveal('.section-header', section_header);
ScrollReveal().reveal('.slideUp', slideUp);