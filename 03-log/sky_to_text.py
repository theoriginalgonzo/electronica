import struct
import socket
from datetime import datetime, timezone

def read_int(f):
    return struct.unpack(">I", f.read(4))[0]

with open("hard.sky", "rb") as f:
    # ---- HEADER ----
    magic = f.read(8)
    version = struct.unpack(">B", f.read(1))[0]
    creation_ts = read_int(f)

    hostname_len = read_int(f)
    hostname = f.read(hostname_len).decode()

    flag_len = read_int(f)
    flag = f.read(flag_len).decode()

    entry_count = read_int(f)

    print("=== SKY LOG FILE (Human Readable) ===")
    print("Version:", version)
    print("Creation Time (UTC):",
          datetime.fromtimestamp(creation_ts, timezone.utc))
    print("Hostname:", hostname)
    print("Flag:", flag)
    print("Number of Entries:", entry_count)
    print("\n--- Log Entries ---")

    total_bytes = 0

    for i in range(entry_count):
        src_ip = socket.inet_ntoa(struct.pack(">I", read_int(f)))
        dst_ip = socket.inet_ntoa(struct.pack(">I", read_int(f)))
        ts = read_int(f)
        bytes_tx = read_int(f)

        total_bytes += bytes_tx

        print(f"{i+1}. {src_ip} -> {dst_ip} | "
              f"{datetime.fromtimestamp(ts, timezone.utc)} | "
              f"{bytes_tx} bytes")

    print("\nTotal Bytes Transferred:", total_bytes)

