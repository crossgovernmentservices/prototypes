;(function($) {

  $(function() {
    $(".submit-app-btn").on("click", function(e) {
      $(".app-submitted__wrap").slideDown('slow');
      $.post( "/jobs/submit_application" );
      e.preventDefault();
    });

    $(".settings__save").on("click", function(e) {
      e.preventDefault();
      e.stopPropagation();
      $(".settings-msg__success").show().fadeOut(3000);
      return false;
    });

    $(".data-item__edit").on("click", function() {
      var $item = $(this).parent().siblings(".data-item__entry");
      var current_val = $item.text();
          $item
            .text("")
            .append( $( document.createElement("input") ).addClass("form-control data-item__edit__input").val(current_val).on("change", saveChange) );
    });

    var replaceText = function($el, txt) {
      $el.empty().text(txt);
    };

    var saveChange = function() {
      var $this = $(this);
      var $container = $this.parent();

      if( $container.data("key") ) {
        var val = $this.val();
        var data = {};

        data[ $this.parent().data("key") ] = val;
        $.ajax({
          type: 'POST',
          url: '/profile/',
          contentType: 'application/json; charset=utf-8',
          dataType: 'json',
          data: JSON.stringify(data)
        });
      }
    };
  });

}(jQuery));
