// this function executes our search via an AJAX call
function runSearch( term ) {
    // Clear dbTextArea where the Sequence will be fetched from the Database
    $('#dbTextArea').empty();
    
    // transforms all the form parameters into a string we can send to the server
    var frmStr = $('getFaaSeqDB').serialize();
    
    $.ajax({
	    url: './search.cgi',
		dataType: 'json',
		data: frmStr,
		success: function(data, textStatus, jqXHR) {
		processJSON(data);
	    },
		error: function(jqXHR, textStatus, errorThrown){
		alert("Failed to perform search! textStatus: (" + textStatus +
		      ") and errorThrown: (" + errorThrown + ")");
	    }
	});
}


// this processes a passed JSON structure
function processJSON( data ) {
    //print the items into dbTextArea
    $.each(data, function(i, item) {
            $("#dbTextArea").val(item.Title + "\n" + item.Sequence);
	});
}
    

// run our javascript once the page is ready
$(document).ready( function() {

	// define what should happen when a user clicks submit on our search form
	$('#button3').click( function() {
		runSearch();
		return false;  // prevents 'normal' form submission
	    });
    
    });


                                                    