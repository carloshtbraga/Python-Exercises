class Person:
    def __init__(self, params):
        self.name = params.get('name', '')
        self.age = params.get('age', 0)
        self.gender = params.get('gender', '')

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")

# Exemplo de uso
person_data = {
    'name': 'Alice',
    'age': 25,
    'gender': 'female'
}

person = Person(person_data)
person.display_info()
