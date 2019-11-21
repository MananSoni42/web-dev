//window.localStorage.setItem('name','none');
//console.log(window.localStorage.getItem('name'));

function get(key) {
  return window.localStorage.getItem(key);
}

function set(key,value) {
  window.localStorage.setItem(key,value);
}

function disp_chat_page() {
  document.getElementById('channel_list').style.display = 'none';
  document.getElementById('channel_list_small').style.display = 'block';
  document.getElementById('chat_list').style.display = 'block';
}

function disp_home_page() {
  console.log('home');
  document.getElementById('channel_list').style.display = 'block';
  document.getElementById('channel_list_small').style.display = 'none';
  document.getElementById('chat_list').style.display = 'none';
}

function disp_chat_list(messages) {
  for (let i=0;i<messages.length;i++) {
    let message = messages[i];
    if (message[2] === 'l') {
      document.getElementById('chat_list').innerHTML += template_message_left({'name': message[0], 'message': message[1]});
    }
    else {
      document.getElementById('chat_list').innerHTML += template_message_right({'name': message[0], 'message': message[1]});
    }
  }
}

const template_message_left = Handlebars.compile(document.getElementById("message-left").innerHTML);
const template_message_right = Handlebars.compile(document.getElementById("message-right").innerHTML);

let messages = [
  ['manan','my message1','l'],
  ['rahul','other message1','r'],
  ['devesh','other message2','r'],
]

if(get('name') === null || get('name') === 'none') {
  document.querySelector('.overlay').style.display = 'block';
}

document.getElementById('overlay_submit').onclick = () => {
  let name = document.getElementById('disp_name').value;
  console.log(name);
  set('name',name)
  if (name && name.trim()) {
    const ov_div = document.querySelector('.overlay');
    ov_div.style.animationPlayState = 'running';
    ov_div.addEventListener('animationend', () => {
      ov_div.remove();
    });
    return;
  }
  else {
    alert("Name can't be empty!");
  }
}

document.getElementById('channel_button').onclick = () => {
  document.querySelector('.channel_form').style.display = 'block';
}

const button = document.getElementById('back_button');
console.log('button',button,button.onclick);
button.onclick = disp_home_page;
console.log('button',button,button.onclick);

//not working
document.getElementById('channel_create').onclick = () => {
  document.querySelector('.channel_form').style.display = 'none';
}

const buttons = document.querySelectorAll('.chat_button');
for (let i = 0, len = buttons.length; i < len; i++) {
  element = buttons[i];
  element.onclick = () => {
    disp_chat_page();
    disp_chat_list(messages);
  }
}
