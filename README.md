# Lenovo Yoga Slim 7 (14APU8) & Linux
Discussions & Tricks to improve Linux compatibility to the Lenovo Yoga Slim 7 (14APU8)

# Things to know
- All commands have been tested on an updated ArchLinux system as of 28/10/2024
- Most of the issues are related to poorly written BIOS by Lenovo. Lenovo seems to have dropped support for this device as the latest BIOS version is from 15/12/2023.
- Feel free to open issues with your own Linux experience with this laptop.
- I'm not the maintener of the custom firmware / ACPI table files, if you have any problems related with them, open issues on their related repos. 

# Sleep
Sleep will not work on fresh installation. You will need to inject a custom ACPI table to make it work and depending on your distro, it can be tricky to inject.

# Secure Boot

## Hibernation
Hibernation is still quite buggy on this system, see [this issue on GitLab](https://gitlab.freedesktop.org/drm/amd/-/issues/3047).
You should disable it to prevent system crashes:
```bash
sudo nano /etc/systemd/sleep.conf
```
and edit it like this :
```conf
[Sleep]
AllowSuspend=yes
AllowHibernation=no
AllowSuspendThenHibernate=no
AllowHybridSleep=no
```

# Sound
See [this repo](https://github.com/darinpp/yoga-slim-7).

# GPU
The GPU seems to have rare buffer issues related to power profiles.

# Power profiles
On an Arch system do not forget to install `power-profiles-daemon` to get control on power profiles.
