# Kernel upgrades and Android 16 roadmap

Status: assessment and proposed gates, 2026-10-15. This is a plan, not evidence
that any proposed kernel, Android distribution, or hardware function works.
The current checkout is a partial TB-8704F Linux 6.12 scaffold. The documented
Linux entry, read-only `/system` mount and second-stage init are historical,
secondary-referenced runtime evidence only; they do not prove full Android boot.
Linux userspace bring-up is independent of Android framework startup.

## Kernel generation roadmap

Every generation is developed on its own branch, retaining the previous known
diagnostic branch. Do not merge forward until build, boot and stability gates
are recorded against the exact source revision, configuration, DTB and boot
artifact. The current partial board description and reference-device behavior
do not establish TB-8704F compatibility.

| Order / branch | Prerequisites | Boot and stability gates |
|---|---|---|
| Linux 6.12.0 (`tb8704f/linux-6.12.0`) | Preserve the current baseline; identify source commit, config, compiler and reproducible Image/DTB packaging. Verify rescue path before device trials. | Build and inspect artifacts; validate DT and bootimage/loader handoff; diagnostic console and repeatable recoverable boot; record storage, reboot, thermal and sustained-idle observations. This is the baseline, not a complete port. |
| Linux 6.12.x (`tb8704f/linux-6.12-stable`) | Start from a selected stable point on a separate branch; audit each stable update and backport against the device tree and local patches. | Rebuild and boot after each update; compare console, storage and enabled peripherals; run repeated cold/warm boots and extended idle/load checks; investigate regressions before advancing. |
| Linux 6.18.0 (`tb8704f/linux-6.18.0`) | Rebase/port rather than assume ABI continuity; resolve changed drivers, bindings, config, compiler requirements and packaging. | Clean build plus DT schema validation; verify boot handoff and diagnostic shell on device; exercise available hardware and compare boot logs, hangs, crashes, power and thermal behavior to baseline. |
| Linux 6.18.x (`tb8704f/linux-6.18-stable`) | Choose a stable point and separately review stable updates, security fixes and downstream patch conflicts. | Repeat build, DT, recoverable boot, reboot and sustained-run gates for each update; document resolved and outstanding regressions. |
| Linux 7.2.0 (`tb8704f/linux-7.2.0`) | Treat as a major forward port; audit API/ABI, compiler and bootloader interface changes before device use. | Compile and schema-check; boot with diagnostic userspace via verified recovery route; test enabled subsystems, repeated restart, suspend/resume where implemented, and sustained stability. No automatic promotion from 6.x. |
| Linux 7.2.x (`tb8704f/linux-7.2-stable`) | Select a stable point; track maintenance and security coverage and resolve update-specific conflicts on its own branch. | Repeat update-specific build, boot, runtime and regression gates, including security-patch review and reproducible rollback. |
| Later suitable LTS (`tb8704f/linux-lts-<version>`, version TBD) | Select only after applying the criteria below; keep 7.2.x and the existing diagnostic baseline available during evaluation. | Require complete build/DT/boot gates, repeated device stability runs, supported-subsystem inventory, documented security-update process and a tested recovery/rollback before choosing as maintained baseline. |

The version labels above identify requested evaluation milestones, not a
guarantee that each upstream point release will be an LTS or available with a
particular support duration. Maintain distinct development branches and
versioned test evidence for every row.

### Later LTS selection criteria

Choose a later LTS only when evidence supports all of the following:

* **Maintenance and security:** published upstream maintenance horizon is
  adequate for the intended device lifecycle; security fixes are actively
  available and there is a resourced, trackable process to consume and test
  them. Record end-of-life and reassess before it.
* **MSM8953 and board support:** relevant Qualcomm/MSM8953 drivers remain
  supported, and the TB-8704F-specific DT and enabled peripherals can be
  maintained. Evidence from TB-8703, Lenovo P2, Xiaomi or Motorola devices is
  a lead only, not proof of identical hardware or support.
* **Toolchain and subsystems:** supported compiler/binutils can build the
  required configuration; required driver, DRM/display, storage, input, power,
  networking and userspace interfaces are available or realistically
  maintainable.
* **Portability:** patch delta, DT-binding changes and dtschema failures,
  driver/subsystem API changes, MSM8953-specific fixes, toolchain changes,
  bootimage/init integration and expected regression workload are bounded and
  reproducibly testable. Reject a nominally newer LTS if forward-port cost
  exceeds maintainable capacity.
