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

    $(".signup__btn").on("click", function(e) {
      e.preventDefault();
      var openedWindow = window.open('googlelogin',
                                  'signing into google',
                                  'toolbar=no,location=no,status=no,menubar=no,scrollbars=yes,resizable=yes,width=300,height=300');
      window.setTimeout(function() {
        openedWindow.close();
        // do next now logged in thing here...
        $("body").addClass("loggedin");
      }, 4000);
      return false;
    });

    // for the settings section
    $(".settings-btn").on("click", function(e) {
      $(this).blur();
      $(".settings__wrap").toggleClass('settings--active');
      e.preventDefault();
    });

    // for filtering your_apps pages
    var $appsList = $(".apps__list");
    var $apps = $appsList.find(".app__container");
    var $filterBtns = $(".filter .filter-btn");

    var performFilter = function(status) {
      $apps.hide();
      $appsList.find("[data-jd-status='" + status  + "']").show();
    };

    $filterBtns.on("click", function(e) {
      console.log("this fired");
      $filterBtns.removeClass('active');
      $(this).addClass('active');
      performFilter($(this).data("status"));
    });

  });

}(jQuery));