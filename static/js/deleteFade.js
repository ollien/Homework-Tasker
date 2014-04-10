function setupButtons(){
	var imgs=$('img[id*=delete]')
	for (var i=0; i<imgs.length; i++){
		if ($(imgs[i]).attr('listening')==='false'){
				$('img.deleteRed').hide();
				$(imgs[i]).hover(function(){
					var button=$(this).parent().children('.deleteRed')
					button.stop(true,true).fadeToggle()
					// console.log(imgs[i].parent().children('img.deleteRed'))
					console.log("hover");
				});
				$(imgs[i]).click(function(event){
					var li = $(this).parent().parent();
					console.log(li)
					var id = li.attr('taskId')
					console.log(id)
					$(this).unbind(event)
					$.post('/removeAssignment/',{
						'taskId':id,
						'csrfmiddlewaretoken':$("input[name='csrfmiddlewaretoken']").val()
						},function(data){
						data=$.parseJSON(data);
						if (data['result']=='OK'){
							li.fadeOut(function(){li.remove()});
							// console.log($(this).parent().parent();
							console.log('removed');
						}
						else{
							alert(data['result']);
						}
					});
					
				});
				$(imgs[i]).attr('listening','true')
			}	
	}
}

$(document).ready(function(){
	// // alert(counter);
	// $('img.deleteRed').hide();
	// $('img[id*=delete]').hover(function(){
	// 	var delButton=$(this).parent().children('.deleteRed')
	// 	delButton.stop(true,true).fadeToggle()
	// });
	setupButtons()
});
