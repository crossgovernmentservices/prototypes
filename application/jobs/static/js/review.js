;(function($) {
  'use strict';

  var $skillsList = $(".skills__list");

  var addSkill = function(skill) {
    var $skill = $("<li></li>").text(skill);
    $skillsList.append($skill);
  };

  // on DOM ready
  $(function() {

    $("#other-skills").on("keydown", function(e) {
      if (e.keyCode === 13) {
        //check whether this is cross browser
        addSkill(e.currentTarget.value);
        e.preventDefault();
        $(this).val("");
      }
    });

    $skillsList.on("click", "li", function() {
      $(this).remove();
    });
  });

}(jQuery));