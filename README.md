# **Python** Syntax Compiler :desktop_computer:


## Description

Dalam proses pembuatan program dari sebuah bahasa menjadi instruksi yang dapat dieksekusi oleh mesin, terdapat pemeriksaan sintaks atau kompilasi bahasa yang dibuat oleh programmer. Kompilasi ini bertujuan untuk memastikan instruksi yang dibuat oleh programmer mengikuti aturan yang sudah ditentukan oleh bahasa tersebut.

Program ini berisi implementasi compiler untuk Python untuk statement-statement dan sintaks-sintaks bawaan Python. Konsep CFG digunakan untuk pengerjaan compiler yang mengevaluasi syntax program. Untuk nama variabel dalam program, digunakan FA.

## Getting Started

### Dependencies

* [Python 3](https://www.python.org/downloads/)
* Operating System

### Executing program

1. Clone program dengan menjalankan command di bawah ini pada terminal / bash
    ```
    git clone https://github.com/graceclaudia19/compiler-cfg-python.git
    ```
2. Masukkan kode yang ingin diperiksa syntax-nya pada file `py.py`

3. Jalankan terminal, pastikan berada di root folder kemudian jalankan command berikut
    ```
    python main.py py.py
    ```
4. Hasil pemeriksaan Syntax akan keluar, apabila diterima akan mengembalikan `Accepted`, sebaliknya mengembalikan `Not accepted`

    ```
    ...directory...\compiler-cfg-python> python main.py py.py
    Accepted
    ```
## Folder Structure
```
compiler-cfg-python/
├─ grammar/
│  ├─ CFG.txt
│  ├─ CNF.txt
│  ├─ terminal.txt
├─ algorithm/
│  ├─ convertcfg.py
│  ├─ cyk.py
├─ main.py
├─ py.py
├─ README.md
```

## Authors

- [Grace Claudia](https://github.com/graceclaudia19) - 13520078 
- [Sarah Azka Arief](https://github.com/azkazkazka) - 13520083
- [Patrick Amadeus Irawan](https://github.com/patrickamadeus) - 13520109



## Acknowledgments

Inspiration, code snippets, etc.
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [dbader](https://github.com/dbader/readme-template)
* [zenorocha](https://gist.github.com/zenorocha/4526327)
* [fvcproductions](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46)