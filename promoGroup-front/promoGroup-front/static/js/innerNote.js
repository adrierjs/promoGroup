const telefonesInfo = [];


fetch('http://52.87.204.54:5000/notebook')
  .then(res => res.json())
  .then(data => {
    console.log('Dados da API:', data);

    data.forEach(product => {
      const link = product.productLink.replace('http://127.0.0.1:8000/api/', '');

      telefonesInfo.push({
        nome: product.name,
        preco: product.price,
        link: link,
        image: product.srcImg
      });
    });

    console.log(telefonesInfo)

    const jsonTelefones = JSON.stringify(telefonesInfo, null, 2);
    console.log(jsonTelefones);

    const ul = document.getElementById('listaSmart');
    showGallery(telefonesInfo, ul);
  })
  .catch(error => console.error('Ocorreu um erro:', error));

function showGallery(telefonesInfo, ul) {
  ul.innerHTML = '';

  telefonesInfo.forEach((item, index) => {
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