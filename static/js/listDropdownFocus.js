$(document).ready(function(){
	$('img[id*=delete]').on('dragstart',function(event){event.preventDefault()});
	$('li.subjectItem').keydown(function(event){
		if (event.which==13){
			$('#addButton').focus();
			$('#subjectDropDown').attr('chosen','true')
			event.preventDefault();
		}
	});
	$('li.subjectItem').click(function(){
		$('#subjectDropDown').attr('chosen','true')
	});
});

function dropDownSet(name,uid){
	$('#subjectDropDown').html(name+' <span class="caret"></span>').attr('currentsubjectid',uid)
	console.log(name);
}
