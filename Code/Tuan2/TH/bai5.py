from Bai5.operations import vec_add, vec_sub, vec_length, vec_invert
from Bai5.display import input_vector, show_vector

def main_2_5():
    print("\n--- BÀI 2.5: VECTOR 3D ---")
    v1 = input_vector("A")
    v2 = input_vector("B")
    
    # Cộng
    v_sum = vec_add(v1, v2)
    show_vector(v_sum, "Tổng A + B")
    
    # Trừ
    v_diff = vec_sub(v1, v2)
    show_vector(v_diff, "Hiệu A - B")
    
    # Độ dài A
    len_a = vec_length(v1)
    print(f"Độ dài vector A: {len_a:.2f}")
    
    # Đối xứng A
    v_inv = vec_invert(v1)
    show_vector(v_inv, "Đối xứng của A")

if __name__ == "__main__":
    main_2_5()