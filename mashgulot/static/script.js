document.addEventListener("DOMContentLoaded", () => {
  // Join Now tugmasi
  const btn = document.querySelector(".btn");
  if (btn) {
    btn.addEventListener("click", () => {
      alert("Welcome to Game Club! Booking coming soon...");
    });
  }

  // Yulduz reytinglari
  const starContainers = document.querySelectorAll('.stars');
  if (starContainers.length > 0) {
    starContainers.forEach(starContainer => {
      const rating = parseFloat(starContainer.dataset.rating);
      const fullStars = Math.floor(rating);
      const halfStar = rating % 1 >= 0.5;

      let starsHTML = '';
      for (let i = 0; i < fullStars; i++) starsHTML += '★';
      if (halfStar) starsHTML += '☆';
      for (let i = starsHTML.length; i < 5; i++) starsHTML += '☆';

      starContainer.innerHTML = starsHTML;
    });
  }

  // Modal oynasi
  const modal = document.getElementById('modal');
  const modalTitle = document.getElementById('modalTitle');
  const modalText = document.getElementById('modalText');
  const modalImage = document.getElementById('modalImage');
  const modalDescription = document.getElementById('modalDescription');
  const closeBtn = document.querySelector('.close');

  if (modal && modalTitle && modalText && modalImage && modalDescription && closeBtn) {
    document.querySelectorAll('.info-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const game = btn.dataset.game;
        const img = btn.dataset.img;
        const desc = btn.dataset.desc;

        modalTitle.textContent = game;
        modalImage.src = img;
        modalDescription.textContent = desc;
        modalText.textContent = `${game} — bu Game Club’dagi eng mashhur o‘yinlardan biri. Siz uni yuqori sifatli kompyuterlarda, do‘stlaringiz bilan multiplayer tarzda o‘ynashingiz mumkin!`;
        modal.style.display = 'flex';
      });
    });

    closeBtn.addEventListener('click', () => {
      modal.style.display = 'none';
    });

    window.addEventListener('click', e => {
      if (e.target === modal) modal.style.display = 'none';
    });
  }
});