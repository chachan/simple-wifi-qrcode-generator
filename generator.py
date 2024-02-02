"""Simple WiFi QR code generator"""

import argparse

import pyqrcode


def gen(_args):
    """where pyqrcode does the magic"""
    code = f"WIFI:H:{_args.hidden};S:{_args.ssid};T:{_args.auth_type}"
    code = f"{code};;" if _args.auth_type == "nopass" else f"{code};P:{_args.password};;"
    qrcode = pyqrcode.create(code)
    qrcode.png(_args.filename, scale=5)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="wifi-qrcode-generator", description="Creates PNG for easier WiFi setup"
    )
    parser.add_argument("--auth-type", choices=["WPA", "WPA2", "WEP", "nopass"], default="nopass")
    parser.add_argument("--hidden", action="store_true")
    parser.add_argument("--password", default="")
    parser.add_argument("--ssid", default="")
    parser.add_argument("filename", type=argparse.FileType("w", encoding="utf-8"))
    args = parser.parse_args()

    if args.auth_type == "nopass" and args.password:
        parser.error("Password provided but authentication type is nopass")
    gen(args)
