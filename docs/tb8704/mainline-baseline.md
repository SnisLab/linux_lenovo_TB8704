# TB8704F Mainline Baseline

Repository:
`SnisLab/linux_lenovo_TB8704`

Working branch:
`bringup/6.12`

Upstream repository:
`https://github.com/msm8953-mainline/linux`

Upstream branch:
`6.12/main`

Pinned upstream commit:
`d9eabbae3edea6adb08e74c30059aa0933afaae7`

Kernel version:
Linux `6.12.0`, verified from the pinned tree's `Makefile`.

Pinned commit metadata:

- Author: Felix Kaechele <felix@kaechele.ca>
- Author date: 2025-01-13 16:12:00 -0500
- Committer: Barnabas Czeman <barni2000@users.noreply.github.com>
- Commit date: 2025-01-20 07:39:24 +0100
- Subject: `arm64: dts: qcom: msm8953: motorola-potter: add touchscreen reset GPIO`

Vanilla reference:
Linux `v6.12`, commit
`adc218676eef25575469234709c2d87185ca223a`.

Reason for baseline:

- Contains MSM8953 WIP integration needed for bring-up.
- Contains useful Lenovo/APQ8053/MSM8953 reference DTS files.
- Avoids starting the board port from Android 3.18.
- Allows a later controlled rebase toward maintained upstream/LTS.

Legacy reference:
`SnisLab/android_kernel_lenovo_msm8953`

Legacy policy:
Hardware reference only; no wholesale source import.

Device:
Lenovo Tab 4 8 Plus TB-8704F

Primary initial SoC hypothesis:
APQ8053 board identity using common MSM8953 SoC infrastructure.

Confidence:
Medium.

Device validation:
None on mainline yet.

M1 scope:
This commit establishes source provenance and project metadata only. No
TB8704 DTS, legacy DTS port, kernel configuration, build, firmware import,
fastboot operation, or device access is part of M1.
