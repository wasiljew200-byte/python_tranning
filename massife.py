class Massif:
    def __init__(self, size=8):
        self.CONST_SIZE_MASSIF = size

    def create_new_massif(self):
        try:
            line = input("Введите символы через пробел: ")
            if not line.strip():
                raise ValueError("Ввод не может быть пустым")
            massif = list(map(int, line.split()))
            if len(massif) < self.CONST_SIZE_MASSIF:
                for i in range(self.CONST_SIZE_MASSIF-len(massif)):
                    massif.insert(0, 0)
            elif len(massif) > self.CONST_SIZE_MASSIF:
                for i in range(len(massif)-self.CONST_SIZE_MASSIF):
                    massif.pop(0)
    
            return massif

        except ValueError as e:
            if "Ввод не может быть пустым" in str(e):
                raise
            raise ValueError("Все элементы должны быть целыми числами") from e


    def read_new_massif(self, file_name):
        try:
            if not file_name.strip():
                raise ValueError("Имя файла не может быть пустым")
            
            with open(file_name, "r") as file:
                line = file.readline()
                if not line.strip():
                    raise ValueError("Файл пуст")
                    
                massif = list(map(int, line.split()))
                if len(massif) < self.CONST_SIZE_MASSIF:
                    for i in range(self.CONST_SIZE_MASSIF-len(massif)):
                        massif.insert(0, 0)
                elif len(massif) > self.CONST_SIZE_MASSIF:
                    for i in range(len(massif)-self.CONST_SIZE_MASSIF):
                        massif.pop(0)
            
                return massif
                
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл {file_name} не найден")
        except ValueError as e:
            if "Имя файла не может быть пустым" in str(e):
                raise
            raise ValueError("Файл должен содержать только целые числа") from e

    def print_conjunction_massif(self, massif_a, massif_b, name="Результат конъюнкции"):
        massif_c = []
        for i in range(len(massif_a)):
            if massif_a[i] == massif_b[i]:
                massif_c.append(massif_a[i])
            else:
                massif_c.append(0)
                
        print(f"{name}:{massif_c}")
    
    def write_conjunction_massif(self, massif_a, massif_b, file_name, name="Рузультат конъюнкции"):
        file = open(file_name, "w")
        massif_c = []
        for i in range(len(massif_a)):
            if massif_a[i] == massif_b[i]:
                massif_c.append(massif_a[i])
            else:
                massif_c.append(0)
                
        file.write(f"{name}:{massif_c}")
        file.close()
    
    def check_massif(self, massif):
        for i in massif:
            if i != 0 and i != 1:
                return ("В массиве присутствуют плохие символы")
        return ("В массиве отсутствуют плохие символы")

    def print_massif(self, massif, name="Массив"):
        print(f"{name}:{massif}")