$(function(){
    $('.banner-section__slider').slick({dots:false,
        prevArrow:'<button class="banner-section__slider-btn banner-section__slider-btnprev"><img src="http://localhost:8000/static/img/arrow-left.svg" alt=""></button>',
        nextArrow:'<button class="banner-section__slider-btn banner-section__slider-btnnext"><img src="http://localhost:8000/static/img/arrow-right.svg" alt=""></button>'
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
        prevArrow:'<button class="product-slider__slider-btn product-slider__slider-btnprev"><img src="http://localhost:8000/static/img/arrow-black-left.svg" alt=""></button>',
        nextArrow:'<button class="product-slider__slider-btn product-slider__slider-btnnext"><img src="http://localhost:8000/static/img/arrow-black-right.svg" alt=""></button>'
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

$('.cart__content-delete').on('click', function(e){
    localStorage.removeItem($(this).attr('id'))
    location.reload()
});

$('.minus-btn').on('click', function(e) {
    e.preventDefault();
    var $this = $(this);
    var $input = $this.closest('div').find('input');
    var value = parseInt($input.val());
 
    if (value > 1) {
        value = value - 1;} 
    else {
        value = 1;
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

$('.product-card__btn-add').on('click', function(e){
    let productID = $(this).attr('data-id');
    let productProperties = {};

    
    productProperties.productID = productID
    productProperties.productTitle = $(this).attr('data-title')
    productProperties.productImage = $(this).attr('data-img')
    productProperties.productPrice = $(this).attr('data-price')
    if (localStorage.getItem(productID) === null) {
        localStorage.setItem(productID,JSON.stringify(productProperties))
    } else {
        alert('Товар уже добавлен в корзину')
    }


    $('.cart__num').text(localStorage.length)
})

    $('.cart__num').text(localStorage.length)
    
$('.pagination-list_a').on('click', function(e){
    let url = new URL(window.location.href)
    let search_params = url.searchParams
    url.search = search_params.toString()
    let btn_id = $(this).attr('id')
    search_params.set('page', btn_id)

    let new_url = url.toString()

    window.location.href = new_url
})

$('.save-btn').on('click', function(e){
    window.location.href('http://localhost:8000/')
})

$('.open-popup').click(function(e) {
    e.preventDefault();
    $('.popup-bg').fadeIn(800);
    $('html').addClass('no-scroll');
});

$('.close-popup').click(function() {
    $('.popup-bg').fadeOut(800);
    $('html').removeClass('no-scroll');
});

$('.pagination-list_a_catalog').click(function(e){
    let url = new URL(window.location.href)
    let btn_id = $(this).attr('id')
    url.searchParams.set('page_num',btn_id)
    window.location.href = url
})


});

