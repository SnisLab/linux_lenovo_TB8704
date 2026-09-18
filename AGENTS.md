# Agent instructions

This repository is the **mainline Linux workstream** for the Lenovo Tab 4 8 Plus TB-8704F modernization project.

## Scope

You own:
- Linux 6.x / mainline enablement for TB-8704F
- device-tree work for MSM8953/TB-8704F
- postmarketOS/Linux bring-up
- display, touch, storage, USB, GPU, Wi-Fi, Bluetooth, audio, battery/charging and suspend on mainline Linux
- documentation of upstream status and hardware support

You do **not** own:
- legacy Android kernel maintenance (`SnisLab/android_kernel_lenovo_msm8953`)
- TWRP / recovery configuration (`SnisLab/android_recovery_lenovo_TB8704`)
- Android / Lineage device-tree and HAL work (`SnisLab/android_device_lenovo_TB8704`)

If work is required elsewhere, document:

```text
Dependency request:
Repository: <repo>
Required change: <precise change>
Reason: <why it is needed>
Expected interface/result: <what this repo expects afterwards>
```

## Working model

- Start from current MSM8953 mainline work, not from the Lenovo Android 3.18 kernel as a code base.
- Use the legacy Lenovo kernel/device trees only as hardware reference material.
- Prefer upstream Linux, msm8953-mainline and postmarketOS sources.
- Work subsystem by subsystem and keep each bring-up change reviewable.
- Clearly distinguish SoC-level support from TB-8704F-specific validation.
- Never assume that a component used by TB-8703, Lenovo P2, Xiaomi or Motorola MSM8953 devices is identical on TB-8704F.

## Safety

- Mainline testing must use recoverable boot paths whenever possible.
- Do not overwrite bootloader or firmware partitions.
- Do not change the on-device partition table as part of initial bring-up.
- Preserve the stable recovery path as an independent rescue environment.

## Commit discipline

Examples:
- `docs: map TB8704F hardware to mainline drivers`
- `arm64: dts: qcom: add TB-8704F skeleton`
- `arm64: dts: qcom: tb8704f: enable eMMC`

Avoid giant commits that enable many unrelated peripherals at once.

## Initial milestone

Document the exact TB-8704F hardware relevant to mainline and identify the closest supported MSM8953 reference devices. Then create the smallest possible TB-8704F DTS needed for a first diagnostic boot. Do not start implementation until the recovery workstream provides a verified rescue path.
