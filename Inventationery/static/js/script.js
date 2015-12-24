/* 
 * @Author: Alex
 * @Date:   2015-11-16 18:59:28
 * @Last Modified by:   Alex
 * @Last Modified time: 2015-12-23 23:36:06
 */

'use strict';
// A $( document ).ready() block.
$(document).ready(function() {

    /* ----- INITIALIZE DATATABLES ----- */
    // Vendor table list initialize plugin
    $('#VendorsListTableId').DataTable({
        "language": {
            "url": "//cdn.datatables.net/plug-ins/9dcbecd42ad/i18n/Spanish.json"
        }
    });
    // Purch order table list initialize plugin
    $('#PurchOrderListTableId').DataTable({
        "order": [[ 7, "desc" ]],
        "language": {
            "url": "//cdn.datatables.net/plug-ins/9dcbecd42ad/i18n/Spanish.json"
        }
    });
    // Inventory table list initialize plugin
    $('#InventoryListTableId').DataTable({
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
function EnableForm(form, enabled) {
    var formId = '#' + form + ' ' + '*';
    if (enabled) {
        $(formId).not('form_disabled').prop('disabled', false);
    } else {
        $(formId).not('form_disabled').prop('disabled', true);
    }
}
    
/* -------------------- */
