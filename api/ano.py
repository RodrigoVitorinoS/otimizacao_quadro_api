pesos_neja_3= {'Geografia': 15.71,
               'Matemática': 14.92,
               'Português': 15.23,
               'História': 13.72,
               'Filosofia': 14.06,
               'Educação Física': 13.96,
               'Sociologia': 12.4}


pesos_neja_2= {'Matemática': 14.41,
               'Português': 15.08,
               'Vida': 15.14,
               'Química': 13.22,
               'Biologia': 13.06,
               'Física': 15.15,
               'Artes': 13.94}


pesos_neja_1= {'Geografia': 13.59,
               'Matemática': 16.47,
               'Português': 16.21,
               'História': 15.24,
               'Filosofia': 13.12,
               'Educação Física': 13.12,
               'Inglês': 12.24}


pesos_terceiro= {'Geografia': 9.33,
                 'Matemática': 9.39,
                 'Português': 9.73,
                 'História': 7.03,
                 'Filosofia': 9.3,
                 'Química': 8.79,
                 'Biologia': 9.39,
                 'Educacao Física': 9.33,
                 'Física': 9.25,
                 'Língua Estrangeira': 9.6,
                 'Sociologia': 8.87}


pesos_segundo= {'Geografia': 8.83,
                'Matemática': 8.52,
                'Português': 8.58,
                'História': 8.84,
                'Filosofia': 8.44,
                'Química': 8.68,
                'Biologia': 6.64,
                'Educacao Física': 8.51,
                'Física': 8.83,
                'Artes': 8.73,
                'Língua Estrangeira': 6.89,
                'Sociologia': 8.51}


pesos_primeiro = {
    'Geografia':9.3,
    'Matemática':9.44,
    'Português':9.31,
    'Projeto de Vida':8.44,
    'Química':9.15,
    'Educacao Física':9.2,
    'História':9.49,
    'Filosofia':9.3,
    'Biologia':9.48,
    'Inglês':7.6,
    'Física':9.28

}


pesos_nono= {'Geografia': 9.97,
             'Matemática': 10.23,
             'Português': 10.09,
             'História': 10.22,
             'Educação Física': 10.22,
             'Inglês': 9.84,
             'Ciências': 10.01,
             'Artes': 9.6,
             'RPM': 9.82,
             'PT': 10.0}


pesos_oitavo= {'Geografia': 10.01,
               'Matemática': 9.84,
               'Português': 9.9,
               'História': 9.97,
               'Educação Física': 10.17,
               'Inglês': 9.72,
               'Ciências': 10.05,
               'Letramento Matemática': 9.98,
               'Letramento Português': 10.2,
               'Artes': 10.15}


pesos_setimo = {'Geografia': 9.98,
                'Matemática': 10.25,
                'Português': 9.9,
                'História': 9.93,
                'Educação Física': 10.24,
                'Inglês': 9.86,
                'Ciências': 9.8,
                'Letramento Matemática': 10.23,
                'Letramento Português': 10.37,
                'Artes': 9.43}


pesos_sexto = {'Geografia': 9.89,
               'Matemática': 10.15,
               'Português': 10.27,
               'História': 10.13,
               'Educação Física': 9.88,
               'Inglês': 10.02,
               'Ciências': 9.95,
               'Letramento Matemática': 10.1,
               'Letramento Português': 9.76,
               'Artes': 9.85}

def pesos(ano):
    match ano:
        case 'primeiro':
            return pesos_primeiro
        case 'segundo':
            return pesos_segundo
        case 'terceiro':
            return pesos_terceiro
        case 'sexto':
            return pesos_sexto
        case 'setimo':
            return pesos_setimo
        case 'oitavo':
            return pesos_oitavo
        case 'nono':
            return pesos_nono
        case 'neja_1':
            return pesos_neja_1
        case 'neja_2':
            return pesos_neja_2
        case 'neja_3':
            return pesos_neja_3
        case _:
            return "Ano Inválido"

        


