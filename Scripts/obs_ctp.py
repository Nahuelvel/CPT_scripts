from astropy.coordinates import SkyCoord, EarthLocation, AltAz
from astropy.time import Time
import astropy.units as u
import numpy as np

# ==================================================
# Coordenadas fijas del CPT
# ==================================================
CPT = EarthLocation(
    lat=-33.395701*u.deg,
    lon=-70.536878*u.deg,
    height=867*u.m
)

# ==================================================
# Datos del objeto
# ==================================================
ra = input("RA (ej: 08h34m00s): ")
dec = input("Dec (ej: -45d49m59.88s): ")

objeto = SkyCoord(
    ra=ra,
    dec=dec,
    frame='icrs'
)

# ==================================================
# Fecha
# ==================================================
fecha = input(
    "Fecha UTC (ej: 2026-06-05): "
)

# ==================================================
# Hora actual UTC
# ==================================================
hora = input(
    "Hora UTC (ej: 03:30:00): "
)

obs_time = Time(f"{fecha} {hora}")

# ==================================================
# Altitud y azimut instantáneos
# ==================================================
altaz = objeto.transform_to(
    AltAz(
        obstime=obs_time,
        location=CPT
    )
)

print("\n===== POSICIÓN ACTUAL =====")
print(f"Altitud : {altaz.alt.degree:.2f}°")
print(f"Azimut  : {altaz.az.degree:.2f}°")

# ==================================================
# Buscar culminación del día
# ==================================================
t0 = Time(f"{fecha} 00:00:00")

times = t0 + np.arange(24*60)*u.min

altitudes = []

for t in times:

    altaz_t = objeto.transform_to(
        AltAz(
            obstime=t,
            location=CPT
        )
    )

    altitudes.append(
        altaz_t.alt.degree
    )

imax = np.argmax(altitudes)

print("\n===== CULMINACIÓN =====")
print(
    f"Hora UTC: {times[imax].iso}"
)

print(
    f"Altitud máxima: "
    f"{altitudes[imax]:.2f}°"
)

print(
    f"Azimut en culminación: "
    f"{objeto.transform_to(AltAz(obstime=times[imax], location=CPT)).az.degree:.2f}°"
)