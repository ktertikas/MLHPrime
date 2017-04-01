
//Configs
url = "url/here"

function login(username, password){
	var totalprojects;
	var totalrevenue;
	var data = "department="+dept+"&dateFrom="+dateFrom+"&dateTo="+dateTo;

	$.when(
		$.ajax({
	    url : url+"",
	    type: "POST",
	    data : data,
	    success: function(data, textStatus, jqXHR)
	    {
	        totalprojects = data['projects'];
            totalrevenue = data['revenue'] / 1000;
            	
            //console.log("Projects: "+totalprojects);
            //console.log("Revenue: "+totalrevenue);
	    },
	    error: function (jqXHR, textStatus, errorThrown)
	    {
	 		//Catch error in case we want to show a popup dialog
	    }
	})
	).then(function () {
		$("#projects").html(totalprojects);
		$("#revenue").html("$"+totalrevenue.toLocaleString()+" (billion)");
	});

}

function create_user(username, password, email){

}

function get_user_links(session_id, user_email){

}

function get_user_stats(session_id, user_email){

}

function change_user_category(session_id, user_email, link){

}

function change_link_info(session_id, user_email, link){

}

function delete_user_link(session_id, user_email, link){

}

