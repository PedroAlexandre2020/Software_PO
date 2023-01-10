# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'coeficiente.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Calcula_Coeficiente(object):
    def setupUi(self, Calcula_Coeficiente):
        Calcula_Coeficiente.setObjectName("Calcula_Coeficiente")
        Calcula_Coeficiente.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Calcula_Coeficiente)
        self.centralwidget.setObjectName("centralwidget")
        self.botao_calcula_coeficiente = QtWidgets.QPushButton(
            self.centralwidget)
        self.botao_calcula_coeficiente.setGeometry(
            QtCore.QRect(120, 180, 75, 23))
        self.botao_calcula_coeficiente.setObjectName(
            "botao_calcula_coeficiente")
        self.botao_coeficiente_sair = QtWidgets.QPushButton(self.centralwidget)
        self.botao_coeficiente_sair.setGeometry(QtCore.QRect(240, 180, 75, 23))
        self.botao_coeficiente_sair.setObjectName("botao_coeficiente_sair")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 141, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 40, 131, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 60, 91, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 80, 91, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 100, 141, 16))
        self.label_5.setObjectName("label_5")
        self.input_qtd_func = QtWidgets.QLineEdit(self.centralwidget)
        self.input_qtd_func.setGeometry(QtCore.QRect(180, 20, 113, 20))
        self.input_qtd_func.setObjectName("input_qtd_func")
        self.input_salarios = QtWidgets.QLineEdit(self.centralwidget)
        self.input_salarios.setGeometry(QtCore.QRect(180, 40, 113, 20))
        self.input_salarios.setObjectName("input_salarios")
        self.input_Custo_Aluguel = QtWidgets.QLineEdit(self.centralwidget)
        self.input_Custo_Aluguel.setGeometry(QtCore.QRect(180, 60, 113, 20))
        self.input_Custo_Aluguel.setObjectName("input_Custo_Aluguel")
        self.input_Custo_Agua = QtWidgets.QLineEdit(self.centralwidget)
        self.input_Custo_Agua.setGeometry(QtCore.QRect(180, 80, 113, 20))
        self.input_Custo_Agua.setObjectName("input_Custo_Agua")
        self.input_qtd_M2Produzido = QtWidgets.QLineEdit(self.centralwidget)
        self.input_qtd_M2Produzido.setGeometry(QtCore.QRect(180, 100, 113, 20))
        self.input_qtd_M2Produzido.setObjectName("input_qtd_M2Produzido")
        Calcula_Coeficiente.setCentralWidget(self.centralwidget)

        self.retranslateUi(Calcula_Coeficiente)
        self.botao_coeficiente_sair.clicked.connect(Calcula_Coeficiente.close)
        self.botao_calcula_coeficiente.clicked.connect(
            self.calculo_coeficiente)
        QtCore.QMetaObject.connectSlotsByName(Calcula_Coeficiente)

    def calculo_coeficiente(self):
        qtd_func = int(self.input_qtd_func.text())
        sal_func = int(self.input_salarios.text())
        aluguel = int(self.input_Custo_Aluguel.text())
        agua = int(self.input_Custo_Agua.text())
        qtd_m2 = int(self.input_qtd_M2Produzido.text())

        result_coeficiente = (((qtd_func*sal_func) + aluguel + agua) / qtd_m2)

        from software import Ui_Software

        

        return result_coeficiente

    def retranslateUi(self, Calcula_Coeficiente):
        _translate = QtCore.QCoreApplication.translate
        Calcula_Coeficiente.setWindowTitle(_translate(
            "Calcula_Coeficiente", "Calculo do Coeficiente"))
        self.botao_calcula_coeficiente.setText(
            _translate("Calcula_Coeficiente", "Calcular"))
        self.botao_coeficiente_sair.setText(
            _translate("Calcula_Coeficiente", "Sair"))
        self.label.setText(_translate("Calcula_Coeficiente",
                           "Quantidade de Funcionarios"))
        self.label_2.setText(_translate(
            "Calcula_Coeficiente", "Salario dos Funcionários"))
        self.label_3.setText(_translate(
            "Calcula_Coeficiente", "Custo de Aluguel"))
        self.label_4.setText(_translate(
            "Calcula_Coeficiente", "Custo de Água"))
        self.label_5.setText(_translate(
            "Calcula_Coeficiente", "Quantidade de M2 Produzidos"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    telacoeficiente = QtWidgets.QMainWindow()
    ui = Ui_Calcula_Coeficiente()
    ui.setupUi(telacoeficiente)
    telacoeficiente.show()
    sys.exit(app.exec_())
