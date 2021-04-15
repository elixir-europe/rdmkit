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
 * Settings for side navigation
 */
$(document).ready(function () {
  // Initialize navgoco with default options
  $("#menu").navgoco({
    caretHtml: '',
    accordion: true,
    openClass: 'active', // open
    save: false, // leave false or nav highlighting doesn't work right
    cookie: {
      name: 'navgoco',
      expires: false,
      path: '/'
    },
    slide: {
      duration: 400,
      easing: 'swing'
    }
  });
});

/**
 * Activate tooltips
 */

$(function () {
  var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
  var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl, {
      animation: false
    })
  })
})

/**
 * Toggle button texts
 */
 jQuery(function ($) {
  $('.toggle-text[data-bs-toggle="collapse"]').on('click', function () {
      $(this)
      .data('text-original', $(this).text())
      .text($(this).data('text-alt'))
      .data('text-alt', $(this).data('text-original'));
  });
});
