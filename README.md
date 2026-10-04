# UTS Jaringan Komputer Lanjut — Integration Network with Python

**Nama:** Muhammad Husein Permadi
**NIM:** 2409106051
**Program Studi:** Informatika
**Mata Kuliah:** Jaringan Komputer Lanjut

## Deskripsi Project

Project ini merupakan implementasi UTS mata kuliah Jaringan Komputer Lanjut dengan tema **Integration Network with Python**.

Program dibuat secara modular dan terdiri dari beberapa bagian, mulai dari penyimpanan identitas cabang, akses VM melalui SSH, monitoring menggunakan SNMP, pembuatan pesan NETCONF, analisis data telemetry, hingga integrasi seluruh modul melalui `main.py`.

## Struktur Project

```text
.
├── identitas.py
├── ssh_modul.py
├── snmp_modul.py
├── netconf_modul.py
├── telemetry_modul.py
├── main.py
├── README.md
└── .gitignore
```

### Penjelasan File

| File                 | Fungsi                                                                   |
| -------------------- | ------------------------------------------------------------------------ |
| `identitas.py`       | Menyimpan identitas mahasiswa dan kode cabang serta membuat ID perangkat |
| `ssh_modul.py`       | Mengakses VM melalui SSH menggunakan Paramiko                            |
| `snmp_modul.py`      | Mengambil informasi `sysName` melalui SNMPv2c                            |
| `netconf_modul.py`   | Membuat pesan XML NETCONF untuk konfigurasi VLAN                         |
| `telemetry_modul.py` | Menganalisis dan mengklasifikasikan data telemetry                       |
| `main.py`            | Mengintegrasikan seluruh modul dan menampilkan laporan akhir             |
| `README.md`          | Dokumentasi project                                                      |
| `.gitignore`         | Mengabaikan file/folder yang tidak perlu dimasukkan ke repository        |

---

## 1. Identitas Cabang

File:

```text
identitas.py
```

Modul ini digunakan untuk menyimpan identitas mahasiswa dan identitas cabang.

Konfigurasi yang digunakan:

```python
nim = "2409106051"
nama = "Muhammad Husein Permadi"
kode_cabang = "051"
```

Modul juga memiliki function:

```python
buat_id_perangkat(jenis, nomor)
```

Function tersebut menghasilkan ID perangkat dengan format:

```text
kode_cabang-jenis-nomor
```

Contoh:

```python
buat_id_perangkat("SW", 1)
```

menghasilkan:

```text
051-SW-1
```

---

## 2. Akses SSH

File:

```text
ssh_modul.py
```

Modul ini digunakan untuk mengakses VM menggunakan library **Paramiko**.

Konfigurasi SSH:

```text
Host     : 127.0.0.1
Port     : 2222
Username : husein051
```

Function utama:

```python
cek_ssh()
```

Function tersebut melakukan koneksi SSH kemudian menjalankan dua perintah diagnostik:

```text
hostname
whoami
```

Hasil yang diperoleh kemudian ditampilkan dan dikembalikan dalam bentuk dictionary.

Contoh hasil:

```text
[SSH] hostname VM : nama-host
[SSH] whoami di VM : husein051
```

Apabila terjadi kegagalan koneksi, program menggunakan `try/except` sehingga program tidak langsung berhenti.

---

## 3. Monitoring SNMP

File:

```text
snmp_modul.py
```

Modul ini digunakan untuk mengambil informasi `sysName` dari VM menggunakan **SNMPv2c**.

Library yang digunakan:

```python
pysnmp
```

API yang digunakan mengikuti implementasi asynchronous:

```python
from pysnmp.hlapi.v3arch.asyncio import *
```

Konfigurasi SNMP:

```text
Host      : 127.0.0.1
Port      : 1161
Community : comm_051
```

OID yang digunakan untuk mengambil `sysName`:

```text
1.3.6.1.2.1.1.5.0
```

Function utama:

```python
async def cek_snmp()
```

Karena function menggunakan asynchronous API, function dijalankan menggunakan:

```python
asyncio.run(cek_snmp())
```

Jika berhasil, program menampilkan nama perangkat:

```text
[SNMP] sysName VM: ...
```

Jika terjadi kesalahan, program menampilkan pesan:

```text
[SNMP] GAGAL: ...
```

---

## 4. Pembuatan Pesan NETCONF

File:

```text
netconf_modul.py
```

Modul ini digunakan untuk membuat pesan XML NETCONF.

Pembuatan XML dilakukan secara programatis menggunakan:

```python
xml.etree.ElementTree
```

Function utama:

```python
buat_pesan_netconf()
```

Pesan NETCONF terdiri dari tiga bagian utama:

### Messages Layer

Bagian ini menggunakan elemen:

```xml
<rpc>
```

sebagai pembungkus pesan NETCONF.

### Operations Layer

Operasi yang digunakan adalah:

```xml
<edit-config>
```

dengan target:

```xml
<running>
```

### Content Layer

Bagian content berisi konfigurasi VLAN.

VLAN yang digunakan pada project:

```text
VLAN ID : 051
Nama   : VLAN_051
```

Pesan XML dibuat menggunakan `ElementTree`, bukan ditulis sebagai string XML secara manual.

---

## 5. Analisis Data Telemetry

File:

```text
telemetry_modul.py
```

