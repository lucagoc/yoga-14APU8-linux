# Lenovo Yoga Slim 7 (14APU8) & Linux

Discussions & Tricks to improve Linux compatibility to the Lenovo Yoga Slim 7 (14APU8)

![sysinfo](./.github/sysinfo.png)

## Compatibility

| Component | Description | Status |
| --- | --- | --- |
| CPU | AMD Ryzen 7 7840S | ✅ Working OoB |
| GPU | AMD Radeon 780M | ⚠️ See [GPU](#gpu) |
| Memory | 16-32GB LPPDR5X | ✅ Working OoB |
| Storage | 512GB-1TB NVMe SSD | ✅ Working OoB |
| Display | 14" 2944x1840@90 OLED | ✅ Working OoB |
| WiFi | RTL8852CE | ✅ Working OoB |
| Bluetooth | RTL8852CU | ✅ Working OoB |
| Sound (Subwoofer) | TI 2781  | ✅ Working with **[custom firmware](#sound)** |
| Touchpad | Unknown | ✅ Working OoB |
| Camera | 720p | ✅ Working OoB |
| Suspend | - | ✅ Working with injected SSDT |
| Hibernate | - | ❌ Broken |
| Secure Boot | - | ⚠️ See [Secure Boot](#secure-boot) |
| IR Camera auth | 720p | ⚠️ See [Howdy](https://github.com/boltgolt/howdy)

Overall, using this laptop with Linux is really good experience but there is some tweaks to do to get it working properly after installation.

## Things to know

- Everything has been tested on an Arch Linux installation, the 28/10/2024, with BIOS `M6CN38WW` (15/12/2023).
- Most of the issues are related to poorly written BIOS by Lenovo. Lenovo seems to have dropped support for this device as the latest [BIOS version is dated 15/12/2023](https://pcsupport.lenovo.com/fr/fr/products/laptops-and-netbooks/yoga-series/yoga-slim-7-14apu8/downloads/driver-list/component?name=BIOS&id=5AC6A815-321D-440E-8833-B07A93E0428C).
- Feel free to open issues with your own Linux experience with this laptop.
- I'm not the maintener of the custom firmware / injected SSDT, if you have any problems related with them, open issues on their related repos.

## Suspend

Suspend will not work on fresh installation (the laptop instantly wakes up when closing the lid). See [this issue on GitLab](https://gitlab.freedesktop.org/drm/amd/-/issues/2812).
You will need to inject a custom injected SSDT to make it work and depending on your distro, it can be tricky.

If your using Arch Linux, you can use the **[mkinitcpio's acpi_override hook](https://wiki.archlinux.org/title/DSDT#Using_mkinitcpio's_acpi_override_hook)**.

```bash
sudo mkdir /etc/initcpio/acpi_override
sudo cp ssdt6.aml /etc/initcpio/acpi_override/
```

then edit `/etc/mkinitcpio.conf` and add `acpi_override` to the `HOOKS` array.

```conf
HOOKS=(... acpi_override)
```

then rebuild the initramfs with `sudo mkinitcpio -P`.
Reboot.

### Freeze on wake up

This issue is related to the GPU, see [GPU](#gpu) for more informations.

### Hibernation

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

## Secure Boot

Because your using a custom injected SSDT, you will need to disable Secure Boot in your BIOS settings, otherwise the SSDT will not be loaded.

You can also sign the SSDT with your own keys to make it work with Secure Boot, but this is a more advanced topic and I will not cover it here.

## Sound

Sound needs a custom firmware to work properly.
See [this repo](https://github.com/darinpp/yoga-slim-7).

You can use `alsamixer` to adjust the sound levels of the subwoofers and the main speakers (DAC 1 & 2).
![alsamixer](./.github/alsamixer.png)

Sound will not be as good as on Windows (the 4 subwoofers are not calibrated precisely and Dolby Atmos spacial effect is missing.)

However, you can mitigate this with [Easy Effects](https://github.com/wwmm/easyeffects).
There is a preset that I made to improve the sound in the `easyeffect` folder (I'm not an expert so if you want to make a better one, do not forget to share it :) )

## Power profiles

On an Arch system do not forget to install `power-profiles-daemon` to get control over power profiles.

## GPU

The Radeon 780M is not well supported on Linux, and there is some issues related to power profiles.
On a fresh installation, the GPU will have some artifacts on the screen when using 90 Hz mode, and can even crash when the system tries to wake up from suspend.

This can be bypassed by [setting the performance level to `high`](https://wiki.archlinux.org/title/AMDGPU#Screen_artifacts_and_frequency_problem) but this come with a cost in battery life.
However, you can use the `power-profiles-daemon` to switch between profiles easily.
I recommend you to set up a rule to switch the laptop on a `balanced` profile when the laptop wakes up from suspend. You will still have some artifacts on the screen when switching profiles, but at least the system will not crash on wake up.

