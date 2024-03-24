import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QFileDialog
import face_recognition

class FaceComparer(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Configuração da janela
        self.setWindowTitle('Comparador de Faces com PyQt')
        self.setGeometry(100, 100, 200, 100)

        # Layout Vertical
        layout = QVBoxLayout()

        # Botão para selecionar a imagem de referência
        self.btn_select_ref = QPushButton('Selecionar Imagem de Referência', self)
        self.btn_select_ref.clicked.connect(self.selecionarImagemReferencia)
        layout.addWidget(self.btn_select_ref)

        # Botão para selecionar a imagem desconhecida
        self.btn_select_unknown = QPushButton('Selecionar Imagem Desconhecida', self)
        self.btn_select_unknown.clicked.connect(self.selecionarImagemDesconhecida)
        layout.addWidget(self.btn_select_unknown)

        # Label para mostrar o resultado
        self.result_label = QLabel('Resultado aparecerá aqui', self)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def selecionarImagemReferencia(self):
        self.imagem_referencia_path, _ = QFileDialog.getOpenFileName(self, 'Selecione a imagem de referência', '', 'Imagens (*.jpg *.jpeg *.png)')

    def selecionarImagemDesconhecida(self):
        self.imagem_desconhecida_path, _ = QFileDialog.getOpenFileName(self, 'Selecione a imagem desconhecida', '', 'Imagens (*.jpg *.jpeg *.png)')
        self.compararFaces()

    def compararFaces(self):
        if hasattr(self, 'imagem_referencia_path') and hasattr(self, 'imagem_desconhecida_path'):
            resultado, probabilidade = self.comparar_faces(self.imagem_referencia_path, self.imagem_desconhecida_path)
            if resultado is None:
                self.result_label.setText("Não foi possível encontrar faces em uma das imagens.")
            else:
                resultado_str = "Sim" if resultado else "Não"
                self.result_label.setText(f"As faces pertencem à mesma pessoa? {resultado_str}, com {probabilidade:.2f}% de probabilidade.")
        else:
            self.result_label.setText("Seleção de arquivo cancelada.")

    def comparar_faces(self, imagem_referencia_path, imagem_desconhecida_path):
        imagem_referencia = face_recognition.load_image_file(imagem_referencia_path)
        codificacoes_referencia = face_recognition.face_encodings(imagem_referencia)
        imagem_desconhecida = face_recognition.load_image_file(imagem_desconhecida_path)
        codificacoes_desconhecida = face_recognition.face_encodings(imagem_desconhecida)

        if codificacoes_referencia and codificacoes_desconhecida:
            resultados = face_recognition.compare_faces([codificacoes_referencia[0]], codificacoes_desconhecida[0])
            distancia = face_recognition.face_distance([codificacoes_referencia[0]], codificacoes_desconhecida[0])
            probabilidade = max(0, 100 - (distancia[0] * 100))
            return resultados[0], probabilidade
        else:
            return None, None

def main():
    app = QApplication(sys.argv)
    ex = FaceComparer()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
