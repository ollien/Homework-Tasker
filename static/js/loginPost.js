$(document).ready(function(){
	$('#loginForm').submit(function(event){
		$.post('/loginInput/',{
			'username':$('#usernameInput').val(),
			'password':$('#passwordInput').val(),
			'persist':$('#rememberBox').prop('checked'),
			'csrfmiddlewaretoken':$("#loginForm>input[name='csrfmiddlewaretoken']").val()},
			function(data){
				data=$.parseJSON(data);
				if(data['result']==='OK'){
					location.reload()
				}
				else{
					if ($("invalid").is("visible")){
						$("#invalid").css("visibility", "visible").hide().fadeIn(75);
					}
					else{
						$("#invalid").css("visibility", "visible").hide().fadeIn(150);
					}
				}
		});
		 
		event.preventDefault();
	});
});