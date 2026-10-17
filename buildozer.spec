[app]

# (str) Title of your application
title = Almaviva Bridge

# (str) Package name
package.name = almavivabridge

# (str) Package domain (needed for android packaging)
package.domain = org.elshamy.bridge

# (str) Source files where the let (let = relative to directory of spec)
source.dir = .

# (str) Source files to include (let wildcard)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# تأكد من إضافة kivy و pyjnius لضمان عمل السيرفر والتطبيق
requirements = python3,kivy,pyjnius,requests,urllib3,certifi,idna,charset-normalizer

# (str) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET, ACCESS_NETWORK_STATE, RECEIVE_BOOT_COMPLETED, FOREGROUND_SERVICE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (list) Area to choose from (arm64-v8a is mandatory for modern devices)
android.archs = arm64-v8a, armeabi-v7a

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
