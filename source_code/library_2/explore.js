$(document).ready(function() {
	// When the search button is clicked
	$("#searchButton").click(function() {
		// Get the user's input
		var input = $("#searchInput").val().toLowerCase();

		// Show all cards if input is empty
		if (input == "") {
			$(".card").show();
		}
		else {
			// Hide all cards
			$(".card").hide();
			
			// Show cards with matching genre
			$("." + input).show();
		}
	});
});