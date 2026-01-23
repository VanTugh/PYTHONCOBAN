def print_config_table(config):
    if not config:
        print("Dictionary rỗng!")
        return
    keys = list(config.keys())
    values = [str(v) for v in config.values()]
    max_key_len = max([len(k) for k in keys]) + 2 
    max_val_len = max([len(v) for v in values]) + 2
    line = f"+{'-' * max_key_len}+{'-' * max_val_len}+"
    print(line)
    for k, v in config.items():
        print(f"| {k:<{max_key_len-2}} | {str(v):<{max_val_len-2}} |")
        print(line)
def main():
    config = {
        "n": 1500,
        "CLUSTERS": 3,
        "ITER": 1000,
        "METHOD": "DCA CLUSTERING",
        "MEASURE": "EUCLIDEAN",
        "YEARS": 9,
        "MAX": 200
    }
    #1
    print("\n1. Nội dung từ điển ban đầu:")
    print_config_table(config)
    #2
    config["MEASURE"] = "MANHATAN"
    print(" sau khi sua : ")
    print_config_table(config)
    #3
    print("\n3. Thông số METHOD hiện tại:")
    print(f"   => {config.get('METHOD')}")
    config["LOSS FUNCTION"] = "SOFT MAX"
    print_config_table(config)
    if "YEARS" in config:
        del config["YEARS"]
    print_config_table(config)

    S = input(" nhap xau S : ")
    check = [k for k, v in config.items() if str(v) == S]
    if check :
        print("Co")
    else:
        print("Khum")
    
    print("\n7. Tạo SET các giá trị:")
    value_set = set(config.values())
    print(f"   {value_set}")

    # 8. Tạo LIST chứa toàn bộ giá trị
    print("\n8. Tạo LIST các giá trị:")
    value_list = list(config.values())
    print(f"   {value_list}")
if __name__ == "__main__":
    main()