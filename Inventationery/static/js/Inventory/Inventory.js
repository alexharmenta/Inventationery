/* 
 * @Author: Alex
 * @Date:   2015-12-22 23:49:47
 * @Last Modified by:   harmenta
 * @Last Modified time: 2015-12-28 14:10:33
 */

'use strict';
$(document).ready(function() {
    /* ----- Inventory ----- */

    // Upload image preview
    $('#id_ItemImage').on('change', function() {
        var reader = new FileReader();

        reader.onload = function(e) {
            // get loaded data and render thumbnail.
            document.getElementById("item_image").src = e.target.result;
        };

        // read the image file as a data URL.
        reader.readAsDataURL(this.files[0]);
    });
    // ItemVendor formset
    $('#ItemVendorFormset tbody tr').formset({ // Initialize django-formset plugin
        prefix: 'ivfs',
        formCssClass: 'itemVendor-formset',
        addText: ' + ',
        deleteText: ' X ',
        addCssClass: 'btn btn-success btn-xs',
        deleteCssClass: 'btn btn-danger btn-xs',
    });
    // Inventory formset
    $('#InventoryFormset tbody tr').formset({ // Initialize django-formset plugin
        prefix: 'infs',
        formCssClass: 'inventory-formset',
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
