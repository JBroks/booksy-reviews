$(window).on('load', function () {
		$("#overlay").fadeOut("slow");
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

/* Back to top button */
$("a[href='#back-to-top']").click(function() {
  $("html, body").animate({ scrollTop: 0 }, "slow");
  return false;
});

/* When user clicks edit the comment disabled attribute is set to false */
document.getElementById('edit').addEventListener('click', function(){
    document.getElementById('textarea-posted').disabled = false;
});

/* When user clicks cancel make comment non-editable */
document.getElementById('cancel').addEventListener('click', function(){
    document.getElementById('textarea-posted').disabled = true;
});


/* When clicking on textarea to edit/cancel comment show update button */
$('#edit').on('click', function(){
    $('#update.hide').removeClass('hide');
    $('#cancel.hide').removeClass('hide');
});

/* After updating hide buttons */
$('#update').on('click', function(){
    $('#update').addClass('hide');
    $('#cancel').addClass('hide');
});