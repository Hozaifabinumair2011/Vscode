function validateForm() {
    var x = document.forms["Myform"]["fname"].value;
    if (x == " ") {
        alert("name not found");
        return false;
    }
}