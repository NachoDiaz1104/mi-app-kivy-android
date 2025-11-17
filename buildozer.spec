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
# Nivel de log (2 = detallado, útil para depurar)
log_level = 2

# Advertir si se corre como root
warn_on_root = 1

# Versión de la API de Android que vas a usar para compilar
android.api = 35

# Min API soportada en el dispositivo
android.minapi = 24

# Bootstrap (sdl2 es el estándar actual para Kivy)
android.bootstrap = sdl2

# Aceptar automáticamente las licencias del SDK (IMPRESCINDIBLE para GitHub Actions)
android.accept_sdk_license = True

# Arquitecturas a compilar (dos habituales)
android.arch = arm64-v8a, armeabi-v7a

# Si querés reducir tamaño en release, más adelante podés jugar con estos:
# android.release = 0
# android.add_release_dependencies = 0

# Carpeta donde se guardan cosas temporales de buildozer (dejalo por defecto)
buildozer_dir = .buildozer

# Evitar que intente compilar para OSX/Windows dentro de Android build
# (dejalo tal cual)




