#!/bin/sh

# Call with "PACKAGE_VERSION=[version number] ./build-windows.sh"
# The version from the current pip install of SkyTemple is used if no version number is set.
set -e

export XDG_DATA_DIRS="${BUILD_ROOT}/${MINGW}/share"

rm build -rf || true
rm dist -rf || true

pip3 install -U certifi

# Dummy python-igraph package to force not trying to install it (it has been renamed to igraph.)
pip3 install python_igraph*.whl
pip3 install igraph-*-mingw*.whl
pip3 install skytemple_rust-*-mingw*.whl
pip3 install tilequant-*-mingw*.whl
pip3 install lru_dict-*-mingw*.whl
pip3 install -r ../requirements-mac-windows.txt
pip3 install ..


if [ -n "$IS_DEV_BUILD" ]; then
  ./install-skytemple-components-from-git.sh
fi

pyinstaller skytemple-randomizer.spec

# Check if we need to copy the cacert file
if [ -f "dist/skytemple_randomizer/certifi/cacert.pem" ]; then
  echo "Moved cacert to correct place"
  cp -rf dist/skytemple_randomizer/certifi/cacert.pem dist/skytemple_randomizer/cacert.pem
fi

echo $1 > dist/skytemple_randomizer/VERSION
echo $1 > dist/skytemple_randomizer/data/VERSION
