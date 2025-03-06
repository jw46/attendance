destination=/run/user/1000/gvfs/afc:host=00008110-000E35E43AF2601E,port=3/com.omz-software.Pythonista3/
cp app.py ${destination}app.py
rm -r ${destination}*
cp -r app/ ${destination}
cp app.py ${destination}app.py
cp a.py ${destination}a.py
cp -r metadata/ ${destination}
cp -r classes/ ${destination}
cp -r groups/ ${destination}
cp -r spreadsheets/ ${destination}
cp -r att/ ${destination}
mkdir ${destination}temp/
