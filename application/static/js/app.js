(function($, window) {

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
    var gmailFlag = false;
    // should this just return the value of the provider??
    var checkProvider = function(email) {
      gmailFlag = ( email.indexOf("gmail") !== -1 ) ? true:false;
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

    $sInput.on("change keyup", function(e) {
      checkProvider(e.target.value);
    });

    var submitLogin = function() {
      $("body").removeClass("notloggedin").addClass("loggedin");
      $("#loginForm").submit();
    };

    $(".signup__btn").on("click", function(e) {
      e.preventDefault();
      // only mock google login if gmail address
      if ( gmailFlag ) {
        // create new window to open
        var openedWindow = window.open('/signup/googlelogin',
                                    'signing into google',
                                    'toolbar=no,location=no,status=no,menubar=no,scrollbars=yes,resizable=yes,width=300,height=300');
        // close window after 400ms
        window.setTimeout(function() {
          openedWindow.close();
          // do next now logged in thing here...
          $(".signup__wrap").slideUp("fast");
          submitLogin();
        }, 4000);
      } else {
        submitLogin();
      }
      return false;
    });

  });

}).call(this, jQuery, window);
