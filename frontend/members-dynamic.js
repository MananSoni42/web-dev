let members = [
  ["Name #1", "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Deserunt, rerum!"],
  ["Name #2", "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Deserunt, rerum!"],
  ["Name #3", "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Deserunt, rerum!"],
  ["Name #4", "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Deserunt, rerum!"]
]

let member_template;

function add_member(id, name, details) {
  document.getElementById('members').innerHTML += member_template({
                                                          "id": id,
                                                          "name": name,
                                                          "details": details
                                                        });
}

function set_remove_buttons_opacity(o) {
  let buttons = document.querySelectorAll(".remove-button");
  for (let i=0;i<buttons.length;i++) {
    buttons[i].style.opacity = o;
  }
}

function button_clicked(event) {
  const elem = event.target;
  if (elem.className === 'remove-button') {
    if (elem.style.opacity === 0) {
      return;
    }
    elem.parentElement.style.animationPlayState = 'running';
    elem.parentElement.addEventListener('animationend', () => {
      elem.parentElement.remove();
    });
    set_remove_buttons_opacity(0);
  }

  else if (elem.className === 'standard-button' && elem.id =="add") {
    document.querySelector('.new-member-form').style.opacity = 1;
  }

  else if (elem.className === 'standard-button' && elem.id =="delete") {
    set_remove_buttons_opacity(0.6);
  }

  else if (elem.className === 'form-button') {
    if (elem.parentElement.style.opacity === 0) {
      return;
    }
    let name = document.getElementById("member_name").value;
    let details = document.getElementById("member_name").value;
    members.push([name,details])
    add_member(members.length,name,details)
    elem.parentElement.style.opacity = 0;
  }
}

document.addEventListener('DOMContentLoaded', () => {
  // define template
  member_template = Handlebars.compile(document.getElementById("template").innerHTML);

  // add initial members
  for (let i=0; i<members.length; i++) {
    add_member(i+1,members[i][0],members[i][1]);
  }

  //set initial opacities
  document.querySelector('.new-member-form').style.opacity = 0;
  set_remove_buttons_opacity(0);

  //look for click events
  document.addEventListener('click', event => button_clicked(event));
})
