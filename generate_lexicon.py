import json
import csv
import os

# Folder tempat file JSON disimpan
DATA_FOLDER = "data"

# Daftar file JSON
json_files = [
    "kbbi_v_part1.json",
    "kbbi_v_part2.json",
    "kbbi_v_part3.json",
    "kbbi_v_part4.json"
]

# List untuk menampung semua data
kbbi_data = []

# Baca semua file JSON
for file in json_files:
    path = os.path.join(DATA_FOLDER, file)
    print(f"Membaca {file} ...")

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Struktur utama = dictionary (key = kata)
    if isinstance(data, dict):
        for kata, isi in data.items():
            try:
                entri_list = isi.get("data", {}).get("entri", [])
                if not entri_list:
                    # Jika tidak ada entri, tetap masukkan kata dengan placeholder
                    kbbi_data.append([kata, "-", "-"])
                    continue

                for entri in entri_list:
                    nama = entri.get("nama", kata).strip()

                    # Jika ada makna, ambil semuanya
                    makna_list = entri.get("makna", [])
                    if not makna_list:
                        kbbi_data.append([nama, "-", "-"])
                    else:
                        for m in makna_list:
                            arti = ", ".join(m.get("submakna", [])) or "-"
                            kelas = ", ".join(m.get("kelas", [])) if "kelas" in m else "-"
                            kbbi_data.append([nama, arti, kelas])
            except Exception:
                kbbi_data.append([kata, "-", "-"])
    else:
        print(f"⚠️ Format tidak dikenali di {file}, dilewati.")

# Simpan ke CSV
with open("lexicon.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["kata", "arti", "kelas_kata"])
    writer.writerows(kbbi_data)

print(f"✅ File lexicon.csv berhasil dibuat!")
print(f"Total entri tersimpan: {len(kbbi_data)}")
