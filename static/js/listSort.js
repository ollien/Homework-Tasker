$(document).ready(function(){
	$('ul#assignmentList').sortable({'axis':'y'});
	$('ul#assignmentList').disableSelection();
	$('ul#assignmentList').on("sortbeforestop",function(event){
		var items = $('ul#assignmentList>li.assignmentItem');
		for (var i=0; i<items.length; i++){
			if (!($(items[i]).hasClass('ui-sortable-placeholder'))){
				console.log($(items[i]).attr('taskId'));
			}
		}
	});
})