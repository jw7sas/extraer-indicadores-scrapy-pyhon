# Requesitos
    Tener instalado python y pip

# instalar ambiente virtual
    pip install virtualenv

# crear ambiente virtual
    virtualenv venv

# Activar y desactivar ambiente virtual
    venv\Scripts\activate
    venv\Scripts\deactivate

# Instalar requerimientos
    pip install -r requirements.txt

    -- Verificar scrapy
    scrapy version

# crear proyecto con scrapy
    scrapy startproject indicadores
    cd indicadores


# xpath
    -- Comandos xpath en la consola de Comandos
    xpath: es un lenguaje que permite construir expresiones que recorren y procesan un documento XML

    -- Obtener Datos usando la consola de google - con javascript

    $x('//section[contains(@class, "article-content") and @itemprop="articleBody"]//table//h2/strong/text()').map(i => i.wholeText)

    $x('//section[contains(@class, "article-content") and @itemprop="articleBody"]//table//h1/text()').map(i => i.wholeText)

# verificar xpath por la consola de scrapy
    Archivo Robots.txt: https://www.dane.gov.co/robots.txt

    scrapy shell "https://www.dane.gov.co/index.php/indicadores-economicos"

    response.xpath('//section[contains(@class, "article-content") and @itemprop="articleBody"]//table//h2/strong/text()').getall()

    response.xpath('//section[contains(@class, "article-content") and @itemprop="articleBody"]//table//h1/text()').getall()

    Spider: 'Spider es una clase de python a la cual le decimos que informacion queremos, que informacion no queremos y como guardar esa informacion.'

# Generar nuestro archivo a partir de nuestro spider
    scrapy crawl e_indicators