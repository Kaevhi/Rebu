let htmlPrint = '';
let institutionExtras = ''; // Variable to store the additional content for "Institution" input

function handleSelectClick(type) {
    const selectElement = document.getElementById(`${type}-num`);
    const selectedValue = selectElement.value;

    if (selectedValue === "other") {
        htmlPrint = `<div><input type="text" placeholder="Number" id="${type}-inserts"></div>`;
       
        document.querySelector(`.${type}-output`).innerHTML = htmlPrint;
    } 
    else if(selectedValue === "1"){
        htmlPrint = `<div><input type="text" placeholder="Enter" id="${type}-inserts"></div>`;
       
        document.querySelector(`.${type}-output`).innerHTML = htmlPrint;
    }
    else if(selectedValue === "2"){
        for(let i = 0; i < 2; i++){
        htmlPrint = `<div><input type="text" placeholder="Enter
        " id="${type}-inserts"></div><div><input type="text" placeholder="Institution" id="${type}-inserts"></div>`;
       
        document.querySelector(`.${type}-output`).innerHTML = htmlPrint;
        }
    }
    else if(selectedValue === "3"){
        for(let i = 0; i < 3; i++){
        htmlPrint = `<div><input type="text" placeholder="Institution" id="${type}-inserts"></div><div><input type="text" placeholder="Institution" id="${type}-inserts"></div><div><input type="text" placeholder="Institution" id="${type}-inserts"></div>`;
        document.querySelector(`.${type}-output`).innerHTML = htmlPrint;
        }
    }

    // Handle the "Institution" input with additional content
    if ((type === "institution") && (selectedValue === "1" || selectedValue === "2" || selectedValue === "3")) {
        const numInserts = parseInt(selectedValue);

        institutionExtras = ''; // Clear previous content
        for (let i = 0; i < numInserts; i++) {
            institutionExtras += `<div>
            <input type="text" placeholder="Institution" id="${type}-inserts">
            Start:<input type="date">
            End:<input type="date">
            <p>Did you graduate from this institution?</p>
            Yes<input type="radio" name="graduate">
            No<input type="radio" name="graduate">
        </div>`;
        }
    } else {
        institutionExtras = ''; // Clear previous content
    }

    document.querySelector(`.${type}-output`).innerHTML = htmlPrint + institutionExtras;
}
