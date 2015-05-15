(function() {
  var takePic = document.querySelector("#take-picture"),
      showPic = document.querySelector("#show-picture");

      if( takePic && showPic ) {
        // change event
        takePic.onchange = function(ev) {
          // reference to taken pic or chosen file
          var files = ev.target.files,
              file;
          if( files && files.length > 0 ) {
            file = files[0];
            var URL = window.URL || window.webkitURL;
            var imgURL = URL.createObjectURL(file);
            showPic.src = imgURL;
            showPic.height = "100";
            showPic.onload = function() {
              URL.revokeObjectURL(imgURL);
            };
          }
        };
      }
})();
