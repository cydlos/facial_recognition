import tkinter as tk
from tkinter import filedialog
import face_recognition

def selecionar_arquivo(titulo="Selecione um arquivo", tipo_de_arquivo=(("Imagens", "*.jpg *.jpeg *.png"),)):
    caminho_do_arquivo = filedialog.askopenfilename(title=titulo, filetypes=tipo_de_arquivo)
    return caminho_do_arquivo

def comparar_faces(imagem_referencia_path, imagem_desconhecida_path):
    imagem_referencia = face_recognition.load_image_file(imagem_referencia_path)
    codificacoes_referencia = face_recognition.face_encodings(imagem_referencia)
    imagem_desconhecida = face_recognition.load_image_file(imagem_desconhecida_path)
    codificacoes_desconhecida = face_recognition.face_encodings(imagem_desconhecida)

    if codificacoes_referencia and codificacoes_desconhecida:
        # Comparando as faces
        resultados = face_recognition.compare_faces([codificacoes_referencia[0]], codificacoes_desconhecida[0])
        # Calculando a distância
        distancia = face_recognition.face_distance([codificacoes_referencia[0]], codificacoes_desconhecida[0])

        # Convertendo a distância em uma porcentagem de probabilidade
        # Aqui você pode ajustar a escala conforme necessário. Uma escala comum é inverter a distância e multiplicar por algum fator.
        probabilidade = max(0, 100 - (distancia[0] * 100))
        return resultados[0], probabilidade
    else:
        return None, None

def iniciar_comparacao():
    imagem_referencia_path = selecionar_arquivo("Selecione a imagem de referência")
    imagem_desconhecida_path = selecionar_arquivo("Selecione a imagem desconhecida")

    if imagem_referencia_path and imagem_desconhecida_path:
        resultado, probabilidade = comparar_faces(imagem_referencia_path, imagem_desconhecida_path)
        if resultado is None:
            print("Não foi possível encontrar faces em uma das imagens.")
        else:
            print('As faces pertencem à mesma pessoa?')
            if resultado:
                print(f"Sim, com {probabilidade:.2f}% de probabilidade.")
            else:
                print(f"Não, com {probabilidade:.2f}% de probabilidade.")
    else:
        print("Seleção de arquivo cancelada.")

raiz = tk.Tk()
raiz.withdraw()
iniciar_comparacao()
