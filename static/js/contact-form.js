var coll = document.getElementsByClassName("form-control");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    if (!this.classList.contains("active")) this.classList.toggle("active");
  });
}