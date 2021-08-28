function registerCheck (event) {
	const username = document.getElementById("username");
	const password = document.getElementById("password");
	const confirm = document.getElementById("c_password");
	const confirmError = document.getElementById("confirmerror");
	if (!username.validity.valid) {
			showError();
			event.preventDefault();
		}
	if (!password.validity.valid) {
			showError();
			event.preventDefault();
	}
	if (!confirm.validity.valid) {
			showError();
			event.preventDefault();
	}
	if(password.value != confirm.value)
	{
		showError();
		event.preventDefault();
	}

}

function loginCheck (event) {
	const username = document.getElementById("username");
	const password = document.getElementById("password");
	if (!username.validity.valid) {
			showError();
			event.preventDefault();
		}
	if (!password.validity.valid) {
			showError();
			event.preventDefault();
	}
}

function checker () {
	const form = document.getElementById("loginForm");
	const username = document.getElementById("username");
	const password = document.getElementById("password");
	const confirm = document.getElementById("c_password");
	const nameError = document.getElementById("nameerror");
	const passError = document.getElementById("passerror");
	const confirmError = document.getElementById("confirmerror");

	username.addEventListener('input', function (event) {
		if (username.validity.valid) {
			nameError.textContent = '';
		} else {
			showError();
		}
	});

	password.addEventListener('input', function (event) {
		if (password.validity.valid) {
			passError.textContent = '';
		} else {
			showError();
		}
	});

	if (confirm != null)
	{
		confirm.addEventListener('input', function (event) {
			if (confirm.validity.valid) {
				confirmError.textContent = '';
			} else {
				showError();
			}
		});
	}
}

function showError () {
	const username = document.getElementById("username");
	const password = document.getElementById("password");
	const confirm = document.getElementById("c_password");
	const nameError = document.getElementById("nameerror");
	const passError = document.getElementById("passerror");
	const confirmError = document.getElementById("confirmerror");

	if (username.validity.tooShort)
	{
		nameError.textContent = "Value in field is too short!";
	}
	else if (username.validity.tooLong)
	{
		nameError.textContent = "Value in field is too long!";
	}
	else if (username.validity.valueMissing)
	{
		nameError.textContent = "This field can't be empty";
	}

	if (password.validity.tooShort)
	{
		passError.textContent = "Value in field is too short!";
	}
	else if (password.validity.tooLong)
	{
		passError.textContent = "Value in password field is too long!";
	}
	else if (password.validity.valueMissing)
	{
		passError.textContent = "This field can't be empty";
	}

	if (confirm != null)
	{
		if (confirm.validity.tooShort)
		{
			confirmError.textContent = "Value in field is too short!";
		}
		else if (confirm.validity.tooLong)
		{
			confirmError.textContent = "Value in field is too long!";
		}
		else if (confirm.validity.valueMissing)
		{
			confirmError.textContent = "This field can't be empty";
		}
		else if (!confirm.validity.valueMissing)
		{
			if (password.value != confirm.value)
			{
				confirmError.textContent = "The passwords don't match";
			}
			else
			{
				confirmError.textContent = "";
			}
		}
	}
}