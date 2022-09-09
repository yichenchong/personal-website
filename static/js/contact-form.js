var coll = document.getElementsByClassName("form-control");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    if (!this.classList.contains("active")) this.classList.toggle("active");
  });
}


let emailRegex = /[a-z0-9]+@[a-z]+(\.[a-z]{2,3})+/;

function invalidEmail(valError) {
  valError.textContent = "Invalid email address";
  valError.style.display = "block";
  console.log("email invalid");
  return false;
}

function invalidCheckbox(valError) {
  valError.textContent = "Please tick the \"I am human\" checkbox";
  valError.style.display = "block";
  console.log("checkbox not ticked");
  return false;
}

function validateForm() {
  let form = document.forms["contact-form"];
  var valError = document.getElementsByClassName("validation-error")[0];
  var email = form["contact-email-field"];
  var emailVal = email.value.trim();
  if (!emailRegex.test(emailVal)) return invalidEmail(valError);
  var checkbox = document.getElementsByClassName("robot-checkbox")[0];
  if (!checkbox.checked) return invalidCheckbox(valError);
  valError.style.display = "none";
  return true;
}