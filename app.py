from flask import Flask, render_template, request, jsonify
import time
import random
import string
import logging

# Inisialisasi Flask
app = Flask(__name__)

# Variabel global untuk menyimpan data sementara
stored_text = ""
last_gen_type = "Belum Ada"

def brute_force(text, pattern):
    n, m = len(text), len(pattern)
    matches = []
    if m == 0: return []
    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:
            matches.append(i)
    return matches

def boyer_moore(text, pattern):
    m, n = len(pattern), len(text)
    if m == 0: return []
    bad_char = {pattern[i]: i for i in range(m)}
    matches = []
    s = 0
    while s <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            matches.append(s)
            s += (m - bad_char.get(text[s + m], -1)) if s + m < n else 1
        else:
            s += max(1, j - bad_char.get(text[s + j], -1))
    return matches

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    global stored_text, last_gen_type
    file = request.files.get('file')
    if not file: return jsonify({"error": "No file"}), 400
    stored_text = file.read().decode('utf-8')
    last_gen_type = "Dari Upload"
    return jsonify({"message": "File loaded", "length": len(stored_text)})

@app.route('/generate_source_text', methods=['POST'])
def generate_source_text():
    global stored_text, last_gen_type
    data = request.json
    length = int(data.get('length', 10000))
    gen_type = data.get('type', 'random')
    last_gen_type = gen_type.capitalize()
    if gen_type == 'worst':
        stored_text = ('A' * (length - 1)) + 'B'
    else:
        letters = string.ascii_letters + " "
        stored_text = ''.join(random.choice(letters) for i in range(length))
    return jsonify({"message": f"{gen_type} text generated", "length": len(stored_text)})

@app.route('/generate_pattern', methods=['POST'])
def generate_pattern():
    data = request.json
    length = int(data.get('length', 5))
    if not stored_text: return jsonify({"error": "Sediakan teks sumber dulu"}), 400
    if "Worst" in last_gen_type and len(stored_text) >= length:
        pattern = ('A' * (length - 1)) + 'B'
    else:
        start_idx = random.randint(0, max(0, len(stored_text) - length))
        pattern = stored_text[start_idx : start_idx + length]
    return jsonify({"pattern": pattern})

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    pattern = data.get('pattern')
    if not stored_text or not pattern: return jsonify({"error": "Data tidak lengkap"}), 400
    start_bf = time.perf_counter()
    bf_matches = brute_force(stored_text, pattern)
    bf_time = (time.perf_counter() - start_bf) * 1000
    start_bm = time.perf_counter()
    bm_matches = boyer_moore(stored_text, pattern)
    bm_time = (time.perf_counter() - start_bm) * 1000
    return jsonify({
        "bf_time": round(bf_time, 4),
        "bm_time": round(bm_time, 4),
        "matches_count": len(bf_matches),
        "text_len": len(stored_text),
        "pattern_len": len(pattern),
        "case_type": last_gen_type
    })

if __name__ == '__main__':
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)

    # 2. Tampilkan pesan kustom di terminal
    print("\n" + "="*40)
    print("      SERVER ANALISIS ALGORITMA       ")
    print("="*40)
    print("Aplikasi sedang berjalan di:")
    print("👉 http://127.0.0.1:5000")
    print("-" * 40)
    print("Tekan CTRL + C untuk mematikan server.")
    print("="*40 + "\n")

    # 3. Jalankan aplikasi tanpa debug mode untuk output bersih
    app.run(debug=False, port=5000)