$(document).ready(function(){
	$('ul#assignmentList').sortable({'axis':'y'});
	$('ul#assignmentList').disableSelection();
	$('ul#assignmentList').on("sortbeforestop",function(event){
		var items = $('ul#assignmentList>li.assignmentItem');
		var ids = []
		for (var i=0; i<items.length; i++){
			if (!($(items[i]).hasClass('ui-sortable-placeholder'))){
				ids.push($(items[i]).attr('taskId'))
			}
		}
		console.log(ids);
		$.post('/sortTasks/',
		{
			'taskIds':ids,
			'csrfmiddlewaretoken':$("input[name='csrfmiddlewaretoken']").val()
		},
		function(data){
			
		});
	});
})