import tkinter as tk
from tkinter import filedialog
import face_recognition

def selecionar_arquivo(titulo="Selecione um arquivo", tipo_de_arquivo=(("Imagens", "*.jpg *.jpeg *.png"),)):
    caminho_do_arquivo = filedialog.askopenfilename(title=titulo, filetypes=tipo_de_arquivo)
    return caminho_do_arquivo

def comparar_faces(imagem_referencia_path, imagem_desconhecida_path):
    imagem_referencia = face_recognition.load_image_file(imagem_referencia_path)
    codificacao_referencia = face_recognition.face_encodings(imagem_referencia)[0]

    imagem_desconhecida = face_recognition.load_image_file(imagem_desconhecida_path)
    codificacao_desconhecida = face_recognition.face_encodings(imagem_desconhecida)[0]

    resultado = face_recognition.compare_faces([codificacao_referencia], codificacao_desconhecida)
    print('As faces são iguais? ', resultado[0])

def iniciar_comparacao():
    imagem_referencia_path = selecionar_arquivo("Selecione a imagem de referência")
    imagem_desconhecida_path = selecionar_arquivo("Selecione a imagem desconhecida")

    if imagem_referencia_path and imagem_desconhecida_path:
        comparar_faces(imagem_referencia_path, imagem_desconhecida_path)
    else:
        print("Seleção de arquivo cancelada.")


raiz = tk.Tk()
raiz.withdraw() 
iniciar_comparacao()
