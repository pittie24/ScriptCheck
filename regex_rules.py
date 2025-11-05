import re

# ========================
# POLA REGEX AWAL
# ========================

regex_rules = [
    {
        "id": "double_punctuation",
        "description": "Mendeteksi tanda baca yang muncul lebih dari satu kali berurutan (,, !! ?? ..)",
        "pattern": r"[.,!?]{2,}"
    },
    {
        "id": "lowercase_after_period",
        "description": "Mendeteksi huruf kecil setelah tanda titik",
        "pattern": r"\.\s+[a-z]"
    },
    {
        "id": "double_space",
        "description": "Mendeteksi spasi ganda antar kata",
        "pattern": r"\s{2,}"
    }
]

# ========================
# FUNGSI PENGUJIAN
# ========================

def test_regex_rules(text):
    results = []
    for rule in regex_rules:
        matches = re.findall(rule["pattern"], text)
        if matches:
            results.append({
                "rule": rule["id"],
                "description": rule["description"],
                "matches": matches
            })
    return results

# ========================
# CONTOH UJI
# ========================
if __name__ == "__main__":
    sample_text = "Halo,, nama saya budi. saya tinggal di bandung!!  saya suka kopi..  "
    results = test_regex_rules(sample_text)

    print("Teks uji:", sample_text)
    print("\nHasil deteksi:\n")
    for r in results:
        print(f"- {r['rule']} → {r['description']}")
        print(f"  Cocok dengan: {r['matches']}")
