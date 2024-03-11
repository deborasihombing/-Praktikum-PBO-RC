import random

class Father:
    def __init__(self, blood_types):
        self.blood_types = blood_types

    def get_allele(self):
        return random.choice(self.blood_types)

class Mother:
    def __init__(self, blood_types):
        self.blood_types = blood_types

    def get_allele(self):
        return random.choice(self.blood_types)

class Child:
    def __init__(self, father, mother):
        self.father_allele = father.get_allele()
        self.mother_allele = mother.get_allele()

    def determine_blood_type(self):
        possible_blood_types = [
            (self.father_allele, self.mother_allele),
            (self.mother_allele, self.father_allele)
        ]

        blood_type_mapping = {
            ('A', 'A'): 'Type A',
            ('A', 'O'): 'Type A',
            ('B', 'B'): 'Type B',
            ('B', 'O'): 'Type B',
            ('A', 'B'): 'Type AB',
            ('B', 'A'): 'Type AB',
            ('O', 'O'): 'Type O'
        }

        self.blood_type = blood_type_mapping.get(
            (self.father_allele, self.mother_allele), 'Type O')

    def __str__(self):
        return f"Child's blood type: {self.blood_type}"

# Example usage:
if __name__ == "__main__":
    father_blood_types = input("Enter father's blood types (e.g., 'A' or 'AB'): ").upper()
    mother_blood_types = input("Enter mother's blood types (e.g., 'B' or 'O'): ").upper()

    father = Father(father_blood_types)
    mother = Mother(mother_blood_types)

    child = Child(father, mother)
    child.determine_blood_type()

    print(child)
