#! /usr/bin/env python
"""Cloudmesh Raspberry Pi Mass Image Burner.
Usage:
  cm-burn create [--image=IMAGE]
                 [--group=GROUP]
                 [--names=HOSTS]
                 [--ips=IPS]
                 [--key=PUBLICKEY]
                 [--ssid=SSID]
                 [--psk=PSK]
                 [--domain=DOMAIN]
                 [--bootdrive=BOOTDRIVE]
                 [--rootdrive=ROOTDRIVE]
                 [-n --dry-run]
                 [-i --interactive]
  cm-burn ls [-ni]
  cm-burn rm IMAGE [-ni]
  cm-burn get [URL]
  cm-burn update
  cm-burn check install
  cm-burn hostname [HOSTNAME] [-ni]
  cm-burn ssh [PUBLICKEY] [-ni]
  cm-burn ip IPADDRESS [--domain=DOMAIN] [-ni]
  cm-burn wifi SSID [PASSWD] [-ni]
  cm-burn info [-ni]
  cm-burn image [--image=IMAGE]
                [--device=DEVICE]
                [-ni]
  cm-burn (-h | --help)
  cm-burn --version

Options:
  -h --help         Show this screen.
  -n --dry-run      Show output of commands but don't execute them
  -i --interactive  Confirm each change before doing it
  --version         Show version.
  --key=KEY         the path of the public key [default: ~/.ssh/id_rsa.pub].
  --ips=IPS         the IPs in hostlist format
  --image=IMAGE     the image [default: 2019-09-26-raspbian-buster.img]


Previously [default: 2018-06-27-raspbian-stretch.img]
Other images can be found at

https://downloads.raspberrypi.org/raspbian/images/

Files:
  This is not fully thought through and needs to be documented
  ~/.cloudmesh/images
  ~/.cloudmesh/inventory
  Location where the images will be stored for reuse

BUG:
  bootdrive and rootdrive will be removed in a future release as they are self
  discoverable

Description:
  cm-burn
  cm-burn create [--image=IMAGE]
                 [--group=GROUP]
                 [--names=HOSTS]
                 [--ips=IPS]
                 [--key=PUBLICKEY]
                 [--ssid=SSID]
                 [--psk=PSK]
                 [--bootdrive=BOOTDRIVE]
                 [--rootdrive=ROOTDRIVE]
  cm-burn update
        updates the downloaded images if new once are available
  cm-burn ls
        lists the downloaded images
  cm-burn rm IMAGE
        remove the image
  cm-burn get URL
        downloads the image at the given URL
  cm-burn get jessie
        abbreviation to download a specific version of an image.
        Identify what would be useful.
  cm-burn hostname HOSTNAME
        writes the HOSTNAME as hostname on the currently inserted SD Card
  cm-burn hostname
        reads the hostname form the current SD card

Example:
  cm-burn create --group=red --names=red[5-6] --ip=192.168.1.[5-6]
"""
from __future__ import print_function

import datetime
import getpass
import glob
import os
# noinspection PyCompatibility
import pathlib
import platform
import re
import subprocess
import sys
import textwrap
import time
import zipfile
from os import path
from pprint import pprint

import hostlist
import requests
import wget
from docopt import docopt
from prompter import yesno, prompt

# import wmi


VERSION = "0.1"
debug = False
dry_run = False
interactive = False


def os_is_windows():
    return platform.system() == "Windows"


def os_is_linux():
    return platform.system() == "Linux" and "raspberry" not in platform.uname()


def os_is_mac():
    return platform.system() == "Darwin"


def os_is_pi():
    return "raspberry" in platform.uname()


def truncate_file(pathlib_obj):
    """Truncate a file on disk before writing.

    This is strange, but was found to be necessary when mounting the newly
    burned image with extFS on OS X.
    """
    # NOTE (jobranam 2018-10-04): I'm not sure why, but on my OS X with
    # extFS overwriting the file with a shorter version was not working.
    # There were extra bytes at the end where the file was truncated. Adding
    # this next section fixed the problem. Maybe there is a better solution.
    # This problem only shows up the *first* time after burning the image.
    # Touching the file at all fixes it (e.g. just editing with vim fixes
    # it)
    with pathlib_obj.open("w") as f:
        f.truncate(0)
        f.flush()
        f.write("#")
        f.flush()

