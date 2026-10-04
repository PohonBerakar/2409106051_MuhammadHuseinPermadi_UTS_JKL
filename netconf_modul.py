#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: netconf_modul.py
Tujuan: Membuat pesan XML NETCONF untuk konfigurasi VLAN.
NIM: 2409106051 | Nama: Muhammad Husein Permadi
"""
import xml.etree.ElementTree as ET

def buat_pesan_netconf():
    # Messages layer: <rpc>
    rpc = ET.Element("rpc", {
        "message-id": "101",
        "xmlns": "urn:ietf:params:xml:ns:netconf:base:1.0"
    })

    # Operations layer: <edit-config>
    edit_config = ET.SubElement(rpc, "edit-config")
    target = ET.SubElement(edit_config, "target")
    ET.SubElement(target, "running")

    # Content layer: konfigurasi VLAN
    config = ET.SubElement(edit_config, "config")
    vlan = ET.SubElement(config, "vlan", {"xmlns": "urn:example:network"})
    ET.SubElement(vlan, "id").text = "051"
    ET.SubElement(vlan, "name").text = "VLAN_051"

    return ET.tostring(rpc, encoding="unicode") + "]]>]]>"

if __name__ == "__main__":
    print(buat_pesan_netconf())
