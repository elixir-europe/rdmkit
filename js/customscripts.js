$('#mysidebar').height($(".nav").height());


$(document).ready(function () {
    // activate tooltips. although this is a bootstrap js function, it must be activated this way in your theme.
    $('[data-toggle="tooltip"]').tooltip({
        placement: 'top'
    });

    /**
     * AnchorJS
     */
    //anchors.options.placement = 'left';
    anchors.options.titleText = 'Link to this section';
    anchors.add('h2');
    anchors.remove('.no_anchor')

});

// needed for nav tabs on pages. See Formatting > Nav tabs for more details.
// script from http://stackoverflow.com/questions/10523433/how-do-i-keep-the-current-tab-active-with-twitter-bootstrap-after-a-page-reload
$(function () {
    var json, tabsState;
    $('a[data-toggle="pill"], a[data-toggle="tab"]').on('shown.bs.tab', function (e) {
        var href, json, parentId, tabsState;

        tabsState = localStorage.getItem("tabs-state");
        json = JSON.parse(tabsState || "{}");
        parentId = $(e.target).parents("ul.nav.nav-pills, ul.nav.nav-tabs").attr("id");
        href = $(e.target).attr('href');
        json[parentId] = href;

        return localStorage.setItem("tabs-state", JSON.stringify(json));
    });

    tabsState = localStorage.getItem("tabs-state");
    json = JSON.parse(tabsState || "{}");

    $.each(json, function (containerId, href) {
        return $("#" + containerId + " a[href=" + href + "]").tab('show');
    });

    $("ul.nav.nav-pills, ul.nav.nav-tabs").each(function () {
        var $this = $(this);
        if (!json[$this.attr("id")]) {
            return $this.find("a[data-toggle=tab]:first, a[data-toggle=pill]:first").tab("show");
        }
    });
});

$(document).ready(function () {
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


$(function () {
    $('[data-toggle="tooltip"]').tooltip()
})


$(document).ready(function () {
    $("#tg-sb-link").click(function () {
        $("#tg-sb-sidebar").toggle();
        $("#tg-sb-content").toggleClass('col-md-9');
        $("#tg-sb-content").toggleClass('col-md-12');
        $("#tg-sb-icon").toggleClass('fa-toggle-on');
        $("#tg-sb-icon").toggleClass('fa-toggle-off');
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

function external_new_window() {
    for (var c = document.getElementsByTagName("a"), a = 0; a < c.length; a++) {
        var b = c[a];
        if (b.getAttribute("href") && b.hostname !== location.hostname) {
            b.target = "_blank";
            b.rel = "noopener";
        }
    }
}
