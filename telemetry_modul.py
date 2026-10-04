#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: telemetry_modul.py
Tujuan: Analisis sampel data telemetry cpuUsage.
NIM: 2409106051 | Nama: Muhammad Husein Permadi
"""
data_telemetry = {
    "sampel_1": {"cpuUsage": 5},
    "sampel_2": {"cpuUsage": 50},
    "sampel_3": {"cpuUsage": 81}
}

def klasifikasi_telemetry(data=None):
    if data is None:
        data = data_telemetry
    hasil = []
    for nama_sampel, nilai in data.items():
        cpu = nilai["cpuUsage"]
        if cpu > 80:
            kategori = "KRITIS"
        elif 50 <= cpu <= 80:
            kategori = "WASPADA"
        else:
            kategori = "NORMAL"
        item = {"sampel": nama_sampel, "cpuUsage": cpu, "kategori": kategori}
        hasil.append(item)
        print(f"[TELEMETRY] {nama_sampel}: cpuUsage={cpu}% -> {kategori}")
    return hasil

if __name__ == "__main__":
    klasifikasi_telemetry()
