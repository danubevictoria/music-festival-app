window.console = {
		log: function(str){
			document.getElementById("myLog").innerHTML = str;
		}
}

$(function (){
		    $('#btnSignUp').click(function() {
		 
		        $.ajax({
		            url: '/signup',
		            data: $('form').serialize(),
		            type: 'POST',
		            datatype: 'json',
		            success: function(response) {
		                console.log(response);
		            },
		            error: function(error) {
		                console.log(error);

		            }
		        });
		    });
		});