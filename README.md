# Lenovo Yoga Slim 7 (14APU8) & Linux
Discussions & Tricks to improve Linux compatibility to the Lenovo Yoga Slim 7 (14APU8)

# Things to know
- All commands have been tested on an updated ArchLinux system as of 28/10/2024
- Most of the issues are related to poorly written BIOS by Lenovo. Lenovo seems to have dropped support for this device as the latest BIOS version is from 15/12/2023.
- Feel free to open issues with your own Linux experience with this laptop.
- I'm not the maintener of the custom firmware / ACPI table files, if you have any problems related with them, open issues on their related repos. 

# Suspend
Suspend will not work on fresh installation. See [this issue on GitLab](https://gitlab.freedesktop.org/drm/amd/-/issues/2812).
You will need to inject a custom ACPI table to make it work and depending on your distro, it can be tricky to inject.

## Freeze on wake up
This issue is related to the GPU, see **GPU** below.

## Hibernation
Hibernation is still quite buggy on this system, see [this issue on GitLab](https://gitlab.freedesktop.org/drm/amd/-/issues/3047).
You should at least disable `suspend-then-hibernate` to prevent unexpected crashes, and disable hibernation completely if your not using this feature:
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

# Secure Boot

# Sound
See [this repo](https://github.com/darinpp/yoga-slim-7).
Sound is not as good as on Windows, the 4 subwoofers are not calibrated precisely and Dolby Atmos spacialization effect is missing.
This can be partially mitigated with [Easyeffects](https://github.com/wwmm/easyeffects).

# Power profiles
On an Arch system do not forget to install `power-profiles-daemon` to get control on power profiles.

# GPU
Depending on your power profile the GPU will crash and freeze your entire system when trying to wake up from suspend. It seems that if system is using "Performance Mode" ("Maximum Performance" in BIOS), the issue will not occured.

Also, the GPU seems to have rare buffer issues related to power profiles (same here, using "Performance Mode" seems to have less artifacts than other modes).
