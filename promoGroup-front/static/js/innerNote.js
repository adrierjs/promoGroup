const listaNotebooks = [
    "Dell XPS 13",
    "MacBook Air",
    "HP Spectre x360",
    "Lenovo ThinkPad X1 Carbon",
    "Asus ZenBook",
    "Microsoft Surface Laptop",
    "Acer Swift 3",
    "LG Gram"
];

const priceNotebooks = [
    "R$ 3.000",
    "R$ 2.500",
    "R$ 1.800",
    "R$ 2.200",
    "R$ 1.500",
    "R$ 2.000",
    "R$ 1.200",
    "R$ 1.700",
];

const listaLinksNotebooks = [
    "https://www.link9.com",
    "https://www.link10.com",
    "https://www.link11.com",
    "https://www.link12.com",
    "https://www.link13.com",
    "https://www.link14.com",
    "https://www.link15.com",
    "https://www.link16.com"
];

const notebooksInfo = [];

for (let index = 0; index < listaNotebooks.length; index++) {
    notebooksInfo.push({
        nome: listaNotebooks[index],
        preco: priceNotebooks[index],
        link: listaLinksNotebooks[index]
    });
}

const jsonProdutos = JSON.stringify(notebooksInfo, null, 2);
const produtos = JSON.parse(jsonProdutos);

console.log(jsonProdutos);

const ul = document.getElementById('listanote'); // Use o ID 'listanote'

showGalery(jsonProdutos);
function showGalery(jsonProdutos) {
    const ul = document.getElementById('listanote'); // Use o ID 'listanote'
    ul.innerHTML = '';

    produtos.forEach((item, index) => {
        const li = document.createElement("li");
        li.classList.add('col-lg-3', 'col-md-4', 'col-sm-6', 'pb-1');
        li.innerHTML = `
            <div class="product-item bg-light mb-4">
                <div class="product-img position-relative overflow-hidden">
                    <!-- Como não há informações de imagem no JSON, você pode adicionar uma imagem padrão ou deixar em branco -->
                    <img class="img-fluid w-100" src="/static/img/product-1.jpg" alt="">
                    <div class="product-action">
                        <a class="btn btn-outline-dark btn-square" href="${item.link}"><i class="fa fa-search"></i></a>
                    </div>
                </div>
                <div class="text-center py-4">
                    <a class="h6 text-decoration-none text-truncate" href="${item.link}" id="productName${index}">${item.nome}</a>
                    <div class="d-flex align-items-center justify-content-center mt-2">
                        <h5 id="productPrice${index}">${item.preco}</h5>
                    </div>
                </div>
            </div>
        `;
        ul.appendChild(li);
    });
}

const input = document.getElementById('product-input');
input.addEventListener('input', filtrarLista);

function filtrarLista() {
    const ul = document.getElementById('listanote');
    const textoFiltrado = input.value.toLowerCase();

    const liItens = ul.querySelectorAll('li');
    liItens.forEach((li) => {
        const nomeItem = li.querySelector('.h6').textContent.toLowerCase();
        if (nomeItem.includes(textoFiltrado)) {
            li.style.display = 'block';
        } else {
            li.style.display = 'none';
        }
    });
}
