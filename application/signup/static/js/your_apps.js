;(function(exports) {
  // -------
  // Add global QueryString property
  // usage QueryString.param
  // -------
  var QueryString = function () {
    // This function is anonymous, is executed immediately and 
    // the return value is assigned to QueryString!
    var query_string = {};
    var query = window.location.search.substring(1);
    var vars = query.split("&");
    for (var i=0;i<vars.length;i++) {
      var pair = vars[i].split("=");
          // If first entry with this name
      if (typeof query_string[pair[0]] === "undefined") {
        query_string[pair[0]] = pair[1];
          // If second entry with this name
      } else if (typeof query_string[pair[0]] === "string") {
        var arr = [ query_string[pair[0]], pair[1] ];
        query_string[pair[0]] = arr;
          // If third or later entry with this name
      } else {
        query_string[pair[0]].push(pair[1]);
      }
    } 
      return query_string;
  }();
  exports.QueryString = QueryString;
}(window));

;(function($) {
  $(function() {
    var noOfferSetUp = function() {
      var $apps_with_offers = $("[data-jd-status='offer']");
      var $offer_filter_btn = $(".button--offer");
      $apps_with_offers.hide();
      $offer_filter_btn.hide();
    };
    if( QueryString.hasOffer === "yes" ) {
      console.log("there is an offer");
    } else {
      noOfferSetUp();
    }
  });
}(jQuery));
