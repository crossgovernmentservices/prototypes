(function($) {
  var URL = window.URL || window.webkitURL;

  $(function() {
    var tmpl = $(".receipt-process__container").first();
    var $desc = $("#item-description");
    console.log(tmpl);
    var takePic = document.querySelector("#take-picture");

    var renderExpense = function(imgURL, desc) {
      var $item = tmpl.clone();
      $item
        .removeClass("hidden")
        .find(".receipt-process__image")
          .attr("height", 100)
          .attr("src", imgURL)
          .on("load", function() {
            URL.revokeObjectURL(imgURL);
          })
        .end()
        .find(".receipt__description")
          .text( desc )
        .end()
        .appendTo(".receipt__list");

        // process for x seconds then change
        setTimeout(function(){
          $item.addClass("receipt--processed");
        }, 2000);
    };

    if( takePic ) {
      // change event
      takePic.onchange = function(ev) {
        // check if description is filled in
        if( $desc.val() !== "" ) {
          // reference to taken pic or chosen file
          var files = ev.target.files,
              file;
          if( files && files.length > 0 ) {
            file = files[0];
            var imgURL = URL.createObjectURL(file);
            renderExpense(imgURL, $desc.val());
          }
        } else {
          // ask for desc
          console.log("no description");
        }
      };
    }
  });

})(jQuery);