* **Android interfaces:** if Android is in scope, establish required kernel
  interfaces and any GKI/vendor-module requirements from actual manifests,
  source and binary/interface evidence. GKI compatibility is not inferred from
  version naming or successful Linux boot.

### Upgrade review checklist (apply to each branch)

1. **Patch portability:** classify every local patch as upstreamed, obsolete,
   cleanly portable or requiring redesign; inspect conflicts and semantic
   changes rather than relying on a successful cherry-pick.
2. **DT and bindings:** rebase DTS changes, review binding changes, run relevant
   `dt_binding_check`/`dtbs_check` (dtschema) and resolve warnings/errors.
3. **Driver/subsystem APIs:** audit changed interfaces and configuration
   dependencies for each enabled driver and downstream consumer.
4. **MSM8953:** verify SoC-specific clocks, regulators, interconnects, pinctrl,
   reserved memory and relevant driver support; distinguish upstream SoC
   support from TB-8704F validation.
5. **Toolchain:** record compiler, binutils and build configuration; confirm
   reproducible build and resolve warnings or unsupported toolchain needs.
6. **Bootimage/init:** verify actual loader expectations, Image compression,
   DTB placement/selection, command line, initramfs and partition/mount setup;
   do not infer boot compatibility from artifact naming.
7. **Runtime regressions:** compare boot logs and test repeat boot, storage,
   available peripherals, idle/load, thermal behavior, suspend/resume where
   supported, and reboot. Mark untested functions explicitly.
8. **LTS security care:** record upstream stable/security updates, local
   backports, build/boot regression results, responsible maintenance and
   end-of-support date.
9. **Android GKI compatibility:** inspect Android requirements, GKI/KMI and
   module interfaces, vendor modules and boot image format. No compatibility
   claim without interface evidence and an appropriate device test.

## Android 16 assessment

The Android projects are separate from mainline Linux userspace bring-up.
Missing source trees, vendor blobs, manifests, HAL source/interface details,
and device-specific runtime logs are open prerequisites; no compatibility or
product-readiness conclusion is confirmed without them.

### Primary target: AOSP Android 16

Assess AOSP first as the primary Android 16 target. Required evidence includes
the exact Android 16 manifest and device/vendor trees; proprietary vendor
components and licensing/availability; required HAL implementations and
versions; kernel interfaces and module/KMI expectations; SELinux policy and
denial review; recovery integration and a verified rescue path. Determine
whether TB-8704F-specific trees can be built and maintained against that
release rather than assuming the legacy Android 3.18 tree is portable.

At present, source/build reproducibility, vendor/HAL availability, interface
compatibility, hardware coverage and framework startup are unknown. The
historical second-stage-init observation does not prove Android 16 operation.
Gate any maturity claim on reproducible build, recoverable device boot, logs
showing framework startup, security-policy validation, and per-component
hardware tests. Until then this is an investigation target, not an everyday-use
system.

### Subsequent separate assessment: PixelOS

Evaluate PixelOS only after AOSP Android 16 dependencies and baseline are
understood. Independently establish the exact PixelOS release/base, device
trees, vendor components, HALs, kernel interfaces and any GKI/KMI assumptions;
review SELinux policy, recovery support, upstream/downstream maintenance and
security-update path. AOSP compatibility does not establish PixelOS
compatibility, and PixelOS branding or another MSM8953 device's support is not
interface evidence.

No local PixelOS-specific source or TB-8704F integration evidence is established
here. Product maturity, security, hardware coverage, daily-use reliability and
recovery behavior therefore remain unverified. Keep PixelOS a later technical
evaluation, gated on source/interface evidence, reproducible build, safe
recovery, device boot, hardware matrix and sustained real-use testing.

### Open prerequisites and evidence ownership

Obtain and record Android 16 AOSP and PixelOS manifests/source availability,
TB-8704F device trees, proprietary vendor binaries/source and HAL inventories,
kernel interface requirements, SELinux policy, and recovery/build artifacts.
Until supplied, report these as missing prerequisites rather than assume
availability. Recovery readiness is separately owned: the recovery repository
and `recovery/src/android_recovery_lenovo_TB8704/docs/status.md` are absent from
this checkout, so no recovery status is asserted or edited here. The recovery
workstream must provide a verified rescue-path result before device kernel
upgrade testing.
