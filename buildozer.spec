[app]
title = Mis Tareas & Reclamos
package.name = mistareas
package.domain = org.nachodiaz
source.dir = .
source.include_exts = py,kv,png,jpg,jpeg,db,sqlite3,ttf,ico,zip
version = 0.1

# DEJARLO LO MÁS SIMPLE POSIBLE
requirements = python3,kivy,kivymd

orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

# Dejá que la imagen de Buildozer elija la API que sabe manejar
# (si más adelante hace falta, lo fijamos)
# android.api = 35
# android.minapi = 24

android.accept_sdk_license = True
android.bootstrap = sdl2
android.arch = arm64-v8a, armeabi-v7a

