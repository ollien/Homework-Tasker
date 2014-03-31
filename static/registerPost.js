$(document).ready(function(){
	// $(document).on('click','#registerButton',function(){
		$('#registerForm').submit(function(event){
			
			$.post('/registerInput/',{
				'username':$('#usernameInput').val(),
				'password':$('#passwordInput').val(),
				'email':$('#emailInput').val(),
				'csrfmiddlewaretoken':$("#loginForm>input[name='csrfmiddlewaretoken']").val()
				},function(data){
					alert(data);
			});
			
			event.preventDefault();
	})
});