from pyomo.core.base.PyomoModel import ConcreteModel
from pyomo.core.base.objective import Objective
from pyomo.environ import *



class Simplex(object):

    def solution(self, parent_obj=None):
        self.parent_obj = parent_obj
        if self.parent_obj:
            self.custo_pvc_b = self.parent_obj.retorna_custos_pvc(0)
            self.custo_pvc_v = self.parent_obj.retorna_custos_pvc(1)
            self.custo_pvc_e = self.parent_obj.retorna_custos_pvc(2)

            self.preco_est_1 = self.parent_obj.retorna_preco_esteiras(0)
            self.preco_est_2 = self.parent_obj.retorna_preco_esteiras(1)
            self.preco_est_3 = self.parent_obj.retorna_preco_esteiras(2)

            self.limite = self.parent_obj.retorna_limite()

            self.imposto = self.parent_obj.retorna_preco_esteiras()

            self.frete = self.parent_obj.retorna_imposto()

            self.custo_unidade = self.parent_obj.calculo_coeficiente()

            lim_pvc_b = 8000
            lim_pvc_v = 9000
            lim_pvc_e = 7000

            model = ConcreteModel()

            # Variáveis
            model.x1 = Var(within=NonNegativeReals)
            model.x2 = Var(within=NonNegativeReals)
            model.x3 = Var(within=NonNegativeReals)

            # Dados
            receita = (model.x1 * self.preco_est_1) + (model.x2 * self.preco_est_2) + (model.x3 * self.preco_est_3)
            custo_total_prod = self.custo_unidade * (model.x1 + model.x2 + model.x3)
            imposto_total = self.imposto * (model.x1 + model.x2 + model.x3)

            # Função Objetivo
            funcao_obj = receita - custo_total_prod - imposto_total
            model.obj = Objective(expr = funcao_obj, sense = maximize)

            # Restrições
            custo_total_pvc_b = self.custo_pvc_b * ((model.x1.value * 2) + (model.x2.value * 3) + (model.x3.value * 1))
            custo_total_pvc_v = self.custo_pvc_v * ((model.x1.value * 6) + (model.x2.value * 5) + (model.x3.value * 2))
            custo_total_pvc_e = self.custo_pvc_e * ((model.x1.value * 4) + (model.x2.value * 1) + (model.x3.value * 2))

            model.c1 = Constraint(expr = custo_total_pvc_b <= lim_pvc_b)
            model.c2 = Constraint(expr = custo_total_pvc_v <= lim_pvc_v)
            model.c3 = Constraint(expr = custo_total_pvc_e <= lim_pvc_e)
            model.c4 = Constraint(expr = model.x1.value >= 0)
            model.c5 = Constraint(expr = model.x2.value >= 0)
            model.c6 = Constraint(expr = model.x3.value >= 0)

            optimizer = SolverFactory('glpk')
            results = optimizer.solve(model, tee = True)

            lucro_final = model.obj.expr()
            x1_value = model.x1.value
            x2_value = model.x2.value
            x3_value = model.x3.value

            print("x1 =", x1_value)
            print("x2 =", x2_value)
            print("x3 =", x3_value)


            status = results.solver.status
            print("Status: ", status)

            termination = results.solver.termination_condition
            print("Critério de Parada: ", termination)  # verifica a condição de parada


if __name__ == "__main__":
    s = Simplex()
