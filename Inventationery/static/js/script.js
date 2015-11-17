/* 
* @Author: Alex
* @Date:   2015-11-16 18:59:28
* @Last Modified by:   Alex
* @Last Modified time: 2015-11-16 18:59:30
*/

'use strict';
// A $( document ).ready() block.
$( document ).ready(function() {
    //For getting CSRF token
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

   	// Llenar información de proveedores
   	$("#id_Name").keyup(function () {
        var Name = $(this).val();
        var FirstLastName = "";
        if ($("#OneTimeVendor_Id").val() == 'PER') {
        	FirstLastName = $("#id_FirstLastName").val();	
        };
        var NameAlias = Name + " " + FirstLastName;
        $("#id_NameAlias").val(NameAlias);
    });
    $("#id_FirstLastName").keyup(function () {
        var Name = $("#id_Name").val();
        var FirstLastName = $(this).val();
        if ($("#OneTimeVendor_Id").val() == 'PER') {
        	FirstLastName = $("#id_FirstLastName").val();	
        };
        var NameAlias = Name + " " + FirstLastName;
        $("#id_NameAlias").val(NameAlias);
    });

   	if ($('#OneTimeVendor_Id').val() === 'PAR') {
   		$(".fill-person").val("xxxxx");
		$('.person-info').hide();
   	}
   	if ($('#OneTimeVendor_Id').val() === 'PER') {
   		$(".fill-person").val("");
		$('.person-info').show();
   	}

   $( "#OneTimeVendor_Id" ).change(function() {
	  	if ($('#OneTimeVendor_Id').val() === 'PAR') {
	  		$(".fill-person").val("xxxxx");
	  		$("#id_NameAlias").val("");
			$('.person-info').hide();
	   	}
	   	if ($('#OneTimeVendor_Id').val() === 'PER') {
	   		$(".fill-person").val("");
	   		$("#id_NameAlias").val("");
			$('.person-info').show();
	   }
	 });
   	// Llenar información de proveedores
   	
   	// Vendor table initialize

    $('#VendorsListTableId').DataTable(
      {
      
      }
    );

    /* Postal formset validation logic */
    $('.party_formset').formset({
        prefix: 'pfs',
        formCssClass: 'party-formset',
        addText: 'Agregar dirección',
        deleteText: 'Eliminar dirección',
        addCssClass: 'btn btn-success btn-xs',
        deleteCssClass: 'btn btn-warning btn-xs',
    });
    /* Postal formset validation logic */

    /* Contact formset validation logic */
    $('.electronic_formset tbody tr').formset({
        prefix: 'efs',
        formCssClass: 'electronic-formset',
        addText: 'Agregar contacto',
        deleteText: 'Eliminar contacto',
        addCssClass: 'btn btn-success btn-xs',
        deleteCssClass: 'btn btn-warning btn-xs',
    });
    /* Contact formset validation logic */

    // PurchOrder table initialize

    $('#PurchOrderListTableId').DataTable(
      {
      
      }
    );
    /* Purchline formset validation logic */
    $('#PurchOrderForm tbody tr').formset({
        prefix: 'plfs',
        addText: 'Agregar linea',
        deleteText: ' X ',
        addCssClass: 'btn btn-success btn-xs',
        deleteCssClass: 'btn btn-danger btn-xs',
    });
    /* Purchline formset validation logic */
    // Inventory table initialize

    $('#InventoryListTableId').DataTable(
      {
      
      }
    );

    /* Get purchase order info with AJAX */
    $('#id_OrderAccount').on('change', function(){
      $('#id_InvoiceAccount').val($(this).val()).change(); //Change invoice value
      var AccountNum = getCharsBefore($('#id_OrderAccount option:selected').text(), ' ');
      var AccountNum = $('#id_OrderAccount option:selected').text();
      // AJAX Code for retrieving data from vendor
      var csrftoken = getCookie('csrftoken');

      $.ajax({
        url : window.location.href, // the endpoint,commonly same url
        type: "POST",
        //This is the dictionary you are SENDING to your Django code. We are sending the 'action':get_data and the 'id: $AccountNum  
        //which is a variable that contains what car the user selected
        data: { 
                action: 'get_purch_data',
                AccountNum: AccountNum,
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
        }

      });

    });
    // Global variables
    var qty;
    var price;
    var disc;
    var percent;
    var total;
    // Global variables
    $('.purchline_formset_td').on('change', '*', function(){
      var id = $(this).attr('id');
      var id_lower = id.toLowerCase()
      var rownum = id.replace(/\D/g,'');
      var ItemName_id = '#id_plfs-'+ rownum + '-ItemName'
      var PurchUnit_id = '#id_plfs-'+ rownum + '-PurchUnit'
      var PurchPrice_id = '#id_plfs-'+ rownum + '-PurchPrice'

      if(id_lower.indexOf('itemid') != -1) {
        var ItemId = getCharsBefore($('#'+ id + ' option:selected').text(), ' ');
        var ItemId = $('#'+ id + ' option:selected').text();
        // AJAX Code for retrieving data from vendor
        var csrftoken = getCookie('csrftoken');

        $.ajax({
          url : window.location.href, // the endpoint,commonly same url
          type: "POST",
          //This is the dictionary you are SENDING to your Django code. We are sending the 'action':get_data and the 'id: $AccountNum  
          //which is a variable that contains what car the user selected
          data: { 
                  action: 'get_purchline_data',
                  ItemId: ItemId,
                  csrfmiddlewaretoken : csrftoken, 
                },// data sent with the post request

          // handle a successful response
          success: function(data){
            //This will execute when where Django code returns a dictionary called 'data' back to us.
            $(ItemName_id).val(data.ItemName);
            $(PurchUnit_id).val(data.UnitId);
            $(PurchPrice_id).val(data.VendorPrice);
          }
        });
      }
      // Calc data from purch lines
      if(id_lower.indexOf('qty') != -1) {
        qty = $(this).val();
      } else if(id_lower.indexOf('price') != -1) {
        price = $(this).val();
      } else if(id_lower.indexOf('disc') != -1) {
         disc = $(this).val();
      } else if(id_lower.indexOf('percent') != -1) {
         percent = $(this).val();
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
      total = parseFloat(total);
      var total_id = '#id_plfs-'+ rownum + '-LineAmount'
      $(total_id).val(total);

    });
    /* Get purchase order info with AJAX */

    /* Function to get substring before some given char */
    function getCharsBefore(str, chr) {
      var index = str.indexOf(chr);
      if (index != -1) {
          return(str.substring(0, index));
      }
      return("");
    }

});