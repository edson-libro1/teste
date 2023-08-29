from faker import Faker

fake = Faker()

def generate_fake_telefone():
    telefone = ""
    for _ in range(2):
        telefone += str(fake.random_int(min=1000, max=9999))
        telefone += "."
    return telefone

num_telefones = 1  # Número de telefone a serem gerados

telefones = [generate_fake_telefone() for _ in range(num_telefones)]

for idx, telefone in enumerate(telefones, start=1):
    print(f"telefone {idx}: {telefone}")
