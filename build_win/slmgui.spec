# -*- mode: python -*-
# this requires the lib directory to be on the library path when freezing
# export DYLD_LIBRARY_PATH="./lib/"
# also requires dev version of pyinstaller and python 3.5 (not 3.6)
# pip install git+https://github.com/pyinstaller/pyinstaller.git

import os
from PyInstaller.building.build_main import Analysis, PYZ, EXE, COLLECT, BUNDLE

###############

block_cipher = None
APP_NAME = 'LLSpy-SLM'
DEBUG = False
ONEFILE = True
WINDOWED = True
UPX = False

#####################

# put version info into __version__ variable
with open('../slmgen/version.py') as v:
    exec(v.read())

datafiles = [(os.path.abspath('../img/slmgen_logo.ico'), 'img'),
             (os.path.abspath('../img/slmgen_logo.png'), 'img')]

a = Analysis(['../slmgen/__main__.py'],
            pathex=[os.path.abspath('..')],
            binaries=[],
            datas=datafiles,
            hiddenimports=[],
            hookspath=[],
            runtime_hooks=[],
            excludes=['llspy', 'fiducialreg', 'docs', 'tests'],
            win_no_prefer_redirects=False,
            win_private_assemblies=False,
            cipher=block_cipher)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)


exe = EXE(pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    name=APP_NAME,
    debug=DEBUG,
    strip=False,
    upx=UPX,
    version=None,  # optional windows version file
    # runtime_tmpdir=None,  #  used for --onefile
    console=(not WINDOWED),
    icon='../img/slmgen_logo.ico')

if not ONEFILE:
    coll = COLLECT(exe,   # only without --onefile
                a.binaries,
                a.zipfiles,
                a.datas,
                strip=False,
                upx=UPX,
                name=APP_NAME)
