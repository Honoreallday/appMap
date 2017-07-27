/* the fade in function for the title, it takes a bit to load the whole page because of it so just comment out when your working
on css and html */
function fades(){
  $('#pt1').fadeTo(0,0);
  $('#pt2').fadeTo(0,0);
  $('#pt3').fadeTo(0,0);
  $('.title').fadeTo(0,0);
  $('#else').fadeTo(0,0);
  $('.title').delay(400).fadeTo(2500,1);
  $('#pt1').delay(1550).fadeTo(2500,1);
  $('#pt2').delay(2700).fadeTo(2500,1);
  $('#pt3').delay(3850).fadeTo(2500,1);
  $('#else').delay(5000).fadeTo(0,1);
  console.log('it woks');
};

$(document).ready(fades);
