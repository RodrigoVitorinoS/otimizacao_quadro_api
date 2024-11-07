from ortools.linear_solver import pywraplp


tempos = [1, 2, 3, 4, 5, 6]
dias = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta']




def criar_modelo_inteiro(materias, tempos_materia, pesos):
    
    # Cria o solver
    solver = pywraplp.Solver.CreateSolver('SCIP')
    


    # Declara variáveis
    aulas = {}
    for dia in dias:
        for materia in materias:
            for tempo in range(1, tempos_materia[materia]+1):  # Considerando tempos de 1 a 6
                aulas[(dia, materia, tempo)] = solver.BoolVar(f'aulas[{dia, materia, tempo}]')

    menor_qtd_materias = solver.IntVar(0, solver.infinity(), 'menor_qtd_materias')

    # Função objetivo: maximizar a menor quantidade de matérias
    solver.Maximize(menor_qtd_materias)

    # Restrição de menor quantidade de aulas
    for dia in dias:
        solver.Add(sum(pesos[materia] * aulas[(dia, materia, tempo)] 
                       for materia in materias 
                       for tempo in range(1, tempos_materia[materia]+1)) >= menor_qtd_materias)

    # Restrição de tempos por dia
    for dia in dias:
        solver.Add(sum(aulas[(dia, materia, tempo)] 
                       for materia in materias 
                       for tempo in range(1, tempos_materia[materia]+1)) <= 6)

    # Restrição de tempos de cada matéria
    for materia in materias:
        solver.Add(sum(aulas[(dia, materia, tempo)] 
                       for dia in dias 
                       for tempo in range(1, tempos_materia[materia]+1)) == tempos_materia[materia])

    # Restrições específicas para as matérias
    for materia in materias:
        for tempo in range(1, tempos_materia[materia]+1):
            # Restrição de aulas de 1 a 6
            solver.Add(sum(aulas[(dia, materia, tempo)] for dia in dias) == 1)
        for dia in dias:
            solver.Add(aulas[(dia, materia, 2)] <= aulas[(dia, materia, 1)])
            # if tempos_materia[materia] >= 4:
            #     solver.Add(aulas[(dia, materia, 4)] <= aulas[(dia, materia, 3)])
            # if tempos_materia[materia] == 5:
            #     solver.Add(aulas[(dia, materia, 5)] <= aulas[(dia, materia, 4)])

            # Restrição de no máximo 4 aulas por dia
            solver.Add(sum(aulas[(dia, materia, tempo)] for tempo in range(1, tempos_materia[materia]+1)) <= 4)
    
    # Solução
    status = solver.Solve()

    # if status == pywraplp.Solver.OPTIMAL:
    #     return solver.Objective().Value()
    # else:
    #     return 'errado'
    

    quadro = {}
    for dia in dias:
        for materia in materias:
            for tempo in range(1, tempos_materia[materia]+1):
                if aulas[(dia, materia, tempo)].solution_value() == 1:
                    quadro[dia] = quadro.get(dia, []) + [materia]
    return quadro
    


