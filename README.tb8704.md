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

## Kernel and Android roadmap

The kernel-generation plan, upgrade gates, LTS selection criteria and separate
Android 16 assessments are maintained in `state/kernel-android-roadmap.md`.
Linux 6.12 remains the current diagnostic baseline; later generations are
independent experiments, not claims of device support. AOSP Android 16 is the
primary Android target, with PixelOS assessed only as a subsequent variant.

## Status and provenance (2026-10-15 review)

The local `KERN-1` checkout is Linux 6.12-based and includes a **partial**
TB-8704F identity/bring-up scaffold, not a complete board port. The historical KERN-1 starting commit
was `9ce1a2452913170159c00d439d02dced337610c6` (`docs: record ARM64
compressed-image handoff limit`, 2026-09-28). The earlier project baseline is
`62969f1eb5e42e596760924c0845bfdb384851d9` (2026-09-18); later history adds
the partial DTS (`0c145e2a5fd96ca087b143f903e87c2627d4a6b5`) and diagnostic
initramfs/handoff documentation (`f7887d5db164ec80703bec6a37f6428428470abe`,
`9ce1a2452913170159c00d439d02dced337610c6`).

Commit `9ce1a245` records that ARM64 Linux requires the loader to decompress
`Image.gz`; generic Kbuild's gzip output is not a self-decompressing zImage
and there is no generic `Image.gz-dtb` target. It therefore does **not** solve
the earlier static kernel-address conflict or prove loader placement, DTB in
x0, or appended-DTB compatibility. Historical gzip-plus-DTB bytes show a
packaging convention only. See `docs/tb8704/m6.12-handoff-status.md` and
`mainline/build/m612at/report.md` in the project evidence tree.

Latest preserved runtime milestone in the reachable ledger is M6.12cw:
Linux 6.12 entry, read-only `/system` mount and Android second-stage init are
proven; complete framework/UI startup, later vendor mounts, and reboot cause
are not. Detailed chronology and evidence limits are in
`state/current-status.md` (reconstructed chronology and M6.12cw entry) and
`mainline/build/m612cw/report.md`. Builds and Fastboot acceptance are not
equivalent to runtime proof. The repository root `README` remains the upstream
Linux kernel README; this device-specific status belongs in this file.

## Related repositories

- `SnisLab/android_recovery_lenovo_TB8704`
- `SnisLab/android_kernel_lenovo_msm8953`
- `SnisLab/android_device_lenovo_TB8704`
