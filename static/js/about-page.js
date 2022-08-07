var coll = document.getElementsByClassName("content-heading");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    var timeout = setTimeout(function () {;});
    var content = this.nextElementSibling;
    var contentCollIndicator = this.getElementsByClassName("content-coll-indicator")[0];
    var indicatorContainer = contentCollIndicator.getElementsByClassName("center-text-container")[0];
    if (this.classList.contains("active")) {
      content.style.maxHeight = content.scrollHeight + "px";
      clearTimeout(timeout);
      timeout = setTimeout(function () {;});
      indicatorContainer.innerText = "+";
      var item = this;
      content.style.paddingBottom = "0px";
      content.style.maxHeight = "0px";
      item.classList.toggle("active");
    } else {
      indicatorContainer.innerText = "-";
      content.style.maxHeight = content.scrollHeight + "px";
      var item = this;
      content.style.paddingBottom = "2em";
      timeout = setTimeout(function () {
        content.style.maxHeight = "none";
        item.classList.toggle("active");
      }, 200);
    }
  });
}