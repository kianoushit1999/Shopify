AOS.init();
var swiper = new Swiper('.swiper-one', {
    slidesPerView: 1,
    spaceBetween: 10,
    // init: false,
    autoplay: true,
    pagination: {
        el: '.swiper-pagination',
        clickable: true,
    },
    breakpoints: {
        '@0.00': {
            slidesPerView: 1,
            spaceBetween: 10,
        },
        '@0.75': {
            slidesPerView: 2,
            spaceBetween: 20,
        },
        '@1.00': {
            slidesPerView: 3,
            spaceBetween: 40,
        },
        '@1.50': {
            slidesPerView: 4,
            spaceBetween: 50,
        },
    }
});

var swiper = new Swiper('.swiper-two', {
    slidesPerView: 1,
    spaceBetween: 30,
    slidesPerGroup: 3,
    loop: true,
    loopFillGroupWithBlank: true,
    pagination: {
        el: '.swiper-pagination',
        clickable: true,
    },
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
    breakpoints: {
        '@0.00': {
            slidesPerView: 2,
            spaceBetween: 10,
        },
        '@0.75': {
            slidesPerView: 2,
            spaceBetween: 20,
        },
        '@1.00': {
            slidesPerView: 3,
            spaceBetween: 40,
        },
        '@1.50': {
            slidesPerView: 3,
            spaceBetween: 50,
        },
    }
});

var swiper = new Swiper('.swiper-three', {
    slidesPerView: 4,
    spaceBetween: 30,
    slidesPerGroup: 4,
    loop: true,
    loopFillGroupWithBlank: true,
    pagination: {
        el: '.swiper-pagination',
        clickable: true,
    },
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
    breakpoints: {
        '@0.00': {
            slidesPerView: 2,
            spaceBetween: 10,
        },
        '@0.75': {
            slidesPerView: 2,
            spaceBetween: 20,
        },
        '@1.00': {
            slidesPerView: 3,
            spaceBetween: 40,
        },
        '@1.50': {
            slidesPerView: 4,
            spaceBetween: 50,
        },
    }
});