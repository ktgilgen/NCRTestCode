//With the help of http://stackoverflow.com/questions/17919808/twitter-bootstrap-multiple-dropdowns-on-click-jquery-assistance -->

$(function(){
  $('.nested-dropdown').click(function(event){
                              event.stopPropagation();
                              var dropdown = $(this).children('.dropdown-menu');
                              dropdown.toggle();
                              });
  });