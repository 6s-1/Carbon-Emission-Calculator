// api url
const api_url = 
    "http://127.0.0.1:8000/api/get_br_data/laptop-pj0gvm88/power";

// Defining async function
async function getapi(url) {
    
    // Storing response
    const response = await fetch(url);
    
    // Storing data in form of JSON
    var data = await response.json();
    console.log(data);

    // Showing Data
    document.getElementById("power").innerText = data.power;
    document.getElementById("carbon").innerText = data.carbon;
}

// Calling that async function
getapi(api_url);

