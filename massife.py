class Massif:
    def __init__(self, size=8):
        self.CONST_SIZE_MASSIF = size
        
    def create_new_massif(self):
        line = input("Введите символы через пробел: ")
        massif = list(map(int, line.split()))
        
        if len(massif) < self.CONST_SIZE_MASSIF:
            for i in range(self.CONST_SIZE_MASSIF-len(massif)):
                massif.insert(0, 0)
        elif len(massif) > self.CONST_SIZE_MASSIF:
            for i in range(len(massif)-self.CONST_SIZE_MASSIF):
                massif.pop(0)
    
        return massif
    
    def read_new_massif(self, file_name):
        file = open(file_name, "r")
        line = file.readline()
        massif = list(map(int, line.split()))
        file.close()
        if len(massif) < self.CONST_SIZE_MASSIF:
            for i in range(self.CONST_SIZE_MASSIF-len(massif)):
                massif.insert(0, 0)
        elif len(massif) > self.CONST_SIZE_MASSIF:
            for i in range(len(massif)-self.CONST_SIZE_MASSIF):
                massif.pop(0)
    
        return massif
        
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

