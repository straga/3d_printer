
Example printer FLSUN
/opt/printer/flsun
                /cfg
                    /printer.cfg #klipper put manual, 
                    /moonraker.cfg #moonraker put manual , 
                    /.fluidd.json - # auto generate config 
                /klipper # repo
                /moonraker # repo
                /sdcard # store gcode
                /ui
                    /fluidd # extract fluidd.zip
                    /server.py # copy manual


# Fluidd:
on ORPi.
extract https://github.com/cadriel/fluidd/releases/download/v1.4.0/fluidd.zip -> /opt/printer/flsun/ui/fluidd
copy server.py -> /opt/printer/flsun/ui/fluidd/

Go to where docker fluidd.yml file.

docker-compose -f  fluidd.yml -p printer_ui build
docker-compose -f  fluidd.yml -p printer_ui up -d


# Klipper:

git clone from repo klipper to  /opt/printer/flsun/klipper
config -> /opt/printer/flsun/cfg

docker-compose -f  flsun.yml -p flsun run --rm --service-ports klliper bash
make config and other for run klipper

cd klipper
make menuconfig
make

make flash FLASH_DEVICE=/dev/ttyUSB0 # for Atmega
copy from build to SD for other.

# Moonraker
git clone from repo Moonraker https://github.com/Arksine/moonraker.git to  /opt/printer/flsun/moonraker
config -> /opt/printer/flsun/cfg


moonraker\plugins\file_manager.py
def register_directory(self, root, path):

        path = os.path.normpath(os.path.expanduser(path))
        if not os.path.isdir(path):
            logging.info("path: {}, for: {}, is not dir".format(path, root))
            return False
        # home = os.path.expanduser('~')
        # path = os.path.normpath(os.path.expanduser(path))
        # if not os.path.isdir(path) or path == home or \
        #         not (path.startswith(home) or path.startswith(ETC_DIR)):
        #     logging.info(
        #         f"\nSupplied path ({path}) for ({root}) not valid. Please\n"
        #         "check that the path exists and is a subfolder in the HOME\n"
        #         "directory. Note that the path may not BE the home directory.")
        #     return False



docker-compose -f  flsun.yml -p flsun build
docker-compose -f  fluidd.yml -p printer_ui up -d


bash:
docker-compose -f  flsun.yml -p flsun run --rm --service-ports moonraker bash





