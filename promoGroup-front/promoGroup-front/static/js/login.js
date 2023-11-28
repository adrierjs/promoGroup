function emailValidation() {
    var emailInput = document.querySelector('input[name="email"]');
    var value = emailInput.value;
    if (!/^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/.test(value)) {
        emailInput.setCustomValidity('Insira um email válido');
    } else {
        emailInput.setCustomValidity('');
        email_validation = true
    }
}

function passwordValidation() {
    let passwordInput = document.getElementById('password');
    let value = passwordInput.value;
    if (value.length < 8) {
        passwordInput.setCustomValidity('Insira pelo menos 8 caracteres');
    } else {
        passwordInput.setCustomValidity('');
        senha_validation = true
    }
}

const password = document.getElementById('password');
const togglePassword = document.getElementById('togglePassword');

togglePassword.addEventListener('click', function (event) {
    event.preventDefault();
    if (password.type === 'password') {
        password.type = 'text';
        togglePassword.setAttribute('uk-icon', 'icon: unlock');
    } else {
        password.type = 'password';
        togglePassword.setAttribute('uk-icon', 'icon: lock');
    }
});