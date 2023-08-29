from faker import Faker

fake = Faker()

def generate_fake_cpf():
    cpf = ""
    for _ in range(3):
        cpf += str(fake.random_int(min=100, max=999))
        cpf += "."
    cpf += str(fake.random_int(min=10, max=99))
    return cpf

num_cpfs = 1  # Número de CPFs a serem gerados

cpfs = [generate_fake_cpf() for _ in range(num_cpfs)]

for idx, cpf in enumerate(cpfs, start=1):
    print(f"CPF {idx}: {cpf}")
