(function($,sr){
 
  // debouncing function from John Hann
  // http://unscriptable.com/index.php/2009/03/20/debouncing-javascript-methods/
  var debounce = function (func, threshold, execAsap) {
      var timeout;
 
      return function debounced () {
          var obj = this, args = arguments;
          function delayed () {
              if (!execAsap)
                  func.apply(obj, args);
              timeout = null; 
          };
 
          if (timeout)
              clearTimeout(timeout);
          else if (execAsap)
              func.apply(obj, args);
 
          timeout = setTimeout(delayed, threshold || 100); 
      };
  }
	// smartresize 
	jQuery.fn[sr] = function(fn){  return fn ? this.bind('resize', debounce(fn)) : this.trigger(sr); };
 
})(jQuery,'smartresize');

(function ($) {
	var $container = $('.isoContain'),
		colWidth = function () {
			var w = $container.width(), 
				columnNum = 1,
				columnWidth = 0;
			//Create breaks that cause more or less columns to form
			if (w > 1000) {
				columnNum  = 7;
			} else if (w > 900) {
				columnNum  = 6;
			} else if (w > 600) {
				columnNum  = 5;
			} else if (w > 300) {
				columnNum  = 4;
			}
			//Width = screenWidth/columnNumber
			columnWidth = Math.floor(w/columnNum);
			$container.find('.item').each(function() {
				var $item = $(this),
					multiplier_w = $item.attr('class').match(/w(\d)/),
					multiplier_h = $item.attr('class').match(/h(\d)/),
					//Edit the heightFactor (0.75) to change the size of the box, 1 makes it a perfect square
					heightFactor = 1
					//Find instances of height and width variables
					width = multiplier_w ? columnWidth*multiplier_w[1]-4 : columnWidth-4,
					height = multiplier_h ? columnWidth*multiplier_h[1]*heightFactor-4 : columnWidth*heightFactor-4;
				//Update the $('.item') css
				$item.css({
					width: width,
					height: height
				});
			});
			return columnWidth;
		},
		//Initiate the isotope container
		isotope = function () {
			$container.isotope({
				resizable: false,
				itemSelector: '.item',
				masonry: {
					columnWidth: colWidth(),
					gutterWidth: 4
				}
			});
		};
	isotope();
	//Call smartresize function to adjust at every screen size change
	$(window).smartresize(isotope);
}(jQuery));