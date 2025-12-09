from massife import Massif

primer_1 = Massif().create_new_massif()
Massif().print_massif(primer_1)
print(Massif().check_massif(primer_1))
name_file_1 = str(input("Введите название файла счтения: "))
primer_2 = Massif().read_new_massif(name_file_1)
Massif().print_massif(primer_2)
print(Massif().check_massif(primer_2))
Massif().print_conjunction_massif(primer_1, primer_2)
name_file_2 = str(input("Введите название записывающего файла: "))
Massif().write_conjunction_massif(primer_1, primer_2, name_file_2)


m1 = Massif(data=[1, 0, 1, 1, 0, 1, 0, 1])
m2 = Massif(data=[1, 1, 0, 1, 0, 0, 1, 1])

print("Исходные массивы:")
print(f"m1 = {m1}")
print(f"m2 = {m2}")

print(f"m1[0] = {m1[0]}")

result_and = m1 & m2
print(f"m1 & m2 = {result_and}")

result_shift_left = m1 << 2
print(f"m1 << 2 = {result_shift_left}")

result_shift_right = m1 >> 2
print(f"m1 >> 2 = {result_shift_right}")