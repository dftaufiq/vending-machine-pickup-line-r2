import os

LINE = "You shook me in March when the coil jammed \u2014 I've been leaning ever since, and the repairman says I'm tilted. I say I'm in love."

def main() -> None:
    assert 1 <= len(LINE) <= 200, f"LINE length {len(LINE)} out of range (1-200)"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read-back verification: the written line must be byte-identical.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise ValueError("entry.txt contents do not match LINE")


if __name__ == "__main__":
    main()
