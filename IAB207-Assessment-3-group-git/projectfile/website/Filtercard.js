function filterCards() {
    const citySelecter = document.getElementById('citySelect');
    const selectedCity = citySelecter.value;
    const cards = document.getElementsByClassName('m-2');
    const inputElements = document.querySelector('#BySearch');
    const InputValue = inputElements.value;

    for (let i = 0; i < cards.length; i++) {
        let titles = cards[i].querySelector(".card-title");
        const card = cards[i];
        const city = card.getAttribute('data-city');         
    
        if ((selectedCity === city || selectedCity === 'all') && titles.innerText.toLowerCase().indexOf(InputValue.toLowerCase()) > -1) {
            card.style.display = 'flex';
            card.closest('.col-sm-12').classList.remove('d-none');
        } else {
            card.style.display = 'none';
            card.closest('.col-sm-12').classList.add('d-none');
        }
    }
};