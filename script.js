document.addEventListener("DOMContentLoaded", function() {
    const typedText = document.getElementById('typed-text');
    const roles = ["Data Analyst", "Data Engineer", "Python Developer"];
    let currentIndex = 0;
    
    function typeText() {
        typedText.textContent = "";
        let role = roles[currentIndex];
        let i = 0;
        
        const interval = setInterval(() => {
            typedText.textContent += role[i];
            i++;
            if (i === role.length) {
                clearInterval(interval);
                setTimeout(() => {
                    currentIndex = (currentIndex + 1) % roles.length; // Loop through roles
                    typeText();
                }, 1000); // Wait before starting the next word
            }
        }, 150); // Typing speed
    }
    
    typeText();
});
