device=/run/user/1000/gvfs/afc:host=00008110-0006015636F0A01E,port=3/com.omz-software.Pythonista3/
local=/home/jon/agh-backup/
ct=$(date +"%Y%m%d%H%M%S")
echo mkdir ${local}${ct}/
cp -r ${device} ${local}${ct}/