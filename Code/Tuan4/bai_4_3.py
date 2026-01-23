from typing import Dict

def manage_student_scores() -> None:
    score: Dict[str, float] = {
        "SV001": 9,
        "SV002": 4,
        "SV003": 9.5,
        "SV004": 6
    }

    count = sum(1 for s in score.values() if 2.5 <= s <= 4.5)
    print(f"Số SV trong đoạn [2.5, 4.5]: {count}")

    score["SV006"] = 4

    new_score = {k: x for k, x in score.items() if x >= 2}
    print("Sau khi xóa:", new_score)

if __name__ == "__main__":
    manage_student_scores()
