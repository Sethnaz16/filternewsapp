$(document).ready(function(){
$('.tooltipped').tooltip();
    // This will remove the tooltip functionality for the buttons on this page
$('.tooltipped').tooltip('remove');

  $(".act-mod").sideNav({
    menuWidth: 350,
    edge: 'right', // Choose the horizontal origin
    closeOnClick: true, // Closes side-nav on <a> clicks, useful for Angular/Meteor
    draggable: true, // Choose whether you can drag to open on touch screens,
  });
  $('.collapsible').collapsible({
    onOpen: function(e) { e.preventDefault(); }, // Callback for Collapsible open
    onClose: function(e) { e.preventDefault(); } // Callback for Collapsible close
  });

  $('.collapsible-header').click(function(){
      alert("success");
  })
        
});

