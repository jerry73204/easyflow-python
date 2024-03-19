#!/usr/bin/env python3
import pyeasyflow
import time
import struct
from pathlib import Path

script_dir = Path(__file__).resolve().parent

flow = pyeasyflow.load_dataflow(script_dir / 'dataflow.json5')
sender = flow.build_sender('publisher')

while True:
    tick = int(time.time())
    payload = struct.pack("<L", tick)
    sender.send(payload)
    print(f"sent {tick}")
    time.sleep(1)
