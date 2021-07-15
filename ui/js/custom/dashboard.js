$(function () {
  //Json data by api call for order table
  $.get(orderListApiUrl, function (response) {
    if (response) {
      var table = "";
      var totalCost = 0;
      $.each(response, function (index, order) {
        totalCost += parseFloat(order.total);
        table +=
          '<tr data-id="' +
          order.order_id +
          '">' +
          "<td>" +
          order.datetime +
          "</td>" +
          "<td>" +
          order.order_id +
          "</td>" +
          "<td>" +
          order.customer_name +
          "</td>" +
          "<td>" +
          order.total.toFixed(2) +
          " Rs</td>" +
          '<td><span class="btn btn-xs btn-warning order-details">Details</span></td></tr>';
      });
      table +=
        '<tr><td colspan="3" style="text-align: end"><b>Total</b></td><td><b>' +
        totalCost.toFixed(2) +
        " Rs</b></td></tr>";
      $("table").find("tbody").empty().html(table);
    }
  });
});

$(document).on("click", ".order-details", function () {
  var tr = $(this).closest("tr");
  var order_id = tr.data("id");

  window.location =
    "C:/Users/jaikumar%20singh/Desktop/python_projects_grocery_webapp/ui/order-details.html?order_id=" +
    order_id;
});
