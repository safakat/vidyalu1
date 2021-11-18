console.log(window.location.host);
// const url = 'wss://'+window.location.host+'ws/chat';
const url = 'wss://vidyalu.myvtd.site:8890/ws/chat/'
const ws = new WebSocket(url);
function SendMessage(){
    console.log("Hello");
}

ws.onopen = function(event){
    console.log("Connection is opend");
    ws.send("Thanks for connecting");
}

ws.onmessage = function(event){
    console.log(event);
    console.log("Message is received");
    const data = event.data
    document.querySelector('#chat-log').value += (data + '\n');
}

ws.onclose = function(event){
    console.log("connection is closed");
}
ws.onerror = function(event){
    console.log("Something fucked up.");
}

document.querySelector('#chat-message-input').focus();
document.querySelector('#chat-message-input').onkeyup = function(e){
 if (e.keyCode === 13) {
     document.querySelector('#chat-message-submit').click();    
 }   
};

document.querySelector('#chat-message-submit').onclick = function(e){
    const messageInputDom = document.querySelector('#chat-message-input');
    const message = messageInputDom.value;
    ws.send(message)
    // chatSocket.send(JSON.stringify({
    //     'message':message,
    //     'command':'fetch_messages'
    // }));
    messageInputDom.value = '';
};
