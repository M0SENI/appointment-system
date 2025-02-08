var ClinicMasterCarousel = function() {
    function a() {
        var e;
        0 < jQuery(".blog-vertical-swiper").length && (e = new Swiper(".blog-vertical-swiper-thumb", {
            direction: "vertical",
            slidesPerView: "3",
            mousewheel: !1,
            autoplay: {
                delay: 3e3
            },
            breakpoints: {
                320: {
                    slidesPerView: 1,
                    direction: "horizontal"
                },
                767: {
                    slidesPerView: 2,
                    direction: "vertical"
                },
                1191: {
                    slidesPerView: 3
                }
            }
        }), new Swiper(".blog-vertical-swiper", {
            slidesPerView: "1",
            effect: "fade",
            grabCursor: !0,
            thumbs: {
                swiper: e
            },
            navigation: {
                nextEl: ".blog-swiper-next",
                prevEl: ".blog-swiper-prev"
            }
        }))
    }
    return {
        init: function() {
            function e() {
                var e = $(".testimonial-swiper2 .swiper-slide").length,
                    i = document.querySelector(".testimonial-slider__current"),
                    r = document.querySelector(".testimonial-slider__total"),
                    s = t.realIndex + 1,
                    s = (s = e < s ? 1 : s) < 10 ? "0" + s : s;
                r.innerHTML = e < 10 ? "0" + e : e, i.innerHTML = s
            }
            var t, i, n, l;

            function r() {
                var e = $(".dz-team-swiper1 .swiper-slide").length,
                    i = document.querySelector(".team-slider__current"),
                    r = document.querySelector(".team-slider__total"),
                    s = n.realIndex + 1,
                    s = (s = e < s ? 1 : s) < 10 ? "0" + s : s;
                r.innerHTML = e < 10 ? "0" + e : e, i.innerHTML = s
            }

            function s() {
                var e = $(".compare-swiper .swiper-slide").length,
                    i = document.querySelector(".compare-slider__current"),
                    r = document.querySelector(".compare-slider__total"),
                    s = l.realIndex + 1,
                    s = (s = e < s ? 1 : s) < 10 ? "0" + s : s;
                r.innerHTML = e < 10 ? "0" + e : e, i.innerHTML = s
            }
            0 < jQuery(".testimonial-swiper1").length && new Swiper(".testimonial-swiper1", {
                loop: !0,
                spaceBetween: 20,
                slidesPerView: 1,
                autoplay: {
                    delay: 3e3
                },
                navigation: {
                    nextEl: ".swiper1-button-next",
                    prevEl: ".swiper1-button-prev"
                }
            }), 0 < jQuery(".testimonial-swiper2").length && (t = new Swiper(".testimonial-swiper2", {
                loop: !0,
                spaceBetween: 0,
                slidesPerView: 2,
                autoplay: {
                    delay: 3e3
                },
                pagination: {
                    el: ".testimonial-pagination-swiper2",
                    type: "progressbar"
                },
                breakpoints: {
                    1481: {
                        slidesPerView: 2
                    },
                    1280: {
                        slidesPerView: 1.6
                    },
                    991: {
                        slidesPerView: 1.2
                    },
                    320: {
                        slidesPerView: 1
                    }
                }
            }), 0 < $(".testimonial-slider__pagination2").length) && (e(), t.on("slideChange", function() {
                e()
            })), 0 < jQuery(".testimonial-swiper3").length && new Swiper(".testimonial-swiper3", {
                loop: !0,
                spaceBetween: 0,
                slidesPerView: 1,
                autoplay: {
                    delay: 3e3
                },
                pagination: {
                    el: ".testimonial-pagination-swiper3",
                    clickable: !0
                }
            }), 0 < jQuery(".testimonial-swiper4").length && (i = new Swiper(".testimonial-thumb-swiper4", {
                slidesPerView: "1",
                effect: "fade",
                centeredSlides: !0
            }), new Swiper(".testimonial-swiper4", {
                loop: !0,
                spaceBetween: 20,
                slidesPerView: 1,
                centeredSlides: !0,
                autoplay: {
                    delay: 3e3
                },
                thumbs: {
                    swiper: i
                },
                navigation: {
                    nextEl: ".swiper4-button-next",
                    prevEl: ".swiper4-button-prev"
                }
            })), 0 < jQuery(".testimonial-swiper5").length && new Swiper(".testimonial-swiper5", {
                loop: !0,
                spaceBetween: 20,
                slidesPerView: 3,
                autoplay: {
                    delay: 3e3
                },
                pagination: {
                    el: ".testimonial-pagination-swiper2",
                    type: "progressbar"
                },
                breakpoints: {
                    1481: {
                        slidesPerView: 3
                    },
                    1280: {
                        slidesPerView: 1.6
                    },
                    991: {
                        slidesPerView: 1.2
                    },
                    320: {
                        slidesPerView: 1
                    }
                }
            }), 0 < jQuery(".awards-swiper").length && new Swiper(".awards-swiper", {
                loop: !0,
                slidesPerView: 5,
                autoplay: {
                    delay: 3e3
                },
                breakpoints: {
                    1200: {
                        slidesPerView: 5
                    },
                    991: {
                        slidesPerView: 4
                    },
                    767: {
                        slidesPerView: 3
                    },
                    575: {
                        slidesPerView: 2.5
                    },
                    320: {
                        slidesPerView: 1.5
                    }
                }
            }), 0 < jQuery(".dz-team-swiper1").length && (i = new Swiper(".dz-team-swiper1-thumb", {
                slidesPerView: "2",
                grid: {
                    rows: 2
                },
                autoplay: {
                    delay: 3e3
                },
                breakpoints: {
                    320: {
                        slidesPerView: 1.2,
                        grid: {
                            rows: 1
                        }
                    },
                    591: {
                        slidesPerView: 2
                    },
                    991: {
                        slidesPerView: 3
                    },
                    1200: {
                        slidesPerView: 2
                    }
                }
            }), n = new Swiper(".dz-team-swiper1", {
                slidesPerView: "1",
                effect: "fade",
                thumbs: {
                    swiper: i
                },
                pagination: {
                    el: ".team-progressbar-swiper",
                    type: "progressbar"
                },
                navigation: {
                    nextEl: ".team-swiper-next",
                    prevEl: ".team-swiper-prev"
                }
            }), 0 < $(".team-pagination-swiper").length) && (r(), n.on("slideChange", function() {
                r()
            })), 0 < jQuery(".client-swiper").length && new Swiper(".client-swiper", {
                loop: !0,
                slidesPerView: 5,
                spaceBetween: 30,
                autoplay: {
                    delay: 3e3
                },
                breakpoints: {
                    1200: {
                        slidesPerView: 6
                    },
                    991: {
                        slidesPerView: 4
                    },
                    575: {
                        slidesPerView: 3
                    },
                    320: {
                        slidesPerView: 2
                    }
                }
            }), 0 < jQuery(".client-swiper2").length && new Swiper(".client-swiper2", {
                loop: !0,
                slidesPerView: 4,
                spaceBetween: 30,
                autoplay: {
                    delay: 3e3
                },
                breakpoints: {
                    767: {
                        slidesPerView: 4
                    },
                    575: {
                        slidesPerView: 3
                    },
                    320: {
                        slidesPerView: 2
                    }
                }
            }), a(), 0 < jQuery(".dz-flex-swiper").length && new Swiper(".dz-flex-swiper", {
                speed: 500,
                loop: !1,
                slidesPerView: "auto",
                spaceBetween: 0,
                autoplay: {
                    delay: 3e3
                },
                breakpoints: {
                    991: {
                        slidesPerView: "auto"
                    },
                    320: {
                        slidesPerView: 1
                    }
                }
            }), 0 < jQuery(".compare-swiper").length && (l = new Swiper(".compare-swiper", {
                loop: !0,
                slidesPerView: 4,
                spaceBetween: 20,
                centeredSlides: !0,
                autoplay: {
                    delay: 3e3
                },
                navigation: {
                    nextEl: ".compare-swiper-next",
                    prevEl: ".compare-swiper-prev"
                },
                pagination: {
                    el: ".compare-pagination-swiper",
                    type: "progressbar"
                },
                breakpoints: {
                    1481: {
                        slidesPerView: 4.4
                    },
                    1280: {
                        slidesPerView: 4
                    },
                    991: {
                        slidesPerView: 3.5
                    },
                    320: {
                        slidesPerView: 2
                    }
                }
            }), 0 < $(".compare-slider__pagination").length) && (s(), l.on("slideChange", function() {
                s()
            }))
        },
        load: function() {},
        resize: function() {
            a()
        }
    }
}();
jQuery(document).ready(function() {
    ClinicMasterCarousel.init()
}), jQuery(window).on("load", function() {
    ClinicMasterCarousel.load()
}), jQuery(window).on("resize", function() {
    ClinicMasterCarousel.resize()
});