function toggle() {
    const button = document.getElementsByClassName("button")[0];
    const extra = document.getElementById("extra");
    if (extra.style.display === "none") {
        button.textContent = "Less";
        extra.style.display = "block";
    } else {
        button.textContent = "More";
        extra.style.display = "none";
    }
}