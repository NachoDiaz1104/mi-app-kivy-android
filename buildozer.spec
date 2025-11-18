[app]
title = Mis Tareas & Reclamos
package.name = mistareas
package.domain = org.nachodiaz
source.dir = .
source.include_exts = py,kv,png,jpg,jpeg,db,sqlite3,ttf,ico,zip
version = 0.1
requirements = python3,kivy==2.2.1,kivymd==1.1.1,plyer
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

# API
android.api = 35
android.minapi = 24

# NO pongas sdk_path ni ndk_path, dejá que la action se encargue
# android.sdk_path = 
# android.ndk_path = 

# Aceptar licencias (esto sí está bien)
android.accept_sdk_license = True

android.bootstrap = sdl2
android.arch = arm64-v8a, armeabi-v7a

