$(document).ready(function(){
  $('a[href^="#sg_eat"]').on('click', function (event) {
    event.preventDefault();
    $("html,body").animate({
        scrollTop: $($.attr(this, 'href')).offset().top
    }, 500);
  });
  $('a[href^="#sg_charity"]').on('click', function (event) {
    event.preventDefault();
    $("html,body").animate({
        scrollTop: $($.attr(this, 'href')).offset().top
    }, 500);
  });
  $('a[href^="#sg_education"]').on('click', function (event) {
    event.preventDefault();
    $("html,body").animate({
        scrollTop: $($.attr(this, 'href')).offset().top
    }, 500);
  });
  $('a[href^="#sg_luxury"]').on('click', function (event) {
    event.preventDefault();
    $("html,body").animate({
        scrollTop: $($.attr(this, 'href')).offset().top
    }, 500);
  });

  $('a[href^="#sg_invest"]').on('click', function (event) {
    event.preventDefault();
    $("html,body").animate({
        scrollTop: $($.attr(this, 'href')).offset().top
    }, 500);
  });



});
