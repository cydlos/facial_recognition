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
        resultado = face_recognition.compare_faces([codificacoes_referencia[0]], codificacoes_desconhecida[0])
        return resultado[0]
    else:
        return None

def iniciar_comparacao():
    imagem_referencia_path = selecionar_arquivo("Selecione a imagem de referência")
    imagem_desconhecida_path = selecionar_arquivo("Selecione a imagem desconhecida")

    if imagem_referencia_path and imagem_desconhecida_path:
        resultado = comparar_faces(imagem_referencia_path, imagem_desconhecida_path)
        if resultado is None:
            print("Não foi possível encontrar faces em uma das imagens.")
        else:
            print('As faces são iguais? ', resultado)
    else:
        print("Seleção de arquivo cancelada.")

raiz = tk.Tk()
raiz.withdraw()
iniciar_comparacao()

