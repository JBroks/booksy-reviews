$(window).on('load', function() {
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

/* Display only the comment form which user choosed to update */

$(document).ready(function() {
  /*Hide all (update) form as a default*/
  $('.posted-form').hide();
  $('.edit').click(function() {
    $(this).parents('div.card-action').prevAll('.card-text').hide();
    $(this).parents('div.card-action').prevAll('.posted-form').show();
    $(this).parents('div.card-action').hide();
  });
});


