/* 
 * @Author: Alex
 * @Date:   2016-01-02 12:49:12
 * @Last Modified by:   Alex
 * @Last Modified time: 2016-01-05 21:20:15
 */

'use strict';
$(document).ready(function() {
    /*----- Counter -----*/
    (function ($) {
		$.fn.countTo = function (options) {
			options = options || {};
			
			return $(this).each(function () {
				// set options for current element
				var settings = $.extend({}, $.fn.countTo.defaults, {
					from:            $(this).data('from'),
					to:              $(this).data('to'),
					speed:           $(this).data('speed'),
					refreshInterval: $(this).data('refresh-interval'),
					decimals:        $(this).data('decimals')
				}, options);
				
				// how many times to update the value, and how much to increment the value on each update
				var loops = Math.ceil(settings.speed / settings.refreshInterval),
					increment = (settings.to - settings.from) / loops;
				
				// references & variables that will change with each update
				var self = this,
					$self = $(this),
					loopCount = 0,
					value = settings.from,
					data = $self.data('countTo') || {};
				
				$self.data('countTo', data);
				
				// if an existing interval can be found, clear it first
				if (data.interval) {
					clearInterval(data.interval);
				}
				data.interval = setInterval(updateTimer, settings.refreshInterval);
				
				// initialize the element with the starting value
				render(value);
				
				function updateTimer() {
					value += increment;
					loopCount++;
					
					render(value);
					
					if (typeof(settings.onUpdate) == 'function') {
						settings.onUpdate.call(self, value);
					}
					
					if (loopCount >= loops) {
						// remove the interval
						$self.removeData('countTo');
						clearInterval(data.interval);
						value = settings.to;
						
						if (typeof(settings.onComplete) == 'function') {
							settings.onComplete.call(self, value);
						}
					}
				}
				
				function render(value) {
					var formattedValue = settings.formatter.call(self, value, settings);
					$self.html(formattedValue);
				}
			});
		};
		
		$.fn.countTo.defaults = {
			from: 0,               // the number the element should start at
			to: 0,                 // the number the element should end at
			speed: 1000,           // how long it should take to count between the target numbers
			refreshInterval: 100,  // how often the element should be updated
			decimals: 0,           // the number of decimal places to show
			formatter: formatter,  // handler for formatting the value before rendering
			onUpdate: null,        // callback method for every time the element is updated
			onComplete: null       // callback method for when the element finishes updating
		};
		
		function formatter(value, settings) {
			return value.toFixed(settings.decimals);
		}
	}(jQuery));

	jQuery(function ($) {
	  // custom formatting example
	  $('#count-number').data('countToOptions', {
		formatter: function (value, options) {
		  return value.toFixed(options.decimals).replace(/\B(?=(?:\d{3})+(?!\d))/g, ',');
		}
	  });
	  
	  // start all the timers
	  $('.timer').each(count);  
	  
	  function count(options) {
		var $this = $(this);
		options = $.extend({}, options || {}, $this.data('countToOptions') || {});
		$this.countTo(options);
	  }
	});
	/*----- Counter -----*/
	/*----- Charts -----*/
	var randomScalingFactor = function(){ return Math.round(Math.random()*100)};

	var barChartData = {
		labels : ["January","February","March","April","May","June","July"],
		datasets : [
			{
				fillColor : "rgba(243,86,93,0.75)",
				strokeColor : "rgba(243,86,93,0.75)",
				highlightFill: "rgba(243,86,93,1)",
				highlightStroke: "rgba(243,86,93,1)",
				data : [randomScalingFactor(),randomScalingFactor(),randomScalingFactor(),randomScalingFactor(),randomScalingFactor(),randomScalingFactor(),randomScalingFactor()]
			},
			{
				fillColor : "rgba(97,195,174,0.75)",
				strokeColor : "rgba(97,195,174,0.75)",
				highlightFill : "rgba(97,195,174,1)",
				highlightStroke : "rgba(97,195,174,1)",
				data : [randomScalingFactor(),randomScalingFactor(),randomScalingFactor(),randomScalingFactor(),randomScalingFactor(),randomScalingFactor(),randomScalingFactor()]
			}
		]

	}
	var bar = function(){
		var ctx1 = document.getElementById("canvas").getContext("2d");
		window.myBar = new Chart(ctx1).Bar(barChartData, {
			responsive : true
		});
	}
	var polarData = [
		{
			value: 300,
			color:"#F7464A",
			highlight: "#FF5A5E",
			label: "Red"
		},
		{
			value: 50,
			color: "#46BFBD",
			highlight: "#5AD3D1",
			label: "Green"
		},
		{
			value: 100,
			color: "#FDB45C",
			highlight: "#FFC870",
			label: "Yellow"
		},
		{
			value: 40,
			color: "#949FB1",
			highlight: "#A8B3C5",
			label: "Grey"
		},
		{
			value: 120,
			color: "#4D5360",
			highlight: "#616774",
			label: "Dark Grey"
		}

	];

	var chart = function(){
		var ctx2 = document.getElementById("chart-area").getContext("2d");
		window.myPolarArea = new Chart(ctx2).PolarArea(polarData, {
			responsive:true
		});
	};

	window.onload = function() {
	    bar();
	    chart();
	};
	/*----- Charts -----*/
	//Credit Sales
	var sales = new ProgressBar.Circle('#sales', {
	  color: '#61C3AE',
	  strokeWidth: 9,
	  trailWidth: 9,
	  duration: 1500,
	  text: {
	    value: '0%'
	  },
	  step: function(state, bar) {
	    bar.setText((bar.value() * 100).toFixed(0) + "%");
	  }
	});
	var purchases = new ProgressBar.Circle('#purchases', {
	  color: '#e88e3c',
	  strokeWidth: 9,
	  trailWidth: 9,
	  duration: 1500,
	  text: {
	    value: '0%'
	  },
	  step: function(state, bar) {
	    bar.setText((bar.value() * 100).toFixed(0) + "%");
	  }
	});
	var articles = new ProgressBar.Circle('#articles', {
	  color: '#02baf2',
	  strokeWidth: 9,
	  trailWidth: 9,
	  duration: 1500,
	  text: {
	    value: '0%'
	  },
	  step: function(state, bar) {
	    bar.setText((bar.value() * 100).toFixed(0) + "%");
	  }
	});
	var sale = parseFloat($('#id_SalesMov').text());
	var purchase = parseFloat($('#id_PurchMov').text());
	var invent = parseFloat($('#id_InvMov').text());
	var salesPct = ((sale * 100) / invent).toFixed(1);
	var purchasesPct = ((purchase * 100) / invent).toFixed(1);
	var inventPct = parseFloat(salesPct + purchasesPct);
	sales.animate(salesPct / 100);
	purchases.animate(purchasesPct / 100);
	articles.animate(inventPct / 100);
	$('#id_InvMov').text(sale + purchase);
});
