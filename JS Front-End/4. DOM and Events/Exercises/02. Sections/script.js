function create(words) {
   const content = document.getElementById("content");
   for (const text of words) {
      let div = document.createElement("div");
      let p = document.createElement("p");
      p.textContent = text;
      p.setAttribute("style", "display:none");
      div.appendChild(p);
      div.addEventListener("click", clicked);
      content.appendChild(div);
   }
   function clicked(e) {
      const div = this;
      div.querySelector("p").setAttribute("style", "display:block");
   }
}