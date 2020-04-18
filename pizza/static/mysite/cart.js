window.cust_name = sessionStorage.getItem("cust_name");

function close_order() {
  $.ajax({
    url: '/ajax/close_cart/',
    success: function(response) {
      window.location = "/";
    },
    data: {
      'name': window.cust_name
    }
  });
}

function load_cart(response) {

  $("#title").html('Order #' + response['num']);

  tab = $('#order-table-body');
  tab.html('');

  for (var i=0;i<response['table'].length; i++) {
    row = "<tr>"
    for (var j=0;j<response['table'][i].length; j++) {
      row += "<td>" + response['table'][i][j] + "</td>"
    }
    row += "</tr>"
    tab.append(row)
  }
  row = '<tr><td class="font-weight-bold text-center">Total</td><td>' + response['total'] + '</td></tr>'
  tab.append(row)
}

$(document).ready(function() {
  $.ajax({
    url: '/ajax/load_cart/',
    success: load_cart,
    data: {
      'name': window.cust_name
    }
  });
});
