import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import PyQt5.QtWidgets
from simplex import otimiza

qtCreatorFile = "main.ui" 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.btn_calc.clicked.connect(self.calcula)
        self.btn_sair.clicked.connect(lambda:self.close())

    def calcula(self):
        custo_pvc_b = int(self.custo_pvc_b.text())
        custo_pvc_v = int(self.custo_pvc_v.text())
        custo_pvc_e = int(self.custo_pvc_e.text())

        lim_pvc_b = int(self.lim_pvc_b.text())
        lim_pvc_v = int(self.lim_pvc_v.text())
        lim_pvc_e = int(self.lim_pvc_e.text())

        preco_est_1 = int(self.preco_est_1.text())
        preco_est_2 = int(self.preco_est_2.text())
        preco_est_3 = int(self.preco_est_3.text())

        num_func = int(self.num_func.text())
        aluguel = int(self.aluguel.text())
        agua = int(self.agua.text())

        frete = int(self.frete.text())
        imposto = float(self.imposto.text())

        q_est_1, q_est_2, q_est_3, lucro = otimiza(custo_pvc_b, custo_pvc_v, custo_pvc_e, lim_pvc_b, lim_pvc_v, lim_pvc_e, preco_est_1, preco_est_2, preco_est_3, num_func, aluguel, agua, frete, imposto)

        self.quant_est_1.setText(str(q_est_1))
        self.quant_est_2.setText(str(q_est_2))
        self.quant_est_3.setText(str(q_est_3))
        self.lucro.setText(str(lucro))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())