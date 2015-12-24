/* 
* @Author: Alex
* @Date:   2015-12-22 19:23:28
* @Last Modified by:   Alex
* @Last Modified time: 2015-12-23 23:49:45
*/

'use strict';
$(document).ready(function(){
	/* ----- Local Variables ----- */
	var csrftoken = '';
	var qty;
    var price;
    var disc;
    var percent;
    var total = 0;
    var Purch_SubTotal = 0;
    var LineAmount = 0.0;
    var purch_enabled; // Purchase Enabled Form
	/* ----- Local Variables ----- */

	/* ----- INIT VALUES ----- */

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
	SetTotals();
	// Enable/Disable discount fields
	EnableDiscounts();
    // Enable/Disable purchase lines on load if status is REC
    ChangePurchaseStatus($('#id_PurchStatus').val());
	// Enable/Disable purch order on load
    if ($('#id_Enabled').is(':checked')) {
        purch_enabled = true;
    } else {
        purch_enabled = false;
    }
    EnableForm('PurchOrderForm', purch_enabled);

	/* -------------------- */

	/* ----- Purchase Order ----- */

    // Get purchase order vendor info with AJAX
    $('#id_Vendor').on('change', function() {
        var Vendor_pk = $('#id_Vendor option:selected').val(); // Selected vendor pk
        // AJAX Code for retrieving data from vendor
        csrftoken = getCookie('csrftoken');

        $.ajax({
            url: window.location.href, // the endpoint,commonly same url
            type: "POST",
            //This is the dictionary you are SENDING to your Django code. 
            //We are sending the 'action':get_purch_data and the 'id: $Vendor_pk  
            //which is a variable that contains what account user selected
            data: {
                action: 'get_purch_data',
                Vendor_pk: Vendor_pk,
                csrfmiddlewaretoken: csrftoken,
            }, // data sent with the post request

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
                type: "POST",
                //This is the dictionary you are SENDING to your Django code. We are sending the 'action':get_data and the 'id: $AccountNum  
                //which is a variable that contains what car the user selected
                data: {
                    action: 'get_purchline_data',
                    Item_pk: Item_pk,
                    csrfmiddlewaretoken: csrftoken,
                }, // data sent with the post request

                // handle a successful response
                success: function(data) {
                    //This will execute when where Django code returns a dictionary called 'data' back to us.
                    $(ItemName_id).val(data.ItemName);
                    $(PurchUnit_id).val(data.UnitId);
                    $(PurchPrice_id).val(data.VendorPrice);
                    price = data.VendorPrice;
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

        total = parseFloat(total).toFixed(2); // Set line Total
        $(Total_id).val(total);
        SetTotals(true);
    });

	// Set balance on Paid change
    $('#id_Paid').on('change', function() {
        SetBalance();
        if($('#id_Paid').val() == 0) {
            EnablePurchLines(true);
        }
        ChangePurchaseStatus('OPE');
    });

    // Enable/Disable purch order on click
    $('#cancel_order_btn').on('click', function() {
        csrftoken = getCookie('csrftoken');
        var formData = $('#PurchOrderForm').serialize(); // Serialized form data
        var action = '&action=update_enabled'; //Action to execute on Django View
        if ($('#id_Enabled').is(':checked')) {
            purch_enabled = true;
        } else {
            purch_enabled = false;
        }

        $.ajax({
            url: window.location.href, // the endpoint,commonly same url
            type: "POST",
            data: {
                    action: 'update_enabled',
                    purch_enabled: purch_enabled,
                    csrfmiddlewaretoken: csrftoken,
                }, // data sent with the post request
            // handle a successful response
            success: function(json) {
                //console.log(json); // another sanity check
                //On success show the data posted to server as a message
                
                $('#id_Enabled').prop('checked', json.Enabled);
                if (!json.Enabled) {
                    $('#cancel_order_btn').text('Reabrir pedido');
                    SetBalance();
                    notie.alert(2, 'Pedido cancelado.', 1.5);
                } else {
                    $('#cancel_order_btn').text('Cancelar pedido');
                    notie.alert(4, 'Pedido abierto.', 1.5);
                }
                $('#id_Paid').val(0);
                ChangePurchaseStatus(json.PurchStatus);
            },

            // handle a non-successful response
            error: function(xhr, errmsg, err) {
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
                swal("Error al cancelar pedido", "La información del pedido no se ha modificado", "error")
            }

        });
    });

    //Pay
    $('#pay_order').on('click', function(event) {
        event.preventDefault();

        swal({
                title: 'Se pagará un total de: '+ getPurchTotal(),
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
                    success: function(json) {
                        swal(
                            'Orden de compra pagada',
                            'Correcto',
                            'success'
                        );
                        // Actions when order is Paid
                        ChangePurchaseStatus(json.PurchStatus); // Change status function
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
    });

    //Receive and pay
    $('#receive_pay').on('click', function(event) {
        event.preventDefault();

        swal({
                title: 'Se pagará un total de: '+ getPurchTotal(),
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
                    success: function(json) {
                        //On success show the data posted to server as a message
                        swal(
                            'Orden de compra pagada',
                            'Recibió ' + getTotalItems().toString() + ' artículos',
                            'success'
                        );
                        ChangePurchaseStatus(json.PurchStatus);
                        //$('#cancel_order_btn').prop('disabled', true); //Bloquear cancelación
                        //$('#delPurchOrderBtn').hide(); //Bloquear eliminación
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
    });
    
    //Receive
    $('#receive_invent').on('click', function(event) {
        event.preventDefault();
        if($('#id_PurchStatus').val() != 'REC') { // Prevent receiving
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
	                // var csrftoken = getCookie('csrftoken'); Not necesary through serialization
	                var formData = $('#PurchOrderForm').serialize(); // Serialized form data
	                var action = '&action=receive'; //Action to execute on Django View

	                $.ajax({
	                    url: window.location.href, // the endpoint,commonly same url
	                    type: "POST",
	                    data: formData + action,
	                    // handle a successful response
	                    success: function(json) {
	                        //On success show the data posted to server as a message
	                        swal(
	                            'Orden de compra recibida',
	                            'Se recibieron un total de ' + getTotalItems().toString() + ' artículos',
	                            'success'
	                        );
	                        if (json.Enabled == false){
	                          
	                        }
                            $('#cancel_order_btn').prop('disabled', true); //Bloquear cancelación
                            $('#delPurchOrderBtn').hide(); //Bloquear eliminación
                            
	                        $('#id_PurchStatus').val(json.PurchStatus.toString()).change();
	                    },
	                    // handle a non-successful response
	                    error: function(xhr, errmsg, err) {
	                        console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
	                        swal("Error al recibir pedido", "La información del pedido no se ha modificado", "error");
	                    }

	                });
	            });
		}
    });
    
    if($('#id_Paid').val() != 0) {
        $('#delPurchOrderBtn').hide(); //Bloquear eliminación
    }
    $('#id_Paid').on('change', function(){
        if(!$(this).val() || $(this).val() == 0) {
            $('#delPurchOrderBtn').show(); //Bloquear eliminación
        } else {
            $('#delPurchOrderBtn').hide(); //Bloquear eliminación
        }
    });

    /* ----- Purchase Order ----- */

});

/* ----- LOCAL FUNCTIONS ----- */
// Set totals in PO
function SetTotals(setBalance){
	var total = getPurchTotal();

    $('#id_SubTotal').val(total);
    $('#id_Total').val(total);
	$('#id_Balance').val($('#id_Total').val() - $('#id_Paid').val());
}
// Block discount fields
function EnableDiscounts(setBalance){
	var total = 0;

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
// Disable Table items
function EnablePurchLines(enable){
    if(enable) {
        $('.del-row').show();
        $('.add-row').show();
        $("#purchline_table *").attr("readonly", false);
        $('#purchline_table tr').each(function(){
            $(this).find('td:first select').css('-webkit-appearance', '');
            $(this).find('td:first select').css('-moz-appearance', '');
            $(this).find('td:first select').css('text-indent', '');
            $(this).find('td:first select').css('text-overflow', '');
            $(this).find('td:first select option').show();
        }); 
    } else {
        $('.del-row').hide();
        $('.add-row').hide();
        $("#purchline_table *").attr("readonly", true);
        $('#purchline_table tr').each(function(){
            $(this).find('td:first select').css('-webkit-appearance', 'none');
            $(this).find('td:first select').css('-moz-appearance', 'none');
            $(this).find('td:first select').css('text-indent', '0px');
            $(this).find('td:first select').css('text-overflow', '');
            $(this).find('td:first select option').hide();
        });    
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
            total = (Math.round( total * 100 )/100 );
        }
    });
    return total;
}

// Pay Purchase Order Total
function PayPurchOrder() {
    $('#id_Paid').val(getPurchTotal());
    SetBalance();
}

// Set balance
function SetBalance() {
    var Balance = parseFloat(getPurchTotal() - $('#id_Paid').val()).toFixed(2);
    $('#id_Balance').val(Balance);
}
/* ----- Status control section ----- */

function ChangePurchaseStatus(action) {
    switch(action) {
        case 'PAI':
            $('#id_PurchStatus').val('PAI').change();
            EnablePurchLines(false);
            EnableForm('PurchOrderForm',true);
            break;
        case 'REC':
            $('#id_PurchStatus').val('REC').change();
            EnablePurchLines(false);
            EnableForm('PurchOrderForm',true);
            break;
        case 'RPA':
            $('#id_PurchStatus').val('RPA').change();
            EnablePurchLines(false);
            EnableForm('PurchOrderForm',false);
            break;
        case 'OPE':
            $('#id_PurchStatus').val('OPE').change();
            //EnablePurchLines(true);
            EnableForm('PurchOrderForm',true);
            break;
        case 'CAN':
            $('#id_PurchStatus').val('CAN').change();
            //EnablePurchLines(false);
            EnableForm('PurchOrderForm',false);
            break;
    }
}

/* .---- Status control section ----- */
/* -------------------- */