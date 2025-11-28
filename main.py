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