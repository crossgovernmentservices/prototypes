;(function($) {

  $(function() {
    $(".pop_blob").hover(
      function() {
        var location = $( this ).data("id");
        var row = $("[data-location='" + location + "']").addClass("row--active");
      },
      function() {
        var location = $( this ).data("id");
        var row = $("[data-location='" + location + "']").removeClass("row--active");
      }
    );
  });

}(jQuery));