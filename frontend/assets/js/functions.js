
//Configs
url = "ec2-52-15-166-59.us-east-2.compute.amazonaws.com"

function login(username, password){
	var data = "email="+username+"&pass="+password;

	$.ajax({
	    url : url+"/login",
	    type: "POST",
	    data : data,
	    /*success: function(data, textStatus, jqXHR)
	    {
	    	if(data['status']==1){
	    		localeStorage.setItem("tosemail", username);
	    	}
	    	else{

	    	}
	        cookie = data['cookie'];
            	
            //console.log("Projects: "+totalprojects);
            //console.log("Revenue: "+totalrevenue);
	    },*/
	    error: function (jqXHR, textStatus, errorThrown)
	    {
	 		//Catch error in case we want to show a popup dialog
	    }
	});

	/*$.when(
		
	).then(function () {
		$("#projects").html(totalprojects);
		$("#revenue").html("$"+totalrevenue.toLocaleString()+" (billion)");
	});*/

}

function create_user(username, password, email){
	var data = "user="+username+"&pass="+password+"&email="+email;

	$.ajax({
	    url : url+"/signup",
	    type: "POST",
	    data : data,
	    /*success: function(data, textStatus, jqXHR)
	    {
	    	if(data['status']==1){
	    		localeStorage.setItem("tosemail", username);
	    	}
	    	else{

	    	}
	        cookie = data['cookie'];
            	
            //console.log("Projects: "+totalprojects);
            //console.log("Revenue: "+totalrevenue);
	    },*/
	    error: function (jqXHR, textStatus, errorThrown)
	    {
	 		//Catch error in case we want to show a popup dialog
	    }
	});
}

function get_user_links(session_id, user_email){

}

function get_user_stats(session_id, user_email){

}

function get_link_details(session, user_email){

}

function change_user_category(session_id, user_email, link){

}

function change_link_info(session_id, user_email, link){

}

function delete_user_link(session_id, user_email, link){

}

