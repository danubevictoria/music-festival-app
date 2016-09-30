window.console = {
		log: function(str){
			document.getElementById("myLog").innerHTML = str;
		}
}

$(function (){
		    $('#btnSignIn').click(function() {
		 
		        $.ajax({
		            url: '/signin',
		            data: $('form').serialize(),
		            type: 'POST',
		            datatype: 'json',
		            success: function(response) {
		                console.log(response);
		                location.href="/welcome"
		            },
		            error: function(error) {
		                console.log(error);
		                location.href = "/error";
		            }
		        });
		    });
		});