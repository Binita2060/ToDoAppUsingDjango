document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM fully loaded and parsed');

    const contactForm = document.getElementById('contactForm');
    if (!contactForm) {
        console.error('Contact form not found!');
        return;
    }

    contactForm.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the default form submission

        // Display a success message using a Bootstrap modal
        const thankYouModal = new bootstrap.Modal(document.getElementById('thankYouModal'));
        thankYouModal.show();

        // Optionally, send form data to the server
        const formData = new FormData(contactForm);
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
