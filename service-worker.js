function updateCountdown() {
    const lastDate = new Date(localStorage.getItem('lastMealDate'));
    const interval = parseInt(localStorage.getItem('interval')) || 7;
    const now = new Date();
    const daysPassed = Math.floor((now - lastDate) / (1000 * 60 * 60 * 24));
    const diffTime = interval - daysPassed;

    let countdownText = '';
    if (diffTime > 0) {
        countdownText = `⏳ ${diffTime} day(s) left until your next cheat meal`;
    } else if (diffTime === 0) {
        countdownText = `✅ You can eat your cheat meal today!`;
    } else {
        countdownText = `⚠️ You're ${-diffTime} day(s) late! Eat that cheat meal ASAP!`;
    }
    document.getElementById('countdown').innerText = countdownText;

    // Update progress bar
    const percent = Math.min((daysPassed / interval) * 100, 100);
    document.getElementById('progressBar').style.width = `${percent}%`;
}
