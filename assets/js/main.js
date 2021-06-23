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


/**
 * Making relevant events visible
 */
 function nowToDateString() {
  return new Date().toISOString().substring(0, 10);
};

function showUpcomingEvents() {
  var dstr = nowToDateString();
  var events_block = $(document.getElementsByClassName("events"));
  var elements = $('li.upcoming-event').filter(function () {
    return $(this).data('start') >= dstr;
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
$(function($, win) {
  $.fn.inViewport = function(cb) {
    return this.each(function(i,el){
      function visPx(){
        var H = $(this).height(),
            r = el.getBoundingClientRect(), t=r.top, b=r.bottom;
        return cb.call(el, Math.max(0, t>0? H-t : (b<H?b:H)));  
      } visPx();
      $(win).on("resize scroll", visPx);
    });
  };
}(jQuery, window));


jQuery(function($) { // DOM ready and $ in scope
  $(".count-number").inViewport(function(px) { // Make use of the `px` argument!!!
    if(px>0 && !this.initNumAnim) { 
      this.initNumAnim = true; // Set flag to true to prevent re-running the same animation
      $(this).prop('Counter',0).animate({
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

/**
 * Search based on just the docs
 * 
 * https://github.com/pmarsceill/just-the-docs
 * The MIT License (MIT)
 * Copyright (c) 2016 Patrick Marsceill
 */

 (function (Website, undefined) {
 
 // Event handling
 
 Website.addEvent = function(el, type, handler) {
   if (el.attachEvent) el.attachEvent('on'+type, handler); else el.addEventListener(type, handler);
 }
 Website.removeEvent = function(el, type, handler) {
   if (el.detachEvent) el.detachEvent('on'+type, handler); else el.removeEventListener(type, handler);
 }
 Website.onReady = function(ready) {
   // in case the document is already rendered
   if (document.readyState!='loading') ready();
   // modern browsers
   else if (document.addEventListener) document.addEventListener('DOMContentLoaded', ready);
   // IE <= 8
   else document.attachEvent('onreadystatechange', function(){
       if (document.readyState=='complete') ready();
   });
 }
 
 function initSearch() {
   var request = new XMLHttpRequest();
   request.open('GET', '{{ "assets/js/search-data.json" | relative_url }}', true);
 
   request.onload = function(){
     if (request.status >= 200 && request.status < 400) {
       var docs = JSON.parse(request.responseText);
       
       lunr.tokenizer.separator = /[\s/]+/
 
       var index = lunr(function(){
         this.ref('id');
         this.field('title', { boost: 200 });
         this.field('content', { boost: 2 });
         this.field('relUrl');
         this.metadataWhitelist = ['position']
 
         for (var i in docs) {
           this.add({
             id: i,
             title: docs[i].title,
             content: docs[i].content,
             relUrl: docs[i].relUrl
           });
         }
       });
 
       searchLoaded(index, docs);
     } else {
       console.log('Error loading ajax request. Request status:' + request.status);
     }
   };
 
   request.onerror = function(){
     console.log('There was a connection error');
   };
 
   request.send();
 }
 
 function searchLoaded(index, docs) {
   var index = index;
   var docs = docs;
   var searchInput = document.getElementById('search-input');
   var searchResults = document.getElementById('search-results');
   var currentInput;
   var currentSearchIndex = 0;
 
   function showSearch() {
     document.documentElement.classList.add('search-active');
   }
 
   function hideSearch() {
     document.documentElement.classList.remove('search-active');
   }
 
   function update() {
     currentSearchIndex++;
 
     var input = searchInput.value;
     if (input === '') {
       hideSearch();
     } else {
       showSearch();
       // scroll search input into view, workaround for iOS Safari
       window.scroll(0, -1);
       setTimeout(function(){ window.scroll(0, 0); }, 0);
     }
     if (input === currentInput) {
       return;
     }
     currentInput = input;
     searchResults.innerHTML = '';
     if (input === '') {
       return;
     }
 
     var results = index.query(function (query) {
       var tokens = lunr.tokenizer(input)
       query.term(tokens, {
         boost: 10
       });
       query.term(tokens, {
         wildcard: lunr.Query.wildcard.TRAILING
       });
     });
 
     if ((results.length == 0) && (input.length > 2)) {
       var tokens = lunr.tokenizer(input).filter(function(token, i) {
         return token.str.length < 20;
       })
       if (tokens.length > 0) {
         results = index.query(function (query) {
           query.term(tokens, {
             editDistance: Math.round(Math.sqrt(input.length / 2 - 1))
           });
         });
       }
     }
 
     if (results.length == 0) {
       var noResultsDiv = document.createElement('div');
       noResultsDiv.classList.add('search-no-result');
       noResultsDiv.innerText = 'No results found';
       searchResults.appendChild(noResultsDiv);
 
     } else {
       var resultsList = document.createElement('ul');
       searchResults.appendChild(resultsList);
 
       addResults(resultsList, results, 0, 10, 100, currentSearchIndex);
     }
 
     function addResults(resultsList, results, start, batchSize, batchMillis, searchIndex) {
       if (searchIndex != currentSearchIndex) {
         return;
       }
       for (var i = start; i < (start + batchSize); i++) {
         if (i == results.length) {
           return;
         }
         addResult(resultsList, results[i]);
       }
       setTimeout(function() {
         addResults(resultsList, results, start + batchSize, batchSize, batchMillis, searchIndex);
       }, batchMillis);
     }
 
     function addResult(resultsList, result) {
       var doc = docs[result.ref];
 
       var resultsListItem = document.createElement('li');
       resultsList.appendChild(resultsListItem);
 
       var resultLink = document.createElement('a');
       resultLink.setAttribute('href', doc.url);
       resultsListItem.appendChild(resultLink);
 
       var resultTitle = document.createElement('div');
       resultTitle.classList.add('search-result-title');
       resultLink.appendChild(resultTitle);
 
       var resultDoc = document.createElement('div');
       resultDoc.classList.add('search-result-doc');
       resultTitle.appendChild(resultDoc);
 
       var resultDocTitle = document.createElement('div');
       resultDocTitle.classList.add('search-result-doc-title');
       resultDocTitle.innerHTML = doc.doc;
       resultDoc.appendChild(resultDocTitle);
       var resultDocOrSection = resultDocTitle;
 
       if (doc.doc != doc.title) {
         resultDoc.classList.add('search-result-doc-parent');
         var resultSection = document.createElement('div');
         resultSection.classList.add('search-result-section');
         resultSection.innerHTML = doc.title;
         resultTitle.appendChild(resultSection);
         resultDocOrSection = resultSection;
       }
 
       var metadata = result.matchData.metadata;
       var titlePositions = [];
       var contentPositions = [];
       for (var j in metadata) {
         var meta = metadata[j];
         if (meta.title) {
           var positions = meta.title.position;
           for (var k in positions) {
             titlePositions.push(positions[k]);
           }
         }
         if (meta.content) {
           var positions = meta.content.position;
           for (var k in positions) {
             var position = positions[k];
             var previewStart = position[0];
             var previewEnd = position[0] + position[1];
             var ellipsesBefore = true;
             var ellipsesAfter = true;
             for (var k = 0; k < 4; k++) {
               var nextSpace = doc.content.lastIndexOf(' ', previewStart - 2);
               var nextDot = doc.content.lastIndexOf('. ', previewStart - 2);
               if ((nextDot >= 0) && (nextDot > nextSpace)) {
                 previewStart = nextDot + 1;
                 ellipsesBefore = false;
                 break;
               }
               if (nextSpace < 0) {
                 previewStart = 0;
                 ellipsesBefore = false;
                 break;
               }
               previewStart = nextSpace + 1;
             }
             for (var k = 0; k < 4; k++) {
               var nextSpace = doc.content.indexOf(' ', previewEnd + 1);
               var nextDot = doc.content.indexOf('. ', previewEnd + 1);
               if ((nextDot >= 0) && (nextDot < nextSpace)) {
                 previewEnd = nextDot;
                 ellipsesAfter = false;
                 break;
               }
               if (nextSpace < 0) {
                 previewEnd = doc.content.length;
                 ellipsesAfter = false;
                 break;
               }
               previewEnd = nextSpace;
             }
             contentPositions.push({
               highlight: position,
               previewStart: previewStart, previewEnd: previewEnd,
               ellipsesBefore: ellipsesBefore, ellipsesAfter: ellipsesAfter
             });
           }
         }
       }
 
       if (titlePositions.length > 0) {
         titlePositions.sort(function(p1, p2){ return p1[0] - p2[0] });
         resultDocOrSection.innerHTML = '';
         addHighlightedText(resultDocOrSection, doc.title, 0, doc.title.length, titlePositions);
       }
 
       if (contentPositions.length > 0) {
         contentPositions.sort(function(p1, p2){ return p1.highlight[0] - p2.highlight[0] });
         var contentPosition = contentPositions[0];
         var previewPosition = {
           highlight: [contentPosition.highlight],
           previewStart: contentPosition.previewStart, previewEnd: contentPosition.previewEnd,
           ellipsesBefore: contentPosition.ellipsesBefore, ellipsesAfter: contentPosition.ellipsesAfter
         };
         var previewPositions = [previewPosition];
         for (var j = 1; j < contentPositions.length; j++) {
           contentPosition = contentPositions[j];
           if (previewPosition.previewEnd < contentPosition.previewStart) {
             previewPosition = {
               highlight: [contentPosition.highlight],
               previewStart: contentPosition.previewStart, previewEnd: contentPosition.previewEnd,
               ellipsesBefore: contentPosition.ellipsesBefore, ellipsesAfter: contentPosition.ellipsesAfter
             }
             previewPositions.push(previewPosition);
           } else {
             previewPosition.highlight.push(contentPosition.highlight);
             previewPosition.previewEnd = contentPosition.previewEnd;
             previewPosition.ellipsesAfter = contentPosition.ellipsesAfter;
           }
         }
 
         var resultPreviews = document.createElement('div');
         resultPreviews.classList.add('search-result-previews');
         resultLink.appendChild(resultPreviews);
 
         var content = doc.content;
         for (var j = 0; j < Math.min(previewPositions.length, 3); j++) {
           var position = previewPositions[j];
 
           var resultPreview = document.createElement('div');
           resultPreview.classList.add('search-result-preview');
           resultPreviews.appendChild(resultPreview);
 
           if (position.ellipsesBefore) {
             resultPreview.appendChild(document.createTextNode('... '));
           }
           addHighlightedText(resultPreview, content, position.previewStart, position.previewEnd, position.highlight);
           if (position.ellipsesAfter) {
             resultPreview.appendChild(document.createTextNode(' ...'));
           }
         }
       }
      //  Show relative url in search results 
      //  var resultRelUrl = document.createElement('span');
      //  resultRelUrl.classList.add('search-result-rel-url');
      //  resultRelUrl.innerText = doc.relUrl;
      //  resultTitle.appendChild(resultRelUrl);
     }
 
     function addHighlightedText(parent, text, start, end, positions) {
       var index = start;
       for (var i in positions) {
         var position = positions[i];
         var span = document.createElement('span');
         span.innerHTML = text.substring(index, position[0]);
         parent.appendChild(span);
         index = position[0] + position[1];
         var highlight = document.createElement('span');
         highlight.classList.add('search-result-highlight');
         highlight.innerHTML = text.substring(position[0], index);
         parent.appendChild(highlight);
       }
       var span = document.createElement('span');
       span.innerHTML = text.substring(index, end);
       parent.appendChild(span);
     }
   }
 
   Website.addEvent(searchInput, 'focus', function(){
     setTimeout(update, 0);
   });
 
   Website.addEvent(searchInput, 'keyup', function(e){
     switch (e.keyCode) {
       case 27: // When esc key is pressed, hide the results and clear the field
         searchInput.value = '';
         break;
       case 38: // arrow up
       case 40: // arrow down
       case 13: // enter
         e.preventDefault();
         return;
     }
     update();
   });
 
   Website.addEvent(searchInput, 'keydown', function(e){
     switch (e.keyCode) {
       case 38: // arrow up
         e.preventDefault();
         var active = document.querySelector('.search-results a.active');
         if (active) {
           active.classList.remove('active');
           if (active.parentElement.previousSibling) {
             var previous = active.parentElement.previousSibling.querySelector('.search-results a');
             previous.classList.add('active');
           }
         }
         return;
       case 40: // arrow down
         e.preventDefault();
         var active = document.querySelector('.search-results a.active');
         if (active) {
           if (active.parentElement.nextSibling) {
             var next = active.parentElement.nextSibling.querySelector('.search-results a');
             active.classList.remove('active');
             next.classList.add('active');
           }
         } else {
           var next = document.querySelector('.search-results a');
           if (next) {
             next.classList.add('active');
           }
         }
         return;
       case 13: // enter
         e.preventDefault();
         var active = document.querySelector('.search-results a.active');
         if (active) {
           active.click();
         } else {
           var first = document.querySelector('.search-results');
           if (first) {
             first.click();
           }
         }
         return;
     }
   });
 
   Website.addEvent(document, 'click', function(e){
     if (e.target != searchInput) {
       hideSearch();
     }
   });
 }
 
 // Document ready
 
 Website.onReady(function(){
   initSearch();
 });
 
 })(window.Website = window.Website || {});
 
 