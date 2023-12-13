import tkinter as tk
from tkinter import ttk

def calcular_emissao_carbono():
    combustivel = combo_combustivel.get().lower()
    km = float(entry_km.get())

    fatores_emissao = {
        'gasolina': 2.31,
        'diesel': 2.68,
        'etanol': 1.96,
        'gás natural': 1.99
        # Adicione outros combustíveis e seus fatores de emissão conforme necessário
    }

    if combustivel in fatores_emissao:
        fator_emissao = fatores_emissao[combustivel]
        emissao_carbono = fator_emissao * km

        creditos_carbono = emissao_carbono
        arvores_necessarias = emissao_carbono / 21.77

        lbl_resultado['text'] = f"A emissão de carbono ao percorrer {km} km utilizando {combustivel} é de {emissao_carbono:.2f} kg CO2."
        lbl_resultado.config(font=("Arial", 20, "bold"))  # Aumentando a fonte e deixando em negrito
        lbl_creditos['text'] = f"Compra de créditos de carbono: {creditos_carbono:.2f} créditos de carbono"
        lbl_arvores['text'] = f"Plantio de árvores: {arvores_necessarias:.2f} árvores necessárias"

        # Ajustar a resolução da janela de acordo com o tamanho do conteúdo
        largura_conteudo = max(lbl_resultado.winfo_reqwidth(), lbl_creditos.winfo_reqwidth(), lbl_arvores.winfo_reqwidth())
        altura_conteudo = lbl_resultado.winfo_reqheight() + lbl_creditos.winfo_reqheight() + lbl_arvores.winfo_reqheight() + 200  # Ajuste adicional

        root.geometry(f"{largura_conteudo}x{altura_conteudo}")
    else:
        lbl_resultado['text'] = "Tipo de combustível não suportado"


# Criando a janela principal
root = tk.Tk()
root.title("Calculadora de Emissão de Carbono")

# Criando os widgets com fonte aumentada e títulos em negrito
fonte_titulo = ("Arial", 20, "bold")  # Fonte para os títulos

label_instrucao = tk.Label(root, text="Insira o tipo de combustível e a quantidade de quilômetros percorridos:", font=fonte_titulo)
label_instrucao.pack()

combo_combustivel = ttk.Combobox(root, values=['Gasolina', 'Diesel', 'Etanol', 'Gás Natural'], font=fonte_titulo)
combo_combustivel.pack()

label_km = tk.Label(root, text="Quilômetros percorridos:", font=fonte_titulo)
label_km.pack()
entry_km = tk.Entry(root, font=fonte_titulo)
entry_km.pack()

btn_calcular = tk.Button(root, text="Calcular", command=calcular_emissao_carbono, font=fonte_titulo)
btn_calcular.pack()

fonte_resultados = ("Arial", 25, "bold")  # Fonte para os resultados, aumentada e em negrito

lbl_resultado = tk.Label(root, text="", font=fonte_resultados)
lbl_resultado.pack()

lbl_creditos = tk.Label(root, text="", font=fonte_resultados)
lbl_creditos.pack()

lbl_arvores = tk.Label(root, text="", font=fonte_resultados)
lbl_arvores.pack()

# Ajustar a resolução inicial da janela de acordo com o tamanho do conteúdo
largura_conteudo = max(lbl_resultado.winfo_reqwidth(), lbl_creditos.winfo_reqwidth(), lbl_arvores.winfo_reqwidth())
altura_conteudo = lbl_resultado.winfo_reqheight() + lbl_creditos.winfo_reqheight() + lbl_arvores.winfo_reqheight() + 200  # Ajuste adicional

largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()

pos_x = (largura_tela // 50) - (largura_conteudo // 50)
pos_y = (altura_tela // 50) - (altura_conteudo // 50)

root.geometry(f"{largura_conteudo}x{altura_conteudo}+{pos_x}+{pos_y}")

# Executando o loop principal da aplicação
root.mainloop()