Modul ini digunakan untuk melakukan analisis terhadap data sampel telemetry.

Data disimpan dalam dictionary Python dengan parameter:

```text
cpuUsage
```

Contoh struktur data:

```python
data_telemetry = {
    "sampel_1": {"cpuUsage": 5},
    "sampel_2": {"cpuUsage": 50},
    "sampel_3": {"cpuUsage": 81}
}
```

Function utama:

```python
klasifikasi_telemetry()
```

Klasifikasi CPU menggunakan aturan:

| Nilai `cpuUsage` | Kategori |
| ---------------: | -------- |
|             > 80 | KRITIS   |
|            50–80 | WASPADA  |
|             < 50 | NORMAL   |

Contoh hasil:

```text
[TELEMETRY] sampel_1: cpuUsage=5% -> NORMAL
[TELEMETRY] sampel_2: cpuUsage=50% -> WASPADA
[TELEMETRY] sampel_3: cpuUsage=81% -> KRITIS
```

---

## 6. Integrasi Program

File:

```text
main.py
```

File ini digunakan untuk mengintegrasikan seluruh modul menjadi satu program.

Urutan proses:

```text
1. SSH
2. SNMP
3. NETCONF
4. Telemetry
5. Laporan akhir
```

SSH dijalankan menggunakan:

```python
cek_ssh()
```

SNMP dijalankan menggunakan:

```python
asyncio.run(cek_snmp())
```

Pesan NETCONF dibuat menggunakan:

```python
buat_pesan_netconf()
```

Data telemetry dianalisis menggunakan:

```python
klasifikasi_telemetry()
```

Kemudian seluruh hasil dirangkum menggunakan class:

```python
LaporanCabang
```

Class tersebut memiliki method:

```python
tampilkan_laporan()
```

yang digunakan untuk menampilkan laporan akhir seluruh proses.

---

## 7. Instalasi Library

Pastikan Python sudah terinstall.

Library yang digunakan dalam project:

```text
paramiko
pysnmp
```

Install menggunakan:

```bash
python -m pip install paramiko pysnmp
```

Jika menggunakan Windows dan perintah `python` tidak tersedia, dapat menggunakan:

```bash
py -m pip install paramiko pysnmp
```

---

## 8. Menjalankan Program

Pastikan seluruh file berada dalam satu folder:

```text
identitas.py
ssh_modul.py
snmp_modul.py
netconf_modul.py
telemetry_modul.py
main.py
```

Kemudian jalankan:

```bash
python main.py
```

atau pada Windows:

```bash
py main.py
```

Program akan menjalankan proses secara berurutan:

```text
SSH
 ↓
SNMP
 ↓
NETCONF
 ↓
Telemetry
 ↓
Laporan Akhir
```

---

## 9. Contoh Output

Contoh output program secara umum:

```text
[SSH] hostname VM : ...
[SSH] whoami di VM : ...

[SNMP] sysName VM: ...

[TELEMETRY] sampel_1: cpuUsage=5% -> NORMAL
[TELEMETRY] sampel_2: cpuUsage=50% -> WASPADA
[TELEMETRY] sampel_3: cpuUsage=81% -> KRITIS

======================================================================
LAPORAN AKHIR INTEGRASI JARINGAN
======================================================================
NIM  : 2409106051
Nama : Muhammad Husein Permadi

[HASIL SSH]
...

[HASIL SNMP]
...

[HASIL NETCONF]
...

[HASIL TELEMETRY]
sampel_1: cpuUsage=5% -> NORMAL
sampel_2: cpuUsage=50% -> WASPADA
sampel_3: cpuUsage=81% -> KRITIS
======================================================================
```

Hasil SSH dan SNMP bergantung pada kondisi VM serta service SSH/SNMP yang sedang berjalan.

---

## 10. Konfigurasi Personalisasi

Personalisasi yang digunakan dalam project:

```text
NIM          : 2409106051
Nama         : Muhammad Husein Permadi
Kode Cabang  : 051
Username SSH : husein051
Community    : comm_051
VLAN ID      : 051
```

Password/kredensial tidak dicantumkan dalam dokumentasi README.

---

## 11. Git

Project dikerjakan secara bertahap menggunakan Git sesuai struktur commit tugas.

Urutan commit minimum:

```text
Inisialisasi struktur project dan .gitignore
Tambah modul identitas cabang (identitas.py)
Tambah modul akses SSH (ssh_modul.py)
Tambah modul monitoring SNMP (snmp_modul.py)
Tambah modul pembuatan pesan NETCONF (netconf_modul.py)
Tambah modul analisis data telemetry (telemetry_modul.py)
Integrasi akhir: main.py dan README.md
UTS-final
```

Repository berisi seluruh source code project dan README sebagai dokumentasi.

---

## 12. Teknologi yang Digunakan

Project menggunakan:

* Python
* Paramiko
* PySNMP
* XML ElementTree
* SSH
* SNMPv2c
* NETCONF
* Telemetry
* Git

---

## Penutup

Project ini mengintegrasikan beberapa konsep jaringan menggunakan Python, yaitu identitas perangkat, akses remote menggunakan SSH, monitoring menggunakan SNMP, pembuatan konfigurasi NETCONF, analisis data telemetry, dan integrasi seluruh proses ke dalam satu laporan akhir.
