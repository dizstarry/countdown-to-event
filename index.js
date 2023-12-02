const countdownDisplay = document.getElementById("countdown-display");

function renderCountdown() {
    const christmas = new Date(new Date().getFullYear(), 11, 25);

    // Calculate remaining time
    const currentTime = new Date();
    const timeDifference = christmas - currentTime;

    // Calculate days, hours, minutes, and seconds
    const days = Math.floor(timeDifference / (1000 * 60 * 60 * 24));
    const hours = Math.floor((timeDifference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((timeDifference % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((timeDifference % (1000 * 60)) / 1000);

    // Display remaining time in countdownDisplay
    countdownDisplay.textContent = `Countdown: ${days} days, ${hours} hours, ${minutes} minutes, ${seconds} seconds`;
}

// Call the function to update the countdown display
renderCountdown();

// Update the countdown every second
setInterval(renderCountdown, 1000);


