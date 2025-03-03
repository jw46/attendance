destination=/run/user/1000/gvfs/afc:host=00008110-0006015636F0A01E,port=3/com.omz-software.Pythonista3/
rm -r ${destination}app/*
cp -r app/ ${destination}
cp app.py ${destination}app.py

