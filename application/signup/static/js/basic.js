;(function($) {
  'use strict';

  var swapClasses = function($el, remove, add) {
    $el
      .removeClass(remove)
      .addClass(add);
  };

  $(function() {
    var $cvInput = $("#cv-upload");
    var $cvUploadBtn = $(".cv-upload-btn");
    var $linkedinBtn = $(".linkedin-upload-btn");

    $cvUploadBtn.on("click", function(e) {
      $cvInput.trigger("click");
      e.preventDefault();
    });

    $cvInput.on("change", function() {
      var $item = $(this).parents(".job-search-item");
      window.setTimeout(function() {
        $item.addClass("cv-active");
      }, 2000);
    });

    $linkedinBtn.on("click", function(e) {
      e.preventDefault();
      var $linkedinItem = $("[data-item-type='linkedin']");
      swapClasses($linkedinItem, "linkedin--associated-not", "linkedin--associating");
      window.setTimeout(function() {
        swapClasses($linkedinItem, "linkedin--associating", "linkedin--associated");
        $(".skills__extra__wrap").removeClass("skills__extra--no-linkedin");
      }, 2000);
    });

  });

}(jQuery));