var socket;
function fullscreen(element) {
  if(element.requestFullscreen) {
    element.requestFullscreen();
  } else if(element.mozRequestFullScreen) {
    element.mozRequestFullScreen();
  } else if(element.webkitRequestFullscreen) {
    element.webkitRequestFullscreen();
  } else if(element.msRequestFullscreen) {
    element.msRequestFullscreen();
  }
}
/*$(document).ready(function(){
    if(window.location.protocol != "https:"){
    	window.location.href = "https://"+window.location.hostname +":"+window.location.port + "/";
    }
});*/
$(document).ready(function(){
socket = io.connect(window.location.protocol+'//' + document.domain + ':' + location.port + '/main');
socket.on('connect', function() {
        document.getElementById("connecting").style.display = "none";
    });
socket.on('disconnect', function(){
document.getElementById("connecting").style.display = "block";
});
});