/* 
* @Author: Alex
* @Date:   2015-12-22 23:49:47
* @Last Modified by:   Alex
* @Last Modified time: 2015-12-22 23:50:19
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
    // Inventory formset
    $('#InventoryForm tbody tr').formset({ // Initialize django-formset plugin
        prefix: 'infs',
        formCssClass: 'inventory-formset',
        addText: ' + ',
        deleteText: ' X ',
        addCssClass: 'btn btn-success btn-xs',
        deleteCssClass: 'btn btn-danger btn-xs',
    });
    /* ----- Inventory ----- */
});