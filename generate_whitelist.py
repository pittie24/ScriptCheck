import csv

# Daftar singkatan umum Bahasa Indonesia
whitelist = [
    ("dr.", "dokter"),
    ("drg.", "dokter gigi"),
    ("dsb.", "dan sebagainya"),
    ("dst.", "dan seterusnya"),
    ("dll.", "dan lain-lain"),
    ("s.d.", "sampai dengan"),
    ("a.n.", "atas nama"),
    ("u.p.", "untuk perhatian"),
    ("dkk.", "dan kawan-kawan"),
    ("no.", "nomor"),
    ("spt.", "seperti"),
    ("yg", "yang"),
    ("ttd.", "tanda tangan"),
    ("spt.", "seperti"),
    ("sda.", "sama dengan di atas"),
    ("S.Pd.", "Sarjana Pendidikan"),
    ("S.H.", "Sarjana Hukum"),
    ("S.E.", "Sarjana Ekonomi"),
    ("S.Kom.", "Sarjana Komputer"),
    ("S.Sos.", "Sarjana Sosial"),
    ("M.Kom.", "Magister Komputer"),
    ("M.Si.", "Magister Sains")
]

whitelist.extend([
    ("yth.", "yang terhormat"),
    ("Yth.", "Yang Terhormat"),
    ("u.b.", "untuk beliau"),
    ("ttg.", "tentang"),
    ("tgl.", "tanggal"),
    ("bln.", "bulan"),
    ("thn.", "tahun"),
    ("Ir.", "Insinyur"),
    ("Dr.", "Doktor"),
    ("Drs.", "Doktorandus"),
    ("H.", "Haji"),
    ("Hj.", "Hajjah"),
    ("Prof.", "Profesor"),
    ("No.", "Nomor"),
    ("Kpd.", "Kepada"),
    ("Kpt.", "Kapitan"),
    ("PT.", "Perseroan Terbatas"),
    ("CV.", "Commanditaire Vennootschap"),
    ("RI", "Republik Indonesia"),
    ("TNI", "Tentara Nasional Indonesia"),
    ("Polri", "Kepolisian Negara Republik Indonesia")
])

# Simpan ke whitelist.csv
with open("whitelist.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["singkatan", "arti"])
    writer.writerows(whitelist)

print(f"✅ File whitelist.csv berhasil dibuat dengan {len(whitelist)} entri!")
