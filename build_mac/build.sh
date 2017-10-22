#!/usr/bin/env bash
rm -rf ./_dist
rm -rf ./_build

pyinstaller  --noconfirm --clean \
	--log-level=INFO \
	--distpath=./_dist \
	--workpath=./_build \
	--upx-dir="/usr/local/bin/" \
	slmgui.spec

# create the dmg
echo "creating the dmg..."
mkdir _dist/dmg
ln -s /Applications _dist/dmg
cp -r _dist/LLSpy-SLM.app _dist/dmg
hdiutil create _dist/LLSpy-SLM.dmg -srcfolder _dist/dmg
rm -rf _dist/dmg
rm -rf _dist/LLSpy-SLM
rm -rf _dist/LLSpy-SLM.app


# rm -rf _dist/LLSpy

# productbuild --component ./_dist/LLSpy.app /Applications LLSpy.pkg \
#   --sign "3rd Party Mac Developer Installer: Talley Lambert"