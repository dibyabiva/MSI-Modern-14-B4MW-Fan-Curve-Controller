# Modern-14-B4MW-Fan-Curve-Controller

### This is a small script to control fan speeds via the embedded controller in this specific laptop model in Ubuntu 20.04.4

* Execute `sudo ./install.sh` 
* Reboot
* Execute `sudo crontab -e`
* Type `@reboot /path/to/startup_script.sh`
* Reboot

You can tweak the fan speeds within the python script `set_fan_curve.py`.
