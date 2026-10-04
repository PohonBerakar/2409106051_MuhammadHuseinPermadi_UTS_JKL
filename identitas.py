#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Nama file : identitas.py
Tujuan    : Menyimpan identitas cabang dan membuat ID perangkat.
Pembuat   : Muhammad Husein Permadi
"""

nim = "2409106051"
nama = "Muhammad Husein Permadi"
kode_cabang = "051"


def buat_id_perangkat(jenis, nomor):
    return f"{kode_cabang}-{jenis}-{nomor}"