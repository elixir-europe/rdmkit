
$(document).ready(function () {
    // activate tooltips. although this is a bootstrap js function, it must be activated this way in your theme.
    $('[data-toggle="tooltip"]').tooltip({
        placement: 'top'
    });

    /**
     * AnchorJS
     */
    //anchors.options.placement = 'left';
    anchors.options = {
        placement: 'left'
    };
    anchors.add('h2:not(.no-anchor)');

    // Initialize navgoco with default options
    $("#mysidebar").navgoco({
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

// Function to open external links in separate tab
function external_new_window() {
    for (var c = document.getElementsByTagName("a"), a = 0; a < c.length; a++) {
        var b = c[a];
        if (b.getAttribute("href") && b.hostname !== location.hostname) {
            b.target = "_blank";
            b.rel = "noopener";
        }
    }
}


/*
* Dropdown boxes for the home page
*/
document.addEventListener('DOMContentLoaded', () => {
  var acc = document.getElementsByClassName("accordion");
  var i;

  for (i = 0; i < acc.length; i++) {
    acc[i].addEventListener("click", function() {
      this.classList.toggle("active");
      var panelWidth = $(this).innerWidth();
      var panel = this.nextElementSibling;
      if (panel.style.maxHeight) {
        panel.style.maxHeight = null;
      } else {
        if ($(window).width() > 600) {
          panel.style.maxHeight = "225px";
          panel.style.overflowY = "scroll";
          panel.style.width = panelWidth + "px";
        } else {
          panel.style.maxHeight = panel.scrollHeight + "px";
        }
      }
    });
  }
});
