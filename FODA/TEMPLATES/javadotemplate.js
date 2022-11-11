var dark = document.getElementById('button');
var light = document.getElementById('slider');
var body = document.querySelector('body');
dark.onclick = function(){
 body.className = "dark";
}

light.onclick = function(){
 body.className = "light";
}