const loginForm = document.getElementById('login-form');
const signupForm = document.getElementById('signup-form');
const toggleForm = document.getElementById('toggle-form');

toggleForm.addEventListener('click', function() {
    if (loginForm.style.display === 'block') {
        loginForm.style.display = 'none';
        signupForm.style.display = 'block';
        toggleForm.innerHTML = "Already a member? <a href='#'>Login</a>";
    } else {
        loginForm.style.display = 'block';
        signupForm.style.display = 'none';
        toggleForm.innerHTML = "Not a member? <a href='#'>Signup</a>";
    }
});