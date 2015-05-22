;(function($) {
  'use strict';

  var swapClasses = function($el, remove, add) {
    $el
      .removeClass(remove)
      .addClass(add);
  };

  var updateProfileData = function(data) {
    $.ajax({
      type: 'POST',
      url: '/profile/',
      contentType: 'application/json; charset=utf-8',
      dataType: 'json',
      data: JSON.stringify(data)
    });
  };

  $(function() {
    var $cvInput = $("#cv-upload");
    var $cvUploadBtn = $(".cv-upload-btn");
    var $linkedinBtn = $(".linkedin-upload-btn");
    var $welcomeEl = $(".welcome__wrap");

    $(".welcome__skip").on("click", function(e) {
      e.preventDefault();
      $welcomeEl.slideUp();
    });

    $cvUploadBtn.on("click", function(e) {
      $cvInput.trigger("click");
      e.preventDefault();
    });

    $cvInput.on("change", function() {
      var $item = $(this).parents(".job-search-item");
      window.setTimeout(function() {
        $item.addClass("cv-active");
        updateProfileData({ cv: 'true' });
      }, 2000);
    });

    var pic_src = "/static/images/colm-britton.jpg";
    $linkedinBtn.on("click", function(e) {
      e.preventDefault();
      var $linkedinItem = $("[data-item-type='linkedin']");
      swapClasses($linkedinItem, "linkedin--associated-not", "linkedin--associating");
      window.setTimeout(function() {
        swapClasses($linkedinItem, "linkedin--associating", "linkedin--associated");
        $(".skills__extra__wrap").removeClass("skills__extra--no-linkedin");
        $(".basicprofile__pic").attr("src", pic_src);
        var data = {
          integrations: {
              linkedin: 'true'
          }
        };
        updateProfileData(data);
        updateProfileData({ profile_pic: pic_src });
      }, 2000);
    });

  });

}(jQuery));