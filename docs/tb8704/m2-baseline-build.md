# M2 Baseline Build

Source repository:
SnisLab/linux_lenovo_TB8704

Branch:
bringup/6.12

Source commit:
50a208d01b152eba99739af7d0cea4f516bccaee

Kernel base:
Linux 6.12.0

Build host:
Ubuntu 24.04.5 LTS
x86_64
14 CPUs
16 GiB RAM

Compiler:
aarch64-linux-gnu-gcc 13.3.0

Binutils:
2.42

Architecture:
arm64

Cross prefix:
aarch64-linux-gnu-

Base config:
arch/arm64/configs/defconfig

MSM8953 config fragment:
arch/arm64/configs/msm8953.config

Config merge:
29 redefined-by-fragment warnings
0 requested values missing from final config

The redefined symbols were:
`CONFIG_BINFMT_MISC`, `CONFIG_BT_LE`, `CONFIG_CHECKPOINT_RESTORE`,
`CONFIG_DEVFREQ_GOV_PERFORMANCE`, `CONFIG_DEVFREQ_GOV_POWERSAVE`,
`CONFIG_DEVFREQ_GOV_USERSPACE`, `CONFIG_DRM_PANEL_MSM8953_GENERATED`,
`CONFIG_FW_LOADER_USER_HELPER`, `CONFIG_INTERCONNECT_QCOM_MSM8953`,
`CONFIG_MFD_QCOM_RPM`, `CONFIG_MSM_GCC_8953_DEBUG`, `CONFIG_MSM_GCC_8953`,
`CONFIG_NR_CPUS`, `CONFIG_PHY_QCOM_QUSB2`, `CONFIG_PSTORE_CONSOLE`,
`CONFIG_PSTORE_PMSG`, `CONFIG_PSTORE_RAM`, `CONFIG_QCOM_CLK_APCS_MSM8953`,
`CONFIG_QCOM_COINCELL`, `CONFIG_QCOM_CPR4PD`, `CONFIG_RTC_HCTOSYS`,
`CONFIG_RTC_SYSTOHC`, `CONFIG_SCHED_CLUSTER`, `CONFIG_SCSI_SCAN_ASYNC`,
`CONFIG_SND_SOC_QDSP6_Q6VOICE`, `CONFIG_THERMAL_GOV_BANG_BANG`,
`CONFIG_THERMAL_GOV_USER_SPACE`, `CONFIG_UEVENT_HELPER`,
`CONFIG_WCN36XX_DEBUGFS`.

Final config SHA256:
7552b35991179401d2401f91e682230b1445f4d568297abcd5ef48ecfacb8a4e

Kernel release:
6.12.0-g50a208d01b15

Build result:
success

Build targets:
Image.gz dtbs

Image:
size 46014976
sha256 526eb7cf45b88c2d40dfa4014c951e4a0d2359a25b3724bcb9f72c47dff6ab31

Image.gz:
size 14602374
sha256 da08d9c4db3c46529237c37b84a1a330dc6bba2258d34052a43866333a0fded9

Embedded version:
Linux version 6.12.0-g50a208d01b15
(root@OpenCode; aarch64-linux-gnu-gcc 13.3.0; GNU ld 2.42)

Reference DTB:
apq8053-lenovo-cd-18781y.dtb
size 65531
sha256 0abcd71a0b87d34d97314f30884f26fa36ce0b86c7dfc872eb2705ecd5f374b0

Reference DTB:
msm8953-lenovo-kuntao.dtb
size 62554
sha256 dd6d7c687c23eea5dd5eca36452bdad693e78eb79350e51b8348c35a260686d6

Source modifications required:
none

Device validation:
none

Fastboot:
not used

Flash:
not used
