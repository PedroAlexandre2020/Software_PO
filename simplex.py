from pyomo.core.base.PyomoModel import ConcreteModel
from pyomo.core.base.objective import Objective
from pyomo.environ import *

#? Definindo Variáveis globais -------------------------------

# Custo de cada material por m2
custo_pvc_b = 110
custo_pvc_v = 90
custo_pvc_e = 118

# Limite máximo em dinheiro para gasto com material
lim_pvc_b = 8000
lim_pvc_v = 9000
lim_pvc_e = 7000

# Preço de venda de cada esteira;
preco_est_1 = 755
preco_est_2 = 534
preco_est_3 = 822

# Custo de produção
num_func = 20
aluguel = 20
agua = 20
custo_unidade = (num_func * 0.45) + aluguel + agua

# Frete por metro quadrado de material
frete = 3

# Imposto sobre venda de unidade de esteira
imposto = 0.1

#? Definindo Funções -----------------------------------------

def solution ():
    global custo_pvc_b, custo_pvc_v, custo_pvc_e
    global lim_pvc_b, lim_pvc_v, lim_pvc_e
    global preco_est_1, preco_est_2, preco_est_3
    global custo_unidade, frete, imposto

    model = ConcreteModel()

    # Variáveis
    model.x1 = Var(within=NonNegativeReals)
    model.x2 = Var(within=NonNegativeReals)
    model.x3 = Var(within=NonNegativeReals)

    # Dados
    receita = (model.x1 * preco_est_1) + (model.x2 * preco_est_2) + (model.x3 * preco_est_3)
    custo_total_prod = custo_unidade * (model.x1 + model.x2 + model.x3)
    imposto_total = imposto * (model.x1 + model.x2 + model.x3)

    # Função Objetivo
    funcao_obj = receita - custo_total_prod - imposto_total
    model.obj = Objective(expr = funcao_obj, sense = maximize)

    # Restrições
    custo_total_pvc_b = custo_pvc_b * ((model.x1 * 2) + (model.x2 * 3) + (model.x3 * 1))
    custo_total_pvc_v = custo_pvc_v * ((model.x1 * 6) + (model.x2 * 5) + (model.x3 * 2))
    custo_total_pvc_e = custo_pvc_e * ((model.x1 * 4) + (model.x2 * 1) + (model.x3 * 2))

    model.c1 = Constraint(expr = custo_total_pvc_b <= lim_pvc_b)
    model.c2 = Constraint(expr = custo_total_pvc_v <= lim_pvc_v)
    model.c3 = Constraint(expr = custo_total_pvc_e <= lim_pvc_e)
    model.c4 = Constraint(expr = model.x1 >= 0)
    model.c5 = Constraint(expr = model.x2 >= 0)
    model.c6 = Constraint(expr = model.x3 >= 0)

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

solution()