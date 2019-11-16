let counter = 1;
const qty = 20;
const template = Handlebars.compile(document.getElementById("post-template").innerHTML);

function del_post(button) {
  button.parentElement.style.animationPlayState = 'running';
  button.parentElement.addEventListener('animationend', () => {
    button.parentElement.remove();
  });
}

function add_posts() {
  var i;
  var post;
  for (i = 0; i < qty; i++) {
    post = template({'number': counter});
    document.querySelector('body').innerHTML += post;
    counter++;
  }
  return false;
}

document.addEventListener('DOMContentLoaded', () => {
  add_posts();
})

document.addEventListener('click', event => {
  const elem = event.target;
  if (elem.className === 'hide') {
    console.log(elem);
    elem.parentElement.style.animationPlayState = 'running';
    elem.parentElement.addEventListener('animationend', () => {
      elem.parentElement.remove();
    });
  }
});

window.onscroll = () => {
  if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
      document.querySelector('body').color = 'green';
      add_posts()
  }
}
