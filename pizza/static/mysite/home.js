const template_item = Handlebars.compile(document.getElementById("item_disp").innerHTML);
//document.getElementById('channel_list_small').innerHTML += template_channel_small({'name': name});
var name = "-1"

function get_name() {
  if (name == "-1") {
    $('#overlay').show();
    $('#overlay_submit').on('click', function() {
      name = document.getElementById("disp_name").value;
      $('#overlay').hide();
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
  $('#overlay').hide();
  get_name();

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
