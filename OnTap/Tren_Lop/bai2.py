import string
def nhap_lieu_va_xu_ly():
    input_str = input("nhap vao chuoi : ")
    data = str.maketrans('', '', string.punctuation)
    cleaned_str = input_str.translate(data)
    return cleaned_str.lower().split()
def tao_dictionary(words_dict):
    words_dict = {
        key : words_dict.count(key)
        for key in words_dict
    }
    return words_dict
def sort_dictionary(words_dict):
    sorted_dict = sorted(
        words_dict.items(),
        key = lambda item: item[1],
        reverse = True
    )
    return sorted_dict
def main():
    words = nhap_lieu_va_xu_ly()
    print("Cac tu sau khi xu ly la:")
    print(words)
    words_dict = tao_dictionary(words)
    print(words_dict)
    sorted_dict = sort_dictionary(words_dict)
    print("Cac tu sau khi sap xep la:")
    print(sorted_dict)
if __name__ == "__main__":
    main()