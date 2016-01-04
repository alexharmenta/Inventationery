/* 
 * @Author: Alex
 * @Date:   2015-12-22 19:23:28
 * @Last Modified by:   Alex
 * @Last Modified time: 2016-01-03 20:33:52
 */

'use strict';
$(document).ready(function() {
    /* ----- Local Variables ----- */
    var csrftoken = '';
    var qty;
    var price;
    var disc;
    var percent;
    var total = 0;
    var LineAmount = 0.00;
    var sales_enabled; // Sales Enabled Form
    var SalesId = $('#id_SalesId').val();
    /* ----- Local Variables ----- */
    
    /* ----- INITIALIZE VALUES ----- */
    // Salesline formset
    $('#SalesOrderForm tbody tr').formset({ // Initialize django-formset plugin
        prefix: 'slfs',
        formCssClass: 'salesline-formset',
        addText: 'Agregar artículo',
        deleteText: ' X ',
        addCssClass: 'btn btn-success btn-xs add-row',
        deleteCssClass: 'btn btn-danger btn-xs del-row',
    });
    // Set Totals from init
    SetAmounts(true);
    // Enable/Disable sales lines on load if status is RED
    ChangeSalesStatus($('#id_SalesStatus').val());
    /* ----- INITIALIZE VALUES ----- */

    /* ----- Sales Order Functions ----- */
    // Get sales order customer info with AJAX
    $('#id_Customer').on('change', function() {
        var Customer_pk = $('#id_Customer option:selected').val(); // Selected customer pk
        // AJAX Code for retrieving data from customer
        csrftoken = getCookie('csrftoken'); // Always get the CSRFTOKEN
        $.ajax({
            url: window.location.href, // the endpoint,commonly same url
            type: "POST", // data sent with the post request
            //Dictionary send to django view as JSON
            data: {
                action: 'get_sales_data', // Action to execute on view
                Customer_pk: Customer_pk, // Customer Primary Key to get data
                csrfmiddlewaretoken: csrftoken, // CSRFTOKEN
            },
            // handle a successful response
            success: function(data) {
                //This will execute when where Django code returns a dictionary called 'data' back to us.
                $('#OneTimeCustomer').prop('checked', data.OneTimeCustomer);
                $("#VATNum").val(data.VATNum);
                $("#id_WorkerSalesPlacer").val(data.NameAlias);
                $("#id_CurrencyCode").val(data.CurrencyCode);
                $("#id_LanguageCode").val(data.LanguageCode);
                $("#id_DeliveryName").val(data.DeliveryName);
                $("#id_DeliveryContact").val(data.DeliveryContact);
            },
            // handle a non-successful response
            error: function(xhr, errmsg, err) {
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
                notie.alert(3, 'El servidor no responde.', 1.5);
            }
        });
    });
    // Get sales line info with AJAX
    $('.salesline_formset').on('change', 'tr td select,input', function() {
        var id = $(this).attr('id');
        var id_lower = id.toLowerCase()
        var rownum = id.replace(/\D/g, '');
        var ItemName_id = '#id_slfs-' + rownum + '-ItemName'
        var SalesUnit_id = '#id_slfs-' + rownum + '-SalesUnit'
        var SalesPrice_id = '#id_slfs-' + rownum + '-SalesPrice'
        var SalesQty_id = '#id_slfs-' + rownum + '-SalesQty'
        var LineDisc_id = '#id_slfs-' + rownum + '-LineDisc'
        var LinePercent_id = '#id_slfs-' + rownum + '-LinePercent'
        var Total_id = '#id_slfs-' + rownum + '-LineAmount'

        if (id_lower.indexOf('itemid') != -1) {
            var Item_pk = getCharsBefore($('#' + id + ' option:selected').val(), ' ');
            var Item_pk = $('#' + id + ' option:selected').val();
            // AJAX Code for retrieving data from customer
            csrftoken = getCookie('csrftoken');

            $.ajax({
                url: window.location.href, // the endpoint,commonly same url
                type: "POST", // data sent with the post request
                //Dictionary send to django view as JSON
                data: {
                    action: 'get_salesline_data', // Action to execute on view
                    Item_pk: Item_pk, // Item Primary Key to get data
                    csrfmiddlewaretoken: csrftoken, // CSRFTOKEN
                },
                // handle a successful response
                success: function(data) {
                    //This will execute when where Django code returns a dictionary called 'data' back to us.
                    $(ItemName_id).val(data.ItemName);
                    $(SalesUnit_id).val(data.UnitId);
                    $(SalesPrice_id).val(data.SalesPrice);
                },
                // handle a non-successful response
                error: function(xhr, errmsg, err) {
                    console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
                    notie.alert(3, 'El servidor no responde.', 1.5);
                }
            });
        }
        // Calc data from sales lines
        qty = $(SalesQty_id).val();
        price = $(SalesPrice_id).val();
        disc = $(LineDisc_id).val();
        percent = $(LinePercent_id).val();
        total = $(Total_id).val();
        if (id_lower.indexOf('disc') != -1) { // Enable/Disable percent if disc
            if (disc) {
                $(LinePercent_id).prop('readonly', true);
            } else {
                $(LinePercent_id).prop('readonly', false);
            }
        } else if (id_lower.indexOf('percent') != -1) { // Enable/Disable disc if percent
            if (percent) {
                $(LineDisc_id).prop('readonly', true);
            } else {
                $(LineDisc_id).prop('readonly', false);
            }
        }

        // Calc discounts
        if (qty && price) {
            if (disc && !percent) {
                total = (qty * price) - disc;
            } else if (!disc && percent) {
                total = qty * price;
                percent = total * (percent / 100);
                total = total - percent;
            } else {
                total = qty * price;
            }
        } else {
            total = 0;
        }
        // Set line Total
        total = parseFloat(total).toFixed(2);
        $(Total_id).val(total);
        SetAmounts(true);
    });
    // Set tooltip info
    $('.salesline_formset').on('focus change', 'tr td select,input', function() {
        var id = $(this).attr('id');
        var element = $(this);
        if (id.indexOf('SalesQty') != -1) {
            csrftoken = getCookie('csrftoken');
            var item_id = $(this).parent().parent().find("td:first").children('select').attr('id');
            var item_pk = $('#'+item_id+' option:selected').val();
            var location = $('#id_Location').val();
            $.ajax({
                url: window.location.href, // the endpoint,commonly same url
                type: "POST",
                data: {
                    item_pk: item_pk,
                    location: location,
                    sl_qty: element.val(),
                    SalesId, SalesId,
                    csrfmiddlewaretoken: csrftoken,
                    action: 'get_invent',
                }, // data sent with the post request
                // handle a successful response
                success: function(data) {
                    //console.log(data); // another sanity check
                    //On success show the data posted to server as a message
                    $('#item_info').text(data.item);
                    $('#location_info').text(data.location);
                    $('#stock_info').text(data.on_stock);
                    $('#available_info').text(data.available);
                    $('#reserved_info').text(data.reserved);
                    if(data.available < 0) {
                        swal({
                            title: "Sin stock suficiente para cumplir con todos los pedidos",
                            text: "Realice una orden de compra para cumplir con la capacidad de venta",
                            type: 'warning',
                            showConfirmButton: true,
                        });
                        element.val(0);
                    }

                },

                // handle a non-successful response
                error: function(xhr, errmsg, err) {
                    console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
                    //swal("Error al cancelar pedido", "La información del pedido no se ha modificado", "error")
                }
            });
            
        }
    });
    // Set balance on Cashed change
    $('#id_Paid').on('change', function() {
        SetBalance();
        if ($('#id_Paid').val() == 0 || !$('#id_Paid').val()) {
            EnableSalesLines(true);
        }
        ChangeSalesStatus('OPE');
    });
    // Apply discount to saleslines
    $('#apply_discount').on('click', function() {
        if ($('#id_SalesStatus').val() != 'CAS' && $('#id_SalesStatus').val() != 'RCA' && $('#id_SalesStatus').val() != 'CAN') {
            var customer_pk = $('#id_Customer option:selected').val();
            csrftoken = getCookie('csrftoken');
            $.ajax({
                url: window.location.href, // the endpoint,commonly same url
                type: "POST",
                data: {
                    customer_pk: customer_pk,
                    csrfmiddlewaretoken: csrftoken,
                    action: 'get_customer_discount',
                },
                // handle a successful response
                success: function(data) {
                    $('.sl_percent').each(function() {
                        var itemId = $('td:first', $(this).parents('tr')).find('select').attr('id');
                        if($('#' + itemId + ' option:selected').val()) {
                            $(this).val(data.discount).change();
                        }
                    });
                    $('#id_Paid').val(0);
                    SetBalance();
                },
                // handle a non-successful response
                error: function(xhr, errmsg, err) {
                    console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
                    swal('Error','El servidor no responde','error');
                }

            });
        } else {
            swal({
                title: "Pedido cobrado ó cancelado",
                text: "",
                type: 'info',
                timer: 3000,
                showConfirmButton: true,
            });
        }
    });
    // Enable/Disable sales order on click
    $('#cancel_order_btn').on('click', function(event) {
        event.preventDefault();

        var formData = $('#SalesOrderForm').serialize(); // Serialized form data
        var action = '&action=update_enabled'; //Action to execute on Django View
        // Check sales status
        if ($('#id_Enabled').is(':checked')) { // Set checkbox to boolean value
            sales_enabled = true;
        } else {
            sales_enabled = false;
        }
        switch ($('#id_DocumentState').val()) {
            case 'Abierto':
                // Set value to the view as serialized string
                sales_enabled = '&sales_enabled=' + (sales_enabled).toString();
                $.ajax({
                    url: window.location.href, // the endpoint,commonly same url
                    type: "POST",
                    data: formData + action + sales_enabled, // data sent with the post request
                    // handle a successful response
                    success: function(json) {
                        //console.log(json); // another sanity check
                        //On success show the data posted to server as a message
                        $('#id_Enabled').prop('checked', json.Enabled);
                        if (!json.Enabled) {
                            notie.alert(2, 'Pedido cancelado.', 1.5);
                        } else {
                            notie.alert(4, 'Pedido abierto.', 1.5);
                        }
                        $('#id_Paid').val(0);
                        SetBalance();
                        ChangeSalesStatus(json.SalesStatus);
                    },

                    // handle a non-successful response
                    error: function(xhr, errmsg, err) {
                        console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
                        swal("Error al cancelar pedido", "La información del pedido no se ha modificado", "error")
                    }

                });
                break;
            case 'Proceso':
                swal({
                        title: 'Abrir pedido',
                        text: 'Reabrir el pedido completo suspenderá todos los movimientos de inventario y los registros de cobro',
                        type: 'warning',
                        showCancelButton: true,
                        confirmButtonColor: '#3085d6',
                        cancelButtonColor: '#d33',
                        confirmButtonText: 'Aceptar',
                        closeOnConfirm: true,
                    },
                    function() {
                        // Set value to the view as serialized string
                        sales_enabled = '&sales_enabled=' + (sales_enabled).toString();
                        $.ajax({
                            url: window.location.href, // the endpoint,commonly same url
                            type: "POST",
                            data: formData + action + sales_enabled, // data sent with the post request
                            // handle a successful response
                            success: function(json) {
                                //console.log(json); // another sanity check
                                //On success show the data posted to server as a message
                                $('#id_Enabled').prop('checked', json.Enabled);
                                if (!json.Enabled) {
                                    notie.alert(2, 'Pedido cancelado.', 1.5);
                                } else {
                                    notie.alert(4, 'Pedido abierto.', 1.5);
                                }
                                $('#id_Paid').val(0);
                                SetBalance();
                                ChangeSalesStatus(json.SalesStatus);
                            },
                            // handle a non-successful response
                            error: function(xhr, errmsg, err) {
                                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
                                swal("Error al cancelar pedido", "La información del pedido no se ha modificado", "error")
                            }
                        });
                    });
                break;
            case 'Cerrado':
                swal({
                        title: 'Abrir pedido',
                        text: 'Reabrir el pedido completo suspenderá todos los movimientos de inventario y los registros de cobro',
                        type: 'warning',
                        showCancelButton: true,
                        confirmButtonColor: '#3085d6',
                        cancelButtonColor: '#d33',
                        confirmButtonText: 'Aceptar',
                        closeOnConfirm: true,
                    },
                    function() {
                        // Set value to the view as serialized string
                        sales_enabled = '&sales_enabled=' + (sales_enabled).toString();
                        $.ajax({
                            url: window.location.href, // the endpoint,commonly same url
                            type: "POST",
                            data: formData + action + sales_enabled, // data sent with the post request
                            // handle a successful response
                            success: function(json) {
                                //console.log(json); // another sanity check
                                //On success show the data posted to server as a message
                                $('#id_Enabled').prop('checked', json.Enabled);
                                if (!json.Enabled) {
                                    notie.alert(2, 'Pedido cancelado.', 1.5);
                                } else {
                                    notie.alert(4, 'Pedido abierto.', 1.5);
                                }
                                $('#id_Paid').val(0);
                                SetBalance();
                                ChangeSalesStatus(json.SalesStatus);
                            },
                            // handle a non-successful response
                            error: function(xhr, errmsg, err) {
                                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
                                swal("Error al cancelar pedido", "La información del pedido no se ha modificado", "error")
                            }
                        });
                    });
                break;
        }
    });
    //Charge
    $('#charge_order').on('click', function(event) {
        event.preventDefault();
        if ($('#id_SalesStatus').val() != 'CAS' && $('#id_SalesStatus').val() != 'RCA' && $('#id_SalesStatus').val() != 'CAN') {
            swal({
                    title: 'Se cobrará un total de: ' + getSalesTotal(),
                    type: 'warning',
                    showCancelButton: true,
                    confirmButtonColor: '#3085d6',
                    cancelButtonColor: '#d33',
                    confirmButtonText: 'Si, cobrar!',
                    closeOnConfirm: false,
                },
                function() {
                    // var csrftoken = getCookie('csrftoken'); Not necesary through serialization
                    // Current form values
                    var CashedAmount = parseFloat($('#id_Paid').val());
                    var BalanceAmount = parseFloat($('#id_Balance').val());
                    var TotalAmount = parseFloat($('#id_Total').val());
                    // Change values to send form
                    ChargeSalesOrder();
                    var formData = $('#SalesOrderForm').serialize(); // Serialized form data
                    var action = '&action=charge_order'; //Action to execute on Django View
                    $.ajax({
                        url: window.location.href, // the endpoint,commonly same url
                        type: "POST",
                        data: formData + action,
                        // handle a successful response
                        success: function(data) {
                            swal(
                                'Orden de venta cobrada',
                                'Correcto',
                                'success'
                            );
                            // Actions when order is Cashed
                            ChangeSalesStatus(data.SalesStatus); // Change status function
                        },
                        // handle a non-successful response
                        error: function(xhr, errmsg, err) {
                            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
                            swal("Error al cancelar pedido", "La información del pedido no se ha modificado", "error");
                            $('#id_Paid').val(CashedAmount); // Restore Cashed    
                            $('#id_Balance').val(BalanceAmount); // Restore Balance
                            $('#id_Total').val(TotalAmount); // Restore Total
                        }
                    });
                });
        } else {
            swal({
                title: "La orden de venta ya está cobrada ó cancelada",
                text: "",
                type: 'info',
                timer: 3000,
                showConfirmButton: true,
            });
        }
    });
    //Reduce and charge
    $('#reduce_charge').on('click', function(event) {
        event.preventDefault();
        if ($('#id_SalesStatus').val() != 'RED' && $('#id_SalesStatus').val() != 'RCA' && $('#id_SalesStatus').val() != 'CAN') {
            if(GetItemsAvailable()) {
                swal({
                        title: 'Se cobrará un total de: ' + getSalesTotal(),
                        text: 'Reducirá ' + getTotalItems().toString() + ' artículos',
                        type: 'warning',
                        showCancelButton: true,
                        confirmButtonColor: '#3085d6',
                        cancelButtonColor: '#d33',
                        confirmButtonText: 'Si, cobrar!',
                        closeOnConfirm: false
                    },
                    function() {
                        // var csrftoken = getCookie('csrftoken'); Not necesary through serialization
                        // Change values to send form
                        var CashedAmount = parseFloat($('#id_Paid').val());
                        var BalanceAmount = parseFloat($('#id_Balance').val());
                        var TotalAmount = parseFloat($('#id_Total').val());

                        ChargeSalesOrder();

                        var formData = $('#SalesOrderForm').serialize(); // Serialized form data
                        var action = '&action=reduce_charge'; //Action to execute on Django View

                        $.ajax({
                            url: window.location.href, // the endpoint,commonly same url
                            type: "POST",
                            data: formData + action,
                            // handle a successful response
                            success: function(data) {
                                //On success show the data posted to server as a message
                                swal(
                                    'Orden de venta cobrada',
                                    'Redujo ' + getTotalItems().toString() + ' artículos',
                                    'success'
                                );
                                ChangeSalesStatus(data.SalesStatus);
                            },
                            // handle a non-successful response
                            error: function(xhr, errmsg, err) {
                                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
                                swal("Error al cancelar pedido", "La información del pedido no se ha modificado", "error");
                                $('#id_Paid').val(CashedAmount); // Restore Cashed    
                                $('#id_Balance').val(BalanceAmount); // Restore Balance
                                $('#id_Total').val(TotalAmount); // Restore Total
                                $('#id_SalesStatus').val(SalesStatus).change();
                            }

                        });
                    });
            } else {
                swal({
                    title: "Sin stock suficiente para cumplir con todos los pedidos",
                    text: "Realice una orden de compra para cumplir con la capacidad de venta",
                    type: 'warning',
                    showConfirmButton: true,
                });
            }
        } else {
            swal({
                title: "Pedido reducido y cobrado ó cancelado",
                text: "",
                type: 'info',
                timer: 3000,
                showConfirmButton: true,
            });
        }
    });
    //Reduce
    $('#reduce_invent').on('click', function(event) {
        event.preventDefault();
        if ($('#id_SalesStatus').val() != 'RED' && $('#id_SalesStatus').val() != 'RCA' && $('#id_SalesStatus').val() != 'CAN') { // Prevent receiving again
            if(GetItemsAvailable()) {
                swal({
                        title: 'Se reducirá completamente la orden de venta, no se cobrará ningún monto',
                        text: 'Reducirá un total de ' + getTotalItems().toString() + ' artículos',
                        type: 'warning',
                        showCancelButton: true,
                        confirmButtonColor: '#3085d6',
                        cancelButtonColor: '#d33',
                        confirmButtonText: 'Si, reducir!',
                        closeOnConfirm: false
                    },
                    function() {
                        var formData = $('#SalesOrderForm').serialize(); // Serialized form data
                        var action = '&action=reduce'; //Action to execute on Django View

                        $.ajax({
                            url: window.location.href, // the endpoint,commonly same url
                            type: "POST",
                            data: formData + action,
                            // handle a successful response
                            success: function(data) {
                                //On success show the data posted to server as a message
                                swal(
                                    'Orden de venta recibida',
                                    'Redujo ' + getTotalItems().toString() + ' artículos',
                                    'success'
                                );
                                ChangeSalesStatus(data.SalesStatus);
                            },
                            // handle a non-successful response
                            error: function(xhr, errmsg, err) {
                                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
                                swal("Error al reducir pedido", "La información del pedido no se ha modificado", "error");
                            }

                        });
                    });
            } else {
                swal({
                    title: "Sin stock suficiente para cumplir con todos los pedidos",
                    text: "Realice una orden de compra para cumplir con la capacidad de venta",
                    type: 'warning',
                    showConfirmButton: true,
                });
            }            
        } else {
            swal({
                title: "Pedido reducido ó cancelado",
                text: "",
                type: 'info',
                timer: 3000,
                showConfirmButton: true,
            });
        }
    });

    /* ----- Sales Order Functions ----- */
    /* ----- Fill info selects Functions ----- */
    $('#id_Customer').on('focus', function(){
        var element = document.getElementById('id_Customer');;
        csrftoken = getCookie('csrftoken');
        $.ajax({
            url: window.location.href, // the endpoint,commonly same url
            type: "POST",
            dataType: 'json',
            data: {
                csrfmiddlewaretoken: csrftoken,
                action: 'get_customers',
            }, // data sent with the post request
            // handle a successful response
            success: function(data) {
                //console.log(json); // another sanity check
                //On success show the data posted to server as a message
                element.options.length = 0;
                element.options.add(new Option("---------", ''));
                $.each(JSON.parse(data), function(idx) {
                    var pk = JSON.parse(data)[idx].pk;
                    var value = JSON.parse(data)[idx].fields.AccountNum;
                    element.options.add(new Option(value, pk));
                });
            },
            // handle a non-successful response
            error: function(xhr, errmsg, err) {
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
                swal("Error al cancelar pedido", "La información del pedido no se ha modificado", "error")
            }
        });
    });
    $('#id_Payment').on('focus', function(){
        var element = document.getElementById('id_Payment');;
        csrftoken = getCookie('csrftoken');
        $.ajax({
            url: window.location.href, // the endpoint,commonly same url
            type: "POST",
            dataType: 'json',
            data: {
                csrfmiddlewaretoken: csrftoken,
                action: 'get_payments',
            }, // data sent with the post request
            // handle a successful response
            success: function(data) {
                //console.log(json); // another sanity check
                //On success show the data posted to server as a message
                element.options.length = 0;
                element.options.add(new Option("---------", ''));
                $.each(JSON.parse(data), function(idx) {
                    var pk = JSON.parse(data)[idx].pk;
                    var value = JSON.parse(data)[idx].fields.PaymName;
                    element.options.add(new Option(value, pk));
                });
            },
            // handle a non-successful response
            error: function(xhr, errmsg, err) {
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
                swal("Error al cancelar pedido", "La información del pedido no se ha modificado", "error")
            }
        });
    });
    $('#id_PaymMode').on('focus', function(){
        var element = document.getElementById('id_PaymMode');;
        csrftoken = getCookie('csrftoken');
        $.ajax({
            url: window.location.href, // the endpoint,commonly same url
            type: "POST",
            dataType: 'json',
            data: {
                csrfmiddlewaretoken: csrftoken,
                action: 'get_paymmodes',
            }, // data sent with the post request
            // handle a successful response
            success: function(data) {
                //console.log(json); // another sanity check
                //On success show the data posted to server as a message
                element.options.length = 0;
                element.options.add(new Option("---------", ''));
                $.each(JSON.parse(data), function(idx) {
                    var pk = JSON.parse(data)[idx].pk;
                    var value = JSON.parse(data)[idx].fields.PaymModeName;
                    element.options.add(new Option(value, pk));
                });
            },
            // handle a non-successful response
            error: function(xhr, errmsg, err) {
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
                swal("Error al cancelar pedido", "La información del pedido no se ha modificado", "error")
            }
        });
    });
    $('#id_Location').on('focus', function(){
        var element = document.getElementById('id_Location');;
        csrftoken = getCookie('csrftoken');
        $.ajax({
            url: window.location.href, // the endpoint,commonly same url
            type: "POST",
            dataType: 'json',
            data: {
                csrfmiddlewaretoken: csrftoken,
                action: 'get_locations',
            }, // data sent with the post request
            // handle a successful response
            success: function(data) {
                //console.log(json); // another sanity check
                //On success show the data posted to server as a message
                element.options.length = 0;
                element.options.add(new Option("---------", ''));
                $.each(JSON.parse(data), function(idx) {
                    var pk = JSON.parse(data)[idx].pk;
                    var value = JSON.parse(data)[idx].fields.LocationName;
                    element.options.add(new Option(value, pk));
                });
            },
            // handle a non-successful response
            error: function(xhr, errmsg, err) {
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
                swal("Error al cancelar pedido", "La información del pedido no se ha modificado", "error")
            }
        });
    });
    $('.item-id').on('focus', function(){
        var element = document.getElementById($(this).attr('id'));;
        csrftoken = getCookie('csrftoken');
        $.ajax({
            url: window.location.href, // the endpoint,commonly same url
            type: "POST",
            dataType: 'json',
            data: {
                csrfmiddlewaretoken: csrftoken,
                action: 'get_items',
            }, // data sent with the post request
            // handle a successful response
            success: function(data) {
                //console.log(json); // another sanity check
                //On success show the data posted to server as a message
                element.options.length = 0;
                element.options.add(new Option("---------", ''));
                $.each(JSON.parse(data), function(idx) {
                    var pk = JSON.parse(data)[idx].pk;
                    var value = JSON.parse(data)[idx].fields.ItemId;
                    element.options.add(new Option(value, pk));
                });
            },
            // handle a non-successful response
            error: function(xhr, errmsg, err) {
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
                swal("Error al cancelar pedido", "La información del pedido no se ha modificado", "error")
            }
        });
    });
    /* ----- Fill info selects Functions ----- */
    // Check if there's available items to sell
function GetItemsAvailable() {
    var csrftoken = getCookie('csrftoken');
    var element;
    var sl_qty;
    var id;
    var item_pk;
    var location = $('#id_Location').val();
    var CanReduce = true;
    $('.item-id').each( function(index) {
        element = $(this);
        id = element.attr('id');
        item_pk = $('#'+id+' option:selected').val();
        var SalesId = $('#id_SalesId').val();
        if (item_pk) {
            sl_qty = element.closest('td').siblings('.sl_qty').find('input').val();
            $.ajax({
                url: window.location.href, // the endpoint,commonly same url
                type: "POST",
                data: {
                    item_pk: item_pk,
                    location: location,
                    sl_qty: sl_qty,
                    SalesId, SalesId,
                    csrfmiddlewaretoken: csrftoken,
                    action: 'get_invent',
                },
                // handle a successful response
                success: function(data) {
                    if(parseInt(data.available) > 0) {
                        CanReduce = true;
                    } else {
                        CanReduce = false;
                    }
                },
                // handle a non-successful response
                error: function(xhr, errmsg, err) {
                    console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
                }

            });
        }
    });

    return CanReduce;
}
});

