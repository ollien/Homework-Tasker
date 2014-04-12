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
					if ($('button#subjectDropDown').hasClass('error')){
						$('button#subjectDropDown').removeClass('error');
					}
					$('#assignmentList').append("<li class='assignmentItem list-group-item' id='assignmentJS"+counter+"' taskId='"+data['assignmentId']+"'><span class='primary'>"+data['assignmentName']+"</span> <br /> <span class='secondary'> "+data['assignmentSubject']+" </span> <span class='deleteContainer'><img class='delete' id='deleteBlkJS"+counter+"' src='/static/img/delete.png' listening='false'/> <img class='deleteRed' id='deleteRed"+counter+"'src='/static/img/deleteRed.png' visibility='hidden' listening='false' /> </span> </li>")
					counter++;
					setupButtons();
					// $('#assignmentList').append("<img src=/static/img/delete.png />")
					$('#assignmentBox').val('');
				}
				else if (data['result']=='noSubject'){
					$('button#subjectDropDown').addClass('error');
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
		$('#addSubjectModal').modal()
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
					$('#subjectSpan').append('<li class="subjectItem" subjectId="'+data['subjectId']+'"><a href="#" onkeydown="if (event.keyCode==13) dropDownSet('+subjectName+','+data['subjectId']+')" onclick="dropDownSet(\''+subjectName+'\',\''+data['subjectId']+'\')">'+subjectName+'</a><span class="delSubjectContainer"><img class="delSubject" id="delSubjectBlkJS'+counter+'" src="/static/img/delete.png" listening="false"/><img class="delSubjectRed" id="delSubjectRedJS'+counter+'" src="/static/img/deleteRed.png" listening="false"></span></li>')
					counter++;
					setupSubjectButtons();
				}
				else{
					alert(data['result'])
				}
			});
		}
	});

});
