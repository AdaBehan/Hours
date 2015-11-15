# Simple SH script useing awk to get the active window ID and from that the 
# Windows name. The program will return only the name of the window 


ACTIVE_ID=$(xprop -root | awk '/_NET_ACTIVE_WINDOW\(WINDOW\)/{print $NF}') 

ACTIVE_NAME=$(xprop -id $ACTIVE_ID | awk '/WM_CLASS\(STRING\)/{print $NF}')

echo $ACTIVE_NAME

