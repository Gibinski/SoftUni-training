function colorize() {
    const evenTds = document.querySelectorAll("tr:nth-child(even) > td");
    for (let td of evenTds) {
        td.setAttribute("style", "background:teal");
    }
}