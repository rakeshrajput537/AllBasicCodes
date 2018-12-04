 //********* Goback*********
function goBack() {
    window.history.back();
}
var i = 0;
var txt = 'College/School List, Rath Hamirpur';
var speed = 50;
 
 // **********TypeWriter***********
function typeWriter() {
  if (i < txt.length) {
    document.getElementById("type").innerHTML += txt.charAt(i);
    i++;
    setTimeout(typeWriter, speed);
  }
}


