function copyText() {
    let copyText = document.getElementById("result").textContent;
    navigator.clipboard.writeText(copyText).then(function () {
        console.log("Text copied to clipboard");
    }, function () {
        console.error("Error copying text to clipboard");
    });
}
