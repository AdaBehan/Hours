#test if the computer is currently locked. if locked rets True

if (gnome-screensaver-command -q | grep "is active");
then
    echo True        
else
    echo False
fi
