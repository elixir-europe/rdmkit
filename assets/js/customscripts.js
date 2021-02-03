/**
 * AnchorJS
 */
$(document).ready(function () {
  anchors.options = {
    placement: 'left'
  };
  anchors.add('h2:not(.no-anchor)');
})
/**
 * Bootstrap Tooltip activation
 */

var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl)
})

/**
 * Function to open external links in separate tab
 */
function external_new_window() {
  for (var c = document.getElementsByTagName("a"), a = 0; a < c.length; a++) {
    var b = c[a];
    if (b.getAttribute("href") && b.hostname !== location.hostname) {
      b.target = "_blank";
      b.rel = "noopener";
    }
  }
}

/**
 * Collapsing sidebar
 */
$(document).ready(function() {
	$('.menu li:has(ul)').click(function(e) {
		e.preventDefault();

		if($(this).hasClass('active')) {
			$(this).removeClass('active');
			$(this).children('ul').slideUp();
		} else {
			$('.menu li ul').slideUp();
			$('.menu li').removeClass('active');
			$(this).addClass('active');
			$(this).children('ul').slideDown();
		}

		$('.menu li ul li a').click(function() {
			window.location.href = $(this).attr('href');
		})
	});
});
