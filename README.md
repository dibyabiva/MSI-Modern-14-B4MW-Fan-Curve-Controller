# Modern-14-B4MW-Fan-Curve-Controller

### This is a small script to control fan speeds via the embedded controller in this specific laptop model in Ubuntu 20.04.2

You need to run the script `set_fan_curve.py` as root, like: `sudo python3 set_fan_curve.py`

The script `startup_script.sh` can be added to your Ubuntu startup applications so that the fan curve is set everytime you log into the system.

You can tweak the fan speeds within the python script.
