def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firtname": "Edder", "lastname": "Figueredo"}

    super_list = [
        {"firtname": "Edder", "lastname": "Figueredo"},
        {"firtname": "Alexander", "lastname": "Moreno"},
        {"firtname": "Marcia", "lastname": "Muñoz"},
        {"firtname": "Alejandra", "lastname": "Garcia"},
        {"firtname": "José", "lastname": "Martini"},
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(key, "->", value)

    for values in super_list:
        for key, value in values.items():
            print(value, end=" ")
        print(" ", sep="\n")
    print("Bye!")

if __name__ == '__main__':
    run()