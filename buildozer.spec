[app]
title = Almaviva Bridge
package.name = almavivabridge
package.domain = org.elshamy.bridge
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0
requirements = python3,kivy,pyjnius

# إعدادات الشاشة
orientation = portrait
fullscreen = 0

# صلاحيات أندرويد المتقدمة (الإنترنت، الذاكرة، وخلفية النظام)
android.permissions = INTERNET, ACCESS_NETWORK_STATE, RECEIVE_BOOT_COMPLETED, FOREGROUND_SERVICE

# استهداف أندرويد
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1
