import tkinter as tk
from tkinter import messagebox

def validar_cpf():
    cpf = entrada.get()


    if len(cpf) != 11 or not cpf.isdigit():
         messagebox.showerror("ERRO", "Digite exatamente 11 números!")
         return
    nove_primeiros = cpf[:9]

    # Calcular o primeiro digito verificador
    soma = 0
    peso = 10

    for digito in nove_primeiros:
        soma += int(digito) * peso
        peso -= 1

    resultado = (soma * 10) % 11
    digito1 = 0 if resultado > 9 else resultado

    # Calcular o segundo digito verificador
    cpf_base10 = nove_primeiros + str(digito1)

    soma2 = 0
    peso2 = 11

    for digito in cpf_base10:
        soma2 += int(digito) * peso2
        peso2 -= 1

    resultado2 = (soma2 * 10) % 11
    digito2 = 0 if resultado2 > 9 else resultado2

    # Formatar com ponto e traço
    if len(cpf) == 11:
        cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

    # Verificar se os digitos batem com os que o usuários digitou
    if cpf[-2:] == f"{digito1}{digito2}":
         print(f'\033[1mCPF {cpf_formatado} válido!\033[m')
    else:
       print(f'\033[31;1mCPF {cpf_formatado} inválido!\033[m')

# Criar a Janlea
janela = tk.Tk()
janela.title("Validador de CPF")
janela.geometry("300x150")

# Criando Label (Mostrar a mensagem)
Label = tk.Label(janela, text = "Digite seu CPF aqui (Apenas números): ")
Label.pack(pady= 10)

# Campo de entrada
entrada = tk.Entry(janela)
entrada.pack()

# Criando o botão
Botao = tk.Button(janela, text = "Validar CPF", command = validar_cpf)
Botao.pack(pady=10)

# Mostrar a janela
janela.mainloop()
