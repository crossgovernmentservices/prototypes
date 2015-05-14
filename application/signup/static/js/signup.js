;(function() {

  var providers = [
    {"name": "google", "identifier": "gmail.com" },
    {"name": "facebook", "identifier": "facebook.com" }
  ];

  $.fn.removeClassPrefix = function(prefix) {
      this.each(function(i, el) {
          var classes = el.className.split(" ").filter(function(c) {
              return c.lastIndexOf(prefix, 0) !== 0;
          });
          el.className = $.trim(classes.join(" "));
      });
      return this;
  };

  $(function() {
    // should this just return the value of the provider??
    var checkProvider = function(email) {
      providers.forEach(function(prov, ind, arr) {
        if( email !== "" && email.indexOf(prov.identifier) >= 0 ) {
          $sBtn.removeClassPrefix("signup__btn--");
          $sBtn.addClass("signup__btn--" + prov.name);
          console.log("service provider detected: ", prov.name);
          updateVisibleLabel(prov.name);
        }
      });
    };

    var updateVisibleLabel = function(provider) {
      $sBtn
        .find("span")
          .removeClass("signup__btn__content--active")
          .end()
        .find("[data-provider="+provider+"]")
          .addClass("signup__btn__content--active");
    };

    var $sInput = $(".signup__input");
    var $sBtn = $(".signup__btn");

    $sInput.on("keyup", function(e) {
      checkProvider(e.target.value);
    });

  });

}(jQuery));