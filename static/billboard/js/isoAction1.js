$(document).ready(function() {
var $container = $('.isoContain'),
		colWidth = function () {
			var w = $container.width(), 
				columnNum = 1,
				columnWidth = 0;
			if (w > 1200) {
				columnNum  = 5;
			} else if (w > 900) {
				columnNum  = 4;
			} else if (w > 600) {
				columnNum  = 3;
			} else if (w > 300) {
				columnNum  = 2;
			}
		columnWidth = Math.floor(w/columnNum);
			$container.find('.item').each(function() {
				var $item = $(this),
					multiplier_w = $item.attr('class').match(/w(\d)/),
					multiplier_h = $item.attr('class').match(/h(\d)/),
					width = multiplier_w ? columnWidth*multiplier_w[1]-4 : columnWidth-4,
					height = multiplier_h ? columnWidth*multiplier_h[1]*0.5-4 : columnWidth*0.5-4;
				$item.css({
					width: width,
					height: height
				});
			});
			return columnWidth;
		},

	$container.isotope({
	    itemSelector: '.grid-block',
	    animationEngine: 'best-available',
	    resizable: false,
	    masonry: { columnWidth: $container.width() / 4 }
	    });
	    
	    $(window).smartresize(function(){  $container.isotope({
	    // update columnWidth to a percentage of container width
	    masonry: { columnWidth: $container.width() / 4 }
	  });
	});
    
$(window).smartresize();