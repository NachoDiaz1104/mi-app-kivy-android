[app]
# Nombre que va a ver el usuario en el celular
title = Mis Tareas & Reclamos

# Nombre interno del paquete (sin espacios, solo minúsculas y guiones bajos)
package.name = mistareas

# Dominio “al revés” cualquiera que no exista (solo para identificar el paquete)
package.domain = org.nachodiaz

# Carpeta donde está tu main.py (en tu repo está en la raíz)
source.dir = .

# Extensiones de archivos que se incluyen en el APK
source.include_exts = py,kv,png,jpg,jpeg,db,sqlite3,ttf,ico,zip

# Versión de tu app
version = 0.1

# Módulos de Python que se empaquetan en el APK
# OJO: sin sqlite3 (no hace falta y da problemas)
requirements = python3,kivy==2.2.1,kivymd==1.1.1,plyer

# Orientación de la pantalla
orientation = portrait

# Si tu app usa ventana completa
fullscreen = 0

# Icono de la app (opcional) – si tenés un icono, descomentá y poné la ruta
# icon.filename = assets/icon.png

# Si usás presplash (pantalla de carga), podés definirlo acá
# presplash.filename = assets/presplash.png

# Modo de depuración (0 = no, 1 = sí)
use_library = 1

# Lenguaje a usar (por defecto Python)
osx.python_version = 3

# Permisos Android (descomentá si necesitás acceso a archivos / cámara / etc.)
# android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

# Si usás archivo local (SQLite en el directorio de la app) NO hace falta permiso especial.

[buildozer]
log_level = 2
warn_on_root = 1

# API de Android que usamos para compilar
android.api = 35
android.minapi = 24

# Aceptar licencias (no hace daño tenerlo en True)
android.accept_sdk_license = True

# ⚠️ Usar el SDK y NDK que YA VIENEN instalados en GitHub Actions
# (estas rutas son las que tiene el runner ubuntu-latest)
android.sdk_path = /usr/local/lib/android/sdk
android.ndk_path = /usr/local/lib/android/sdk/ndk/27.3.13750724

# Bootstrap por defecto para Kivy
android.bootstrap = sdl2






