	$(document).ready(function() {
		$('.start').click(function(event) {
			$('.opener').fadeOut('slow');
		});
		$('h1').css('color', 'brown');
		// hide - show
		$('.hide-show a').click(function() {
			var link = $(this).data("fun");
			if ( link == "hide" ) {
				$('p.hideShow').hide();
			} else if ( link == "show" ) {
				$('p.hideShow').show();
			}
		});
		// toggle
		$('.toggle a').click(function() {
			$('p.toggle').toggle( "slow", function() {
    		$(this).css('color', 'red');
  		});
		});
		// slide
		$('.slide a').click(function() {
			var link = $(this).data("fun");
			if ( link == "down" ) {
				$('p.slide').slideDown('slow');
			} else if ( link == "up" ) {
				$('p.slide').slideUp('slow')
			}
		});
		//fade
		$('.fade a').click(function() {
			var link = $(this).data("fun");
			if ( link == "fade-out" ) {
				$('p.fade').fadeOut('slow');
			} else if ( link == "fade-in" ) {
				$('p.fade').fadeIn('slow')
			}
		});
		// add class
		$('.add-Class a').click(function() {
				$('p.add-Class').addClass('addClass');
		});
		//before - after
		$('.before-after a').click(function() {
			var link = $(this).data("fun");
			if ( link == "before" ) {
				$('p.before-after').before( "<p>before</p>" );
			} else if ( link == "after" ) {
				$('p.before-after').after( "<p>after</p>" );
			}
		});
		// html -- text
		$('.html-text a').click(function() {
			var link = $(this).data("fun");
			if ( link == "html" ) {
				$('.html-text-holder').html("<p>html copy here</p>");
			} else if ( link == "text" ) {
				$('.html-text-holder').text( "plain text here" );
			}
		});
		// append
		$('.append').click(function() {
			$('p.append').append(' Some text added.');
		});
		// attribute - value
		$('.attr-val a').click(function() {
			var text = $( this ).text();
  			$( "input" ).val( text );
		});
	});