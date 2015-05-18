(function($) {
  var URL = window.URL || window.webkitURL;
  var monthNames = [
    "Jan", "Feb", "Mar", "Apr",
    "May", "Jun", "Jul", "Aug"
  ];

  var prettyDate = function() {
    var date = new Date(),
        day = date.getDate(),
        monthInd = date.getMonth(),
        year = date.getFullYear();
    return day + " " + monthNames[monthInd];
  };

  var makeCellElement = function(text, _class) {
    var _class = _class || "";
    return $(document.createElement("td")).addClass(_class).text( text );
  };

  $(function() {
    var tmpl = $(".receipt-process__container").first();
    var $desc = $("#item-description");
    var takePic = document.querySelector("#take-picture");
    var $expTable = $(".expenses__table");

    var addExpenseLine = function(amount, desc) {
      var row = document.createElement("tr");
      $(row)
        .append( makeCellElement( prettyDate() ) )
        .append( makeCellElement( desc ) )
        .append( makeCellElement(amount, "numeric"))
        .append( makeCellElement("waiting", "numeric") )
        .prependTo( $(".expenses__table").find("tbody") );
    };

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

        $item
          .find(".receipt__submit")
            .on("click", function() {
              var amount = $item.find(".receipt__amount").text();
              addExpenseLine(amount, desc);
              $item.fadeOut();
            });
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
