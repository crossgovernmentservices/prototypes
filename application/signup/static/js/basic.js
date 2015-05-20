;(function($) {
  'use strict';

  $(function() {
    var $cvInput = $("#cv-upload");
    var $cvUploadBtn = $(".cv-upload-btn");

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
  });

}(jQuery));