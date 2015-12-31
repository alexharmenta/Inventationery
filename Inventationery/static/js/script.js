/* 
 * @Author: Alex
 * @Date:   2015-11-16 18:59:28
 * @Last Modified by:   Alex
 * @Last Modified time: 2015-12-31 00:04:01
 */

'use strict';
// A $( document ).ready() block.
$(document).ready(function() {

    /* ----- INITIALIZE DATATABLES ----- */
    // Location table list initialize plugin
    var locationTable = $('#LocationListTableId').DataTable({
        "language": {
            "url": "//cdn.datatables.net/plug-ins/9dcbecd42ad/i18n/Spanish.json"
        }
    });
    // Vendor table list initialize plugin
    var vendorTable = $('#VendorsListTableId').DataTable({
        "language": {
            "url": "//cdn.datatables.net/plug-ins/9dcbecd42ad/i18n/Spanish.json"
        }
    });
    // Customer table list initialize plugin
    var customerTable = $('#CustomersListTableId').DataTable({
        "language": {
            "url": "//cdn.datatables.net/plug-ins/9dcbecd42ad/i18n/Spanish.json"
        }
    });
    // Purch order table list initialize plugin
    /* Custom filtering function which will search data in column four between two values */
    
    var purchTable = $('#PurchOrderListTableId').DataTable({
        "order": [[ 0, "asc" ]],
        "language": {
            "url": "//cdn.datatables.net/plug-ins/9dcbecd42ad/i18n/Spanish.json"
        }
    });
    
    // Inventory table list initialize plugin
    var inventoryTable = $('#InventoryListTableId').DataTable({
        "language": {
            "url": "//cdn.datatables.net/plug-ins/9dcbecd42ad/i18n/Spanish.json"
        }
    });
    /* -------------------- */
    $('.success').each(function(index) {
        notie.alert(1, $(this).text(), 1.5);
        $(this).fadeOut('fast');
    });
    $('.error').each(function(index) {
        notie.alert(3, $(this).text(), 1.5);
        $(this).fadeOut('fast');
    });
    $('.warning').each(function(index) {
        notie.alert(2, $(this).text(), 1.5);
        $(this).fadeOut('fast');
    });

    $('.datepicker').datepicker({
        //todayBtn: "",
        clearBtn: true,
        language: "es",
        //daysOfWeekHighlighted: "1,2,3,4,5",
        autoclose: true,
        todayHighlight: true,
    });
    
}); /* Document Ending */



/* ----- GLOBAL EXTRA FUNCTIONS ----- */
// Function for getting CSRF token
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
// Function to get substring before some given char
function getCharsBefore(str, chr) {
    var index = str.indexOf(chr);
    if (index != -1) {
        return (str.substring(0, index));
    }
    return ("");
}
// Enable/Disable forms
function EnableForm(form, enable) {
    var formId = '#' + form + ' :input';
    $(formId).each(function() {
        var element = $(this);
        if(!element.hasClass('form_disabled')){
            if(enable){
                element.attr('readonly', false);
                if(element.is('select')){
                    element.css('-webkit-appearance', '');
                    element.css('-moz-appearance', '');
                    element.css('text-indent', '');
                    element.css('text-overflow', '');
                    element.find('option').show();
                }
            } else {
                element.attr('readonly', true);
                if(element.is('select')){
                    element.css('-webkit-appearance', 'none');
                    element.css('-moz-appearance', 'none');
                    element.css('text-indent', '0px');
                    element.css('text-overflow', '');
                    element.find('option').hide();
                }
            }
        }
    });
    if(enable) {
        $('#'+form).unbind('submit');
    } else {
        $('#'+form).bind('submit',function(e){e.preventDefault();});
    }
}
    
/* -------------------- */
