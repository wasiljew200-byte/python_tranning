class Massif:
    def __init__(self, size=8, data=None):
        self.CONST_SIZE_MASSIF = size
        if data is not None:
            if len(data) < self.CONST_SIZE_MASSIF:
                self._data = [0] * (self.CONST_SIZE_MASSIF - len(data)) + data
            elif len(data) > self.CONST_SIZE_MASSIF:
                self._data = data[-self.CONST_SIZE_MASSIF:]
            else:
                self._data = data.copy()
        else:
            self._data = [0] * size

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


    # Перегрузка операций
    def __len__(self):
        return len(self._data)

    def __getitem__(self, index):
        if isinstance(index, slice):
            return self._data[index]
        if index < 0 or index >= len(self._data):
            raise IndexError("Индекс выходит за диапазон массива")
        return self._data[index]
    
    def __and__(self, other):  
        result = []
        for i in range(len(self)):
            if self[i] == 1 and other[i] == 1:
                result.append(1)
            else:
                result.append(0)
        return Massif(data=result, size=len(self))
    
    def __lshift__(self, k1):
        result = self._data[k1:] + [0] * k1
        return Massif(data=result, size=len(self))
    
    def __rshift__(self, k2):
        result = [0] * k2 + self._data[:-k2]
        return Massif(data=result, size=len(self))
    
    def __eq__(self, other):
        return self._data == other._data
    
    def __str__(self):
        return str(self._data)
    
    def __repr__(self):
        return f"Massif({self._data})"
    
    @property
    def data(self):
        return self._data.copy()