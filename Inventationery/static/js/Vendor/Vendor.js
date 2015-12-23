/* 
 * @Author: Alex
 * @Date:   2015-11-16 18:59:28
 * @Last Modified by:   Alex
 * @Last Modified time: 2015-12-22 23:48:46
 */

'use strict';
// A $( document ).ready() block.
$(document).ready(function() {
    /* ----- Vendor ----- */
    // Fill NameAlias
    $("#id_Name").focusout(function() {
        var Name = $(this).val();
        var FirstLastName = "";
        if ($("#id_AccountType").val() == 'PER') {
            FirstLastName = $("#id_FirstLastName").val();
        };
        var NameAlias = Name + " " + FirstLastName;
        $("#id_NameAlias").val(NameAlias);
    });
    $("#id_FirstLastName").focusout(function() {
        var Name = $("#id_Name").val();
        var FirstLastName = $(this).val();
        if ($("#id_AccountType").val() == 'PER') {
            FirstLastName = $("#id_FirstLastName").val();
        };
        var NameAlias = Name + " " + FirstLastName;
        $("#id_NameAlias").val(NameAlias);
    });

    if ($('#id_AccountType').val() === 'PAR') {
        $(".fill-person").val("xxxxx");
        $('.person-info').hide();
        $('.NameDiv').toggleClass('col-md-6 col-sm-6 col-xs-12');
    }
    if ($('#id_AccountType').val() === 'PER') {
        $('.person-info').show();
        $('.NameDiv').toggleClass('col-md-6 col-sm-6 col-xs-12');
    }

    $("#id_AccountType").change(function() {
        if ($('#id_AccountType').val() === 'PAR') {
            $(".fill-person").val("xxxxx");
            $("#id_NameAlias").val("");
            $('.person-info').hide();
            $('.NameDiv').toggleClass('col-md-6 col-sm-6 col-xs-12');
        }
        if ($('#id_AccountType').val() === 'PER') {
            $(".fill-person").val("");
            $("#id_NameAlias").val("");
            $('.person-info').show();
            $('.NameDiv').toggleClass('col-md-6 col-sm-6 col-xs-12');
        }
    });

    

    // Contact formset
    $('.electronic_formset tbody tr').formset({ // Initialize django-formset plugin
        prefix: 'efs',
        formCssClass: 'electronic-formset',
        addText: 'Agregar contacto',
        deleteText: 'Eliminar contacto',
        addCssClass: 'btn btn-success btn-xs',
        deleteCssClass: 'btn btn-warning btn-xs',
    });

    // Postal formset
    $('.party_formset').formset({ // Initialize django-formset plugin
        prefix: 'pfs',
        formCssClass: 'party-formset',
        addText: 'Agregar dirección',
        deleteText: 'Eliminar dirección',
        addCssClass: 'btn btn-success btn-xs',
        deleteCssClass: 'btn btn-warning btn-xs',
    });

    // Loading content on Ajax GET
    /*$('#NewVendorBtn').on('click', function(){
      $.ajax({
        url: NewVendorURL,
        type: 'get',
        success: function(data) {
            var content = $("#content", data);
            $('#content').html(content);
            // Replace url on browser without reloading the entire page
            // window.history.pushState({"html":data.html,"pageTitle":data.pageTitle},"", NewVendorURL);
            // Replace url on browser reloading the entire page
            //window.location = NewVendorURL;
        },
        error: function(xhr, textStatus, errorThrown) {
            alert("Please report this error: "+errorThrown+xhr.status+xhr.responseText);
        }
      });
    });*/

    /* ----- Vendor ----- */

/* -------------------- */
});