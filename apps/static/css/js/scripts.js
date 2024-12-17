// apps/static/js/scripts.js
document.addEventListener('DOMContentLoaded', function() {
    // Adiciona uma animação à imagem do card ao clicar
    const cards = document.querySelectorAll('.card');
    cards.forEach(card => {
        card.addEventListener('click', () => {
            const img = card.querySelector('img');
            img.classList.toggle('active');
        });
    });
});