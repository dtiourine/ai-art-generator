document.addEventListener('DOMContentLoaded', function() {
    const generateBtn = document.getElementById('generate-btn');
    const downloadBtn = document.getElementById('download-btn');
    const imageContainer = document.getElementById('image-container');
    const placeholderText = document.getElementById('placeholder-text');
    const generatedImage = document.getElementById('generated-image');
    const loadingIndicator = document.getElementById('loading-indicator');
    const gallery = document.getElementById('gallery');

    // Store the current base64 image data
    let currentImageData = null;

    // Array to store generated images (in a real app, these would be stored in a database)
    let generatedImages = [];

    async function generateArtFromAPI() {
        // Make the actual API call to your GAN backend
        const response = await fetch('http://127.0.0.1:8000/generate-art', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({})
        });

        if (!response.ok) {
            throw new Error('API request failed');
        }

        const data = await response.json();

        // Assuming your API returns { image: "base64string" }
        // Make sure to add the data URI prefix if your API doesn't include it
        return data.image.startsWith('data:')
            ? data.image
            : `data:image/png;base64,${data.image}`;
    }

    // Initialize gallery with some sample base64 images
    function initializeGallery() {
        // Clear gallery first
        gallery.innerHTML = '';

        // Create 6 sample images
        for (let i = 0; i < 6; i++) {
            const canvas = document.createElement('canvas');
            canvas.width = 300;
            canvas.height = 300;
            const ctx = canvas.getContext('2d');

            // Create a simple colored background
            const hue = i * 60; // Different hue for each sample
            ctx.fillStyle = `hsl(${hue}, 70%, 60%)`;
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            // Add some shapes
            for (let j = 0; j < 20; j++) {
                ctx.beginPath();
                ctx.arc(
                    Math.random() * canvas.width,
                    Math.random() * canvas.height,
                    Math.random() * 30,
                    0,
                    Math.PI * 2
                );
                ctx.fillStyle = `hsla(${hue + Math.random() * 60}, 100%, 50%, ${Math.random() * 0.8})`;
                ctx.fill();
            }

            // Convert to base64 and add to gallery
            const base64Data = canvas.toDataURL('image/png');
            generatedImages.push({
                data: base64Data,
                date: new Date().toLocaleDateString()
            });

            addImageToGallery(base64Data, new Date().toLocaleDateString());
        }
    }

    // Add image to gallery
    function addImageToGallery(base64Data, date) {
        const galleryItem = document.createElement('div');
        galleryItem.className = 'bg-white rounded-lg shadow overflow-hidden';

        const img = document.createElement('img');
        img.src = base64Data;
        img.className = 'w-full h-48 object-cover';
        img.alt = 'AI generated artwork';

        const infoDiv = document.createElement('div');
        infoDiv.className = 'p-4';

        const dateElement = document.createElement('p');
        dateElement.className = 'text-sm text-gray-500';
        dateElement.textContent = date;

        const downloadButton = document.createElement('button');
        downloadButton.className = 'mt-2 text-sm text-indigo-600 hover:text-indigo-800';
        downloadButton.textContent = 'Download';
        downloadButton.addEventListener('click', function() {
            downloadImage(base64Data, 'ai-artwork.png');
        });

        infoDiv.appendChild(dateElement);
        infoDiv.appendChild(downloadButton);
        galleryItem.appendChild(img);
        galleryItem.appendChild(infoDiv);

        // Add to the beginning of the gallery
        gallery.insertBefore(galleryItem, gallery.firstChild);

        // Remove the last item if there are more than 6
        if (gallery.children.length > 6) {
            gallery.removeChild(gallery.lastChild);
        }
    }

    // Download image function
    function downloadImage(base64Data, fileName) {
        const link = document.createElement('a');
        link.href = base64Data;
        link.download = fileName;
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    }

    // Generate art function
    generateBtn.addEventListener('click', async function() {
        // Show loading state
        placeholderText.classList.add('hidden');
        generatedImage.classList.add('hidden');
        loadingIndicator.classList.remove('hidden');
        downloadBtn.disabled = true;

        try {
            // Call the API to get base64 image data
            const base64Data = await generateArtFromAPI();

            // Store the current image data
            currentImageData = base64Data;

            // Hide loading state
            loadingIndicator.classList.add('hidden');

            // Set the image source to the base64 data
            generatedImage.src = base64Data;
            generatedImage.classList.remove('hidden');

            // Enable download button
            downloadBtn.disabled = false;

            // Add to gallery and store in our array
            const date = new Date().toLocaleDateString();
            generatedImages.unshift({
                data: base64Data,
                date: date
            });

            // Keep only the latest 50 images in memory
            if (generatedImages.length > 50) {
                generatedImages.pop();
            }

            // Update the gallery UI
            addImageToGallery(base64Data, date);

        } catch (error) {
            console.error('Error generating art:', error);
            // Show error message
            loadingIndicator.classList.add('hidden');
            placeholderText.textContent = 'Error generating art. Please try again.';
            placeholderText.classList.remove('hidden');
        }
    });

    // Download button event listener
    downloadBtn.addEventListener('click', function() {
        if (currentImageData) {
            downloadImage(currentImageData, 'ai-generated-art.png');
        }
    });

    // Initialize the gallery with sample images
    initializeGallery();
});