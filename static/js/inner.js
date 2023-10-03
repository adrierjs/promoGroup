// Celulares

const listaTelefones = [
    "iPhone X",
    "Samsung Galaxy S21",
    "Google Pixel 5",
    "OnePlus 9",
    "Huawei P40",
    "Sony Xperia 1",
    "LG V60 ThinQ",
    "Xiaomi Mi 11"
];

const priceTelefones = [
    "R$ 1.000",
    "R$ 2.000",
    "R$ 1.300",
    "R$ 6.020",
    "R$ 1.999",
    "R$ 1.000",
    "R$ 2.000",
    "R$ 1.300",
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

const images = [
    "https://www.tradeinn.com/f/13759/137594118/apple-remodelado-iphone-x-256gb-5.8.jpg",
    "https://samsungbrshop.vtexassets.com/arquivos/ids/222466/image-147812a827ce414cbeecb5bb91eecb25-1-.jpg?v=638315272752900000",
    "https://m.media-amazon.com/images/I/71C0RBjkc2L._AC_UF1000,1000_QL80_.jpg",
    "https://9a4cdd8e5789bb85.cdn.gocache.net/rbaimporta1/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/o/n/oneplus-9_rbaimportados.com_1_.jpg",
    "https://www.romapy.com/46976-large_default/celular-smartphone-huawei-p40-lite-6gb128gb-jenny-l22a-green---jenny-l22a-green.jpg",
    "https://hayloubrasil.com.br/wp-content/uploads/2023/04/1748edae8d78869f0babe21c81d55009.jpg",
    "https://i.ebayimg.com/images/g/DwYAAOSwI~Vi8Vqd/s-l1600.jpg",
    "https://m.media-amazon.com/images/I/51b8b4RTyGL.jpg"
]

const telefonesInfo = [];

for (let index = 0; index < listaTelefones.length; index++) {
    telefonesInfo.push({
        nome: listaTelefones[index],
        preco: priceTelefones[index],
        link: listaLinks[index],
        image: images[index]
    });
}

const jsonTelefones = JSON.stringify(telefonesInfo, null, 2);
const telefones = JSON.parse(jsonTelefones);

console.log(jsonTelefones);


const ul = document.getElementById('listaSmart');


showGalery(jsonTelefones);
function showGalery(jsonTelefones) {
    const ul = document.getElementById('listaSmart');
    ul.innerHTML = '';

    telefones.forEach((item, index) => {
        const li = document.createElement("li");
        li.classList.add('col-lg-3', 'col-md-4', 'col-sm-6', 'pb-1');
        li.innerHTML = `
            <div class="product-item bg-light mb-4">
                <div class="product-img position-relative overflow-hidden">
                    <!-- Como não há informações de imagem no JSON, você pode adicionar uma imagem padrão ou deixar em branco -->
                    <img class="img-fluid w-100" src="${item.image}" alt="">
                    <div class="product-action">
                        <a class="btn btn-outline-dark btn-square" href="${item.link}"><i class="fa fa-search"></i></a>
                    </div>
                </div>
                <div class="text-center py-4">
                    <a class="h6 text-decoration-none text-truncate" href="${item.link}" id="phoneName${index}">${item.nome}</a>
                    <div class="d-flex align-items-center justify-content-center mt-2">
                        <h5 id="price${index}">${item.preco}</h5>
                    </div>
                </div>
            </div>
        `;
        ul.appendChild(li);
    });
}

// Adicione um evento de escuta ao campo de entrada
const input = document.getElementById('product-input');
input.addEventListener('input', filtrarLista);

function filtrarLista() {
    const ul = document.getElementById('listaSmart');
    const textoFiltrado = input.value.toLowerCase(); // Obtenha o texto inserido e converta para minúsculas para comparação

    // Iterar sobre as <li> e verificar se o texto filtrado está contido no nome do telefone
    const liItens = ul.querySelectorAll('li');
    liItens.forEach((li) => {
        const nomeItem = li.querySelector('.h6').textContent.toLowerCase();
        if (nomeItem.includes(textoFiltrado)) {
            li.style.display = 'block'; // Mostrar a <li> se corresponder ao filtro
        } else {
            li.style.display = 'none'; // Ocultar a <li> se não corresponder ao filtro
        }
    });
}
