#Système de Conversion de Notes
student_scores = [92, 85, 77, 68, 45, 89, 95, 100, 58, 72]

convert = lambda note: (
    'A' if note >= 90 else
    'B' if note >= 80 else
    'C' if note >= 70 else
    'D' if note >= 60 else
    'F'
)
notes_lettres = map(convert, student_scores)

notes_lettres = list(notes_lettres)
print(notes_lettres)

#Filtre des Salaires des Employés

employees = [
    {'name': 'Alice Johnson', 'salary': 45000, 'dept': 'Sales'},
    {'name': 'Bob Smith', 'salary': 55000, 'dept': 'Sales'},
    {'name': 'Charlie Brown', 'salary': 48000, 'dept': 'IT'},
    {'name': 'Diana Prince', 'salary': 42000, 'dept': 'Marketing'},
    {'name': 'Eve Wilson', 'salary': 38000, 'dept': 'Marketing'},
    {'name': 'Frank Miller', 'salary': 52000, 'dept': 'IT'}
]

is_eligible = lambda emp: emp['salary'] < 50000 and emp['dept'] in ['Sales', 'Marketing']
eligible_employees = filter(is_eligible, employees)

eligible_employees = list(eligible_employees)
print(eligible_employees)

#Calcul des Commissions de Vente

sales = [8500, 12000, 9500, 15000, 8000, 20000, 11000, 7000]

eligible_sales = filter(lambda sale: sale >= 10000, sales)
commissions = map(lambda sale: (sale - 10000) * 0.10, eligible_sales)
commissions = list(commissions)
print(commissions)


#Pipeline Robuste de Traitement de Données

raw_ages = ['25', 'invalid', '42', '150', 'None', '17', '-5', '71', 'thirty', '68', None, '55']

def safe_convert(age):
    try:
        return int(age)
    except (ValueError, TypeError):
        return None

def is_valid_age(age):
    return age is not None and 0 <= age <= 120


category = lambda age: (
    'Minor' if age < 18 else
    'Adult' if age <= 65 else
    'Senior'
)

converted_ages = map(safe_convert, raw_ages)
valid_ages = filter(is_valid_age, converted_ages)
categorized_ages = map(category, valid_ages)

result = list(categorized_ages)
print(result)


#Traitement et Analyse des Dossiers Étudiants

student_records = [
    {'name': 'Alice', 'scores': ['85', '92', '78']},
    {'name': 'Bob', 'scores': ['45', '52', '38']},
    {'name': None, 'scores': ['70', '68', '72']},       
    {'name': 'Charlie', 'scores': ['invalid', '85', '90']},  
    {'name': 'Diana', 'scores': ['88', '91', '95']},
    {'name': 'Eve', 'scores': ['55', '48', '62']}
]

def validate_record(record):
    try:
        name = record['name']
        scores = record['scores']

        if not isinstance(name, str) or name.strip() == '':
            return False

        scores = list(map(float, scores))
        return len(scores) == 3

    except:
        return False

def calculate_average(scores):
    scores = sorted(map(float, scores))[1:] 
    return sum(scores) / 2



valid_records = filter(validate_record, student_records)

name_average = map(
    lambda r: (r['name'], calculate_average(r['scores'])),
    valid_records
)

final_data = map(
    lambda item: (
        item[0],
        {
            'status': 'REUSSI' if item[1] >= 50 else 'ECHEC',
            'average': round(item[1], 2)
        }
    ),
    name_average
)


result = dict(final_data)
print(result)
