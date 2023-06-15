import re  # Regular Expressions -- RegEx

# Ex: Cep- 5 dígitos + hífen (opcional) + 3 digitos

endereco = "Rua das Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"

padrao = re.compile('[0-9]{5}[-]?[0-9]{3}')
busca = padrao.search(endereco)  # match
if busca:
    cep = busca.group()
    print(cep)
