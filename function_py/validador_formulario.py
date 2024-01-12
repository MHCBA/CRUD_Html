def validar_valor_forms(valor):
    try:
        int(valor)
        return True
    except ValueError:
        return False
