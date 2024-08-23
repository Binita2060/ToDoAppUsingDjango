document.addEventListener('DOMContentLoaded', function() {
    var contactForm = document.getElementById('contactForm');
    
    contactForm.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the default form submission

        // Show the modal
        $('#thankYouModal').modal('show');

        // Optionally, send form data to the server
        var formData = new FormData(contactForm);
        fetch('/your-server-endpoint/', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    });
});
