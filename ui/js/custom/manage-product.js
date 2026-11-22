var productModal = $("#productModal");

$(function () {
    $.get(productListApiUrl, function (products) {
        var tableBody = $("table").find("tbody").empty();

        $.each(products, function (index, product) {
            var row = $("<tr>").data({
                id: product.product_id,
                name: product.name,
                unit: product.uom_id,
                price: product.price_per_unit
            });

            row.append($("<td>").text(product.name));
            row.append($("<td>").text(product.uom_name));
            row.append($("<td>").text(product.price_per_unit));

            var editButton = $("<button>", {
                type: "button",
                class: "btn btn-xs btn-primary edit-product",
                text: "Edit"
            });
            var deleteButton = $("<span>", {
                class: "btn btn-xs btn-danger delete-product",
                text: "Delete"
            });

            row.append($("<td>").append(editButton, " ", deleteButton));
            tableBody.append(row);
        });
    });
});

$("#saveProduct").on("click", function () {
    var productId = Number($("#id").val());
    var requestPayload = {
        product_name: $("#name").val(),
        uom_id: $("#uoms").val(),
        price_per_unit: $("#price").val()
    };

    var apiUrl = productSaveApiUrl;

    if (productId > 0) {
        requestPayload.product_id = productId;
        apiUrl = productUpdateApiUrl;
    }

    callApi("POST", apiUrl, {
        data: JSON.stringify(requestPayload)
    });
});

$(document).on("click", ".edit-product", function () {
    var product = $(this).closest("tr").data();

    $("#id").val(product.id);
    $("#name").val(product.name);
    $("#price").val(product.price);
    productModal.data("selectedUnit", product.unit);

    productModal.find(".modal-title").text("Edit Product");
    $("#saveProduct").prop("disabled", true);
    productModal.modal("show");
});

$(document).on("click", ".delete-product", function () {
    var row = $(this).closest("tr");

    if (confirm("Are you sure to delete " + row.data("name") + " item?")) {
        callApi("POST", productDeleteApiUrl, {
            product_id: row.data("id")
        });
    }
});

productModal.on("hide.bs.modal", function () {
    $("#id").val("0");
    $("#name, #uoms, #price").val("");
    $("#saveProduct").prop("disabled", false);
    productModal.removeData("selectedUnit");
    productModal.find(".modal-title").text("Add New Product");
});

productModal.on("show.bs.modal", function () {
    var unitDropdown = $("#uoms").empty();
    unitDropdown.append($("<option>").val("").text("--Select--"));

    $.get(uomListApiUrl, function (units) {
        $.each(units, function (index, unit) {
            unitDropdown.append(
                $("<option>").val(unit.uom_id).text(unit.uom_name)
            );
        });

        var selectedUnit = productModal.data("selectedUnit");
        unitDropdown.val(selectedUnit || "");
        $("#saveProduct").prop("disabled", false);
    });
});