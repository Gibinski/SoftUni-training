function solve() {
  const exercise = document.getElementById("exercise");
  const [textareaGenerate, textareaBuy] = Array.from(exercise.querySelectorAll("textarea"));
  const [btnGenerate, btnBuy] = Array.from(exercise.querySelectorAll("button"));
  const tbody = exercise.querySelector(".table > tbody");
  
  btnGenerate.addEventListener("click", generated);
  btnBuy.addEventListener("click", buying)


  function generated() {
    const data = JSON.parse(textareaGenerate.value);
    console.log("CLICK");
    
    for (const {img, name, price, decFactor} of data) {
      const tableRow = createElement("tr", "", tbody);
      const firstColumnTd = createElement("td", "", tableRow);
      createElement("img", "", firstColumnTd, "", "", {src: img});      
      const secondColumnTd = createElement("td", "", tableRow);
      createElement("p", name, secondColumnTd);      
      const thirdColumnTd = createElement("td", "", tableRow);
      createElement("p", price, thirdColumnTd);      
      const fordColumnTd = createElement("td", "", tableRow);
      createElement("p", decFactor, fordColumnTd);      
      const fiftColumnTd = createElement("td", "", tableRow);
      createElement("input", "", fiftColumnTd, "", "", {type: "checkbox"});      
    }
  }
  
  function buying(e) {
    const btn = this;
    console.log("I buy!");
  }

}

// type = str
// content = str
// id = str
// classes = arry of str
// attributes = obj
function createElement(type, content, parentNode, id, classes, attributes) {
  const htmlElement = document.createElement(type);
  
  if (content && type !== 'input') {
    htmlElement.textContent = content;
  }
  
  if (content && type === 'input') {
    htmlElement.value = content; 
  }
  
  if (id) {
    htmlElement.id = id;
  }
  
  // ["list", "item"]
  if (classes) {
    htmlElement.classList.add(...classes);
  }
  
  console.log(parentNode)
  if (parentNode) {
    parentNode.appendChild(htmlElement);
  }

  // src: "link to img", href: "link to site"
  if (attributes) {
    for (const key in attributes)
    htmlElement.setAttribute(key, attributes[key])
  }

  return htmlElement
}