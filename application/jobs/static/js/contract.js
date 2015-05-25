;(function($) {
  'use strict';

  var sendData = function(data) {
    $.ajax({
      type: 'POST',
      url: '/profile/',
      contentType: 'application/json; charset=utf-8',
      dataType: 'json',
      data: JSON.stringify(data)
    });
  };

  // on DOM ready
  $(function() {
    var $label = $(".switch__checkbox__label");

    $(".contract").bind("contractSigned", function() {
      $(this).toggleClass("contract--signed");
      $label.toggleClass("switch__checkbox__label--on");
    });

    $(".switch__checkbox").on("change", function() {
      // not DRY at this point but this likely to 
      // need to be the case
      if( $(this).is(':checked') ) {
        $(".contract").trigger("contractSigned");
        sendData({ "contract_signed": true });
      } else {
        $(".contract").trigger("contractSigned");
        sendData({ "contract_signed": false });
      }
    });
  });

}(jQuery));