try:
    columns, lines = os.get_terminal_size()
except:
    columns = 80
    lines = 24

# TODO: the dirs are only needed for windows as they are
#  implemented now in self.filename for OSX
# we should remove them and make sure that cloudmesh images gets created on osx
# and linux if it does not exist
IMAGE_DIR = os.path.expanduser("~/.cloudmesh/images")
BOOT_DIR = ''


# noinspection PyPep8Naming
def WARNING(*args, **kwargs):
    print("WARNING:", *args, file=sys.stderr, **kwargs)


# noinspection PyPep8Naming
def ERROR(*args, **kwargs):
    print("ERROR:", *args, file=sys.stderr, **kwargs)


def getoutput(command):
    if dry_run:
        print("DRY RUN - skipping command:\n{}".format(command))
        return ""
    elif interactive:
        if not yesno(("About to run the command\n" + command +
                      "\nPlease confirm:")):
            return ""
    # TODO: Is this different or better than run() below? Can we just keep one?
    return subprocess.getoutput(command)


def run(command):
    if dry_run:
        print("DRY RUN - skipping command:\n{}".format(command))
        return ""
    elif interactive:
        if not yesno(("About to run the command\n" + command +
                      "\nPlease confirm:")):
            return ""
    return subprocess.run(command,
                          stdout=subprocess.PIPE).stdout.decode('utf-8')


def cat(path):
    with open(path, 'r') as file:
        content = file.read()
    return content


def execute_with_progress(command):
    if dry_run:
        print("DRY RUN - skipping command:\n{}".format(command))
        return
    elif interactive:
        if not yesno(("About to run the command\n" + command +
                      "\nPlease confirm:")):
            return
    p = subprocess.Popen(command.split(" "),
                         shell=True,
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         encoding='utf8')

    while True:
        line = p.stdout.readlines()
        if not line:
            break
        if len(line) > 0:
            print(line)


def execute(commands):
    """
       execute the commands that are included in the \n separated string line by
       line

       :param commands: the commands
       :return:
    """
    lines = commands.split("\n")
    for command in lines:
        if dry_run:
            print("DRY RUN - skipping command:\n{}".format(command))
            continue
        elif interactive:
            if not yesno(("About to run the command\n" + command +
                          "\nPlease confirm:")):
                continue
        print(command)
        proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT)
        while proc.poll() is None:
            line = proc.stdout.readline()
            if len(line) > 0:
                print(line.decode(
                    sys.stdout.encoding))
                # give output from your execution/your own message
        # self.commandResult = proc.wait() #catch return code


