<img src="../images/main_bkgd.png" width="260" height="10" alt="" border="0">// JavaScript Document

$(document).ready(function() {

  $("nav#global a").click(function(){
    $("nav#global a").removeClass("fpo");
    $(this).addClass("fpo");
    });
  
});