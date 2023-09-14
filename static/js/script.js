const listaTelefones = [
    "iPhone X",
    "Samsung Galaxy S21",
    "Google Pixel 5",
    "OnePlus 9",
    "Huawei P40",
    "Sony Xperia 1",
    "LG V60 ThinQ",
    "Xiaomi Mi 11",
    "Motorola Moto G Power",
    "Nokia 9 PureView"
];

const priceTelefones = [
    "R$ 1.000",
    "R$ 2.000",
    "R$ 1.300",
    "R$ 6.020",
    "R$ 1.999",
    "R$ 1.000",
    "R$ 2.000",
    "R$ 3.000",
];

const listaLinks = [
    "https://www.link1.com",
    "https://www.link2.com",
    "https://www.link3.com",
    "https://www.link4.com",
    "https://www.link5.com",
    "https://www.link6.com",
    "https://www.link7.com",
    "https://www.link8.com"
];

// Preenche cada tag <h1> com um elemento da lista
for (let i = 0; i < listaTelefones.length; i++) {
    const h1Element = document.getElementById(`phoneName${i + 1}`);
    if (h1Element) {
        h1Element.textContent = listaTelefones[i];
    }
}

// Preenche cada tag <h1> com um elemento da lista
for (let i = 0; i < priceTelefones.length; i++) {
    const h1Element = document.getElementById(`price${i + 1}`);
    if (h1Element) {
        h1Element.textContent = priceTelefones[i];
    }
}

// Preenche os atributos href das tags <a> com os URLs da lista
for (let i = 0; i < listaLinks.length; i++) {
    const linkElement = document.getElementById(`link${i + 1}`);
    if (linkElement) {
        linkElement.href = listaLinks[i];
    }
}