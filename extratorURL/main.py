class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        return url.strip() if type(url) == str else ""

    def valida_url(self):
        if not self.url:
            raise ValueError("URL vazia")

    def separando_url_base(self):
        indice = self.url.find("?")
        url_base = self.url[:indice]
        return url_base

    def separando_url_parametros(self):
        indice = self.url.find("?")
        url_parametros = self.url[indice + 1:]
        return url_parametros

    def get_parametro(self, busca):
        indice_busca = self.url.find(busca)
        indice_valor = indice_busca + len(busca) + 1
        corte = self.url.find("&", indice_valor)
        url_valor = self.url[indice_valor:] if corte == -1 else self.url[indice_valor:corte]
        return url_valor
