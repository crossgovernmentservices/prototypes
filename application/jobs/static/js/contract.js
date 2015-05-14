;(function($) {
  'use strict';

  // on DOM ready
  $(function() {

    $(".contract").bind("contractSigned", function() {
      $(this).toggleClass("contract--signed");
    });

    $(".switch__checkbox").on("change", function() {
      // not DRY at this point but this likely to 
      // need to be the case
      if( $(this).is(':checked') ) {
        $(".contract").trigger("contractSigned");
      } else {
        $(".contract").trigger("contractSigned");
      }
    });
  });

}(jQuery));
