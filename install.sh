destination=/run/user/1000/gvfs/afc:host=00008110-0006015636F0A01E,port=3/com.omz-software.Pythonista3/
#destination=/run/user/1000/gvfs/afc:host=00008110-000E35E43AF2601E,port=3/com.omz-software.Pythonista3/
cp app.py ${destination}app.py
cp test_table_df_v.py ${destination}test_table_df_v.py
rm -r ${destination}app/
cp -r app/ ${destination}
# cp -r classes/ ${destination}
# cp -r groups/ ${destination}
# cp -r spreadsheets/ ${destination}
# cp -r att/ ${destination}
