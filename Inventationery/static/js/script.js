/* 
* @Author: Alex
* @Date:   2015-11-16 18:59:28
* @Last Modified by:   Alex
* @Last Modified time: 2015-12-06 22:00:56
*/

'use strict';
// A $( document ).ready() block.
$( document ).ready(function() {
    
    $('.success').each(function(index) {
      notie.alert(1, $(this).text(), 1.5);
      $(this).fadeOut('fast');
    });
    $('.error').each(function(index) {
      notie.alert(3, $(this).text(), 1.5);
      $(this).fadeOut('fast');
    });

   	/* ----- Vendor ----- */
    // Fill NameAlias
   	$("#id_Name").focusout(function () {
        var Name = $(this).val();
        var FirstLastName = "";
        if ($("#id_AccountType").val() == 'PER') {
        	FirstLastName = $("#id_FirstLastName").val();	
        };
        var NameAlias = Name + " " + FirstLastName;
        $("#id_NameAlias").val(NameAlias);
    });
    $("#id_FirstLastName").focusout(function () {
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

    $( "#id_AccountType" ).change(function() {
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

   	// Vendor table list initialize plugin
    $('#VendorsListTableId').DataTable(
      {
        "language": {
            "url": "//cdn.datatables.net/plug-ins/9dcbecd42ad/i18n/Spanish.json"
        }
      }
    );

    // Contact formset
    $('.electronic_formset tbody tr').formset({// Initialize django-formset plugin
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

    /* ----- Purchase Order ----- */
    // PurchOrder table list initialize plugin
    $('#PurchOrderListTableId').DataTable(
      {
        "language": {
            "url": "//cdn.datatables.net/plug-ins/9dcbecd42ad/i18n/Spanish.json"
        }
      }
    );
    // Purchline formset
    $('#PurchOrderForm tbody tr').formset({ // Initialize django-formset plugin
        prefix: 'plfs',
        formCssClass: 'purchline-formset',
        addText: 'Agregar linea',
        deleteText: ' X ',
        addCssClass: 'btn btn-success btn-xs',
        deleteCssClass: 'btn btn-danger btn-xs',
    });
    
    // Get purchase order info with AJAX
    $('#id_Vendor').on('change', function(){
      var Vendor_pk = $('#id_Vendor option:selected').val();
      // AJAX Code for retrieving data from vendor
      var csrftoken = getCookie('csrftoken');

      $.ajax({
        url : window.location.href, // the endpoint,commonly same url
        type: "POST",
        //This is the dictionary you are SENDING to your Django code. 
        //We are sending the 'action':get_purch_data and the 'id: $Vendor_pk  
        //which is a variable that contains what account user selected
        data: { 
          action: 'get_purch_data',
          Vendor_pk: Vendor_pk,
          csrfmiddlewaretoken : csrftoken, 
        },// data sent with the post request

        // handle a successful response
        success: function(data){
          //This will execute when where Django code returns a dictionary called 'data' back to us.
          $('#OneTimeVendor').prop('checked', data.OneTimeVendor);
          $("#VATNum").val(data.VATNum);
          $("#id_WorkerPurchPlacer").val(data.NameAlias);
          $("#id_CurrencyCode").val(data.CurrencyCode);
          $("#id_LanguageCode").val(data.LanguageCode);
          $("#id_DeliveryName").val(data.DeliveryName);
          $("#id_DeliveryContact").val(data.DeliveryContact);
        }

      });
    });

    // Global variables
    var qty;
    var price;
    var disc;
    var percent;
    var total = 0;
    var Purch_SubTotal = 0;
    var LineAmount = 0.0;
    // Global variables
    $('.total_amount').each(function(index){
      if($(this).val()) {
        total += parseFloat($(this).val());
        total = Math.round(total * 100) / 100;
        $('#id_SubTotal').val(total);
        $('#id_Total').val(total);
        $('#id_Paid').val(0);
      }
    });
    // Get purchase line info with AJAX
    $('.purchline_formset').on('change', 'tr td select,input', function(){
      var id = $(this).attr('id');
      var id_lower = id.toLowerCase()
      var rownum = id.replace(/\D/g,'');
      var ItemName_id = '#id_plfs-'+ rownum + '-ItemName'
      var PurchUnit_id = '#id_plfs-'+ rownum + '-PurchUnit'
      var PurchPrice_id = '#id_plfs-'+ rownum + '-PurchPrice'
      var PurchQty_id = '#id_plfs-'+ rownum + '-PurchQty'
      var LineDisc_id = '#id_plfs-'+ rownum + '-LineDisc'
      var LinePercent_id = '#id_plfs-'+ rownum + '-LinePercent'
      var Total_id = '#id_plfs-'+ rownum + '-LineAmount'

      if(id_lower.indexOf('itemid') != -1) {
        var Item_pk = getCharsBefore($('#'+ id + ' option:selected').val(), ' ');
        var Item_pk = $('#'+ id + ' option:selected').val();
        // AJAX Code for retrieving data from vendor
        var csrftoken = getCookie('csrftoken');

        $.ajax({
          url : window.location.href, // the endpoint,commonly same url
          type: "POST",
          //This is the dictionary you are SENDING to your Django code. We are sending the 'action':get_data and the 'id: $AccountNum  
          //which is a variable that contains what car the user selected
          data: { 
                  action: 'get_purchline_data',
                  Item_pk: Item_pk,
                  csrfmiddlewaretoken : csrftoken, 
                },// data sent with the post request

          // handle a successful response
          success: function(data){
            //This will execute when where Django code returns a dictionary called 'data' back to us.
            $(ItemName_id).val(data.ItemName);
            $(PurchUnit_id).val(data.UnitId);
            $(PurchPrice_id).val(data.VendorPrice);
            price = data.VendorPrice;
          }
        });
      }

      // Calc data from purch lines
      qty = $(PurchQty_id).val();
      price = $(PurchPrice_id).val();
      disc = $(LineDisc_id).val();
      percent = $(LinePercent_id).val();
      total = $(Total_id).val();
      
      if(id_lower.indexOf('disc') != -1) {
         if(disc){
            $(LinePercent_id).prop('readonly', true);
         } else {
            $(LinePercent_id).prop('readonly', false);
         }
      } else if(id_lower.indexOf('percent') != -1) {
         if(percent){
            $(LineDisc_id).prop('readonly', true);
         } else {
            $(LineDisc_id).prop('readonly', false);
         }
      }

      if(qty && price) {
        if(disc && !percent){
          total = (qty * price) - disc;
        } else if(!disc && percent) {
          total = qty * price;
          percent = total * (percent / 100);
          total = total - percent;
        } else {
          total = qty * price;
        }
      }
      total = Math.round(parseFloat(total) * 100) / 100;
      $(Total_id).val(total);

      if(total){
        total = 0;
        $('.total_amount').each(function(index){
          if($(this).val()) {
            total += parseFloat($(this).val());
            total = Math.round(total * 100) / 100;
            $('#id_SubTotal').val(total);
            $('#id_Total').val(total);
            $('#id_Balance').val($('#id_Total').val() - $('#id_Paid').val());
          }
        });
      }
    });
    
    $('#id_Balance').val($('#id_Total').val() - $('#id_Paid').val());
    $('#id_Paid').on('change', function(){
      $('#id_Balance').val($('#id_Total').val() - $(this).val());
    });
    
    // Enable/Disable purch order on load
    var purch_enabled;
    if ($('#id_Enabled').is(':checked')) {
      purch_enabled = true;
    } else {
      purch_enabled = false;
    }
    disableForm('PurchOrderForm', purch_enabled);
    $('#cancel_order_btn').prop('disabled', false);
    // Enable/Disable purch order on click
    $('#cancel_order_btn').on('click', function(){
      var csrftoken = getCookie('csrftoken');

      $.ajax({
        url : window.location.href, // the endpoint,commonly same url
        type: "POST",

        data: { 
          action: 'update_enabled',
          purch_enabled: !purch_enabled,
          csrfmiddlewaretoken : csrftoken,
        },// data sent with the post request

        // handle a successful response
        success : function(json) {
          //console.log(json); // another sanity check
          //On success show the data posted to server as a message
          purch_enabled = !purch_enabled;
          $('#id_Enabled').prop('checked', purch_enabled);
          if(!purch_enabled){
            $('#cancel_order_btn').text('Reabrir pedido');
            notie.alert(2, 'Pedido cancelado.', 1.5);
          } else {
            $('#cancel_order_btn').text('Cancelar pedido');
            notie.alert(4, 'Pedido abierto.', 1.5);
          }
          disableForm('PurchOrderForm', purch_enabled);
          $('#cancel_order_btn').prop('disabled', false);
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
          console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
          swal("Error al cancelar pedido", "La información del pedido no se ha modificado", "error")
        }

      });

    });
    
    //Receive and pay
    $('#receive_pay').on('click', function(event){
      event.preventDefault();

      swal({   
        title: 'Se pagará completamente la orden de compra',   
        text: 'Recibirá un total de ' + getTotalItems().toString() + ' artículos',   
        type: 'warning',   
        showCancelButton: true,   
        confirmButtonColor: '#3085d6',   
        cancelButtonColor: '#d33',   
        confirmButtonText: 'Si, pagar!',   
        closeOnConfirm: false 
      }, 
      function() {
        var csrftoken = getCookie('csrftoken');
        $.ajax({
          url : window.location.href, // the endpoint,commonly same url
          type: "POST",

          data: { 
            action: 'receive_pay',
            csrfmiddlewaretoken : csrftoken,
          },// data sent with the post request

          // handle a successful response
          success : function(json) {
            //console.log(json); // another sanity check
            //On success show the data posted to server as a message
            swal(     
            'Orden de compra pagada',     
            'Se recibieron un total de ' + getTotalItems().toString() + ' artículos',     
            'success'   
            );
            $('#id_Paid').val($('#id_Total').val()); // Pagar todo el monto     
            $('#id_Balance').val($('#id_Total').val() - $('#id_Paid').val()); // Calcular balance
            disableForm('PurchOrderForm', false); // Bloquear pedido
            $('#cancel_order_btn').prop('disabled', true);
          },

          // handle a non-successful response
          error : function(xhr,errmsg,err) {
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            swal("Error al cancelar pedido", "La información del pedido no se ha modificado", "error")
          }

        });
        
      });
    });

    // Get current items
    function getTotalItems(){
      var total=0;
      $('.pl_qty').each(function(index, el) {
        if($(this).val() != ''){
          total += parseFloat($(this).val());
        }
      });
      return total;
    }
    /* ----- Purchase Order ----- */

    /* ----- Inventory ----- */
    // Inventory table list initialize plugin
    $('#InventoryListTableId').DataTable(
      {
        "language": {
            "url": "//cdn.datatables.net/plug-ins/9dcbecd42ad/i18n/Spanish.json"
        }
      }
    );
    // Upload image preview
    $('#id_ItemImage').on('change', function(){
      var reader = new FileReader();

      reader.onload = function (e) {
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

    /* ----- EXTRA FUNCTIONS ----- */
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
            return(str.substring(0, index));
        }
        return("");
    }

    // Enable/Disable forms
    function disableForm(form, enabled){
      var formId = '#' + form + ' ' + '*';
      if(!enabled){
        $(formId).not('form_disabled').prop('disabled',true);
      } else {
        $(formId).not('form_disabled').prop('disabled',false);
      }
    }
    /* ----- EXTRA FUNCTIONS ----- */


    $('.datepicker').datepicker({
        //todayBtn: "",
        clearBtn: true,
        language: "es",
        //daysOfWeekHighlighted: "1,2,3,4,5",
        autoclose: true,
        todayHighlight: true,
    });
});/* Document Ending */