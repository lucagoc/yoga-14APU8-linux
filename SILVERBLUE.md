# Configuration for Fedora Silverblue

*Or any Fedora immutable based distro (kenoite, universal blue...)*

![alt text](.github/sysinfo_silverblue.png)

Silverblue is an immutable variant of Fedora Workstation. This guide will help you set up your Lenovo Yoga Slim 7 14APU8 on Silverblue.

Because of Silverblue's immutability, everything will be done using `rpm-ostree` to install packages and overlays to modify system files.

## Fixing Suspend

Install the ACPI override package to get suspend working properly:

```bash
rpm-ostree install RPMs/acpi-yoga-fix-2.0-1.noarch.rpm
```

Reboot your system to apply, then reboot again, and check if the ACPI tables have been applied correctly with :

```bash
sudo dmesg | grep ACPI | grep "Table Upgrade"
```

You should see something like :

```bash
[    0.003464] ACPI: Table Upgrade: override [SSDT-LENOVO-    UPEP]
```

The script come with a tiny CLI to manage the ACPI override, you can check the available options with :

```bash
acpi-yoga-fix help
```

By default, the service `acpi-yoga` will check if the ACPI override is applied at each shutdown/reboot, and will re-apply it if not. You can disable this behavior with :
```bash
sudo systemctl disable acpi-yoga.service
```

## Fixing Sound

You need to install a custom firmware for the sound card to get the subwoofer working properly.

```bash
rpm-ostree install RPMs/cfw_ti2781-1.0-1.x86_64.rpm
```

Reboot your system to apply changes.
