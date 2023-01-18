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
        self.setStyleSheet("background-color: rgb(120, 120, 120);")
        self.btn_sair.setStyleSheet("background-color: rgb(168, 0, 0);")
        self.btn_calc.setStyleSheet("background-color: rgb(60, 120, 120);")
        self.custo_pvc_b.setStyleSheet("background-color: white")
        self.custo_pvc_v.setStyleSheet("background-color: white")
        self.custo_pvc_e.setStyleSheet("background-color: white")
        self.lim_pvc_b.setStyleSheet("background-color: white")
        self.lim_pvc_v.setStyleSheet("background-color: white")
        self.lim_pvc_e.setStyleSheet("background-color: white")
        self.preco_est_1.setStyleSheet("background-color: white")
        self.preco_est_2.setStyleSheet("background-color: white")
        self.preco_est_3.setStyleSheet("background-color: white")

        self.num_func.setStyleSheet("background-color: white")
        self.aluguel.setStyleSheet("background-color: white")
        self.agua.setStyleSheet("background-color: white")

        self.frete.setStyleSheet("background-color: white")
        self.imposto.setStyleSheet("background-color: white")

        self.quant_est_1.setStyleSheet("background-color: white")
        self.quant_est_2.setStyleSheet("background-color: white")
        self.quant_est_3.setStyleSheet("background-color: white")

        self.lucro.setStyleSheet("background-color: white")
        self.label.setStyleSheet("color: white")
        self.label_2.setStyleSheet("color: white")
        self.label_3.setStyleSheet("color: white")
        self.label_4.setStyleSheet("color: white")
        self.label_5.setStyleSheet("color: white")
        self.label_6.setStyleSheet("color: white")
        self.label_7.setStyleSheet("color: white")
        self.label_8.setStyleSheet("color: white")
        self.label_9.setStyleSheet("color: white")

        self.label_10.setStyleSheet("color: white")
        self.label_11.setStyleSheet("color: white")
        self.label_12.setStyleSheet("color: white")
        self.label_13.setStyleSheet("color: white")

        self.label_14.setStyleSheet("color: white")
        self.label_15.setStyleSheet("color: white")
        self.label_16.setStyleSheet("color: white")
        self.label_17.setStyleSheet("color: white")
        self.label_18.setStyleSheet("color: white")
        self.label_19.setStyleSheet("color: white")
        self.label_20.setStyleSheet("color: white")

        self.label_21.setStyleSheet("color: white")
        self.label_22.setStyleSheet("color: white")
        self.label_23.setStyleSheet("color: white")
        self.label_24.setStyleSheet("color: white")



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
