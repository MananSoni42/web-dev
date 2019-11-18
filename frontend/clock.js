function update_clock() {
  var currentTime = new Date();
  var hr = currentTime.getHours();
  var min = currentTime.getMinutes();
  var sec = currentTime.getSeconds();
  console.log(hr,min,sec);
  document.getElementById("hour-hand").style.transform = `rotate(${360*hr/12}deg)`;
  document.getElementById("minute-hand").style.transform = `rotate(${360*min/60}deg)`;
  document.getElementById("second-hand").style.transform = `rotate(${360*sec/60}deg)`;
}

document.addEventListener('DOMContentLoaded', () => {
  setInterval(update_clock, 1000);
})
