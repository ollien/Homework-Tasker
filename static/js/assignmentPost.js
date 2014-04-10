$(document).ready(function(){
	var counter=0;
	$('#addButton').click(function(event){
		if ($('#assignmentBox').val()!=""){
			$.post('/addAssignment/',{
				'name':$('#assignmentBox').val(),
				 'subjectId':$('button#subjectDropDown').attr('currentsubjectid'),
				'csrfmiddlewaretoken':$("input[name='csrfmiddlewaretoken']").val()
			},function(data){
				data=$.parseJSON(data);
				if (data['result']==='OK'){
					$('#assignmentList').append("<li id='assignmentJS"+counter+"' taskId='"+data['assignmentId']+"'>"+data['assignmentName']+" | "+data['assignmentSubject']+" <span class='deleteContainer'><img class='delete' id='deleteBlkJS"+counter+"' src='/static/img/delete.png' listening='false'/> <img class='deleteRed' id='deleteRed"+counter+"'src='/static/img/deleteRed.png' visibility='hidden' listening='false' /> </span> </li>")
					setupButtons();
					// $('#assignmentList').append("<img src=/static/img/delete.png />")
					$('#assignmentBox').val('');
				}
				else{
					alert(data['result'])
				}
			});
		}

});
	$('#assignmentBox, #subjects').keydown(function(event){
		if (event.which===13){
			$('#addButton').click();	
		}
	});
	
	// $('img[class*=delete]').click(function(event){
	// 	var li = $(this).parent().parent();
	// 	var id = li.attr('taskId')
	// 	$.post('/removeAssignment/',{
	// 		'taskId':id,
	// 		'csrfmiddlewaretoken':$("input[name='csrfmiddlewaretoken']").val()
	// 		},function(data){
	// 		data=$.parseJSON(data);
	// 		if (data['result']=='OK'){
	// 			li.fadeOut(function(){li.remove()});
	// 			// console.log($(this).parent().parent();
	// 			console.log('removed');
	// 		}
	// 		else{
	// 			alert(data['result']);
	// 		}
	// 	});
	// 	
	// });
	$('li#addSubject').click(function(){
		$('#subjectInput').val('');
		$('#myModal').modal()
	});
	$('#subjectInput').keydown(function(event){
		if (event.which==13){
			$('#saveSubject').click();	
		}
	});
	$('#saveSubject').click(function(event){
		var subjectName=$('#subjectInput').val()
		if (subjectName!=''){
			$.post("/addSubject/",{
				'subjectName':subjectName,
				'csrfmiddlewaretoken':$("input[name='csrfmiddlewaretoken']").val()
			}, function(data){
				data=$.parseJSON(data);
				if (data['result']=='OK'){
					$('#subjectSpan').append('<li class="subjectItem" subjectId="'+data['subjectId']+'"><a href="#" onkeydown="if (event.keyCode==13) dropDownSet('+subjectName+')" onclick="dropDownSet(\''+subjectName+'\',\''+$('button#subjectDropDown').attr('currentSubjectId')+'\')">'+subjectName+'</a></li>')
				}
				else{
					alert(data['result'])
				}
			});
		}
	});

});
