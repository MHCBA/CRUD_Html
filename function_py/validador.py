import re

def validar_valor(coluna, novo_valor):
    if coluna == 'nome':
        # Qualquer valor é válido para a coluna 'nome'
        return True
    elif coluna == 'idade':
        # Verifica se o valor é um número inteiro
        try:
            int(novo_valor)
            return True
        except ValueError:
            return False
    elif coluna == 'email':
        # Verifica se o valor parece ser um endereço de e-mail válido
        return bool(re.match(r"[^@]+@[^@]+\.[^@]+", novo_valor))
    elif coluna == 'senha':
        # Verifica se o valor não contém acentos
        return not any(char in "áéíóúâêîôûàèìòùäëïöüãõñ" for char in novo_valor)
    else:
        # Outras colunas não são suportadas
        return False