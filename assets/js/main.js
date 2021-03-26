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
 * Cookie consent
 */

function setCookie(cookieName, cookieValue, numdaystilexpireasinteger) {
  var d = new Date();
  d.setTime(d.getTime() + (numdaystilexpireasinteger*24*60*60*1000));
  var expires = "expires="+ d.toUTCString();
  document.cookie = cookieName+ "=" + cookieValue + ";" + expires + ";path=/";
}

function getCookie(cookieName) {
  var name = cookieName+ "=";
  var decodedCookie = decodeURIComponent(document.cookie);
  var ca = decodedCookie.split(';');
  for(var i = 0; i <ca.length; i++) {
      var c = ca[i];
      while (c.charAt(0) == ' ') {
          c = c.substring(1);
      }
      if (c.indexOf(name) == 0) {
          return c.substring(name.length, c.length);
      }
  }
  return "";
}

function showLaw() {
  var x = getCookie("cookieName");  //call cookie to get its value
  if (x != "") {
      $("#lawmsg").remove();
  } else {
          setCookie("cookieName", "cookieValue", 2);
      }
  }

