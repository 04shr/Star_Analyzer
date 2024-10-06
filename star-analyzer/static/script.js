// Function to fetch star details based on selected star type
function fetchStarDetails() {
    const starType = document.getElementById('star-type').value;

    if (starType === "") {
        alert("Please select a star type.");
        return;
    }

    const data = {
        star_type: starType
    };

    fetch('/star-details', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        const detailsDiv = document.getElementById('star-details');

        if (result.error) {
            detailsDiv.innerHTML = `<p>Error: ${result.error}</p>`;
        } else {
            detailsDiv.innerHTML = `
                <p><strong>Temperature (K):</strong> ${result.temperature}</p>
                <p><strong>Luminosity (L/Lo):</strong> ${result.luminosity}</p>
                <p><strong>Radius (R/Ro):</strong> ${result.radius}</p>
                <p><strong>Star Color:</strong> ${result.star_color}</p>
                <p><strong>Spectral Class:</strong> ${result.spectral_class}</p>
                <p><strong>Description:</strong> ${result.description}</p>
            `;
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}


