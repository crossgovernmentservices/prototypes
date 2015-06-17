;(function($) {

  $(function() {

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

    // -------
    // for skills component
    // -------
    var $skillsList = $(".skills__additional");
    var $extraSkills = $(".skills__extra");

    var addSkill = function(skill) {
      var $skill = $("<li></li>").addClass("skill").text(skill);
      $skillsList.append($skill);
    };

    $("#other-skills").on("keydown", function(e) {
      if (e.keyCode === 13) {
        addSkill(e.currentTarget.value);
        e.preventDefault();
        $(this).val("");
      }
    });

    $(".skills__extra__btn").on("click", function() {
      $extraSkills.toggleClass("active");
    });

    // -------
    // for services component
    // -------
    $(".component-expand-btn").on("click", function(e) {
      e.preventDefault();
      var elClass = $(this).data("to-expand");
      $( elClass ).slideToggle();
    });

    // -------
    // for people finder
    // -------
    var $finderLabel = $(".people-finder-label");
    $(".people-finder-input")
      .on("focus", function() {
        $finderLabel.hide();
      })
      .on("blur", function() {
        if( $(this).val() === "") {
          $finderLabel.show();
        }
      });

    $(".ical-link").ical();

  });

}(jQuery));