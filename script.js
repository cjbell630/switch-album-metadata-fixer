let list = document.querySelector("#main-form");

function makeSectionDiv() {
    const section = list.appendChild(document.createElement("div"));
    section.classList.add("form-section");
    return section
}

function generateSectionForImage(gameID, imagePath) {
    //const fragment = document.createDocumentFragment();
    const section = makeSectionDiv();
    const label = section.appendChild(document.createElement("label"))
    label.setAttribute("for", gameID);
    const img = label.appendChild(document.createElement("img"))
    img.setAttribute("src", `/read?path=${imagePath}`)
    const input = section.appendChild(document.createElement("input"));
    input.setAttribute("type", "text");
    input.setAttribute("id", gameID);
    input.setAttribute("name", gameID);
}

function populateList(data) {
    for (const [gameID, url] of Object.entries(data)) {
        generateSectionForImage(gameID, url)
    }
    const submitSection = makeSectionDiv();
    const button = submitSection.appendChild(document.createElement("button"));
    // TODO onclick download json
}

/**
 * Compile the UUID: Name associaitions into a json file and prompt the user with Save As download
 */
function compileJSON() {
    // TODO
}

fetch("./game_images.json")
    .then(res => res.json())
    .then(data => {
        populateList(data)
    });

