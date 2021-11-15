---
layout: none
permalink: assets/js/main.js
---

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
$(document).ready(function external_new_window() {
  for (var c = document.getElementsByTagName("a"), a = 0; a < c.length; a++) {
    var b = c[a];
    if (b.getAttribute("href") && b.hostname !== location.hostname) {
      b.target = "_blank";
      b.rel = "noopener";
    }
  }
});

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
 * Activate popovers
 */

$(function () {
  var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'))
  var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
    return new bootstrap.Popover(popoverTriggerEl)
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


/**
 * Making relevant events visible
 */
function nowToDateString() {
  return new Date().toISOString().substring(0, 10);
};

function showUpcomingEvents() {
  var dstr = nowToDateString();
  var events_block = $(document.getElementsByClassName("upcoming-events"));
  var elements = $('li.upcoming-event').filter(function () {
    return $(this).data('start') >= dstr;
  });
  if ($(elements).length > 0) {
    events_block.show()
  }
  elements.show();
};

function showPastEvents() {
  var dstr = nowToDateString();
  var events_block = $(document.getElementsByClassName("past-events"));
  var elements = $('li.past-event').filter(function () {
    return $(this).data('start') < dstr;
  });
  if ($(elements).length > 0) {
    events_block.show()
  }
  elements.show();
};



/** 
 * Animate numbers when in viewport
 */

// inViewport jQuery plugin
// https://stackoverflow.com/a/26831113/383904
$(function ($, win) {
  $.fn.inViewport = function (cb) {
    return this.each(function (i, el) {
      function visPx() {
        var H = $(this).height(),
          r = el.getBoundingClientRect(), t = r.top, b = r.bottom;
        return cb.call(el, Math.max(0, t > 0 ? H - t : (b < H ? b : H)));
      } visPx();
      $(win).on("resize scroll", visPx);
    });
  };
}(jQuery, window));


jQuery(function ($) { // DOM ready and $ in scope
  $(".count-number").inViewport(function (px) { // Make use of the `px` argument!!!
    if (px > 0 && !this.initNumAnim) {
      this.initNumAnim = true; // Set flag to true to prevent re-running the same animation
      $(this).prop('Counter', 0).animate({
        Counter: $(this).text()
      }, {
        duration: 1000,
        step: function (now) {
          $(this).text(Math.ceil(now));
        }
      });
    }
  });

});


