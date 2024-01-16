#Base do alfabeto
base = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#Função encriptar recebe um texto e uma chave
def encrypt(text, key):
    text_encrypt = ''  # Variável que armazenará o texto encriptado
    i = 0  # Inicialização de uma variável que indica a posição atual no texto / reinicia quando o texto termina

    for letter in text:
        if letter == ' ':
            # Se o caractere for um espaço em branco, adiciona diretamente ao texto cifrado
            text_encrypt += ' '
        else:
            # Caso contrário, aplica a cifra de Vigenère normalmente
            sum = base.index(letter) + base.index(key[i % len(key)])  # Soma os índices da letra do texto e da letra da chave
            module = int(sum) % len(base)  # Calcula o módulo para garantir que o resultado esteja dentro dos limites do alfabeto
            text_encrypt += base[module]  # Adiciona a letra cifrada ao texto encriptado
            i += 1  # Incrementa a posição para continuar percorrendo o texto e a chave

    return text_encrypt  # Retorna o texto encriptado

#Função decriptar recebe o texto encriptado e a chave usada para encriptar
def decipher(text_encrypt, key):
    text_decipher = ''  # Variável que armazenará o texto decriptado
    i = 0  # Inicialização de uma variável que indica a posição atual no texto encriptado / reinicia quando o texto encriptado termina

    for letter in text_encrypt:
        if letter == ' ':
            # Se o caractere for um espaço em branco, adiciona diretamente ao texto decifrado
            text_decipher += ' '
        else:
            # Caso contrário, aplica a cifra de Vigenère inversa normalmente
            sum = base.index(letter) - base.index(key[i % len(key)])  # Subtrai os índices da letra cifrada e da letra da chave
            module = int(sum) % len(base)  # Calcula o módulo para garantir que o resultado esteja dentro dos limites do alfabeto
            text_decipher += base[module]  # Adiciona a letra decifrada ao texto decriptado
            i += 1  # Incrementa a posição para continuar percorrendo o texto encriptado e a chave

    return text_decipher  # Retorna o texto decriptado

# Função para guardar as opções do menu
def menu():
    print("\n**** Menu ****")  # Imprime o cabeçalho do menu
    print("[1] Criptografar Texto")  # Opção para criptografar texto
    print("[2] Descriptografar Texto")  # Opção para descriptografar texto
    print("[0] Sair")  # Opção para sair do programa

# Função Principal
def main():
    option = 1  # Inicializa a variável de opção para entrar no loop do menu

    while option != 0:  # Continua executando até que o usuário escolha a opção 0 para sair
        menu()  # Exibe o menu
        option = int(input("\nEntre com número da opção: "))  # Solicita a entrada da opção do usuário como um número inteiro

        if option == 1:
            print("[1] Criptografar Texto\n")  # Exibe a opção selecionada
            text = str(input("Digite a mensagem: \n")).lower()  # Solicita a entrada da mensagem para criptografar
            key = str(input("\nDigite a chave de criptografia:\n")).lower()  # Solicita a entrada da chave de criptografia
            encrypted = encrypt(text, key)  # Chama a função de criptografia
            print("Texto encriptado:\n", encrypted)  # Exibe o texto criptografado

        elif option == 2:
            print("[2] Descriptografar Texto\n")  # Exibe a opção selecionada
            text = str(input("Digite a mensagem criptografada: \n")).lower()  # Solicita a entrada da mensagem criptografada para descriptografar
            key = str(input("\nDigite a chave de criptografia: \n")).lower()  # Solicita a entrada da chave de criptografia
            txt_decipher = decipher(text, key)  # Chama a função de descriptografia
            print("O texto original é:", txt_decipher)  # Exibe o texto original descriptografado

        elif option == 0:
            print("Programa encerrado.")  # Exibe mensagem de encerramento do programa

        else:
            print("Opção inválida. Tente novamente.")  # Informa ao usuário que a opção escolhida é inválida e solicita uma nova entrada

main()  # Chama a função principal para iniciar o programa