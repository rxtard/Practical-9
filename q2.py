import subprocess
import time
NAME = "snesoshi"   # ← put your name here
def nfc_raw():
    try:
        return subprocess.check_output(
            ["/usr/bin/nfc-poll"],
            stderr=subprocess.DEVNULL,
            text=True
        )
    except subprocess.CalledProcessError:
        return None
try:
    while True:
        output = nfc_raw()
        if not output:
            time.sleep(0.5)
            continue
        for line in output.splitlines():
            parts = line.split()
            if parts and parts[0] == "UID":
                uid = "".join(parts[2:])
                print(f"{NAME}: {uid}")
                break
        time.sleep(0.5)
except KeyboardInterrupt:
    print("\nStopped")
