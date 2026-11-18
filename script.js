let form = document.querySelector("#main-form");

/* Source - https://stackoverflow.com/a/64908345
 * Posted by Stelios333, modified by community. See post 'Timeline' for change history
 * Retrieved 2026-11-16, License - CC BY-SA 4.0
 */
function download(content, mimeType, filename) {
    const a = document.createElement('a') // Create "a" element
    const blob = new Blob([content], {type: mimeType}) // Create a blob (file-like object)
    const url = URL.createObjectURL(blob) // Create an object URL from blob
    a.setAttribute('href', url) // Set "a" element link
    a.setAttribute('download', filename) // Set download filename
    a.click() // Start downloading
}


/**
 * Compile the UUID: Name associaitions into a json file and prompt the user with Save As download
 */
function compileAndDownloadJSON() {
    let name_data = {};
    let inputs = form.querySelectorAll("input[type=text]");
    inputs.forEach(input => {
        let uuid = input.id;
        let name = input.value;
        name_data[uuid] = name;
    });
    download(JSON.stringify(name_data), "text/json", "game_names.json")
}

function handleForm(event) {
    event.preventDefault();
    compileAndDownloadJSON();
}

function makeSectionDiv() {
    const section = form.appendChild(document.createElement("div"));
    section.classList.add("form-section");
    return section
}

function generateSectionForImage(gameID, gameName, imagePath) {
    //const fragment = document.createDocumentFragment();
    const section = makeSectionDiv();
    const label = section.appendChild(document.createElement("label"))
    label.setAttribute("for", gameID);
    const img = label.appendChild(document.createElement("img"))
    img.setAttribute("src", `/read?path=${imagePath}`)
    const input = section.appendChild(document.createElement("input"));
    input.setAttribute("type", "text");
    input.value = gameName;
    input.setAttribute("id", gameID);
    input.setAttribute("name", gameID);
}

function populateList(image_data, name_data) {
    for (const [gameID, url] of Object.entries(image_data)) {
        generateSectionForImage(gameID, name_data[gameID], url)
    }
    const submitSection = makeSectionDiv();
    const submit = submitSection.appendChild(document.createElement("input"));
    submit.type = "submit"
    submit.value = "Save"
    form.addEventListener('submit', handleForm);
}

async function load() {
    let image_json_data = await (await fetch("./game_images.json")).json();
    let names_json_data = await (await fetch("./game_names.json")).json();
    populateList(image_json_data, names_json_data)
}

load();

