from faker import Faker

fake = Faker()

# Gera um número de CPF válido
cpf = fake.cpf()
print(cpf)
