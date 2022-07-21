$('.menu-bar .event-btn').on('click', function (e) {
    $('nav').toggleClass('active')
})
$('.dropdown-button').on('click', function(e){
    $(this).parent().find(".dropdown").toggleClass('active')
    $('.dropdown.active').not(this).removeClass('active');
    
})
$('html').click(function(e) {
    var $curr;
    if ($(e.target).parent().hasClass('col-2')) {
      $curr = $(e.target).parent().find('.dropdown').toggleClass('active');
    }
    $('.dropdown.active').not($curr).removeClass('active');
  });


  $(".owl-carousel").owlCarousel({
    loop: false,
    margin: 10,
    dots: false,
    nav: false,
  
    responsive: {
      0: {
        items: 2
      },
      768: {
        items: 3
      },
      1336: {
        item: 4
      },
      1340: {
        items: 4
      }
    }
  })
  