var button = $('#append-button');

console.log(button);
var message = "message";
button.click(function(){

	var myText = $('<p>', {
		'html':message,
		'css': 'large-text blue'
	});

	console.log(myText);
	$('#text-container').append(myText);
});

  // dog ceo api

var dogImageButton = $('#get-dog-image');

function getImageLink(image_link){
	$('#dog-random-image').attr('src', image_link);
}
function getImage(){
	$.ajax({
		type: 'get',
		url: 'https://dog.ceo/api/breeds/image/random',
		success: function(responseData){
			getImageLink(responseData.message);
		},
		error: function(){
			console.log('no ennterner Connection');
		}
	});
}
dogImageButton.click(function(){
	getImage();
});

    // nasa api
function createImage(imageLink){

	// create a tag in memory
	let newImg = $('<img>', {
		'src': imageLink
	});

	// append it to the grid
	$('#image-grid').append(newImg);
}

// get the form
var marsForm = $('#mars-form');

// do something on submit
marsForm.submit(function(event){
	// prevent the default behaviour of the form
	event.preventDefault();


	// send an ajax request to fetch the list of images
	$.ajax({
		type: 'get',
		url: 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos',
		// data is query params for get request
		data: {
			sol: $('#sol').val(),
			page: $('#page').val(),
			api_key: 'a09okZbcZXz0kCABkMkpx66DjkEc2SoAyJTAIXgw'
		},
		// on receiving data successfully, empty the grid and add new images
		success: function(responseData){
			let photos = responseData.photos;
			$('#image-grid').empty();
			for (let i = 0; i < photos.length; i++){
				createImage(photos[i].img_src);
			}


		},
		// in case of an error, handle here
		error: function(){
			console.log('some error');
		}


	});
});
