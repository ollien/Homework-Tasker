$(document).ready(function(){
	// $(document).on('click','#registerButton',function(){
		$('#registerForm').submit(function(event){
			
			$.post('/registerInput/',{
				'username':$('#usernameInput').val(),
				'password':$('#passwordInput').val(),
				'email':$('#emailInput').val(),
				'csrfmiddlewaretoken':$("#registerForm>input[name='csrfmiddlewaretoken']").val()},
				function(data){
					console.log(data);
					data=$.parseJSON(data);
					// $('.error').hide();
					if(data['result']==='OK'){
						window.location.replace('/');
					}
					else{
						$('.error').hide();
						for (var i=0; i<data['result'].length; i++){
							if (data['result'][i]==='blankUsername') {
								$('#blankUsername').show();
							}
							else if (data['result'][i]==='userExists') {
								$('#userExists').show();
							}
							if (data['result'][i]==='passwordTooShort') {
								$('#passwordTooShort').show();
							}
							if (data['result'][i]==='blankEmail' || data['result']==='invalidEmail'){
								$('#invalidEmail').show();
							}
						}
						
					}
					// else{
					// 	alert(data['result'])
					// }
					

			});
			
			event.preventDefault();
	})
});