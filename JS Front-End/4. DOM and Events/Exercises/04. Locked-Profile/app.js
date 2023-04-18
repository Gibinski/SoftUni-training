function lockedProfile() {
    const buttons = Array.from(document.getElementsByTagName("button"));

    for (const button of buttons) {
        button.addEventListener("click", toggleInformation);
    }

    function toggleInformation(e) {
        const btn = this;
        const profile = Array.from(btn.parentElement.children);
        const userHiddenFields = profile[9];
        const unlock = profile[4];
        
        if (unlock.checked) {
            if (btn.textContent === "Show more") {
                userHiddenFields.style.display = "block";
                btn.textContent = "Hide it";
            } else {
                userHiddenFields.style.display = "none";
                btn.textContent = "Show more";
            }
        }     
    }
}