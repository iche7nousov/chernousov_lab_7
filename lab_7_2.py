"""
Решите задачу: создайте словарь, где ключами являются числа, а значениями – строки.
Примените к нему метод items(), c с помощью полученного объекта dict_items создайте
новый словарь, "обратный" исходному, т. е. ключами являются строки, а значениями –
числа

"""

if __name__ == "__main__":
    first_dic = {1: "Один", 2: "Два", 3: "Три"}
    last_dic = {}

    for key, value in first_dic.items():
        print(key, value)
        last_dic[value] = key

    print(last_dic)