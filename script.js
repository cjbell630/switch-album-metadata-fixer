let list = document.querySelector("#main-form");

function generateFormSection(gameID, imagePath){
    //const fragment = document.createDocumentFragment();
    const section = list.appendChild(document.createElement("div"));
    section.classList.add("form-section");
    const label = section.appendChild(document.createElement("label"))
    label.setAttribute("for", gameID);
    const img = label.appendChild(document.createElement("img"))
    img.setAttribute("src", `/read?path=${imagePath}`)
    const input = section.appendChild(document.createElement("input"));
    input.setAttribute("type", "text");
    input.setAttribute("id", gameID);
    input.setAttribute("name", gameID);
}

function populateList(data){
    for (const [gameID, url] of Object.entries(data)) {
        generateFormSection(gameID, url)
    }
}

fetch("./game_images.json")
    .then(res => res.json())
    .then(data => {
        populateList(data)
    });

