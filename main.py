import face_recognition

imagem_referencia = face_recognition.load_image_file("pessoas/rosto1.jpg")
codificacao_referencia = face_recognition.face_encodings(imagem_referencia)[0]
imagem_desconhecida = face_recognition.load_image_file("pessoas/rosto2.jpg")
codificacao_desconhecida = face_recognition.face_encodings(imagem_desconhecida)[0]
resultado = face_recognition.compare_faces([codificacao_referencia], codificacao_desconhecida)

print('As faces são iguais? ', resultado[0])
