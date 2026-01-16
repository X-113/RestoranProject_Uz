document.addEventListener("DOMContentLoaded", () => {
  const btn = document.querySelector(".btn");
  if (btn) {
    btn.addEventListener("click", () => {
      alert("Welcome to Game Club! Booking coming soon...");
    });
  }
});
