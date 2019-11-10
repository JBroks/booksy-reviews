$(window).on('load', function () {
		$("#overlay").delay(1000).fadeOut("slow");
});

$(document).ready(function() {
            $('.collapsible').collapsible();
            $('select').material_select();
            $(".button-collapse").sideNav();
        });
        $(document).ready(function() {
            $('select').material_select();
        });

/* Submit search input on enter */    
$(document).ready(function() {

  $('.submit_on_enter').keydown(function(event) {
    // enter has keyCode = 13, change it if you want to use another button
    if (event.keyCode == 13) {
      this.form.submit();
      return false;
    }
  });

});


