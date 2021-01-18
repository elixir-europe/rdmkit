
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

/*
* Script to show/hide the buttons under the navigation tiles.
*/
window.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.button').forEach(function (item) {
        // Show the tiles when the cursor hovers over the <h2 class="button">.
        // Does not apply to touchscreen devices. The CSS just shows all the
        // subelements by default for those devices.
        item.addEventListener('mouseenter', function () {
            item.classList.add("active-button");
            item.nextElementSibling.classList.add("active-child-box");
        });
        // Hide the child boxes when the cursor leaves the wrapper <div>
        item.parentElement.addEventListener('mouseleave', function () {
            item.classList.remove("active-button");
            item.nextElementSibling.classList.remove("active-child-box");
        });
    });
});
// Script to open external links into new tab

function external_new_window() {
    for (var c = document.getElementsByTagName("a"), a = 0; a < c.length; a++) {
        var b = c[a];
        if (b.getAttribute("href") && b.hostname !== location.hostname) {
            b.target = "_blank";
            b.rel = "noopener";
        }
    }
}
