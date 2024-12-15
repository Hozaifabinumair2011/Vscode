function getHistroy() {
    return document.getElementById("history-value").innerText;
}
function printHistroy(num) {
    document.getElementById("history-value").innerText = num;
}
function getoutput() {
    return document.getElementById("output-value").innerText;
}
function printoutput(num) {
    if (num == "") {
        document.getElementById("output-value").innerText = num;
    }
    else {
        document.getElementById("output-value").innerText = getFormattedNumber(num);
    }
}