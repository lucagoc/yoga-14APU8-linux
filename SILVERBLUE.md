# Configuration for Fedora Silverblue

*Or any Fedora immutable based distro (kenoite, universal blue...)*

![alt text](.github/sysinfo_silverblue.png)

Silverblue is an immutable variant of Fedora Workstation. This guide will help you set up your Lenovo Yoga Slim 7 14APU8 on Silverblue.

Because of Silverblue's immutability, everything will be done using `rpm-ostree` to install packages and overlays to modify system files.

## Fixing Suspend

> ⚠️ **WARNING REALLY EXPERIMENTAL** : Please backup your data before proceeding, i'm still developing this and issues may occur, especially with booting the ACPI override.

```bash
rpm-ostree install RPMs/acpi-yoga-fix-1.0-2.fc43.noarch.rpm
```

Reboot your system to apply, then run :

```bash
sudo bash -x /usr/lib/kernel/install.d/99-acpi-override.install add $(uname -r) /boot /x /y
```

Reboot again, and check if the ACPI tables have been applied correctly with :

```bash
sudo dmesg | grep ACPI | grep "Table Upgrade"
```

You should see something like :

```bash
[    0.003464] ACPI: Table Upgrade: override [SSDT-LENOVO-    UPEP]
```

<!-- Reboot your system to apply, then run :

```bash
acpi-yoga-fix
```

Reboot again to apply changes.

> Todo : Fix the acpi-yoga-fix package to remove fix when uninstalling + find a way to automate the `acpi-yoga-fix` command on boot. -->

## Fixing Sound

You need to install a custom firmware for the sound card to get the subwoofer working properly.

```bash
rpm-ostree install RPMs/cfw_ti2781-1.0-1.x86_64.rpm
```

Reboot your system to apply changes.
