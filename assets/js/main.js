/**
 * Opera Homes Website - Refactored Main JS
 * 
 * CLEAN ARCHITECTURE ENHANCEMENT
 * 
 * This file replaces the original function.js while strictly preserving all logic.
 * Original code is wrapped in descriptive modules for better maintenance.
 */

(function ($) {
    "use strict";

    /**
     * CORE MODULE
     * Handles global variables and core initialization
     */
    const CoreModule = (function() {
        /* --- ORIGINAL CODE START --- */
        var $window = $(window); 
        var $body = $('body'); 
        /* --- ORIGINAL CODE END --- */

        return {
            window: $window,
            body: $body,
            init: function() {
                /* Preloader Effect */
                /* --- ORIGINAL CODE START --- */
                $window.on('load', function(){
                    $(".preloader").fadeOut(600);
                });
                /* --- ORIGINAL CODE END --- */

                /* Scroll to top */
                /* --- ORIGINAL CODE START --- */
                if($("a[href='#top']").length){
                    $(document).on("click", "a[href='#top']", function() {
                        $("html, body").animate({ scrollTop: 0 }, "slow");
                        return false;
                    });
                }
                /* --- ORIGINAL CODE END --- */

                /* Animated Wow Js */	
                /* --- ORIGINAL CODE START --- */
                new WOW().init();
                /* --- ORIGINAL CODE END --- */
            }
        };
    })();

    /**
     * NAVIGATION MODULE
     * Handles sticky header and mobile menus
     */
    const NavModule = (function() {
        return {
            init: function() {
                /* Sticky Header Logic */
                /* --- ORIGINAL CODE START --- */
                if($('.active-sticky-header').length){
                    $(window).on('resize', function(){
                        setHeaderHeight();
                    });

                    function setHeaderHeight(){
                         $("header.main-header").css("height", $('header .header-sticky').outerHeight());
                    }	
                
                    $(window).on("scroll", function() {
                        var fromTop = $(window).scrollTop();
                        setHeaderHeight();
                        var headerHeight = $('header .header-sticky').outerHeight()
                        $("header .header-sticky").toggleClass("hide", (fromTop > headerHeight + 100));
                        $("header .header-sticky").toggleClass("active", (fromTop > 600));
                    });
                }	
                /* --- ORIGINAL CODE END --- */
                
                /* Slick Menu JS Initialization */
                /* --- ORIGINAL CODE START --- */
                $('#menu').slicknav({
                    label : '',
                    prependTo : '.responsive-menu'
                });
                /* --- ORIGINAL CODE END --- */
            }
        };
    })();

    /**
     * SLIDER MODULE
     * Handles all Swiper and slider initializations
     */
    const SliderModule = (function() {
        return {
            init: function() {
                $(document).ready(function() {
                    /* Hero Slider Layout JS */
                    /* --- ORIGINAL CODE START --- */
                    const hero_slider_layout = new Swiper('.hero-slider-layout .swiper', {
                        slidesPerView : 1,
                        speed: 1000,
                        spaceBetween: 0,
                        loop: true,
                        autoplay: {
                            delay: 4000,
                        },
                        pagination: {
                            el: '.hero-pagination',
                            clickable: true,
                        },
                        navigation: {
                            nextEl: '.hero-button-next',
                            prevEl: '.hero-button-prev',
                        },
                    });
                    /* --- ORIGINAL CODE END --- */

                    /* How We Work Client Logo Slider JS */ 
                    /* --- ORIGINAL CODE START --- */
                    if ($('.work-with-company-slider').length) {
                        const work_with_company_slider = new Swiper('.work-with-company-slider .swiper', {
                            slidesPerView : 2,
                            speed: 2000,
                            spaceBetween: 30,
                            loop: true,
                            autoplay: {
                                delay: 5000,
                            },
                            breakpoints: {
                                768:{
                                    slidesPerView: 4,
                                },
                                991:{
                                    slidesPerView: 5,
                                }
                            }
                        });
                    }
                    /* --- ORIGINAL CODE END --- */

                    /* testimonial Slider JS */
                    /* --- ORIGINAL CODE START --- */
                    if ($('.testimonial-slider').length) {
                        const testimonial_slider = new Swiper('.testimonial-slider .swiper', {
                            slidesPerView : 1,
                            speed: 1000,
                            spaceBetween: 30,
                            centeredSlides: true,
                            loop: true,
                            autoplay: {
                                delay: 3000,
                            },
                            pagination: {
                                el: '.swiper-pagination',
                                clickable: true,
                            },
                            breakpoints: {
                                768:{
                                    slidesPerView: 2,
                                },
                                991:{
                                    slidesPerView: 3,
                                }
                            }
                        });
                    }
                    /* --- ORIGINAL CODE END --- */

                    /* Service Single Slider */
                    /* --- ORIGINAL CODE START --- */
                    if ($('.service-single-slider').length) {
                        const service_single_slider = new Swiper('.service-single-slider .swiper', {
                            slidesPerView : 1,
                            speed: 1000,
                            spaceBetween: 30,
                            loop: true,
                            autoplay: {
                                delay: 5000,
                            },
                            navigation: {
                                nextEl: '.service-button-next',
                                prevEl: '.service-button-prev',
                            },
                            breakpoints: {
                                768:{
                                    slidesPerView: 1,
                                },
                                991:{
                                    slidesPerView: 1,
                                }
                            }
                        });
                    }
                    /* --- ORIGINAL CODE END --- */
                });
            }
        };
    })();

    /**
     * ANIMATION MODULE
     * Handles GSAP, Parallax and Scroll Effects
     */
    const AnimationModule = (function() {
        return {
            init: function() {
                /* Image Reveal Animation */
                /* --- ORIGINAL CODE START --- */
                if ($('.reveal').length) {
                    gsap.registerPlugin(ScrollTrigger);
                    let revealContainers = document.querySelectorAll(".reveal");
                    revealContainers.forEach((container) => {
                        let image = container.querySelector("img");
                        let tl = gsap.timeline({
                            scrollTrigger: {
                                trigger: container,
                                toggleActions: "play none none none"
                            }
                        });
                        tl.set(container, {
                            autoAlpha: 1
                        });
                        tl.from(container, 1, {
                            xPercent: -100,
                            ease: Power2.out
                        });
                        tl.from(image, 1, {
                            xPercent: 100,
                            scale: 1,
                            delay: -1,
                            ease: Power2.out
                        });
                    });
                }
                /* --- ORIGINAL CODE END --- */

                /* Text Effect Animations */
                this.initTextAnimations();
                
                /* Parallaxie js */
                /* --- ORIGINAL CODE START --- */
                var $parallaxie = $('.parallaxie');
                if($parallaxie.length && ($(window).width() > 991))
                {
                    if ($(window).width() > 768) {
                        $parallaxie.parallaxie({
                            speed: 0.55,
                            offset: 0,
                        });
                    }
                }
                /* --- ORIGINAL CODE END --- */
            },

            initTextAnimations: function() {
                /* Text Anime Style 1 */
                /* --- ORIGINAL CODE START --- */
                if ($('.text-anime-style-1').length) {
                    let staggerAmount 	= 0.05,
                        translateXValue = 0,
                        delayValue 		= 0.5,
                       animatedTextElements = document.querySelectorAll('.text-anime-style-1');
                    
                    animatedTextElements.forEach((element) => {
                        let animationSplitText = new SplitText(element, { type: "chars, words" });
                            gsap.from(animationSplitText.words, {
                            duration: 1,
                            delay: delayValue,
                            x: 20,
                            autoAlpha: 0,
                            stagger: staggerAmount,
                            scrollTrigger: { trigger: element, start: "top 85%" },
                            });
                    });		
                }
                /* --- ORIGINAL CODE END --- */

                /* Text Anime Style 2 */
                /* --- ORIGINAL CODE START --- */
                if ($('.text-anime-style-2').length) {				
                    let	 staggerAmount 		= 0.03,
                         translateXValue	= 20,
                         delayValue 		= 0.1,
                         easeType 			= "power2.out",
                         animatedTextElements = document.querySelectorAll('.text-anime-style-2');
                    
                    animatedTextElements.forEach((element) => {
                        let animationSplitText = new SplitText(element, { type: "chars, words" });
                            gsap.from(animationSplitText.chars, {
                                duration: 1,
                                delay: delayValue,
                                x: translateXValue,
                                autoAlpha: 0,
                                stagger: staggerAmount,
                                ease: easeType,
                                scrollTrigger: { trigger: element, start: "top 85%"},
                            });
                    });		
                }
                /* --- ORIGINAL CODE END --- */

                /* Text Anime Style 3 */
                /* --- ORIGINAL CODE START --- */
                if ($('.text-anime-style-3').length) {		
                    let	animatedTextElements = document.querySelectorAll('.text-anime-style-3');
                    
                     animatedTextElements.forEach((element) => {
                        //Reset if needed
                        if (element.animation) {
                            element.animation.progress(1).kill();
                            element.split.revert();
                        }

                        element.split = new SplitText(element, {
                            type: "lines,words,chars",
                            linesClass: "split-line",
                        });
                        gsap.set(element, { perspective: 400 });

                        gsap.set(element.split.chars, {
                            opacity: 0,
                            x: "50",
                        });

                        element.animation = gsap.to(element.split.chars, {
                            scrollTrigger: { trigger: element,	start: "top 90%" },
                            x: "0",
                            y: "0",
                            rotateX: "0",
                            opacity: 1,
                            duration: 1,
                            ease: Back.easeOut,
                            stagger: 0.02,
                        });
                    });		
                }
                /* --- ORIGINAL CODE END --- */
            }
        };
    })();

    /**
     * COMPONENT MODULE
     * Handles specific components like Gallery, Forms, Projects
     */
    const ComponentModule = (function() {
        return {
            init: function() {
                /* Counter initialization */
                /* --- ORIGINAL CODE START --- */
                if ($('.counter').length) {
                    $('.counter').counterUp({ delay: 6, time: 3000 });
                }
                /* --- ORIGINAL CODE END --- */

                /* Video/Image Popup */
                this.initPopups();

                /* Contact Form */
                this.initForms();

                /* Project Filter */
                this.initProjectFilter();

                /* Project Showcase Hover */
                this.initProjectShowcase();
            },

            initPopups: function() {
                /* Youtube Background Video JS */
                /* --- ORIGINAL CODE START --- */
                if ($('#herovideo').length) {
                    var myPlayer = $("#herovideo").YTPlayer();
                }
                /* --- ORIGINAL CODE END --- */

                /* Zoom Gallery screenshot */
                /* --- ORIGINAL CODE START --- */
                $('.gallery-items').magnificPopup({
                    delegate: 'a',
                    type: 'image',
                    closeOnContentClick: false,
                    closeBtnInside: false,
                    mainClass: 'mfp-with-zoom',
                    image: {
                        verticalFit: true,
                    },
                    gallery: {
                        enabled: true
                    },
                    zoom: {
                        enabled: true,
                        duration: 300, 
                        opener: function(element) {
                        return element.find('img');
                        }
                    }
                });
                /* --- ORIGINAL CODE END --- */

                /* Popup Video */
                /* --- ORIGINAL CODE START --- */
                if ($('.popup-video').length) {
                    $('.popup-video').magnificPopup({
                        type: 'iframe',
                        mainClass: 'mfp-fade',
                        removalDelay: 160,
                        preloader: false,
                        fixedContentPos: true
                    });
                }
                /* --- ORIGINAL CODE END --- */
            },

            initForms: function() {
                /* Contact form validation */
                /* --- ORIGINAL CODE START --- */
                var $contactform = $("#contactForm");
                $contactform.validator({focus: false}).on("submit", function (event) {
                    if (!event.isDefaultPrevented()) {
                        event.preventDefault();
                        submitForm();
                    }
                });

                function submitForm(){
                    /* Ajax call to submit form */
                    $.ajax({
                        type: "POST",
                        url: "form-process.php",
                        data: $contactform.serialize(),
                        success : function(text){
                            if (text === "success"){
                                formSuccess();
                            } else {
                                submitMSG(false,text);
                            }
                        }
                    });
                }

                function formSuccess(){
                    $contactform[0].reset();
                    submitMSG(true, "Message Sent Successfully!")
                }

                function submitMSG(valid, msg){
                    if(valid){
                        var msgClasses = "h4 text-success";
                    } else {
                        var msgClasses = "h4 text-danger";
                    }
                    $("#msgSubmit").removeClass().addClass(msgClasses).text(msg);
                }
                /* --- ORIGINAL CODE END --- */
            },

            initProjectFilter: function() {
                /* Our Project (filtering) Start */
                /* --- ORIGINAL CODE START --- */
                $(window).on( "load", function(){
                    if( $(".project-item-boxes").length ) {
                            
                        var $menuitem = $(".project-item-boxes").isotope({
                            itemSelector: ".project-item-box",
                            layoutMode: "masonry",
                            masonry: {
                                columnWidth: 1,
                            }
                        });
                            
                        var $menudisesnav = $(".our-Project-nav li a");
                            $menudisesnav.on('click', function (e) { 
                        
                            var filterValue = $(this).attr('data-filter');
                            $menuitem.isotope({
                                filter: filterValue
                            }); 
                            
                            $menudisesnav.removeClass("active-btn"); 
                            $(this).addClass("active-btn");
                            e.preventDefault();
                        });		
                        $menuitem.isotope({ filter: "*" });
                    }			
                });
                /* --- ORIGINAL CODE END --- */
            },

            initProjectShowcase: function() {
                /* Project Showcase Hover Background Change */
                /* --- ORIGINAL CODE START --- */
                if ($('.opera-projects-showcase').length) {
                    const $cols = $('.project-vertical-col');
                    const $layers = $('.project-bg-layer');

                    $cols.on('mouseenter', function() {
                        const target = $(this).data('hover-target');
                        $layers.removeClass('active');
                        $layers.filter('[data-project="' + target + '"]').addClass('active');
                    });
                }
                /* --- ORIGINAL CODE END --- */
            }
        };
    })();

    // Initialize all modules
    CoreModule.init();
    NavModule.init();
    SliderModule.init();
    AnimationModule.init();
    ComponentModule.init();

})(jQuery);
