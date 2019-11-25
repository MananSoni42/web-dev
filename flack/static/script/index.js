//window.localStorage.setItem('name','none');
//console.log(window.localStorage.getItem('name'));

function get(key) {
  return window.localStorage.getItem(key);
}

function set(key,value) {
  window.localStorage.setItem(key,value);
}

function disp_message_page() {
  document.getElementById('channel_page').style.display = 'none';
  document.getElementById('channel_list_small').style.display = 'block';
  document.getElementById('chat_page').style.display = 'block';
}

function disp_channel_page() {
  document.getElementById('channel_page').style.display = 'block';
  document.getElementById('channel_list_small').style.display = 'none';
  document.getElementById('chat_page').style.display = 'none';
}

function clear_message_list() {
  document.getElementById('chat_list').innerHTML = '';
}

function disp_message_list() {
  var request = new XMLHttpRequest();
  request.open('POST','/getMessages');
  request.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8');
  request.onload = () => {
    let messages = JSON.parse(request.responseText).messages;
    for (let i=0;i<messages.length;i++) {
      let message = messages[i];
      if (message[0] === get('name')) {
        document.getElementById('chat_list').innerHTML += template_message_left({'name': message[0], 'message': message[1]});
      }
      else {
        document.getElementById('chat_list').innerHTML += template_message_right({'name': message[0], 'message': message[1]});
      }
    }
  };
  request.send(JSON.stringify({'channel': get('current_channel'), 'name': get('name')}));
}

function clear_channel_list() {
  document.getElementById('channel_list_small').innerHTML = '';
  document.getElementById('channel_list').innerHTML = ''
}

function disp_channel_list(channels) {
    for (let i = 0; i<channels.length; i++) {
      document.getElementById('channel_list_small').innerHTML += template_channel_small({'name': channels[i][0]});
      console.log(channels[i][0],channels[i][1]);
      document.getElementById('channel_list').innerHTML += template_channel(
        {
          'name': channels[i][0],
          'num_messages': channels[i][1]
      });
    }
  }

function disp_inital_channel_list() {
  var request = new XMLHttpRequest();
  request.open('GET','/getChannels');
  request.onload = () => {
    let channels = JSON.parse(request.responseText).channels;
    clear_channel_list();
    disp_channel_list(channels);
  };
  request.send();
}

const template_message_left = Handlebars.compile(document.getElementById("message-left").innerHTML);
const template_message_right = Handlebars.compile(document.getElementById("message-right").innerHTML);
const template_channel = Handlebars.compile(document.getElementById("channel").innerHTML);
const template_channel_small = Handlebars.compile(document.getElementById("channel_small").innerHTML);

var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
var channels = [];

document.addEventListener('click', event => {
  const elem = event.target;
  if (elem.id === 'back_button') {
    disp_channel_page();
    const top_bar = document.getElementById('top_bar');
      top_bar.style.display='flex';
    return;
  }
  else if (elem.id === 'channel_button') {
    document.querySelector('.channel_form').style.display = 'block';
    return;
  }
  else if (elem.id === 'channel_create') {
    let name = document.getElementById('channel_name').value;
    var request = new XMLHttpRequest();
    socket.emit('addChannel',{'channel': name})
    document.getElementById('channel_list_small').innerHTML += template_channel_small({'name': name});
    document.getElementById('channel_list').innerHTML += template_channel(
      {
        'name': name,
        'num_messages': 0
    });
    document.querySelector('.channel_form').style.display = 'none';
    return;
  }
  else if (elem.id === 'chat_button') {
    let channel_name = elem.parentElement.parentElement.id;
    set('current_channel',channel_name);
    disp_message_page();
    clear_message_list();
    disp_message_list();

    const top_bar = document.getElementById('top_bar');
    top_bar.style.animationPlayState = 'running';
    top_bar.addEventListener('animationend', () => {
      top_bar.style.display='none';
      top_bar.style.animationPlayState = 'paused';
    });
  }

  else if (elem.id == 'send_button') {
    let message_typed = document.getElementById('messages_typed').value;
    socket.emit('addMessage',{'name': get('name'), 'channel': get('current_channel'), 'message': message_typed})
  }
});

socket.on('getChannels', data => {
  let channels = data.channel;
  clear_channel_list();
  disp_channel_list(channels);
});

socket.on('newMessage', data => {
  let message = data.message;
  let channels = data.channels;
  console.log(channels)
  if (message[0] === get('name')) {
    document.getElementById('chat_list').innerHTML += template_message_left({'name': message[0], 'message': message[1]});
  }
  else {
    document.getElementById('chat_list').innerHTML += template_message_right({'name': message[0], 'message': message[1]});
  }
  clear_channel_list();
  disp_channel_list(channels);
});

document.addEventListener('DOMContentLoaded', () => {
  document.getElementById('overlay_submit').onclick = () => {
    let name = document.getElementById('disp_name').value;
    set('name',name)
    document.getElementById("true_disp_name").innerHTML = 'Hello, ' + get('name');
    var request = new XMLHttpRequest();
    request.open('POST','/addName');
    request.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8');
    request.send(JSON.stringify({'name': name}));

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

  if(get('name') === null || get('name') === 'none') {
    document.querySelector('.overlay').style.display = 'block';
  }
  else {
    document.getElementById("true_disp_name").innerHTML = 'Hello, ' + get('name');
  }
  disp_inital_channel_list();
});
