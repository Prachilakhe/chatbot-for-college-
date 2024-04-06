// const chatForm = document.querySelector('.chat-form');
// const chatInput = document.querySelector('#chat-input');
// const chatMessages = document.querySelector('#chat-messages');
// console.log(chatForm);


// chatForm.addEventListener('submit',(event)=> {
//   event.preventDefault();
//   const message = chatInput.value.trim();
 
//   if (message !== '') {
//     addMessage(message, 'user');
//     chatInput.value = '';   
//     sendAjaxRequest(message);
//   }
// });



// function sendAjaxRequest(message) {
//   const url = '/chatbot/?message=' + encodeURIComponent(message);
//   const xhr = new XMLHttpRequest();
//   xhr.onreadystatechange = function() {
//     if (xhr.readyState === XMLHttpRequest.DONE) {
//       if (xhr.status === 200) {
//         const response = JSON.parse(xhr.responseText).response;
//         addMessage(response, 'bot');
//       }
//     }
//   };
//   xhr.open('GET', url);
//   xhr.send();
// }



// function addMessage(message, sender) {
//   const li = document.createElement('li');
//   li.textContent = message;
//   li.classList.add(sender);
//   chatMessages.appendChild(li);
//   chatMessages.scrollTop = chatMessages.scrollHeight;

//   // Add the bot's response to the HTML document
 
// }




 
