;(function($) {
  "use strict";

  var writeCookie = function(str) {
    var pathStr = ";path=/";
    document.cookie = str + pathStr;
  };

  $(function() {
    var $emailInput = $("#email");
    var $sMsg = $(".success");

    $sMsg.hide();

    $(".prototype-login__form").on("submit", function(e) {
      e.preventDefault();
      var email = $emailInput.val();
      writeCookie("email="+email);
      $.post( "/prototype_set_user", { email: email } ).done(function(data) {
        $sMsg.hide();
      });
    });

  });
  
}(jQuery));
