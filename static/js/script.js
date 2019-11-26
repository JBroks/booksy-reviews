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

/* Function confirming deletion of the review */

function confirmation(ev) {
  ev.preventDefault();

  swal.fire({
    title: 'Are you sure?',
    text: "You won't be able to revert this!",
    type: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#d33',
    cancelButtonColor: '#3085d6',
    confirmButtonText: 'Yes, delete it!',
    showLoaderOnConfirm: true,
    preConfirm: function() {
      return new Promise(function(resolve) {
           $.ajax({
            url: $(".delete-btn a").attr('href'),
            success: function(result) {
              window.location.replace($(".delete-btn a").attr('href-return'));
            }
          })
          .done(function(response) {
           swal.fire('Review was deleted!', response.message, response.status);
          })
          
          .fail(function() {
            swal.fire('Oops...', 'Something went wrong with ajax !', 'error');
          });
        
      });
    },
    allowOutsideClick: false
  });
}

/* Function confirming deletion of the account */

function confirmationAcc(ev) {
  ev.preventDefault();

  swal.fire({
    title: 'Are you sure?',
    text: "You won't be able to revert this!",
    type: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#d33',
    cancelButtonColor: '#3085d6',
    confirmButtonText: 'Yes, delete it!',
    showLoaderOnConfirm: true,
    preConfirm: function() {
      return new Promise(function(resolve) {
           $.ajax({
            url: $(".delete-acc a").attr('href'),
            success: function(result) {
              window.location.replace($(".delete-acc a").attr('href-return'));
            }
          })
          .done(function(response) {
           swal.fire('Your account has been pernamently deleted!', response.message, response.status);
          })
          
          .fail(function() {
            swal.fire('Oops...', 'Something went wrong with ajax !', 'error');
          });
        
      });
    },
    allowOutsideClick: false
  });
}


/* Comment counter */
document.getElementById('counter').innerHTML = document.getElementsByClassName("card").length;
