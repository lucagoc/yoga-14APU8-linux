# Suspend

Suspend will not work on fresh installation (the laptop instantly wakes up when closing the lid). See [this issue on GitLab](https://gitlab.freedesktop.org/drm/amd/-/issues/2812) for more details.
You will need to inject a custom injected SSDT to make it work and depending on your distro, it can be more or less tricky.

See the specific configuration guides for your distribution.

## Freeze on wake up

If your system crash when waking up from suspend sometimes, BIOS `M6CN42WW` and later fix this issue.
To update the BIOS without Windows, see **[Updating the BIOS](./UPDATE_BIOS.md)**.
