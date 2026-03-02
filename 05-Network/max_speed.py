import sys

def calculate_max_speed(filename):
    max_speed = 0.0

    with open(filename, "r") as f:
        for line in f:
            line = line.strip()

            # Ensure the line contains at least 5 bytes (10 hex chars)
            if len(line) >= 10:
                try:
                    # Extract byte index 3 and 4 (0-based)
                    byte3 = int(line[6:8], 16)
                    byte4 = int(line[8:10], 16)

                    # Reconstruct 16-bit big-endian value
                    raw_speed = (byte3 << 8) + byte4

                    # Apply scaling from C snippet
                    speed_mph = (raw_speed / 100) * 0.6213751

                    if speed_mph > max_speed:
                        max_speed = speed_mph

                except ValueError:
                    # Skip malformed lines
                    continue

    return max_speed


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 max_speed.py <data_file>")
        sys.exit(1)

    filename = sys.argv[1]
    max_speed = calculate_max_speed(filename)

    print(f"Maximum Speed: {max_speed:.2f} mph")