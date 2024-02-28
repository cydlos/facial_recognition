import face_recognition

imagem_referencia = face_recognition.load_image_file("pessoas/rosto1.jpg")

codificacao_referencia = face_recognition.face_encodings(imagem_referencia)[0]

imagem_desconhecida = face_recognition.load_image_file("pessoas/rosto2.jpg")
