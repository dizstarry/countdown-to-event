const countdownDisplay = document.getElementById("countdown-display");

function renderCountdown() {
    const christmas = 25;
    // Task:
    // - Get today's date (you only need the day).
    let today = new Date().toLocaleDateString('en-GB', { day: 'numeric' });
    // - Calculate remaining days.
    let remainingDays;

    // - Display remaining days in countdownDisplay.

    if (today <= christmas) {
        remainingDays = christmas - today;
    }

    // Display remaining days in countdownDisplay
    countdownDisplay.textContent = `Countdown: ${remainingDays} days`;
}

// Call the function to update the countdown display
renderCountdown();

// Stretch goals:
// - Display hours, minutes, seconds.
// - Add a countdown for another festival, your birthday, or Christmas 2022.