const template_item = Handlebars.compile(document.getElementById("item_disp").innerHTML);
const template_popup = Handlebars.compile(document.getElementById("item_popup").innerHTML);
const template_popup_sub = Handlebars.compile(document.getElementById("item_popup_sub").innerHTML);
const template_popup_pizza = Handlebars.compile(document.getElementById("item_popup_pizza").innerHTML);

var name = "-1"
window.toppings = "-1"

function get_extra() {
  return $.ajax({
    url: '/ajax/get_toppings/'
  });
}

function popup_close() {
  $('#cart_popup').hide();
}

function add_cart(name,type) {

  if (!type.localeCompare('pizza')) {
    document.getElementById('popup').innerHTML = template_popup_pizza({
      'name': name,
      'type': type,
    });

    select = $('#topping-select-'+name+'-'+type);

    for (var i=0; i<window.toppings[type].length; i++){
      select.append('<option name="'+window.toppings[type][i]+'">'+window.toppings[type][i]+'</option>');
    }
    select.selectpicker("refresh");

  }
  else if (!type.localeCompare('sub')) {
    document.getElementById('popup').innerHTML = template_popup_sub({
      'name': name,
      'type': type,
    });

    select = $('#topping-select-'+name+'-'+type);

    for (var i=0; i<window.toppings[type].length; i++){
      select.append('<option name="'+window.toppings[type][i]+'">'+window.toppings[type][i]+'</option>');
    }
    select.selectpicker("refresh");

  }
  else {
    document.getElementById('popup').innerHTML = template_popup({
      'name': name,
      'type': type
    });
  }
}

function get_name() {
  if (name == "-1") {
    $('#start_overlay').show();
    $('#overlay_submit').on('click', function() {
      name = document.getElementById("disp_name").value;
      if (name) {
        $('#start_overlay').hide();
      }
      else {
        alert('Name can\'t be empty')
      }
    });
  }
}

function set_active(active_tab) {
  $(".itemname-pizza").parent().attr("class", "nav-item");
  $(".itemname-sub").parent().attr("class", "nav-item");
  $(".itemname-pasta").parent().attr("class", "nav-item");
  $(".itemname-salad").parent().attr("class", "nav-item");
  $(".itemname-platter").parent().attr("class", "nav-item");

  $(".itemname-"+active_tab).parent().addClass("active");
}

function enumerate_items(name,items) {
  set_active(name);
  document.getElementById('item_display').innerHTML = "";
  for (i=0;i<items.length;i++) {
      document.getElementById('item_display').innerHTML += template_item(items[i]);
  }
}

$(document).ready(function() {
  $('#start_overlay').hide();

  get_extra().then(function(response) {
    window.toppings = response;
  });

  $.ajax({
    url: '/ajax/get_item_names/',
    success: function(response) {
      enumerate_items('pizza' , response);
    },
    data: {
      'name': 'pizza'
    }
  });

  $('.home-btn').on('click', function() {
    var nm = $(this).attr('data-name')
    $.ajax({
      url: '/ajax/get_item_names/',
      success: function(response) {
        enumerate_items(nm , response);
      },
      data: {
        'name': nm
      }
    });
  });

});
