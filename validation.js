document.getElementById('emailForm').addEventListener('submit', function(event) {
    event.preventDefault();
    validateEmail();
});

function validateEmail() {
    const emailInput = document.getElementById('email');
    const errorMessage = document.getElementById('error-message');
    const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

    if (emailPattern.test(emailInput.value)) {
        errorMessage.style.display = 'none';
        alert('Email is valid');
        // You can proceed with form submission or other actions here
    } else {
        errorMessage.style.display = 'inline';
    }
}