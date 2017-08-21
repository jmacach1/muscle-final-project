// run our javascript once the page is ready                                               $
$(document).ready(function() {
        // When "Add to Query" button is clicked.                                           
        // The contents of the Bottom TextArea will be added to the                         
        // Top TextArea where the MUSCLE query is.                                           
        $('#button1').click(function() {
            var inputTextArea = $('#inputTextArea');
            var dbTextArea = $('#dbTextArea');
            if (inputTextArea.val() != "") {
                inputTextArea.val(inputTextArea.val() + "\n\n" + dbTextArea.val());
            } else {
                inputTextArea.val(inputTextArea.val() + dbTextArea.val());
            }
        });

        //Autocomplete for Searching a Sequence in the Database
        $("#search_term").autocomplete({
	    source: 'js/search.php'                                            
	});        

});