$(function () {
  setTimeout(function () {
    $(".alert").slideUp(3000);
  }, 5000);
  
  var lastScrollTop = 0;

 
  $(window).scroll(function () {

    var scrollTop = $(this).scrollTop();

    if (scrollTop < lastScrollTop) {

      $('#navigationcontainer').css("backgroundColor","transparent")
    } else {
      $("#search-button-container").show()
      $('#navigationcontainer').css("backgroundColor", "rgba(0, 0, 0, 0.575)")
    }

    lastScrollTop = scrollTop;
  });
  $(window).on("load", () => {
    $('#navigationcontainer').css("backgroundColor", "transparent")
  })
  
 
});
