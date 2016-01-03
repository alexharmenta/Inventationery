/* 
 * @Author: Alex
 * @Date:   2015-12-22 23:49:47
 * @Last Modified by:   Alex
 * @Last Modified time: 2016-01-02 19:23:09
 */

'use strict';
$(document).ready(function() {
    /* ----- Inventory ----- */
    // ItemVendor formset
    $('#PaymentsFormset tbody tr').formset({ // Initialize django-formset plugin
        prefix: 'pfs',
        formCssClass: 'payments-formset',
        addText: ' + ',
        deleteText: ' X ',
        addCssClass: 'btn btn-success btn-xs',
        deleteCssClass: 'btn btn-danger btn-xs',
    });
    // Inventory formset
    $('#PaymModesFormset tbody tr').formset({ // Initialize django-formset plugin
        prefix: 'pmfs',
        formCssClass: 'paymmode-formset',
        addText: ' + ',
        deleteText: ' X ',
        addCssClass: 'btn btn-success btn-xs',
        deleteCssClass: 'btn btn-danger btn-xs',
    });


    $('#SaveInventBtn').on('click', function(event) {
        event.preventDefault();
        var form = $('#InventoryForm');
        swal({
            title: "Inventario: Revise la información antes de guardar",
            text: "Si eliminó alguna linea de inventario no será capaz de recuperarla y perderá el registro de almacén!",
            type: "warning",
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Si, entiendo!',
            closeOnConfirm: false,
        }, function(isConfirm) {
            if (isConfirm) form.submit();
        });
    });
    /* ----- Inventory ----- */

});
