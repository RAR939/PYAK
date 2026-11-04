
class Detail:
    def __init__(self, id, name, price, supplier_id):
        self.id = id
        self.name = name
        self.price = price
        self.supplier_id = supplier_id


class Supplier:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class DetailSupplier:
    def __init__(self, detail_id, supplier_id):
        self.detail_id = detail_id
        self.supplier_id = supplier_id


details = [
    Detail(1, "Процессор", 15000, 1),
    Detail(2, "Материнская плата", 12000, 2),
    Detail(3, "Оперативная память", 5000, 1),
    Detail(4, "Видеокарта", 45000, 3),
    Detail(5, "Блок питания", 7000, 2)
]

suppliers = [
    Supplier(1, "Поставщик электроники"),
    Supplier(2, "ООО Поставщик комплектующих"),
    Supplier(3, "ТехноИмпорт"),
    Supplier(4, "Поставщик оборудования")
]

detail_suppliers = [
    DetailSupplier(1, 1),
    DetailSupplier(1, 2),
    DetailSupplier(2, 2),
    DetailSupplier(3, 1),
    DetailSupplier(3, 3),
    DetailSupplier(4, 3),
    DetailSupplier(5, 2),
    DetailSupplier(5, 4)
]



print("ЗАПРОС 1")

result_1 = [
    (supplier.name, detail.name)
    for supplier in suppliers
    for detail in details
    if detail.supplier_id == supplier.id
]

result_1 = sorted(result_1, key=lambda x: x[0])

for supplier, detail in result_1:
    print(f"{supplier}: {detail}")



print("\nЗАПРОС 2")

result_2 = [
    (
        supplier.name,
        sum(
            detail.price
            for detail in details
            if detail.supplier_id == supplier.id
        )
    )
    for supplier in suppliers
]

result_2 = sorted(result_2, key=lambda x: x[1])

for supplier, total in result_2:
    print(f"{supplier}: {total:.2f} руб.")




print("\nЗАПРОС 3")

result_3 = [
    (
        supplier.name,
        [
            detail.name
            for link in detail_suppliers
            if link.supplier_id == supplier.id
            for detail in details
            if link.detail_id == detail.id
        ]
    )
    for supplier in suppliers
    if "поставщик" in supplier.name.lower()
]

for supplier, detail_list in result_3:
    print(f"{supplier}:")
    for detail in detail_list:
        print(f"  - {detail}")