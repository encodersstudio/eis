mkdir -p dist/dmg

rm -r dist/dmg/*

cp -r "dist/EIS.app" dist/dmg

test -f "dist/EIS.dmg" && rm "dist/EIS.dmg"

create-dmg \
  --volname "EIS" \
  --volicon "EIS.icns" \
  --icon-size 100 \
  --hide-extension "EIS.app" \
  --app-drop-link 425 120 \
  "dist/EIS.dmg" \
  "dist/dmg/"