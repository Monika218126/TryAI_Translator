function copyText(){

let text =
document.getElementById(
"translation"
).innerText;

navigator.clipboard.writeText(text);

alert(
"Copied Successfully!"
);

}

function startVoice(){

const recognition =
new webkitSpeechRecognition();

recognition.lang='en-US';

recognition.start();

recognition.onresult=function(event){

document.getElementById(
"textInput"
).value=
event.results[0][0].transcript;

};

}

function toggleDarkMode(){

document.body.classList.toggle(
"dark-mode"
);

}