/* ----- GLOBAL FUNCTIONS ----- */
/* ----- Amounts and counting functions section ----- */
// Set totals in PO
function SetAmounts(setBalance) {
    $('#id_SubTotal').val(getSalesTotal());
    $('#id_Total').val(getSalesTotal());
    if (setBalance) {
        SetBalance();
    }
}
// Get total items in PO items
function getTotalItems() {
    var total = 0;
    $('.sl_qty').each(function(index, el) {
        if ($(this).val() != '') {
            total += parseFloat($(this).val());
        }
    });

    return parseFloat(total).toFixed(2);
}
// Get Sales Total
function getSalesTotal() {
    var total = 0;
    $('.total_amount').each(function(index) {
        if ($(this).val()) {
            total += parseFloat($(this).val());
        }
    });
    return total.toFixed(2);
}
// Charge Sales Order Total
function ChargeSalesOrder() {
    $('#id_Paid').val(getSalesTotal());
    SetBalance();
}
// Get paid
function getCashed() {
    if ($('#id_Paid').val() != 0 || $('#id_Paid').val()) {
        return parseFloat($('#id_Paid').val()).toFixed(2);
    }
    return 0.00;

}
// Get Balance
function getBalance() {
    var balance = 0;
    if ($('#id_Balance').val()) {
        balance = parseFloat($('#id_Balance').val());
        return balance.toFixed(2);
    }
    return balanc.toFixed(2);
}
// Set balance
function SetBalance() {
    var balance = (getSalesTotal() - getCashed()).toFixed(2);
    $('#id_Balance').val(balance);
}
/* ----- Amount functions section ----- */

