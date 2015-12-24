var socket;
var ping;
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
socket = io.connect(window.location.protocol+'//' + document.domain + ':' + location.port + '/main',{
    'reconnection': true,
    'reconnectionDelay': 1000,
    'reconnectionDelayMax' : 1000
});
ping = function(){
  socket.emit('ping',"ping");
}
socket.on('ping',function(json){
alert('hi');
});
socket.on('connect', function(){
document.getElementById("connecting").style.display = "none";
        document.getElementById("reconnecting").style.display = "none";
        document.getElementById("stations").style.display = "block";
});
socket.on('disconnect', function(){
  document.getElementById("stations").style.display = "none";
document.getElementById("reconnecting").style.display = "block";
});
socket.on('error', function(object){

});
socket.on('reconnect', function(object){

});
});