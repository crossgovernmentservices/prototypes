;(function($) {

  $(function() {
    $(".submit-app-btn").on("click", function() {
      $(".app-submitted__wrap").slideDown('slow');
      $.post( "/jobs/submit_application" );
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
