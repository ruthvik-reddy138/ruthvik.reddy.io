document.getElementById('contactForm').addEventListener('submit', async function (e) {
    e.preventDefault();

    const formData = new FormData(this);
    const data = Object.fromEntries(formData.entries());

    try {
        const response = await fetch('http://localhost:5000/send-email', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data),
        });

        if (response.ok) {
            document.getElementById('confirmationMessage').style.display = 'block';
            this.reset(); // Reset the form
        } else {
            alert('Error sending message. Please try again later.');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('Error sending message. Please try again later.');
    }
});
