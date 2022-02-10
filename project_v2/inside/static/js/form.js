$(document).ready(function() {

	$('form').on('submit', function(event) {

		$.ajax({
			data : {
				name : $('#test').val(),
			},
			type : 'POST',
			url : '/process'
		})
		.done(function(data) {
			
			
			if (data.test) {

				$('#successAlert').text(data.name).show();
			}
			else {
				$('#successAlert').hide();
				$('#errorAlert').hide();
			}

		});

		event.preventDefault();

	});

});