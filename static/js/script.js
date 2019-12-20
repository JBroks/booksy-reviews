// SPINNER OVERLAY

/**
 * Function fading out loading spinner overlay 
 **/

$(window).on('load', function() {
  $("#overlay").fadeOut("slow");
});

// INITIALIZE MATERIALIZE

/** 
 * Function that initializes materialize side navbar, accordion collapsible,
 * select menu and tabs
 **/

$(document).ready(function() {
  $('.collapsible').collapsible();
  $('select').material_select();
  $('.button-collapse').sideNav();
  $('.tabs').tabs();
});

// SEARCH BAR

/** 
 * Function that submits search input when user presses enter
 **/

$(document).ready(function() {

  $('.submit_on_enter').keydown(function(event) {
    // enter has keyCode = 13, change it if you want to use another button
    if (event.keyCode == 13) {
      this.form.submit();
      return false;
    }
  });

});

// BACK TO TOP BUTTON

/**
 * Function implements smooth scrolling back to top after clicking the button
 */

$("a[href='#back-to-top']").click(function() {
  $("html, body").animate({ scrollTop: 0 }, "slow");
  return false;
});

/** 
 * Function that displays only the comment form which user chose to update.
 * Function is initiated on edit button click.
 * When users clicks 'edit' button card view is hidden and editable comment is
 * being displayed
 **/

$(document).ready(function() {
  // Hide all (update) form as a default
  $('.posted-form').hide();
  $('.edit').click(function() {
    $(this).parents('div.card-action').prevAll('.card-text').hide();
    $(this).parents('div.card-action').prevAll('.posted-form').show();
    $(this).parents('div.card-action').hide();
  });
});

// DELETE CONFIRMATION

/** 
 * Functions confirming deletion of a review.
 * When user presses the delete button window requesting a confirmation pops up.
 * User can then confirm deletion or cancel it.
 **/

function confirmDel(ev) {
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
              window.location.reload();
            }
          })
          .done(function(response) {
            swal.fire('Review has been deleted!', response.message, response.status);
          })

          .fail(function() {
            swal.fire('Oops...', 'Something went wrong with ajax !', 'error');
          });

      });
    },
    allowOutsideClick: false
  });
}

function confirmDelView(ev) {
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
            url: $(".delete-btn-view a").attr('href'),
            success: function(result) {
              window.location.href = '/show_collection';
            }
          })
          .done(function(response) {
            swal.fire('Review has been deleted!', response.message, response.status);
          })

          .fail(function() {
            swal.fire('Oops...', 'Something went wrong with ajax !', 'error');
          });

      });
    },
    allowOutsideClick: false
  });
}

/** 
 * Functions confirming deletion of a comment.
 * When user presses the delete button window requesting a confirmation pops up.
 * User can then confirm deletion or cancel it.
 **/

function confirmDelCom(ev) {
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
            url: $(".delete-btn-comment a").attr('href'),
            success: function(result) {
              window.location.reload();
            }
          })
          .done(function(response) {
            swal.fire('Comment has been deleted!', response.message, response.status);
          })

          .fail(function() {
            swal.fire('Oops...', 'Something went wrong with ajax !', 'error');
          });

      });
    },
    allowOutsideClick: false
  });
}

/** 
 * Function confirming deletion of an account.
 * When user presses the delete button window requesting a confirmation pops up.
 * User can then confirm deletion or cancel it.
 **/

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
              window.location.href = '/index';
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

// COMMENT COUNTER

/**
 * Function that counts an amount of comments posted for a given review.
 * Commment count is then displayed next to the 'Comments' heading.
 **/

$(document).ready(function() {
  $('#counter').html($(".card").length);
});

// CHECK TRUNCATE

/**
 * Function that checks which comments were truncated in order to display
 * 'show more' link only for those comments
 **/

$(function() {
     $('.comment-text').each(function(index, elem) {

         if(elem.offsetWidth === elem.scrollWidth){
          	$(this).siblings('.show-more').hide();
         }
     });
 });
 
// SHOW MORE / LESS COMMENT

/**
 * Function that toggles materialize class truncate for the comment text
 * in order to manage very long comments.
 * When comments are truncated link 'more' can be clicked to see full text.
 * On other other hand when user wants to hide the comment again he / she can 
 * click 'show less' which will truncate the comment 
 **/

// Show more
$(document).ready(function() {
  $(function() {
    $('.show-less').hide();
    $('.show-more').click(function() {
      $(this).siblings('.comment-text').toggleClass('truncate');
      $(this).hide();
      $(this).siblings('.show-less').show();
    });
  });
});

// Show less
$(document).ready(function() {
  $(function() {
    $('.show-less').click(function() {
      $(this).siblings('.comment-text').toggleClass('truncate');
      $(this).hide();
      $(this).siblings('.show-more').show();
    });
  });
});

// CURRENT YEAR
/**
 * Function that sets maximum for publication year input.
 * Max attribute is set to the current year for 'Add review' and 'Update review'
 * templates.
 **/

$(document).ready(function() {
  var today = new Date();
  var currentYear = today.getFullYear();
  $('#publication_year').attr("max", currentYear);
});
