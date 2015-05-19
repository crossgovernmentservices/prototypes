;(function($) {
  'use strict';

  // if hash value, fetch and decode
  var hash = (window.location.hash !== "") ?  decodeURIComponent(window.location.hash.substr(1)) : "";

  // on DOM ready
  $(function() {
    var $searchInput = $("#jd_search"),
        $jdResults = $(".jd__results"),
        $skillItems = $(".skill"),
        $searchResultsNum = $(".search-results__number span");

    $jdResults.find(".jd__listing").hide();

    var displaySkillSearchResults = function(skill) {
      var skill = "" || skill;
      $searchInput.val(skill);
      $skillItems.removeClass("skill--highlighted");
      $("[data-skill='" + skill + "']")
        .addClass("skill--highlighted")
        .parents(".jd__listing")
          .show();
      // update the search results value
      $searchResultsNum
        .text($(".jd__listing:visible").length)
        .parent()
          .addClass("search-results__number--active");
    };

    var updateSkillSearch = function(skill) {
      // update hash and encode
      window.location.hash = encodeURIComponent(skill);
      // update input & display results
      $jdResults.find(".jd__listing").hide();
      displaySkillSearchResults(skill);
    };

    if(hash) {
      displaySkillSearchResults(hash);
    }

    // bind events
    $skillItems.on('click', function(e) {
      updateSkillSearch($(this).data('skill'));
    });

    $searchInput.on('change', function() {
      updateSkillSearch($(this).val());
    }).parents("form").on('submit', function(e) {
      e.preventDefault();
    });

    $(".signup__close").on("click", function(e) {
      $(".signup__wrap").slideUp();
      e.preventDefault();
    });

    $(".jd__save").on('click', function() {
      if( $("body").hasClass("notloggedin") ) {
        $(".signup__wrap").slideDown();
        console.log("not logged in");
      } else {
        $(this).toggleClass( 'saved' );
      }
    });
  });

}(jQuery));