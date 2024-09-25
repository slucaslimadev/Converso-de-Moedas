import customtkinter
from pegar_moedas import nomes_moedas, conversoes_disponiveis
from pegar_cotacao import pegar_cotacao_moeda

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("500x500")

dic_conversoes_disponiveis = conversoes_disponiveis()

def converter_moeda():
    moeda_origem = campo_moeda_origem.get()
    moeda_destino = campo_moeda_destino.get()
    if moeda_origem and moeda_destino:
        cotacao = pegar_cotacao_moeda(moeda_origem, moeda_destino)
        texto_da_cotacao_moeda.configure(text=f"1{moeda_origem} = {cotacao} {moeda_destino}")

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               

##Titulo
titulo = customtkinter.CTkLabel(janela, text="Conversor de Moedas", font=("", 20))

def carregar_moedas_destino(moeda_selecionada):
    lista_moedas_destino = dic_conversoes_disponiveis[moeda_selecionada]
    campo_moeda_destino.configure(values=lista_moedas_destino)
    campo_moeda_destino.set(lista_moedas_destino[0])


##Texto Moedas Origem
texto_moedas_origem = customtkinter.CTkLabel(janela, text="Selecione a moeda de origem")
campo_moeda_origem = customtkinter.CTkOptionMenu(janela, values=list(dic_conversoes_disponiveis.keys()), command=carregar_moedas_destino)

#Texto Moeda Destino
texto_moedas_destino = customtkinter.CTkLabel(janela, text="Selecione a moeda de destino")
campo_moeda_destino = customtkinter.CTkOptionMenu(janela, values=["Selecione uma moeda de origem"])


#Botao
botao_converter = customtkinter.CTkButton(janela, text="Converter", command=converter_moeda)

lista_moedas = customtkinter.CTkScrollableFrame(janela)

texto_da_cotacao_moeda = customtkinter.CTkLabel(janela, text="")

moedas_disponiveis = nomes_moedas()
for codigo_moeda in moedas_disponiveis:
    nome_moeda = moedas_disponiveis[codigo_moeda]
    texto_moeda = customtkinter.CTkLabel(lista_moedas, text=f"{codigo_moeda}: {nome_moeda}")
    texto_moeda.pack()

#Aparecer na tela
titulo.pack(padx=10, pady=10)
texto_moedas_origem.pack(padx=10, pady=10)
campo_moeda_origem.pack(padx=10,)
texto_moedas_destino.pack(padx=10, pady=10)
campo_moeda_destino.pack(padx=10,)
botao_converter.pack(padx=10, pady=10)
texto_da_cotacao_moeda.pack(padx=10, pady=10)
lista_moedas.pack(padx=10, pady=10)





janela.mainloop()