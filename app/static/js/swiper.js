new Swiper('.card-wrapper', {
  loop: true,
  spaceBetween: 20,
  slidesPerView: 3, 

  pagination: {
    el: '.swiper-pagination',
  },

  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },

  breakpoints: {
    0: {
      slidesPerView: 1
    },
    768: {
      slidesPerView: 2
    },
    1024: {
      slidesPerView: 3
    }
  }
});
// new Swiper('.swiper', {
//   loop: true,
//   spaceBetween: 20, // adjust as needed
//   slidesPerView: 3,
//   pagination: {
//     el: '.swiper-pagination',
//   },
//   navigation: {
//     nextEl: '.swiper-button-next',
//     prevEl: '.swiper-button-prev',
//   },
//   breakpoints: {
//     0: { slidesPerView: 1 },
//     768: { slidesPerView: 2 },
//     1024: { slidesPerView: 3 }
//   }
// });