/* ----- Status control section ----- */
function ChangeSalesStatus(status) {
    switch (status) {
        case 'CAS':
            $('#id_SalesStatus').val('CAS').change();
            $('#id_DocumentState').val('Proceso').change();
            EnableForm('SalesOrderForm', true);
            EnableSalesLines(false);
            $('#delSalesOrderBtn').hide();
            $('#id_Enabled').prop('checked', true);
            break;
        case 'RED':
            $('#id_SalesStatus').val('RED').change();
            $('#id_DocumentState').val('Proceso').change();
            EnableForm('SalesOrderForm', true);
            EnableSalesLines(false);
            $('#delSalesOrderBtn').hide();
            $('#id_Enabled').prop('checked', true);
            break;
        case 'RCA':
            $('#id_SalesStatus').val('RCA').change();
            $('#id_DocumentState').val('Cerrado').change();
            EnableForm('SalesOrderForm', false);
            EnableSalesLines(false);
            $('#delSalesOrderBtn').hide();
            $('#id_Enabled').prop('checked', false);
            break;
        case 'OPE':
            $('#id_SalesStatus').val('OPE').change();
            $('#id_DocumentState').val('Abierto').change();
            EnableForm('SalesOrderForm', true);
            $('#delSalesOrderBtn').show();
            EnableSalesLines(true);
            $('#id_Enabled').prop('checked', true);
            break;
        case 'CAN':
            $('#id_SalesStatus').val('CAN').change();
            $('#id_DocumentState').val('Cerrado').change();
            EnableForm('SalesOrderForm', false);
            EnableSalesLines(false);
            $('#delSalesOrderBtn').show();
            $('#id_Enabled').prop('checked', false);
            break;
    }
    if (status != 'OPE') {
        $('#cancel_order_btn').text('Reabrir pedido');
    } else {
        $('#cancel_order_btn').text('Cancelar pedido');
    }
}
// Disable Table items
function EnableSalesLines(enable) {
    if (enable) {
        $('#item_action_h').show();
        $('.del-row').show();
        $('.add-row').show();
        $('#salesline_table tr :input').each(function() {
            if (!$(this).hasClass('form_disabled')) {
                $(this).attr("readonly", false);
                if ($(this).is('select')) {
                    $(this).css('-webkit-appearance', '');
                    $(this).css('-moz-appearance', '');
                    $(this).css('text-indent', '');
                    $(this).css('text-overflow', '');
                    $(this).find('td:first select option').show();
                }
            }
        });
    } else {
        $('#item_action_h').hide();
        $('.del-row').hide();
        $('.add-row').hide();
        $('#salesline_table tr :input').each(function() {
            if (!$(this).hasClass('form_disabled')) {
                $(this).attr("readonly", true);
                if ($(this).is('select')) {
                    $(this).css('-webkit-appearance', 'none');
                    $(this).css('-moz-appearance', 'none');
                    $(this).css('text-indent', '0px');
                    $(this).css('text-overflow', '');
                    $(this).find('option').hide();
                }
            }
        });
    }
    EnableDiscounts();
}
// Block discount fields
function EnableDiscounts() {
    $('.sl_disc').each(function(index) {
        var disc = $(this);
        var percent = $(this).closest("td").next().children('input');
        if (disc.val() && !percent.val()) {
            $(percent).prop('readonly', true);
        } else if (!disc.val() && percent.val()) {
            $(disc).prop('readonly', true);
        }
    });
}
/* .---- Status control section ----- */



/* ----- LOCAL FUNCTIONS ----- */
