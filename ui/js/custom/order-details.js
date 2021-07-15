$(function () {
    //Json data by api call for order table
    var urlParams = new URLSearchParams(window.location.search);
    var order_id = parseInt(urlParams.get('order_id'));
    console.log(order_id);

    $.get(orderDetailsApiUrl + "?orderid=" + order_id, function (response) {
        if (response) {
            var table = '';

            $.each(response, function (index, order) {
                console.log(order.order_details);
                table += '<tr>' +
                    '<td>' + order.product_name + '</td>' +
                    '<td>' + order.quantity + '</td>' +
                    '<td>' + order.price_per_unit + '</td>' +
                    '<td>' + order.total_price + ' Rs</td></tr>';
            });

            $("table").find('tbody').empty().html(table);
        }
    });
});