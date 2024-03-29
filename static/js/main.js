$(function(){
    $('.banner-section__slider').slick({dots:false,
        prevArrow:'<button class="banner-section__slider-btn banner-section__slider-btnprev"><img src="http://127.0.0.1:8000/static/img/arrow-left.svg" alt=""></button>',
        nextArrow:'<button class="banner-section__slider-btn banner-section__slider-btnnext"><img src="http://127.0.0.1:8000/static/img/arrow-right.svg" alt=""></button>'
    })
    
    $('.tab').on('click',function(e){
        e.preventDefault();

        $($(this).siblings()).removeClass('tab--active');
        $($(this).parent().siblings().find('div')).removeClass('tabs-content--active');

        $(this).addClass('tab--active');
        $($(this).attr('href')).addClass('tabs-content--active')
    });

    $('.product-item__favorite').on('click',function(){
        $(this).toggleClass('product-item__favorite--active')
    });

    $('.product-slider').slick({
        slidesToShow: 4,
        slidesToScroll: 1,
        prevArrow:'<button class="product-slider__slider-btn product-slider__slider-btnprev"><img src="http://127.0.0.1:8000/static/img/arrow-black-left.svg" alt=""></button>',
        nextArrow:'<button class="product-slider__slider-btn product-slider__slider-btnnext"><img src="http://127.0.0.1:8000/static/img/arrow-black-right.svg" alt=""></button>'
    });

    $('.filter-style').styler();

    $('.filter__item-drop').on('click', function(){
        $(this).toggleClass('filter__item-drop--active');
        $(this).next().slideToggle(200)
    });

    $(".rate-yo").rateYo({
        ratedFill: "#1C62CD",
        spacing: "7x",
        normalFill: "#c4c4c4",
        readOnly: true,
        fullStar: true
    });

    $('.input-file input[type=file]').on('change', function(){
	let file = this.files[0];
	$(this).next().html(file.name);
});
    
$('.minus-btn').on('click', function(e) {
    e.preventDefault();
    var $this = $(this);
    var $input = $this.closest('div').find('input');
    var value = parseInt($input.val());
 
    if (value > 1) {
        value = value - 1;} 
    else {
        value = 0;
    }
 
  $input.val(value);
 
});
 
$('.plus-btn').on('click', function(e) {
    e.preventDefault();
    var $this = $(this);
    var $input = $this.closest('div').find('input');
    var value = parseInt($input.val());
 
    if (value < 100) {
        value = value + 1;
    } else {
        value =100;
    }
 
    $input.val(value);
});



});

