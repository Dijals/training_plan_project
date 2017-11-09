(function () {

	//$(".training-data").hide()

	var default_provider_value = $( "#provider" ).val();
	var default_training_type_value = $( "#training_type" ).val(); 

	var provider_value = $( "#provider" ).val(); // provider select value
	var training_type_value = $( "#training_type" ).val(); // training select value 

	

	$( "#provider" ).change(function() {
	   provider_value = $(this).val()
	   $(".training-data").hide()
	   show_training_info()
	});


	$( "#training_type" ).change(function() {
	   training_type_value = $(this).val()

	   $(".training-data").hide()
	  	show_training_info()

	});


	function show_training_info() {
		//TODO put this in a single function
	   	var providers_parent =[]; 
		var training_type_parent = [];

	   
	   $('.provider_td').each(function() {
	   		if($(this).text() == provider_value){
	   			providers_parent.push($(this).parent())
	   			
	   		}
		})

	   $('.training_td').each(function() {
	   		if($(this).text() == training_type_value){
	   			training_type_parent.push($(this).parent())
	   		}
		})

	   if(provider_value != default_provider_value && training_type_value == default_training_type_value){
	   		for (var i = providers_parent.length - 1; i >= 0; i--) {
	   			providers_parent[i].show()
	   		}
	   } else if (provider_value != default_provider_value && training_type_value != default_training_type_value){
	   		for (var i = providers_parent.length - 1; i >= 0; i--) {
	   			providers_parent[i].each(function(){
	   				if(training_type_value == $(this).find( ".training_td" ).text()){
	   					providers_parent[i].show()
	   				}
	   			})
	   		}
	   } else if (training_type_value != default_training_type_value && provider_value == default_provider_value) {

	   		for (var i = training_type_parent.length - 1; i >= 0; i--) {
	   			training_type_parent[i].show()
	   		}

	   } else if (training_type_value == default_training_type_value && provider_value == default_provider_value) {
	   		$(".training-data").show()
	   }

	}



})();