class PiBurner(object):

    def disable_password(self):
        """
        disables and replaces the password with a random string so that by
        accident the pi can not be logged into. The only way to login is via the
        ssh key

        :return:
        """
        raise NotImplementedError()

    def unmount(self, drive=None):
        """
        unmounts the filesystem regardless of OS using the given path
        :param drive:
        :return:
        """
        if os_is_windows():
            # TODO: Remove drive in windows, why can you not use the mount function build into windows?
            # TODO: Why do you need RemoveDrive?
            # script =  "mountvol {drive} /p".format(drive = self.root_drive)
            script = "RemoveDrive {drive}:".format(drive=self.root_drive)
            execute(script)
        elif os_is_mac():
            if drive is None:
                for drive in ['/Volumes/boot', '/Volumes/rootfs']:
                    execute("sudo umount {drive}".format(drive=drive))
            else:
                # Unmount the entire drive
                execute("sudo diskutil unmountDisk /dev/{drive}".format(
                    drive=drive))
                # execute("sudo umount {drive}".format(drive=drive))
        elif os_is_linux() or os_is_pi():
            # TODO: Why is this using getoutput instead of execute?
            getoutput("sudo umount {drive}".format(drive=self.root_drive))
            getoutput("sudo umount {drive}".format(drive=self.boot_drive))

    def mount(self, device=None, path=None):
        """
        mounts the device to the filesystem regardless of OS using the given
        path

        :param device:
        :param path:
        :return:
        """
        if os_is_windows():
            # TODO: Remove drive in windows, why can you not use the
            #  mount function build into windows?
            # TODO: Why do you need RemoveDrive?
            # mountvol %drive% /p
            # create volume mount pount as volume
            # volume = ...
            # remember to escape \ in volume
            # script = "mount {drive} {volume}:".format(drive=self.root_drive, volume=volume)
            # why remove, should we not mount?
            # script = "RemoveDrive {drive}:".format(drive = self.root_drive)
            # execute(script)
            raise NotImplementedError()
        elif os_is_mac():
            # extFS does outomount so we just check i f they are mounted
            # TODO: check if they exist

            # BUG drive is not defined.

            drive = None

            if drive is None:
                drives = ['/Volume/boot', 'Volume/rootfs']
            else:
                drives = [drive]
            for drive in drives:
                if not os.path.isdir(drive):
                    ERROR('drive is not mounted:', drive)

            #
            # if drive is None:
            #    for drive in ['/Volume/boot', 'Volume/rootfs']:
            #        execute("sudo mount {drive}".format(drive=drive))
            # else:
            #    execute("sudo mount {drive}".format(drive=drive))
        else:
            raise NotImplementedError()

    def disable_password_ssh(self):
        sshd_config = self.filename("/etc/ssh/sshd_config")
        new_sshd_config = ""
        updated_params = False

        def sets_param(param, line):
            """See if a config line sets this parameter to something."""
            # front is only whitespace maybe a comment
            front = r'^\s*#?\s*'
            # only whitespace between param and value
            middle = r'\s+'
            # end can include a comment
            end = r'\s*(?:#.*)?$'
            re_sets_param = front + param + middle + r'.*' + end
            return re.search(re_sets_param, line) is not None

        force_params = [
            ("ChallengeResponseAuthentication", "no"),
            ("PasswordAuthentication", "no"),
            ("UsePAM", "no"),
            ("PermitRootLogin", "no"),
        ]

        found_params = set()
        with sshd_config.open() as f:
            for line in f:
                found_a_param = False
                for param, value in force_params:
                    if sets_param(param, line):
                        # Only set the parameter once
                        if param not in found_params:
                            new_sshd_config += param + " " + value + "\n"
                            updated_params = True
                        found_a_param = True
                        found_params.add(param)
                if not found_a_param:
                    new_sshd_config += line
        # Check if any params not found
        for param, value in force_params:
            if param not in found_params:
                new_sshd_config += param + " " + value + "\n"
                updated_params = True
        if updated_params:
            # NOTE: This is actually necessary, see comment in method
            truncate_file(sshd_config)
            with sshd_config.open("w") as f:
                f.write(new_sshd_config)

    # ok osx
    def activate_ssh(self, public_key):
        """
        sets the public key path and copies the it to the SD card
        :param public_key: the public key location
        :return: True if successful
        """

        # set the keypath
        self.keypath = public_key
        if debug:
            print(self.keypath)
        if not os.path.isfile(self.keypath):
            ERROR("key does not exist", self.keypath)
            sys.exit()

        if dry_run:
            print("DRY RUN - skipping:")
            print("Activate ssh authorized_keys pkey:{}".format(public_key))
            return
        elif interactive:
            if not yesno("About to write ssh config. Please confirm:"):
                return

        # activate ssh by creating an empty ssh file in the boot drive
        pathlib.Path(self.filename("/ssh")).touch()
        # Write the content of the ssh rsa to the authorized_keys file
        key = pathlib.Path(public_key).read_text()
        ssh_dir = self.filename("/home/pi/.ssh")
        print(ssh_dir)
        if not os.path.isdir(ssh_dir):
            os.makedirs(ssh_dir)
        auth_keys = ssh_dir / "authorized_keys"
        auth_keys.write_text(key)

        # We need to fix the permissions on the .ssh folder but it is hard to
        # get this working from a host OS because the host OS must have a user
        # and group with the same pid and gid as the raspberry pi OS. On the PI
        # the pi uid and gid are both 1000.

        # All of the following do not work on OS X:
        # execute("chown 1000:1000 {ssh_dir}".format(ssh_dir=ssh_dir))
        # shutil.chown(ssh_dir, user=1000, group=1000)
        # shutil.chown(ssh_dir, user=1000, group=1000)
        # execute("sudo chown 1000:1000 {ssh_dir}".format(ssh_dir=ssh_dir))

        # Changing the modification attributes does work, but we can just handle
        # this the same way as the previous chown issue for consistency.
        # os.chmod(ssh_dir, 0o700)
        # os.chmod(auth_keys, 0o600)

        # /etc/rc.local runs at boot with root permissions - since the file
        # already exists modifying it shouldn't change ownership or permissions
        # so it should run correctly. One lingering question is: should we clean
        # this up later?

        new_lines = textwrap.dedent('''
                    # FIX298-START: Fix permissions for .ssh directory 
                    if [ -d "/home/pi/.ssh" ]; then
                        chown pi:pi /home/pi/.ssh
                        chmod 700 /home/pi/.ssh
                        if [ -f "/home/pi/.ssh/authorized_keys" ]; then
                            chown pi:pi /home/pi/.ssh/authorized_keys
                            chmod 600 /home/pi/.ssh/authorized_keys
                        fi
                    fi
                    # FIX298-END
                    ''')
        rc_local = self.filename("/etc/rc.local")
        new_rc_local = ""
        already_updated = False
        with rc_local.open() as f:
            for line in f:
                if "FIX298" in line:
                    already_updated = True
                    break
                if line == "exit 0\n":
                    new_rc_local += new_lines
                    new_rc_local += line
                else:
                    new_rc_local += line
        if not already_updated:
            with rc_local.open("w") as f:
                f.write(new_rc_local)
        self.disable_password_ssh()

    # ok osx
    def info(self):
        if os_is_linux() or os_is_mac():
            information = {
                "os": platform.system(),
                "ssh": os.path.exists(self.filename("/ssh")),
                # "key": cat(self.filename("/home/pi/.ssh/authorized_keys")),
                "hostname": cat(self.filename("/etc/hostname")).strip()
            }

            # print(yaml.dump(information, default_flow_style=False))
            pprint(information)

    # ok osx
    def write_hostname(self, host):
        """
        set the hostname

        :param host: the hostname
        :return:
        """
        self.host = host
        path = self.filename("/etc/hostname")
        if debug:
            print(self.host)
        if dry_run:
            print("DRY RUN - skipping:")
            print("Writing host name {} to {}".format(host, path))
            return
        elif interactive:
            if not yesno("About write hostname. Please confirm:"):
                return
        pathlib.Path(path).write_text(host)

        # /etc/hosts needs to be updated also with the hostname
        hosts = self.filename("/etc/hostname")
        with hosts.open() as fr:
            contents = fr.read()
        new_hosts = contents.replace("raspberrypi", host)
        # NOTE: This is actually necessary, see comment in method
        truncate_file(hosts)
        # print(new_hosts)
        with hosts.open("w") as fw:
            fw.write(new_hosts)

    def filename(self, path):
        """
        creates the proper path for the file by using the proper file systyem
        prefix. This method is supposed to universally work, so that we simply
        can use the filesystem name without worrying about the location it it is
        in the boot or root file system of the SD Card.

        :param path:
        :return:
        """
        # print(path)
        if os_is_mac() or os_is_linux():
            if path in ["/etc/hostname",
                        "/etc/hosts",
                        "/etc/rc.local",
                        "/etc/ssh/sshd_config",
                        "/home/pi/.ssh/authorized_keys",
                        "/home/pi/.ssh",
                        "/etc/wpa_supplicant/wpa_supplicant.conf",
                        "/etc/dhcpcd.conf"]:
                volume = self.root_drive
            elif path in ["/ssh"]:
                volume = self.boot_drive
            else:
                ERROR("path not defined in cm-burn", path)
            location = pathlib.Path(
                "{volume}/{path}".format(volume=volume, path=path))
        elif os_is_windows():
            if path in ["/etc/hostname",
                        "/etc/rc.local",
                        "/etc/ssh/sshd_config",
                        "/home/pi/.ssh/authorized_keys",
                        "/home/pi/.ssh",
                        "/etc/wpa_supplicant/wpa_supplicant.conf",
                        "/etc/dhcpcd.conf"]:
                volume = self.root_drive
            elif path in ["/ssh"]:
                volume = self.boot_drive
            else:
                ERROR("path not defined in cm-burn", path)
            print("{volume}:{path}".format(volume=volume, path=path))
            location = pathlib.Path(
                "{volume}:{path}".format(volume=volume, path=path))
        return location

    # ok osx
    def read_hostname(self):
        """
        set the hostname

        :return:
        """
        host = cat(self.filename("/etc/hostname"))
        return host

    def image_exists(self, name):
        path = pathlib.Path(self.home / ".cloudmesh" / "images" / name)
        return os.path.isfile(path)

    def check_device(self, device):
        deviceok = False
        if os_is_linux():
            out = getoutput("lsblk | grep {device}".format(device=device))
            if (self.boot_drive in out) and (self.root_drive in out):
                deviceok = True
        elif os_is_mac():
            devs = getoutput("diskutil list").split("/dev/")
            usbdev = None
            for dev in devs:
                if "boot" in dev and "rootfs" in dev and "Windows_FAT_32" in dev:
                    usbdev = dev.split("\n")[0].split(" ")[0]
            if usbdev == device:
                deviceok = True
        elif os_is_windows():
            deviceok = True
        return deviceok

    def __init__(self):
        """
        initialize the pi burner
        TODO: provide more information
        """
        # store defaults also in ~/.cloudmesh/cm-burn.yaml as we have to
        # execute it a lot, we can than read
        # defaults from there if the file exist
        # if os_is_windows():
        #    self.windows_drive = "K"
        #    self.windows_pi_drive = "L"
        self.root_drive = None
        self.boot_drive = None
        if os_is_linux():
            self.boot_drive = "/media/{user}/boot".format(
                user=getpass.getuser())
            self.root_drive = "/media/{user}/rootfs".format(
                user=getpass.getuser())
        elif os_is_mac():
            self.boot_drive = "/Volumes/boot"
            self.root_drive = "/Volumes/rootfs"
        self.image = None
        self.host = None
        self.ip = None
        self.domain = "192.168.0.1"
        self.home = pathlib.Path(path.expanduser("~"))
        self.keypath = pathlib.Path(self.home / ".ssh" / "id_rsa.pub")
        # BUG: is this not the image directory?
        # should that not also be declared globally with pathlib
        self.cloudmesh_images = pathlib.Path(
            self.home / ".cloudmesh" / "images")
        if debug:
            print("HOME:", self.home)
            print("KEY:", self.keypath)
            print("IMAGES DIR", self.cloudmesh_images)
        pass

    def get(self, image=None):
        """
        downloads the image and stores it in ~/.cloudmesh/images
        TODO: finalize the directory, create it if image already
        exists  doe not  not download
        :param image: The image url
        :return:
        """
        latest = "https://downloads.raspberrypi.org/raspbian_latest"
        if image is None:
            image = latest

        if debug:
            print("Image:", image)
            print("Images dir:", self.cloudmesh_images)
        if not os.path.exists(self.cloudmesh_images):
            # TODO: check if this works if path is ~/.cloudmesh/images
            os.makedirs(self.cloudmesh_images)
        if debug:
            print(image)
        os.chdir(self.cloudmesh_images)
        # find redirectionlink
        source = requests.head(image, allow_redirects=True).url
        size = requests.get(image, stream=True).headers['Content-length']
        destination = os.path.basename(source)
        if debug:
            print(image)
            print(destination)
        download = True
        if os.path.exists(destination):
            if int(os.path.getsize(destination)) == int(size):
                WARNING("file already downloaded. Found at:",
                        pathlib.Path(self.cloudmesh_images / destination))
                download = False
        if download:
            wget.download(image)

        # uncompressing

        image_name = destination.replace(".zip", "") + ".img"
        image_file = pathlib.Path(self.cloudmesh_images / image_name)
        if not os.path.exists(image_file):
            self.unzip_image(image_name)
        else:
            WARNING("file already downloaded. Found at:",
                    pathlib.Path(self.cloudmesh_images / image_name))
        self.image = pathlib.Path(self.cloudmesh_images / image_name)
        return self.image

    def unzip_image(self, source):
        tmp = pathlib.Path(self.cloudmesh_images) / "."
        os.chdir(tmp)
        image_zip = str(pathlib.Path(self.cloudmesh_images / source)).replace(
            ".img", ".zip")
        print("unzip image", image_zip)
        zipfile.ZipFile(image_zip).extractall()

    def ls(self):
        """
        List all images in the image directory
        :return:
        """
        images_search = pathlib.Path(self.cloudmesh_images / "*")
        if debug:
            print("images search", images_search)
        images = glob.glob(str(images_search))
        print()
        print('Available images')
        print(columns * '=')
        print('\n'.join(images))
        print()

    def set_ip(self, ip):
        """
        TODO: How to set the static IP for both wifi and wired
        :param ip: the ip
        :return:
        """

        self.ip = ip

    def set_root_drive(self, drive):
        """
        TODO: provide explanation
        :param drive: the drive name for windows
        :return:
        """
        # BUG: not sure what this drive is so replace abc with something
        # meaningful
        self.root_drive = drive

    def set_boot_drive(self, drive):
        """
        TODO: provide information
        :param drive: the drive name for windows
        :return:
        """
        # BUG: not sure what this drive is so replace efg with something
        # meaningful
        self.boot_drive = drive

    def configure_wifi(self, ssid, psk):
        """
        sets the wifi. ONly works for psk based wifi
        :param ssid: the ssid
        :param psk: the psk
        :return:
        """

        wifi = textwrap.dedent("""\
                ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev 
                update_config=1 
                country=US
                
                network={{
                        ssid=\"{network}\"
                        psk=\"{pwd}\"
                        key_mgmt=WPA-PSK
                }}""".format(network=ssid, pwd=psk))
        print(wifi)
        path = "/etc/wpa_supplicant/wpa_supplicant.conf"
        if dry_run:
            print("DRY RUN - skipping:")
            print("Writing wifi ssid:{} psk:{} to {}".format(ssid,
                                                             psk, path))
            return
        elif interactive:
            if not yesno("About write wifi info. Please confirm:"):
                return
        pathlib.Path(self.filename(path)).write_text(wifi)

    '''
    def gregor(self, names, key, ssid=None, psk=None):
        global columns
        for name in hostlist.expand_hostlist(names):
            print(columns * "-")
            print(name)
            print(columns * "-")

            # self.create_burn_image(name)
            self.mount_burn_image(name + ".img")
    '''

    def configure_static_ip(self):

        # set staticip
        data = {
            "domain": self.domain,
            "ip": self.ip,
        }
        # TODO: why are eth0 and wlan0 differnt? should they not be the same as eth0?
        # OLD:
        #    interface wlan0
        #    static ip_address={ip}/24
        #    static routers=10.0.0.1
        #    static domain_name_servers=10.0.0.1
        dhcp_conf = textwrap.dedent("""
            interface eth0
            
            static ip_address={ip}/24
            static routers={domain}
            static domain_name_servers={domain}

            interface wlan0

            static ip_address={ip}/24
            static routers={domain}
            static domain_name_servers={domain}
        """.format(**data))

        if debug:
            print(dhcp_conf)
        if dry_run:
            print("DRY RUN - skipping statis ip config")
            return
        elif interactive:
            if not yesno("About write static ip config. Please confirm:"):
                return
        #
        # TODO: this seems not coorect, shoudl be in etc/network/interfaces?
        path = pathlib.Path(self.filename("/etc/dhcpcd.conf"))

        with open(path, 'a', encoding='utf-8', newline="\n") as file:
            file.write(dhcp_conf)

        # why is this needed?
        # if os_is_windows():
        #    fileContents = open(path,"r").read()
        #    with open(path,"w", newline="\n") as file:
        #        file.write(fileContents)

    def prepare_burn_on_pi_command(self, image, device):
        """
        assumes you called get before and have valid image
        :return:
        """
        if device is None:
            # activate an image and create a yaml file cmburn.yaml with parameter
            # that is read upon start in __init___
            output = run(["sudo", "ls", "-ltr", "/dev/*"])
            # TODO BUG this is not how run works
            # TODO: find mmcblk0
            device = "mmcblk0"  # hard coded for now
            print(output)
        data = {
            image: self.image,
            device: device
        }

        command = "sudo dd bs=1M if=~{image} of={device} status=progress conv=fsync".format(
            **data).split(" ")
        print(command)
        return command

    def burn(self, image, device=None):
        """
        burn the image onto the SD card
        :return: True if succesfull and test passed, false otherwise
        """
        # burn image on python device
        # if not os.path.exists(IMAGE_DIR):
        # os.makedirs(IMAGE_DIR)
        # BUG: if condition is not implemented

        # output = wmic.query("select DeviceID, Model from Win32_DiskDrive where
        # InterfaceType='USB'")
        # print(output)

        command = ""
        if os_is_windows():
            # BUG: does not use pathlib
            # BUG: command not in path, should be in ~/.cloudmesh/bin so it can easier be found,
            # BUG: should it not be installed from original
            command = "{dir}\\CommandLineDiskImager\\CommandLineDiskImager.exe {image} {drive}".format(
                dir=os.getcwd(), drive=self.boot_drive, image=image)
            # also dir needs to be done in pathlib
            # diskimager = pathlib.Path(r'/CommandLineDiskImager/CommandLineDiskImager.exe')
            # script = """{dir}\\{diskimager} {dir}\\2018-04-18-raspbian-stretch.img {drive}
            # """.format(dir=os.getcwd(), drive=self.windows_drive, diskimiger=dikimiger)
        elif os_is_pi():

            command = self.prepare_burn_on_pi_command(image, device)
            ERROR("not yet implemented")
            sys.exit()
        elif os_is_linux():
            self.unmount(device)
            command = "sudo dd if={image} of=/dev/{device} bs=4M status=progress".format(
                image=image, device=device)
        elif os_is_mac():
            self.unmount(device)
            command = "sudo dd if={image} of=/dev/{device} bs=4m".format(
                image=image, device=device)

        print(command)
        if command:
            execute_with_progress(command)
            # execute(command)
        # TODO: execute test
        # if test successful: return True else: False

    def detect_device(self):
        """
        Detect the device to burn the image to.
        """
        # TODO Implement this
        # Windows doesn't need a device (but it needs drives...)
        # Mac the device can be parsed from diskutil list
        # Linux not sure
        # If we need a device and don't know, ask the user
        if os_is_mac() or os_is_linux() or os_is_pi():
            device = prompt("Please enter the device name to install to:")
        else:
            device = self.boot_drive
        return device

    # TODO: remove bootdrives from parameters as they should be selfdicoverable
    def create(self, image, names, key, ips,
               ssid=None, psk=None,
               domain=None,
               bootdrive=None, rootdrive=None):
        """
        creates a repeated burn on all names specified,
        TODO: why is this not part of the previous class?

        :param ips: TODO
        :param domain: TODO
        :param image: TODO
        :param names: the hostnames of in hostlist format to be burned
        :param key: the public key location # TODO: should be defaulted
                    to ~/.ssh/id_rsa.pub
        :param bootdrive: the boot drive # BUG: on linux we do not have a
                          boot drive, so this should not be a parameter and
                          needs to be autodiscovered
        :param rootdrive: # BUG: on linux we do not have a boot drive, so this
               should not be a parameter and needs to be autodiscovered
        :param ssid: # TODO: should be set to None and if its None we do not do it
                     # we actually do not need wifi, should be handled differently
        :param psk: # TODO: should be set to None and if its None we do not do
                    # it we actually do not need wifi, should be handled differently
        :return:
        """

        """
        TODO The following commented code is specific to retrive the 
        USB drive name - boot drive
        DRIVE_TYPES = {
        0 : "Unknown",
        1 : "No Root Directory",
        2 : "Removable Disk",
        3 : "Local Disk",
        4 : "Network Drive",
        5 : "Compact Disc",
        6 : "RAM Disk"
        }

        c = wmi.WMI ()
        for drive in c.Win32_LogicalDisk ():
            print(drive.Caption, DRIVE_TYPES[drive.DriveType])
        
        """
        hosts = hostlist.expand_hostlist(names)
        iplist = hostlist.expand_hostlist(ips)
        # BUG: can we not discover the boot and rootdrive. Why do we have to set
        # it to I and G, can we not get the next free drive letter?
        # THis only seems to be needed for Windows?
        # bootdrive = find_next_free_drive_letter()
        # rootdrive = find_next_free_drive_letter()
        # BUG: are the drives released after use?         
        print(bootdrive)
        print(rootdrive)
        if bootdrive:
            self.set_boot_drive(bootdrive)
        if rootdrive:
            self.set_root_drive(rootdrive)
        device = self.detect_device()
        if domain is not None:
            self.domain = domain
        for host, ip in zip(hosts, iplist):
            print("Start Time - {currenttime}".format(
                currenttime=datetime.datetime.now()))
            print(columns * '-')
            print("Burning", host)
            # break
            print(columns * '-')
            if not yesno('Please insert the card for ' + host +
                         " and wait until it is recognized by the system." +
                         "\nReady to continue?"):
                break

            print("Beginning to burn image {image} to {device}".format(
                image=image, device=device))
            self.burn(image, device)
            # Sleep for 5 seconds to have the SD to be mounted
            # TODO: OS X can eject ourselves:
            # diskutil eject /dev/{device}
            if not yesno('Please eject the SD card and re-insert.'
                         '\nReady to continue?'):
                break
            time.sleep(5)
            self.set_ip(ip)
            print("Set IP - {ip}".format(ip=ip))
            self.write_hostname(host)
            print("Updating host - {name}".format(name=host))

            print("ssid - {id}".format(id=ssid))
            print("psk - {pwd}".format(pwd=psk))
            if ssid:
                self.configure_wifi(ssid, psk)
                print("Updating wifi")

            self.activate_ssh(key)
            print("Updating ssh")

            self.configure_static_ip()
            print("Updating Network - Static IP")

            self.unmount(device)
            print("Removed drive")

            print("Please remove the card for host", host)
            if not yesno("Ready to continue?"):
                break

            print("take the card out")
            print("End Time - {currenttime}".format(
                currenttime=datetime.datetime.now()))


