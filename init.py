def cifra_de_cesar(texto, chave):
    resultado = ""

    for caractere in texto:
        # Verifica se o caractere é uma letra
        if caractere.isalpha():
            # Obtém o código ASCII do caractere
            codigo = ord(caractere)
            
            # Determina se é maiúscula ou minúscula
            maiuscula = caractere.isupper()
            
            # Aplica o deslocamento da cifra de César
            codigo = (codigo - ord('A' if maiuscula else 'a') + chave) % 26 + ord('A' if maiuscula else 'a')
            
            # Converte o código ASCII de volta para um caractere
            caractere_cifrado = chr(codigo)
            
            # Adiciona o caractere cifrado ao resultado
            resultado += caractere_cifrado
        else:
            # Se não for uma letra, mantém o caractere inalterado
            resultado += caractere

    return resultado

# Exemplo de uso
texto_original = "Hello, World!"
chave = 3
texto_cifrado = cifra_de_cesar(texto_original, chave)

print("Texto Original:", texto_original)
print("Texto Cifrado:", texto_cifrado)
