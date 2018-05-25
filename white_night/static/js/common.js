$(document).ready(function() {
	var user_screen_height = $(window).height();
	// alert(user_screen_height);
	var header_h = $("#header").height();
	var footer_h = $("#all-all-footer").height();
	var bg_min_h = user_screen_height - header_h - footer_h
	$("#wrapper_child_content").css('min-height', bg_min_h + 'px');
	$(".popup").magnificPopup();
})