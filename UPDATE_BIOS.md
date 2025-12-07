# Updating the BIOS without a Windows installation

You can create a WINPE USB key with the BIOS update file.

> WARNING : Updating the BIOS **can** brick your laptop if something goes wrong. Make sure to follow the steps carefully and avoid interrupting the process. Charge your laptop battery to at least 50% before starting the update.

## 1. Creating a WINPE USB key using Ventoy

If you don't have any Windows device, the simplest method is to use Ventoy to create a bootable USB key with WINPE.

1. Go to the [Ventoy website](https://www.ventoy.net/en/index.html) and download the latest version.
2. Flash the Ventoy image on the USB key or use the Ventoy tool to create a bootable USB key.
3. Copy a WINPE ISO on the Ventoy USB key (you can get one [here](https://www.osdcloud.com/sandbox/winpe-downloads))

## 2. Preparing the BIOS update file

1. Go to the [Lenovo website](https://pcsupport.lenovo.com/fr/fr/products/laptops-and-netbooks/yoga-series/yoga-slim-7-14apu8/downloads/driver-list/component?name=BIOS&id=5AC6A815-321D-440E-8833-B07A93E0428C) and download the latest BIOS update.
2. Move the BIOS update to a USB key. You can use the Ventoy USB key if you want.

Checking the checksum of the BIOS update is a good practice to avoid bricking your laptop.

## 3. Booting WINPE & updating the BIOS

1. Reboot the laptop and press `F12` to enter the boot menu
2. Select the USB key. If you don't see it, you may need to disable Secure Boot in the BIOS settings.
3. When a terminal is open, run `notepad`
4. Select `file > open file`
5. Select file type `all files`
6. Navigate to the BIOS update tool
7. Select the BIOS update tool, then right click on it and select `run`
8. Follow the instructions. Never turn off the laptop during the update process, even if you get a black screen. Wait until the laptop reboots itself.
