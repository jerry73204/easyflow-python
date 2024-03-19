#!/usr/bin/env python3
import pyeasyflow
import time
from pathlib import Path
import struct

script_dir = Path(__file__).resolve().parent

flow = pyeasyflow.load_dataflow(script_dir / 'dataflow.json5')

def callback(payload):
    (tick,) = struct.unpack("<L", payload)
    print(f"received {tick}")

listener = flow.listen('subscriber', callback)

while True:
    time.sleep(1)
