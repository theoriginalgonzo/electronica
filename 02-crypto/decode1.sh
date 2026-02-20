#!/bin/bash

text="$1"

# ---------------- ROT13 ----------------
rot13=$(echo "$text" | tr 'A-Za-z' 'N-ZA-Mn-za-m')
echo "=== ROT13 ==="
echo "$rot13"
echo

# ---------------- Atbash ----------------
atbash=$(echo "$text" | tr 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' \
                     'zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA')
echo "=== Atbash ==="
echo "$atbash"
echo

# ---------------- Hex ----------------
if [[ "$text" =~ ^(0x)?[0-9A-Fa-f]+$ ]]; then
    hex=$(echo "$text" | sed 's/^0x//' | xxd -r -p 2>/dev/null)
    echo "=== Hex ==="
    echo "$hex"
    echo
fi

# ---------------- Base64 ----------------
base64_dec=$(echo "$text" | base64 -d 2>/dev/null)
if [ -n "$base64_dec" ]; then
    echo "=== Base64 ==="
    echo "$base64_dec"
    echo
fi

# ---------------- Binary ----------------
if [[ "$text" =~ ^[01\ ]+$ ]]; then
    bin_dec=$(echo "$text" | awk '{for(i=1;i<=NF;i++)printf "%c", strtonum("0b"$i)}')
    echo "=== Binary ==="
    echo "$bin_dec"
    echo
fi

# ---------------- Caesar 1–25 ----------------
echo "=== Caesar 1–25 ==="

caesar() {
    local shift=$1
    local input="$2"
    local lower="abcdefghijklmnopqrstuvwxyz"
    local upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    local lower_shifted="${lower:$shift}${lower:0:$shift}"
    local upper_shifted="${upper:$shift}${upper:0:$shift}"

    echo "$input" | tr "${lower}${upper}" "${lower_shifted}${upper_shifted}"
}

for i in {1..25}; do
    decoded=$(caesar $i "$text")
    echo "Shift $i: $decoded"
done

