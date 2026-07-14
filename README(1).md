# cpt_telescope_control

# Radio Telescope — SPID MD-1 Control Panel

> **Note:** The new scripts (`server.py`, `gui.html`) in this repository are based on the
> original scripts from
> [millimeter-wave-lab/cpt_telescope_control](https://github.com/millimeter-wave-lab/cpt_telescope_control).
> This repository also includes the original CPT control scripts plus the ones developed
> as part of this work.

## Files

```
radiotelescopio/
├── server.py   ← WebSocket / TCP-SPID bridge server
├── gui.html    ← Graphical interface (open in browser)
└── spid.py     ← Rot2Prog protocol (unmodified)
```

## Requirements

```bash
pip install websockets astropy
```

## Startup

```bash
# 1. Start the bridge server
python server.py

# 2. Open the GUI in the browser
#    Option A: the server serves it at:
http://localhost:8766/gui

#    Option B: open gui.html directly in the browser
#    (some browsers may have CORS restrictions)
```

## Usage

1. In the GUI, **check/adjust** the SPID controller's host and port.
2. Click **Connect**.
3. Use the commands:
   - **Status** — reads current EL/AZ position.
   - **Park** — moves to AZ=0° EL=90°.
   - **Service** — moves to AZ=0° EL=0°.
   - **STOP** — stops all movement and tracking.
   - **Move EL/AZ** — manual movement to given coordinates.
   - **RA/Dec Tracking** — continuous astronomical tracking (updates every 5 s).

## Architecture

```
gui.html  ←── WebSocket ──→  server.py  ←── TCP/Telnet ──→  SPID Controller
(Port 8765)                                                 (10.17.89.223:23)
```

The bridge server:
- Converts JSON commands from the WebSocket into Rot2Prog bytes.
- Maintains a persistent TCP connection with the controller.
- Computes Alt/Az from RA/Dec using Astropy (location: Calán).
- Broadcasts status to all connected clients.
