#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Nama file : ssh_modul.py
Tujuan    : Mengakses VM melalui SSH menggunakan Paramiko.
Pembuat   : Muhammad Husein Permadi
"""

import paramiko


# Konfigurasi SSH
host_vm = "127.0.0.1"
port_ssh_vm = 2222
user_ssh = "husein051"
pass_ssh = "8ebcec91bbaB"


def cek_ssh():
    try:
        client = paramiko.SSHClient()

        # Menerima host key secara otomatis
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Membuat koneksi SSH
        client.connect(
            host_vm,
            port=port_ssh_vm,
            username=user_ssh,
            password=pass_ssh,
            timeout=5
        )

        # Perintah diagnostik pertama
        stdin, stdout, stderr = client.exec_command("hostname")
        hasil_hostname = stdout.read().decode().strip()

        # Perintah diagnostik kedua
        stdin, stdout, stderr = client.exec_command("whoami")
        hasil_whoami = stdout.read().decode().strip()

        print("[SSH] hostname VM :", hasil_hostname)
        print("[SSH] whoami di VM :", hasil_whoami)

        client.close()

        return {
            "hostname": hasil_hostname,
            "whoami": hasil_whoami
        }

    except Exception as e:
        print("[SSH] GAGAL :", str(e))

        return {
            "hostname": "GAGAL",
            "whoami": "GAGAL"
        }