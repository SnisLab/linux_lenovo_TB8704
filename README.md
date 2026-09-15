# Lenovo TB-8704 Mainline Linux

Mainline Linux bring-up repository for the Lenovo Tab 4 8 Plus TB-8704 family, with the TB-8704F as the primary target.

## Goals

1. Bring up the TB-8704F on a modern Linux kernel, targeting the Linux 6.12 LTS family for the long-lived baseline.
2. Reuse upstream MSM8953 support wherever possible instead of carrying device-specific hacks.
3. Enable hardware incrementally: boot/logging, storage, USB, display, touch, GPU, Wi-Fi, Bluetooth, audio, battery/charging, suspend and other peripherals.
4. Use postmarketOS or another minimal Linux userspace during hardware enablement.
5. Keep the resulting hardware description useful for later Android-on-modern-kernel experiments.

## Bring-up policy

- Start from verified upstream/MSM8953-mainline work.
- Port TB-8704F hardware through a dedicated device tree.
- Do not claim a subsystem works until it has been tested on-device.
- Keep one functional area per commit where practical.
- Record boot logs and regressions alongside changes.

## Status

Initial project setup. No mainline kernel sources or device-tree patches have been imported yet.

## Related repositories

- `SnisLab/android_recovery_lenovo_TB8704`
- `SnisLab/android_kernel_lenovo_msm8953`
- `SnisLab/android_device_lenovo_TB8704`
