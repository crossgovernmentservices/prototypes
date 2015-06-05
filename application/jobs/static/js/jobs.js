;(function($) {
  'use strict';

  // if hash value, fetch and decode
  var hash = (window.location.hash !== "") ?  decodeURIComponent(window.location.hash.substr(1)) : "";

  // on DOM ready
  $(function() {
    var $searchInput = $("#q"),
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
      console.log('skill', skill);
      // update input & display results
      $jdResults.find(".jd__listing").hide();
      displaySkillSearchResults(skill);
    };

    if(hash) {
      displaySkillSearchResults(hash);
    }

    updateSkillSearch($searchInput.val());

    $(".signup__close").on("click", function(e) {
      $(".signup__wrap").slideUp();
      e.preventDefault();
    });
  });

}(jQuery));