def analyse(arguments):
    print(arguments)
    # Set global dry-run to disable executing (potentially dangerous) commands
    if arguments["--interactive"]:
        global interactive
        interactive = True

    if arguments["--dry-run"]:
        global dry_run
        dry_run = True
        print("DRY RUN - nothing will be executed.")

    if arguments["ls"]:
        burner = PiBurner()
        burner.ls()
    elif arguments["get"]:
        burner = PiBurner()
        burner.get()
    elif arguments["create"]:
        burner = PiBurner()
        wifipass = None
        bootdrv = None
        rootdrv = None
        if "--bootdrive" in arguments:
            bootdrv = arguments["--bootdrive"]
        if "--rootdrive" in arguments:
            rootdrv = arguments["--rootdrive"]
        image = arguments["--image"]
        if not burner.image_exists(image):
            ERROR("The image {image} does not exist".format(image=image))
            sys.exit()
        else:
            burner.image = pathlib.Path(
                burner.home / ".cloudmesh" / "images" / image)
        burner.create(burner.image,
                      names=arguments["--names"],
                      key=arguments["--key"],
                      ips=arguments["--ips"],
                      domain=arguments["--domain"],
                      ssid=arguments["--ssid"],
                      psk=arguments["--psk"],
                      bootdrive=bootdrv,
                      rootdrive=rootdrv)

    elif arguments["check"] and arguments["install"]:
        ERROR("not yet implemented")

    elif arguments["hostname"]:
        host = arguments["HOSTNAME"]
        burner = PiBurner()

        if host is not None:
            print("Set host to:", host)
            burner.write_hostname(host)
        else:
            print(burner.read_hostname())

    elif arguments["wifi"]:
        ssid = arguments["SSID"]
        passwd = arguments["PASSWD"]
        if passwd is None:
            passwd = getpass.getpass()
        print(ssid)
        print(passwd)
        burner = PiBurner()
        burner.configure_wifi(ssid, passwd)

    elif arguments["image"]:
        image = arguments["--image"]
        device = arguments["--device"]
        burner = PiBurner()
        # check if image exists
        if not burner.image_exists(image):
            ERROR("The image {image} does not exist".format(image=image))
            sys.exit(1)
        else:
            burner.image = pathlib.Path(
                burner.home / ".cloudmesh" / "images" / image)

        # TODO: check if device exists
        if not burner.check_device(device):
            ERROR("The device {device} does not exist or not available".format(
                device=device))
            sys.exit()
        burner.burn(burner.image, device)

    elif arguments["ip"]:
        burner = PiBurner()

        ip = arguments["IPADDRESS"]
        print("Use ip:", ip)
        burner.set_ip(ip)

        domain = arguments["--domain"]
        if domain is not None:
            print("Use domain:", domain)
        burner.domain = domain

        burner.configure_static_ip()

    elif arguments["ssh"]:
        key = arguments["PUBLICKEY"]
        if key is None:
            key = os.path.expanduser("~") + "/.ssh/id_rsa.pub"
        print("Use ssh key:", key)
        burner = PiBurner()
        burner.activate_ssh(key)

    elif arguments["info"]:
        burner = PiBurner()
        burner.info()


def main():
    """main entrypoint for setup.py"""
    arguments = docopt(__doc__, version=VERSION)
    # if debug:
    #   print(arguments) # just for debugging
    analyse(arguments)


if __name__ == '__main__':
    main()
