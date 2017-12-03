
 (function(){
  function init(){
	var text = window.location.hash.substring(1)
     document.getElementById('myImg').src=text;
  }
  init();
 
 })();