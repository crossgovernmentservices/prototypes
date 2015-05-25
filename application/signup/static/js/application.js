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
      // should consider adding an onblur event too
      var current_val = $item.text();
          $item
            .text("")
            .append( $( document.createElement("input") ).addClass("form-control data-item__edit__input").val(current_val).on("change", saveChange) );
    });

    var replaceText = function($el, txt) {
      $el.empty().text(txt);
    };

    var sendData = function(data, successCb) {
      $.ajax({
        type: 'POST',
        url: '/profile/',
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        data: JSON.stringify(data),
        success: successCb
      });
    };

    var saveChange = function() {
      var $this = $(this);
      var $container = $this.parent();
      var val = $this.val();
      var data = {};

      if( $container.data("key") ) {

        // this is hacky
        if( $container.hasClass("data-item__entry--email") ) {
          data = {
            email: {
              personal: val
            }
          };
        } else {
          data[ $this.parent().data("key") ] = val;
        }

        sendData(data, function() {
            replaceText($container, val);
        });
      }
    };
  });

}(jQuery));
