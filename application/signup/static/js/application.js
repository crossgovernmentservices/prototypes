;(function($) {

  $(function() {
    $(".submit-app-btn").on("click", function() {
      $(".app-submitted__wrap").slideDown('slow');
      this.preventDefault();
    });

    $(".settings__save").on("click", function(e) {
      e.preventDefault();
      e.stopPropagation();
      $(".settings-msg__success").show().fadeOut(3000);
      return false;
    });
  });

}(jQuery));