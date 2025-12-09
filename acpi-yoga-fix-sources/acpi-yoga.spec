Name:           acpi-yoga-fix
Version:        2.0
Release:        1%{?dist}
Summary:        ACPI SSDT Override for Lenovo Yoga
License:        Proprietary
BuildArch:      noarch

# Sources (Must be in the same folder during build)
Source0:        ssdt-yoga-14apu8.aml
Source1:        acpi-yoga-fix
Source2:        acpi-yoga.service
Source3:        90-acpi-yoga.preset

BuildRequires:  cpio, systemd-rpm-macros

%description
Provides ACPI fix. Patches boot entries automatically on reboot/shutdown.
Includes clean uninstall logic.

%install
# 1. Create uncompressed CPIO image
mkdir -p temp_work/kernel/firmware/acpi
cp %{SOURCE0} temp_work/kernel/firmware/acpi/
cd temp_work
find kernel | cpio -H newc --create > ../acpi_override.img
cd ..

# 2. File installation
# Image in /usr/lib/acpi
mkdir -p %{buildroot}/usr/lib/acpi
install -m 0644 acpi_override.img %{buildroot}/usr/lib/acpi/acpi_override.img

# Script in /usr/bin for user access
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/acpi-yoga-fix

# Systemd Service
mkdir -p %{buildroot}/etc/systemd/system
install -m 0644 %{SOURCE2} %{buildroot}/etc/systemd/system/acpi-yoga.service

# Systemd preset to allow enablement on rpm-ostree
mkdir -p %{buildroot}/usr/lib/systemd/system-preset
install -m 0644 %{SOURCE3} %{buildroot}/usr/lib/systemd/system-preset/90-acpi-yoga.preset

%files
/usr/lib/acpi/acpi_override.img
/usr/bin/acpi-yoga-fix
/etc/systemd/system/acpi-yoga.service
/usr/lib/systemd/system-preset/90-acpi-yoga.preset

%post
# Service is enabled via preset, no manual enabling needed on rpm-ostree

%preun
# Service cleanup handled by systemd, no manual disable needed

%changelog
* Tue Dec 09 2025 lucagoc - 2.0
- Clean version with shutdown hook and cleanup
- Added acpi-yoga-fix script for user convenience