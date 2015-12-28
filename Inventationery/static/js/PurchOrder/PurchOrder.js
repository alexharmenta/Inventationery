/* 
 * @Author: Alex
 * @Date:   2015-12-22 19:23:28
 * @Last Modified by:   Alex
 * @Last Modified time: 2015-12-27 16:29:21
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
    var purch_enabled; // Purchase Enabled Form
    /* ----- Local Variables ----- */

    /* ----- INITIALIZE VALUES ----- */
    // Purchline formset
    $('#PurchOrderForm tbody tr').formset({ // Initialize django-formset plugin
        prefix: 'plfs',
        formCssClass: 'purchline-formset',
        addText: 'Agregar artículo',
        deleteText: ' X ',
        addCssClass: 'btn btn-success btn-xs add-row',
        deleteCssClass: 'btn btn-danger btn-xs del-row',
    });
    // Set Totals from init
    SetAmounts(true);
    // Enable/Disable purchase lines on load if status is REC
    ChangePurchaseStatus($('#id_PurchStatus').val());
    /* ----- INITIALIZE VALUES ----- */

    /* ----- Purchase Order Functions ----- */
    // Get purchase order vendor info with AJAX
    $('#id_Vendor').on('change', function() {
        var Vendor_pk = $('#id_Vendor option:selected').val(); // Selected vendor pk
        // AJAX Code for retrieving data from vendor
        csrftoken = getCookie('csrftoken'); // Always get the CSRFTOKEN
        $.ajax({
            url: window.location.href, // the endpoint,commonly same url
            type: "POST", // data sent with the post request
            //Dictionary send to django view as JSON
            data: {
                action: 'get_purch_data', // Action to execute on view
                Vendor_pk: Vendor_pk, // Vendor Primary Key to get data
                csrfmiddlewaretoken: csrftoken, // CSRFTOKEN
            },
            // handle a successful response
            success: function(data) {
                //This will execute when where Django code returns a dictionary called 'data' back to us.
                $('#OneTimeVendor').prop('checked', data.OneTimeVendor);
                $("#VATNum").val(data.VATNum);
                $("#id_WorkerPurchPlacer").val(data.NameAlias);
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
    // Get purchase line info with AJAX
    $('.purchline_formset').on('change', 'tr td select,input', function() {
        var id = $(this).attr('id');
        var id_lower = id.toLowerCase()
        var rownum = id.replace(/\D/g, '');
        var ItemName_id = '#id_plfs-' + rownum + '-ItemName'
        var PurchUnit_id = '#id_plfs-' + rownum + '-PurchUnit'
        var PurchPrice_id = '#id_plfs-' + rownum + '-PurchPrice'
        var PurchQty_id = '#id_plfs-' + rownum + '-PurchQty'
        var LineDisc_id = '#id_plfs-' + rownum + '-LineDisc'
        var LinePercent_id = '#id_plfs-' + rownum + '-LinePercent'
        var Total_id = '#id_plfs-' + rownum + '-LineAmount'

        if (id_lower.indexOf('itemid') != -1) {
            var Item_pk = getCharsBefore($('#' + id + ' option:selected').val(), ' ');
            var Item_pk = $('#' + id + ' option:selected').val();
            // AJAX Code for retrieving data from vendor
            csrftoken = getCookie('csrftoken');

            $.ajax({
                url: window.location.href, // the endpoint,commonly same url
                type: "POST", // data sent with the post request
                //Dictionary send to django view as JSON
                data: {
                    action: 'get_purchline_data', // Action to execute on view
                    Item_pk: Item_pk, // Item Primary Key to get data
                    csrfmiddlewaretoken: csrftoken, // CSRFTOKEN
                },
                // handle a successful response
                success: function(data) {
                    console.log(data);
                    //This will execute when where Django code returns a dictionary called 'data' back to us.
                    $(ItemName_id).val(data.ItemName);
                    $(PurchUnit_id).val(data.UnitId);
                    $(PurchPrice_id).val(data.VendorPrice);
                },
                // handle a non-successful response
                error: function(xhr, errmsg, err) {
                    console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
                    notie.alert(3, 'El servidor no responde.', 1.5);
                }
            });
        }
        // Calc data from purch lines
        qty = $(PurchQty_id).val();
        price = $(PurchPrice_id).val();
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

    // Set balance on Paid change
    $('#id_Paid').on('change', function() {
        SetBalance();
        if ($('#id_Paid').val() == 0 || !$('#id_Paid').val()) {
            EnablePurchLines(true);
        }
        ChangePurchaseStatus('OPE');
    });

    // Enable/Disable purch order on click
    $('#cancel_order_btn').on('click', function(event) {
        event.preventDefault();

        var formData = $('#PurchOrderForm').serialize(); // Serialized form data
        var action = '&action=update_enabled'; //Action to execute on Django View
        // Check purchase status
        if ($('#id_Enabled').is(':checked')) { // Set checkbox to boolean value
            purch_enabled = true;
        } else {
            purch_enabled = false;
        }
        switch ($('#id_DocumentState').val()) {
            case 'Abierto':
                // Set value to the view as serialized string
                purch_enabled = '&purch_enabled=' + (purch_enabled).toString();
                $.ajax({
                    url: window.location.href, // the endpoint,commonly same url
                    type: "POST",
                    data: formData + action + purch_enabled, // data sent with the post request
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
                        ChangePurchaseStatus(json.PurchStatus);
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
                        text: 'Reabrir el pedido completo suspenderá todos los movimientos de inventario y los registros de pago',
                        type: 'warning',
                        showCancelButton: true,
                        confirmButtonColor: '#3085d6',
                        cancelButtonColor: '#d33',
                        confirmButtonText: 'Aceptar',
                        closeOnConfirm: true,
                    },
                    function() {
                        // Set value to the view as serialized string
                        purch_enabled = '&purch_enabled=' + (purch_enabled).toString();
                        $.ajax({
                            url: window.location.href, // the endpoint,commonly same url
                            type: "POST",
                            data: formData + action + purch_enabled, // data sent with the post request
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
                                ChangePurchaseStatus(json.PurchStatus);
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
                        text: 'Reabrir el pedido completo suspenderá todos los movimientos de inventario y los registros de pago',
                        type: 'warning',
                        showCancelButton: true,
                        confirmButtonColor: '#3085d6',
                        cancelButtonColor: '#d33',
                        confirmButtonText: 'Aceptar',
                        closeOnConfirm: true,
                    },
                    function() {
                        // Set value to the view as serialized string
                        purch_enabled = '&purch_enabled=' + (purch_enabled).toString();
                        $.ajax({
                            url: window.location.href, // the endpoint,commonly same url
                            type: "POST",
                            data: formData + action + purch_enabled, // data sent with the post request
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
                                ChangePurchaseStatus(json.PurchStatus);
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
    //Pay
    $('#pay_order').on('click', function(event) {
        event.preventDefault();
        if ($('#id_PurchStatus').val() != 'PAI' && $('#id_PurchStatus').val() != 'RPA' && $('#id_PurchStatus').val() != 'CAN') {
            swal({
                    title: 'Se pagará un total de: ' + getPurchTotal(),
                    type: 'warning',
                    showCancelButton: true,
                    confirmButtonColor: '#3085d6',
                    cancelButtonColor: '#d33',
                    confirmButtonText: 'Si, pagar!',
                    closeOnConfirm: false,
                },
                function() {
                    // var csrftoken = getCookie('csrftoken'); Not necesary through serialization
                    // Current form values
                    var PaidAmount = parseFloat($('#id_Paid').val());
                    var BalanceAmount = parseFloat($('#id_Balance').val());
                    var TotalAmount = parseFloat($('#id_Total').val());
                    // Change values to send form
                    PayPurchOrder();
                    var formData = $('#PurchOrderForm').serialize(); // Serialized form data
                    var action = '&action=pay_order'; //Action to execute on Django View
                    $.ajax({
                        url: window.location.href, // the endpoint,commonly same url
                        type: "POST",
                        data: formData + action,
                        // handle a successful response
                        success: function(data) {
                            swal(
                                'Orden de compra pagada',
                                'Correcto',
                                'success'
                            );
                            // Actions when order is Paid
                            ChangePurchaseStatus(data.PurchStatus); // Change status function
                        },
                        // handle a non-successful response
                        error: function(xhr, errmsg, err) {
                            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
                            swal("Error al cancelar pedido", "La información del pedido no se ha modificado", "error");
                            $('#id_Paid').val(PaidAmount); // Restore Paid    
                            $('#id_Balance').val(BalanceAmount); // Restore Balance
                            $('#id_Total').val(TotalAmount); // Restore Total
                        }
                    });
                });
        } else {
            swal({
                title: "La orden de compra ya está pagada ó cancelada",
                text: "",
                type: 'info',
                timer: 3000,
                showConfirmButton: true,
            });
        }
    });
    //Receive and pay
    $('#receive_pay').on('click', function(event) {
        event.preventDefault();
        if ($('#id_PurchStatus').val() != 'REC' && $('#id_PurchStatus').val() != 'RPA' && $('#id_PurchStatus').val() != 'CAN') {
            swal({
                    title: 'Se pagará un total de: ' + getPurchTotal(),
                    text: 'Recibirá ' + getTotalItems().toString() + ' artículos',
                    type: 'warning',
                    showCancelButton: true,
                    confirmButtonColor: '#3085d6',
                    cancelButtonColor: '#d33',
                    confirmButtonText: 'Si, pagar!',
                    closeOnConfirm: false
                },
                function() {
                    // var csrftoken = getCookie('csrftoken'); Not necesary through serialization
                    // Change values to send form
                    var PaidAmount = parseFloat($('#id_Paid').val());
                    var BalanceAmount = parseFloat($('#id_Balance').val());
                    var TotalAmount = parseFloat($('#id_Total').val());

                    PayPurchOrder();

                    var formData = $('#PurchOrderForm').serialize(); // Serialized form data
                    var action = '&action=receive_pay'; //Action to execute on Django View

                    $.ajax({
                        url: window.location.href, // the endpoint,commonly same url
                        type: "POST",
                        data: formData + action,
                        // handle a successful response
                        success: function(data) {
                            //On success show the data posted to server as a message
                            swal(
                                'Orden de compra pagada',
                                'Recibió ' + getTotalItems().toString() + ' artículos',
                                'success'
                            );
                            ChangePurchaseStatus(data.PurchStatus);
                        },
                        // handle a non-successful response
                        error: function(xhr, errmsg, err) {
                            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
                            swal("Error al cancelar pedido", "La información del pedido no se ha modificado", "error")
                            $('#id_Paid').val(PaidAmount); // Restore Paid    
                            $('#id_Balance').val(BalanceAmount); // Restore Balance
                            $('#id_Total').val(TotalAmount); // Restore Total
                            $('#id_PurchStatus').val(PurchStatus).change();
                        }

                    });
                });
        } else {
            swal({
                title: "Pedido recibido y pagado ó cancelado",
                text: "",
                type: 'info',
                timer: 3000,
                showConfirmButton: true,
            });
        }
    });
    //Receive
    $('#receive_invent').on('click', function(event) {
        event.preventDefault();
        if ($('#id_PurchStatus').val() != 'REC' && $('#id_PurchStatus').val() != 'RPA' && $('#id_PurchStatus').val() != 'CAN') { // Prevent receiving again
            swal({
                    title: 'Se recibirá completamente la orden de compra, no se pagará ningún monto',
                    text: 'Recibirá un total de ' + getTotalItems().toString() + ' artículos',
                    type: 'warning',
                    showCancelButton: true,
                    confirmButtonColor: '#3085d6',
                    cancelButtonColor: '#d33',
                    confirmButtonText: 'Si, recibir!',
                    closeOnConfirm: false
                },
                function() {
                    var formData = $('#PurchOrderForm').serialize(); // Serialized form data
                    var action = '&action=receive'; //Action to execute on Django View

                    $.ajax({
                        url: window.location.href, // the endpoint,commonly same url
                        type: "POST",
                        data: formData + action,
                        // handle a successful response
                        success: function(data) {
                            //On success show the data posted to server as a message
                            swal(
                                'Orden de compra recibida',
                                'Recibió ' + getTotalItems().toString() + ' artículos',
                                'success'
                            );
                            ChangePurchaseStatus(data.PurchStatus);
                        },
                        // handle a non-successful response
                        error: function(xhr, errmsg, err) {
                            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
                            swal("Error al recibir pedido", "La información del pedido no se ha modificado", "error");
                        }

                    });
                });
        } else {
            swal({
                title: "Pedido recibido ó cancelado",
                text: "",
                type: 'info',
                timer: 3000,
                showConfirmButton: true,
            });
        }
    });

    /* ----- Purchase Order Functions ----- */

});

/* ----- GLOBAL FUNCTIONS ----- */
/* ----- Amounts and counting functions section ----- */
// Set totals in PO
function SetAmounts(setBalance) {
    $('#id_SubTotal').val(getPurchTotal());
    $('#id_Total').val(getPurchTotal());
    if (setBalance) {
        SetBalance();
    }
}
// Get total items in PO items
function getTotalItems() {
    var total = 0;
    $('.pl_qty').each(function(index, el) {
        if ($(this).val() != '') {
            total += parseFloat($(this).val());
        }
    });

    return parseFloat(total).toFixed(2);
}
// Get Purch Total
function getPurchTotal() {
    var total = 0;
    $('.total_amount').each(function(index) {
        if ($(this).val()) {
            total += parseFloat($(this).val());
        }
    });
    return total.toFixed(2);
}
// Pay Purchase Order Total
function PayPurchOrder() {
    $('#id_Paid').val(getPurchTotal());
    SetBalance();
}
// Get paid
function getPaid() {
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
    var balance = (getPurchTotal() - getPaid()).toFixed(2);
    $('#id_Balance').val(balance);
}
/* ----- Amount functions section ----- */

/* ----- Status control section ----- */
function ChangePurchaseStatus(status) {
    switch (status) {
        case 'PAI':
            $('#id_PurchStatus').val('PAI').change();
            $('#id_DocumentState').val('Proceso').change();
            EnableForm('PurchOrderForm', true);
            EnablePurchLines(false);
            $('#delPurchOrderBtn').hide();
            $('#id_Enabled').prop('checked', true);
            break;
        case 'REC':
            $('#id_PurchStatus').val('REC').change();
            $('#id_DocumentState').val('Proceso').change();
            EnableForm('PurchOrderForm', true);
            EnablePurchLines(false);
            $('#delPurchOrderBtn').hide();
            $('#id_Enabled').prop('checked', true);
            break;
        case 'RPA':
            $('#id_PurchStatus').val('RPA').change();
            $('#id_DocumentState').val('Cerrado').change();
            EnableForm('PurchOrderForm', false);
            EnablePurchLines(false);
            $('#delPurchOrderBtn').hide();
            $('#id_Enabled').prop('checked', false);
            break;
        case 'OPE':
            $('#id_PurchStatus').val('OPE').change();
            $('#id_DocumentState').val('Abierto').change();
            EnableForm('PurchOrderForm', true);
            $('#delPurchOrderBtn').show();
            EnablePurchLines(true);
            $('#id_Enabled').prop('checked', true);
            break;
        case 'CAN':
            $('#id_PurchStatus').val('CAN').change();
            $('#id_DocumentState').val('Cerrado').change();
            EnableForm('PurchOrderForm', false);
            EnablePurchLines(false);
            $('#delPurchOrderBtn').show();
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
function EnablePurchLines(enable) {
    if (enable) {
        $('#item_action_h').show();
        $('.del-row').show();
        $('.add-row').show();
        $('#purchline_table tr :input').each(function() {
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
        $('#purchline_table tr :input').each(function() {
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
    $('.pl_disc').each(function(index) {
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
