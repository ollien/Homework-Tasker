$(document).ready(function(){
	$('#loginForm').submit(function(event){
		$.post('/loginInput/',{
			'username':$('#usernameInput').val(),
			'password':$('#passwordInput').val(),
			'csrfmiddlewaretoken':$("#loginForm>input[name='csrfmiddlewaretoken']").val()},
			function(data){
				alert(data);
		});
		
		event.preventDefault();

	});
});