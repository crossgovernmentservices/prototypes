;(function($) {

  $(function() {
    $(".submit-app-btn").on("click", function() {
      $(".app-submitted__wrap").slideDown('slow');
      this.preventDefault();
    });
  });

}(jQuery));