const apiUrl = 'http://127.0.0.1:8000/generate';

function getImage(imageId){
    fetch(apiUrl)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.blob();
        })
        .then(blob => {
            const imageUrl = URL.createObjectURL(blob);
            const imgElement = document.getElementById(imageId);
            imgElement.src = imageUrl;
        })
        .catch(error => {
            console.error('Error:', error);
        });
}