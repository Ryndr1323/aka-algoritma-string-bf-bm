# 📜 Aplikasi Algoritma String: Brute Force dan Boyer-Moore

![Python Version](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)

Aplikasi dengan local-host dari Python dan HTML untuk *membandingkan kecepatan pencarian pattern" dengan "Algoritma Brute Force dan Boyer-Moore*

---

## Fitur Utama
* **🐍 Simplisitas**: Menggunakan *Python sebagai backend* dengan kecepatan performa yang stabil
* **📐 Ukuran Sampel**: Tidak perlu menjadi ahli IT, dengan beberapa klik anda dapat membandingkan kecepatan algoritma dengan mudah
* **⌛ Riwayat Analisa**: Aplikasi ini dapat menampung hingga *5 Iterasi Analisa* pengguna
* **▶️ Nyaman Digunakan**: Tombol yang ada pada aplikasi ini sangat simpel dan sehederhana sehingga tidak merumitkan pengguna

## Aplikasi yang Terlibat

* **Backend**: Python (Py) `flask`
* **Frontend**: HTML5
* **Aplikasi**: VS Code
  
## Cara Menjalankan Aplikasi

Pastikan anda sudah memiliki **Python** pada komputer anda

1. **Clone Repository ini dan Install tambahan Python package**
    ```bash
    git clone https://github.com/Ryndr1323/aka-algoritma-string-bf-bm.git
    cd aka-algoritma-string-bf-bm
    pip install flask
    ```

2. **Jalankan Server**
    Buka terminal di dalam folder, lalu ketik:
    ```bash
    python app.py
    ```

3. **Buka Browser**
    Dengan Browser apapun, akses alamat yang dikirimkan oleh terminal

---

## Struktur Projek

```text
aka-algoritma-string-bf-bm/
├── app.py               # Backend (Algoritma Perhitungan & Server Host)
├── templates/
│   └── index.html        # Tampilan Depan (Frontend HTML)
└── README.md             # Dokumentasi Project 
```

## Analisa Aplikasi Ini

Projek ini melakukan perbandingan terhadap 2 string-algorithm:

1. **Brute Force**
   * **Time Complexity**: O(n x m)
   * **Space Complexity**: O(1)
   * **Kelebihan**: Mudah dipahami dan diimplementasikan, serta efektif untuk teks pendek dengan pola sederhana yang tidak memerlukan optimisasi

3. **Boyer-Moore**
   * **Time Complexity**: O(n/m) pada Best/Average Case dan O(n x m) pada Worst Case
   * **Space Complexity**: O(k), dimana k adalah jumlah karakter unik dalam alfabet
   * **Kelebihan**: Lebih efisien pada teks panjang karena menggunakan pencocokan berdasarkan karakter, mengurangi jumlah perbandingan yang diperlukan untuk menemukan pola

**Hasil Benchmarking**
Melalui benchmarking ini, terbukti bahwa Boyer-Moore memiliki kompleksitas waktu rata-rata yang jauh lebih baik daripada Brute Force. Keunggulan utamanya terletak pada efisiensi waktu yang tetap stabil meskipun ukuran teks meningkat atau struktur teks bersifat repetitif (worst case), menjadikannya pilihan yang cocok sebagai sistem pencarian string yang modern.
Namun Brote Force masih bisa menjadi pilihan terbaik dibandingkan Boyer-Moore pada skala kecil dikarenakan *Space Complexity* yang lebih kecil dibandingkan Boyer-Moore.

---

## Creator

**Naufal Rayandra Gunawan**
* 103012400070
* Telkom University

**M Fahd Asyhab**
* 103012400358
* Telkom University





