#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: snmp_modul.py
Tujuan: Monitoring SNMPv2c dan mengambil sysName VM.
NIM: 2409106051 | Nama: Muhammad Husein Permadi
"""
import asyncio
from pysnmp.hlapi.v3arch.asyncio import *

nim = "2409106051"
host_vm = "127.0.0.1"
port_snmp_vm = 1161
community = "comm_051"

async def cek_snmp():
    try:
        errorIndication, errorStatus, errorIndex, varBinds = await get_cmd(
            SnmpEngine(),
            CommunityData(community),
            await UdpTransportTarget.create((host_vm, port_snmp_vm)),
            ContextData(),
            ObjectType(ObjectIdentity("1.3.6.1.2.1.1.5.0"))
        )
        if errorIndication:
            hasil = "[SNMP] GAGAL: " + str(errorIndication)
        elif errorStatus:
            hasil = "[SNMP] GAGAL: " + errorStatus.prettyPrint()
        else:
            hasil = "\n".join(
                "[SNMP] sysName VM: " + str(vb[1]) for vb in varBinds
            )
        print(hasil)
        return hasil
    except Exception as e:
        hasil = "[SNMP] GAGAL: " + str(e)
        print(hasil)
        return hasil

if __name__ == "__main__":
    asyncio.run(cek_snmp())
