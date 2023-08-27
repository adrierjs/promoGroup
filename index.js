const axios = require('axios');
const cheerio = require('cheerio');

url = 'https://www.zoom.com.br/celular?enableRefinementsSuggestions=true&hitsPerPage=48&page=1&pageTitle=Smartphone&q=&sortBy=default';

axios.get(url)
  .then((response) => {
    const html = response.data;
    const $ = cheerio.load(html);
    const productNamePrice = $('.ProductCard_ProductCard_Name__LT7hv, p.Text_Text__h_AF6.Text_MobileHeadingS__Zxam2');

    for (let index = 0; index < productNamePrice.length; index++) {
        const element = productNamePrice[index];
        const elementText = $(element).text()
        if(elementText != 'Filtros'){
            console.log(elementText)
            }
        }
    })
  .catch((error) => {
    console.log(error);
  });
