# cpt_telescope_control

# Radiotelescopio — Panel de Control SPID MD-1

## Archivos

```
radiotelescopio/
├── server.py   ← Servidor WebSocket / bridge TCP-SPID
├── gui.html    ← Interfaz gráfica (abrir en el navegador)
└── spid.py     ← Protocolo Rot2Prog (sin modificar)
```

## Requisitos

```bash
pip install websockets astropy
```

## Arranque

```bash
# 1. Iniciar el servidor bridge
python server.py

# 2. Abrir la GUI en el navegador
#    Opción A: el servidor la sirve en:
http://localhost:8766/gui

#    Opción B: abrir gui.html directamente con el navegador
#    (puede haber restricciones CORS en algunos navegadores)
```

## Uso

1. En la GUI, **verifica/ajusta** el host y puerto del controlador SPID.
2. Haz clic en **Conectar**.
3. Usa los comandos:
   - **Estado** — lee posición actual EL/AZ.
   - **Park** — mueve a AZ=0° EL=90°.
   - **Service** — mueve a AZ=0° EL=0°.
   - **STOP** — detiene todo movimiento y tracking.
   - **Mover EL/AZ** — movimiento manual a coordenadas.
   - **Seguimiento RA/Dec** — tracking astronómico continuo (actualización cada 5 s).

## Arquitectura

```
gui.html  ←── WebSocket ──→  server.py  ←── TCP/Telnet ──→  Controlador SPID
(Puerto 8765)                                               (10.17.89.223:23)
```

El servidor bridge:
- Convierte los comandos JSON del WebSocket en bytes Rot2Prog.
- Mantiene la conexión TCP persistente con el controlador.
- Calcula Alt/Az a partir de RA/Dec usando Astropy (ubicación: Calán).
- Hace broadcast del estado a todos los clientes conectados.
