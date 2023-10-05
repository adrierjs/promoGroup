let name_validation = false
let email_validation = false
let senha_validation = false
let senha_confirmar_validation = false

let form = document.querySelector('#form');
form.addEventListener('submit', function(event) {
  event.preventDefault();
  validar_form();
});




function nameValidation() {
    let nomeInput = document.querySelector('input[name="nome"]');
    let value = nomeInput.value;
    if (/\d/.test(value)) {
        nomeInput.setCustomValidity('Não insira números');
    } else {
        nomeInput.setCustomValidity('');
        name_validation = true
    }
}

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

function passwordMatchValidation() {
    var passwordInput = document.getElementById('password');
    var confirmPasswordInput = document.querySelector('input[name="confirmPassword"]');
    if (passwordInput.value !== confirmPasswordInput.value) {
        confirmPasswordInput.setCustomValidity('As senhas não coincidem');
    } else {
        confirmPasswordInput.setCustomValidity('');
        senha_confirmar_validation = true
    }
}

document.querySelector('#form').addEventListener('submit', function(event) {
    if (!this.checkValidity()) {
        event.preventDefault();
    } else {
        showTermsError();
    }
});

function show(){
    UIkit.notification({
        message: 'Cadastrado com sucesso',
        status: 'success',
        pos: 'top-right',
        timeout: 5000
    });
}

function validar_form() {
    nameValidation();
    emailValidation();
    passwordValidation();
    passwordMatchValidation();
  
    if (name_validation && email_validation && senha_validation && senha_confirmar_validation) {
      show();
      setTimeout(function () {
        form.submit();
      }, 1000);
      return true;
    }
  }







  