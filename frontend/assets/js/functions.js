
//Configs
url = "http://ec2-52-15-166-59.us-east-2.compute.amazonaws.com:8000"

function login(username, password){
	var data = "email="+username+"&pass="+password;

	$.ajax({
	    url : url+"/login",
	    type: "POST",
	    data : data,
	    success: function(data, textStatus, jqXHR)
	    {
	    	if(data['status']==1){
	    		localStorage.setItem("tosemail", username);
	    		localStorage.setItem("toscookie", data['cookie']);
	    		window.location = url;
	    	}
	    	else{
	    		alert("Error signing in. Please try again.");
	    	}
	    },
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

function logout(){
	//Remove cookie
	localStorage.removeItem("toscookie");
	localStorage.removeItem("tosemail");
	window.location = url+"/login";
	/*$.ajax({
	    url : url+"/logout",
	    type: "POST",
	    error: function (jqXHR, textStatus, errorThrown)
	    {
	 		//Catch error in case we want to show a popup dialog
	    }
	});*/
}

function create_user(username, password, email){
	var data = "user="+username+"&pass="+password+"&email="+email;

	$.ajax({
	    url : url+"/signup",
	    type: "POST",
	    data : data,
	    success: function(data, textStatus, jqXHR)
	    {
	    	if(data['status']==1){
	    		localStorage.setItem("tosemail", email);
	    		localStorage.setItem("toscookie", data['user']);
	    		window.location = url;
	    	}
	    	else{
	    		alert("Error signing in. Please try again.");
	    	}
	    },
	    error: function (jqXHR, textStatus, errorThrown)
	    {
	 		//Catch error in case we want to show a popup dialog
	    }
	});
}

function get_user_links(user_email){
	var data = "email="+user_email;

	$.ajax({
	    url : url+"/getlinks",
	    type: "POST",
	    data : data,
	    success: function(data, textStatus, jqXHR)
	    {
	    	if(data['status']==1){
	    		console.log("Data is: "+data['data']);
	    		var userdata = JSON.parse(data['data']);
	    		//Loop through data
	    		for(var i = 0; i < userdata.length; i++){
	    			var category = userdata[i].tag;
	    			console.log("Category: "+category);
		    		$("#"+category).append('<li><div class="md-list-addon-element"><img src="'+userdata[i].image+'" alt="Thumbnail"></div><div class="md-list-content"><a href="'+userdata[i].link+' target="_blank"><span class="md-list-heading">'+userdata[i].title+'</span></a><span class="uk-text-small uk-text-muted">'+userdata[i].text+'</span></div><div style="float:right; position:relative; bottom:30px;"><input id="checkedItem" value="'+userdata[i].title+'" type="checkbox" data-md-icheck /></div></li>');
	    		}

	    	}
	    	else{
	    		alert("Error: Please try again.");
	    	}
	    },
	    error: function (jqXHR, textStatus, errorThrown)
	    {
	 		//Catch error in case we want to show a popup dialog
	    }
	});
}

function get_user_stats(session_id, user_email){

}

function get_link_details(link){
	var data = "link="+link;

	$.ajax({
	    url : url+"/tag",
	    type: "POST",
	    data : data,
	    success: function(data, textStatus, jqXHR)
	    {
	    	if(data['status']==1){
	    		title = data['title'];
	    		text = data['text'];
	    		thumb = data['image'];

	    		$('#preview').show();
	    		$('#plink_title').html(title);
	    		$('#plink_description').html(text);
	    		$('#plink_img').attr("src", thumb);

	    		console.log("Image link: "+thumb);
	    	}
	    	else{
	    		alert("Error: Please try again.");
	    	}
	    },
	    error: function (jqXHR, textStatus, errorThrown)
	    {
	 		//Catch error in case we want to show a popup dialog
	    }
	});
}

function save_user_link(link, email){
	var email = localStorage.getItem('tosemail');
	var data = "link="+link+"&email="+email;

	$.ajax({
	    url : url+"/savelink",
	    type: "POST",
	    data : data,
	    success: function(data, textStatus, jqXHR)
	    {
	    	console.log("Status: "+data['status']);
	    	if(data['status']==1){
	    		//Append to list
	    		var category = data['data']['tag'];
	    		$("#"+category).append('<li><div class="md-list-addon-element"><img src="'+data['data']['image']+'" alt="Thumbnail"></div><div class="md-list-content"><a href="'+data['data']['link']+' target="_blank"><span class="md-list-heading">'+data['data']['title']+'</span></a><span class="uk-text-small uk-text-muted">'+data['data']['text']+'</span></div><div style="float:right; position:relative; bottom:30px;"><input id="checkedItem" value="'+data['data']['title']+'" type="checkbox" data-md-icheck /></div></li>');

                $("#preview").hide();
                $("#link_field").val("");
	    	}
	    	else{
	    		alert("Error: Please try again");
	    	}
            	
            //console.log("Projects: "+totalprojects);
            //console.log("Revenue: "+totalrevenue);
	    },
	    error: function (jqXHR, textStatus, errorThrown)
	    {
	 		//Catch error in case we want to show a popup dialog
	    }
	});
}

function change_user_category(session_id, user_email, link){

}

function change_link_info(newtitle, user_cookie, link, newcategory){
	var data = "cookie="+user_cookie+"&title="+newtitle+"&link="+link+"&category="+newcategory;

	$.ajax({
	    url : url+"/",
	    type: "POST",
	    data : data,
	    success: function(data, textStatus, jqXHR)
	    {
	    	if(data['status']==1){
	    		
	    	}
	    	else{
	    		alert("Error: Please try again.");
	    	}
	    },
	    error: function (jqXHR, textStatus, errorThrown)
	    {
	 		//Catch error in case we want to show a popup dialog
	    }
	});

}

function delete_user_link(user_cookie, link){
	var data = "cookie="+user_cookie+"&link="+link;

	$.ajax({
	    url : url+"/",
	    type: "POST",
	    data : data,
	    success: function(data, textStatus, jqXHR)
	    {
	    	if(data['status']==1){
	    		
	    	}
	    	else{
	    		alert("Error: Please try again.");
	    	}
	    },
	    error: function (jqXHR, textStatus, errorThrown)
	    {
	 		//Catch error in case we want to show a popup dialog
	    }
	});
}

