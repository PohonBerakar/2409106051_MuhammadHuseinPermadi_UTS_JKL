#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: main.py
Tujuan: Integrasi akhir Bagian C sampai F.
NIM: 2409106051 | Nama: Muhammad Husein Permadi
"""
import asyncio
import paramiko
from snmp_modul import cek_snmp
from netconf_modul import buat_pesan_netconf
from telemetry_modul import klasifikasi_telemetry

nim = "2409106051"
nama = "Muhammad Husein Permadi"
host_vm = "127.0.0.1"
port_ssh_vm = 2222
user_ssh = "husein051"
pass_ssh = "8ebcec91bbaB"

def cek_ssh():
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host_vm, port=port_ssh_vm,
                       username=user_ssh, password=pass_ssh, timeout=5)

        stdin, stdout, stderr = client.exec_command("hostname")
        hasil_hostname = stdout.read().decode().strip()
        stdin, stdout, stderr = client.exec_command("whoami")
        hasil_whoami = stdout.read().decode().strip()

        hasil = (f"[SSH] hostname VM: {hasil_hostname}\n"
                 f"[SSH] whoami di VM: {hasil_whoami}")
        print(hasil)
        client.close()
        return hasil
    except Exception as e:
        hasil = "[SSH] GAGAL: " + str(e)
        print(hasil)
        return hasil

class LaporanCabang:
    def __init__(self, hasil_ssh, hasil_snmp, pesan_netconf, hasil_telemetry):
        self.hasil_ssh = hasil_ssh
        self.hasil_snmp = hasil_snmp
        self.pesan_netconf = pesan_netconf
        self.hasil_telemetry = hasil_telemetry

    def tampilkan_laporan(self):
        print("\n" + "=" * 70)
        print("LAPORAN AKHIR INTEGRASI JARINGAN")
        print("=" * 70)
        print(f"NIM  : {nim}")
        print(f"Nama : {nama}")
        print("\n[HASIL SSH]\n" + self.hasil_ssh)
        print("\n[HASIL SNMP]\n" + self.hasil_snmp)
        print("\n[HASIL NETCONF]\n" + self.pesan_netconf)
        print("\n[HASIL TELEMETRY]")
        for item in self.hasil_telemetry:
            print(f"{item['sampel']}: cpuUsage={item['cpuUsage']}% -> {item['kategori']}")
        print("=" * 70)

def main():
    hasil_ssh = cek_ssh()
    hasil_snmp = asyncio.run(cek_snmp())
    pesan_netconf = buat_pesan_netconf()
    hasil_telemetry = klasifikasi_telemetry()
    LaporanCabang(hasil_ssh, hasil_snmp, pesan_netconf, hasil_telemetry).tampilkan_laporan()

if __name__ == "__main__":
    main()
