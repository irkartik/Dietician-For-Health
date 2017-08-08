$(function()
				{
					navigationMenu();
					testimonialStuff();			// script for client transition
				});
function navigationMenu()
{
	$(function(){
		$('.header-menu').click(function(event)
		{
			$('.sidebar').toggleClass('open');
		});
	});
}
function testimonialStuff(){                // script for client section
$('.testimonial-unit').first().addClass('active-testimonial');
$('.testimonial-logo').first().addClass('active-testimonials');

$('.testimonial-logo').click(function(){
  var $this = $(this),
      $siblings = $this.parent().children(),
      position = $siblings.index($this);

  $('.testimonial-unit').removeClass('active-testimonial').eq(position).addClass('active-testimonial');
  $siblings.removeClass('active-testimonials');
  $this.addClass('active-testimonials');
});

$('.testimonial-control-prev,.testimonial-control-next').click(function(){
  var $this = $(this),
    curActiveClient = $('.testimonial-belt').find('.active-testimonial'),
    position = $('.testimonial-belt').children().index(curActiveClient),
    clientNum = $('.testimonial-unit').length;

    if($this.hasClass('testimonial-control-prev'))
    {
      if(position < clientNum-1){
     $('.active-testimonial').removeClass('active-testimonial').next().addClass('active-testimonial');
      $('.active-testimonials').removeClass('active-testimonials').next().addClass('active-testimonials');
    }else{
      $('.testimonial-unit').removeClass('active-testimonial').first().addClass('active-testimonial');
      $('.testimonial-logo').removeClass('active-testimonials').first().addClass('active-testimonials');
    }
  }else {
    if(position > 0){
    $('.active-testimonial').removeClass('active-testimonial').prev().addClass('active-testimonial');
    $('.active-testimonials').removeClass('active-testimonials').prev().addClass('active-testimonials');
    }
    else {
      $('.testimonial-unit').removeClass('active-testimonial').last().addClass('active-testimonial');
      $('.testimonial-logo').removeClass('active-testimonials').last().addClass('active-testimonials');
    }
  }
});
}
