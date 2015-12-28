/* 
 * @Author: Alex
 * @Date:   2015-12-22 23:49:47
 * @Last Modified by:   harmenta
 * @Last Modified time: 2015-12-28 17:27:39
 */

'use strict';
$(document).ready(function() {
    // Upload image preview
    $('#id_CompanyImage').on('change', function() {
        var reader = new FileReader();

        reader.onload = function(e) {
            // get loaded data and render thumbnail.
            document.getElementById("company_image").src = e.target.result;
        };

        // read the image file as a data URL.
        reader.readAsDataURL(this.files[0]);
    });
});
