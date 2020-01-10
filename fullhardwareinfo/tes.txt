computer                    
    description: Computer
    width: 64 bits
    capabilities: smp vsyscall32
  *-core
       description: Motherboard
       physical id: 0
     *-memory
          description: System memory
          physical id: 0
          size: 3968MiB
     *-cpu
          product: Intel(R) Core(TM) i3-2310M CPU @ 2.10GHz
          vendor: Intel Corp.
          physical id: 1
          bus info: cpu@0
          size: 1844MHz
          capacity: 2100MHz
          width: 64 bits
          capabilities: fpu fpu_exception wp vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ht tm pbe syscall nx rdtscp x86-64 constant_tsc arch_perfmon pebs bts nopl xtopology nonstop_tsc cpuid aperfmperf pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic popcnt tsc_deadline_timer xsave avx lahf_lm epb pti ssbd ibrs ibpb stibp tpr_shadow vnmi flexpriority ept vpid xsaveopt dtherm arat pln pts md_clear flush_l1d cpufreq
     *-pci
          description: Host bridge
          product: 2nd Generation Core Processor Family DRAM Controller
          vendor: Intel Corporation
          physical id: 100
          bus info: pci@0000:00:00.0
          version: 09
          width: 32 bits
          clock: 33MHz
        *-display
             description: VGA compatible controller
             product: 2nd Generation Core Processor Family Integrated Graphics Controller
             vendor: Intel Corporation
             physical id: 2
             bus info: pci@0000:00:02.0
             version: 09
             width: 64 bits
             clock: 33MHz
             capabilities: vga_controller bus_master cap_list rom
             configuration: driver=i915 latency=0
             resources: irq:34 memory:f0000000-f03fffff memory:e0000000-efffffff ioport:2000(size=64) memory:c0000-dffff
        *-communication
             description: Communication controller
             product: 6 Series/C200 Series Chipset Family MEI Controller #1
             vendor: Intel Corporation
             physical id: 16
             bus info: pci@0000:00:16.0
             version: 04
             width: 64 bits
             clock: 33MHz
             capabilities: bus_master cap_list
             configuration: driver=mei_me latency=0
             resources: irq:35 memory:f0705000-f070500f
        *-usb:0
             description: USB controller
             product: 6 Series/C200 Series Chipset Family USB Enhanced Host Controller #2
             vendor: Intel Corporation
             physical id: 1a
             bus info: pci@0000:00:1a.0
             version: 04
             width: 32 bits
             clock: 33MHz
             capabilities: ehci bus_master cap_list
             configuration: driver=ehci-pci latency=0
             resources: irq:16 memory:f070a000-f070a3ff
        *-multimedia
             description: Audio device
             product: 6 Series/C200 Series Chipset Family High Definition Audio Controller
             vendor: Intel Corporation
             physical id: 1b
             bus info: pci@0000:00:1b.0
             version: 04
             width: 64 bits
             clock: 33MHz
             capabilities: bus_master cap_list
             configuration: driver=snd_hda_intel latency=0
             resources: irq:36 memory:f0700000-f0703fff
        *-pci:0
             description: PCI bridge
             product: 6 Series/C200 Series Chipset Family PCI Express Root Port 1
             vendor: Intel Corporation
             physical id: 1c
             bus info: pci@0000:00:1c.0
             version: b4
             width: 32 bits
             clock: 33MHz
             capabilities: pci normal_decode bus_master cap_list
             configuration: driver=pcieport
             resources: irq:24
        *-pci:1
             description: PCI bridge
             product: 6 Series/C200 Series Chipset Family PCI Express Root Port 2
             vendor: Intel Corporation
             physical id: 1c.1
             bus info: pci@0000:00:1c.1
             version: b4
             width: 32 bits
             clock: 33MHz
             capabilities: pci normal_decode bus_master cap_list
             configuration: driver=pcieport
             resources: irq:25 memory:f0600000-f06fffff
           *-network DISABLED
                description: Wireless interface
                product: AR9287 Wireless Network Adapter (PCI-Express)
                vendor: Qualcomm Atheros
                physical id: 0
                bus info: pci@0000:02:00.0
                logical name: wlp2s0
                version: 01
                serial: [REMOVED]
                width: 64 bits
                clock: 33MHz
                capabilities: bus_master cap_list ethernet physical wireless
                configuration: broadcast=yes driver=ath9k driverversion=5.4.8-200.fc31.x86_64 firmware=N/A latency=0 link=no multicast=yes wireless=IEEE 802.11
                resources: irq:17 memory:f0600000-f060ffff
        *-pci:2
             description: PCI bridge
             product: 6 Series/C200 Series Chipset Family PCI Express Root Port 4
             vendor: Intel Corporation
             physical id: 1c.3
             bus info: pci@0000:00:1c.3
             version: b4
             width: 32 bits
             clock: 33MHz
             capabilities: pci normal_decode bus_master cap_list
             configuration: driver=pcieport
             resources: irq:26 memory:dfa00000-dfafffff ioport:f0400000(size=1048576)
           *-network
                description: Ethernet interface
                product: NetLink BCM57785 Gigabit Ethernet PCIe
                vendor: Broadcom Inc. and subsidiaries
                physical id: 0
                bus info: pci@0000:03:00.0
                logical name: enp3s0f0
                version: 10
                serial: [REMOVED]
                capacity: 1Gbit/s
                width: 64 bits
                clock: 33MHz
                capabilities: bus_master cap_list rom ethernet physical tp 10bt 10bt-fd 100bt 100bt-fd 1000bt 1000bt-fd autonegotiation
                configuration: autonegotiation=on broadcast=yes driver=tg3 driverversion=3.137 firmware=sb latency=0 link=no multicast=yes port=twisted pair
                resources: irq:19 memory:f0400000-f040ffff memory:f0410000-f041ffff memory:dfa00000-dfa007ff
           *-generic:0
                description: SD Host controller
                product: BCM57765/57785 SDXC/MMC Card Reader
                vendor: Broadcom Inc. and subsidiaries
                physical id: 0.1
                bus info: pci@0000:03:00.1
                version: 10
                width: 64 bits
                clock: 33MHz
                capabilities: bus_master cap_list
                configuration: driver=sdhci-pci latency=0
                resources: irq:16 memory:f0420000-f042ffff
           *-generic:1 UNCLAIMED
                description: System peripheral
                product: BCM57765/57785 MS Card Reader
                vendor: Broadcom Inc. and subsidiaries
                physical id: 0.2
                bus info: pci@0000:03:00.2
                version: 10
                width: 64 bits
                clock: 33MHz
                capabilities: cap_list
                configuration: latency=0
                resources: memory:f0430000-f043ffff
           *-generic:2 UNCLAIMED
                description: System peripheral
                product: BCM57765/57785 xD-Picture Card Reader
                vendor: Broadcom Inc. and subsidiaries
                physical id: 0.3
                bus info: pci@0000:03:00.3
                version: 10
                width: 64 bits
                clock: 33MHz
                capabilities: cap_list
                configuration: latency=0
                resources: memory:f0440000-f044ffff
        *-pci:3
             description: PCI bridge
             product: 6 Series/C200 Series Chipset Family PCI Express Root Port 5
             vendor: Intel Corporation
             physical id: 1c.4
             bus info: pci@0000:00:1c.4
             version: b4
             width: 32 bits
             clock: 33MHz
             capabilities: pci normal_decode bus_master cap_list
             configuration: driver=pcieport
             resources: irq:27 memory:f0500000-f05fffff
           *-usb
                description: USB controller
                product: uPD720200 USB 3.0 Host Controller
                vendor: NEC Corporation
                physical id: 0
                bus info: pci@0000:04:00.0
                version: 04
                width: 64 bits
                clock: 33MHz
                capabilities: xhci bus_master cap_list
                configuration: driver=xhci_hcd latency=0
                resources: irq:16 memory:f0500000-f0501fff
        *-usb:1
             description: USB controller
             product: 6 Series/C200 Series Chipset Family USB Enhanced Host Controller #1
             vendor: Intel Corporation
             physical id: 1d
             bus info: pci@0000:00:1d.0
             version: 04
             width: 32 bits
             clock: 33MHz
             capabilities: ehci bus_master cap_list
             configuration: driver=ehci-pci latency=0
             resources: irq:23 memory:f0709000-f07093ff
        *-isa
             description: ISA bridge
             product: HM65 Express Chipset LPC Controller
             vendor: Intel Corporation
             physical id: 1f
             bus info: pci@0000:00:1f.0
             version: 04
             width: 32 bits
             clock: 33MHz
             capabilities: isa bus_master cap_list
             configuration: driver=lpc_ich latency=0
             resources: irq:0
        *-sata
             description: SATA controller
             product: 6 Series/C200 Series Chipset Family 6 port Mobile SATA AHCI Controller
             vendor: Intel Corporation
             physical id: 1f.2
             bus info: pci@0000:00:1f.2
             logical name: scsi1
             version: 04
             width: 32 bits
             clock: 66MHz
             capabilities: sata ahci_1.0 bus_master cap_list emulated
             configuration: driver=ahci latency=0
             resources: irq:28 ioport:2088(size=8) ioport:2094(size=4) ioport:2080(size=8) ioport:2090(size=4) ioport:2060(size=32) memory:f0708000-f07087ff
           *-cdrom
                description: DVD-RAM writer
                product: DVD-RAM UJ8A0AS
                vendor: MATSHITA
                physical id: 0.0.0
                bus info: scsi@1:0.0.0
                logical name: /dev/cdrom
                logical name: /dev/sr0
                version: 1.00
                capabilities: removable audio cd-r cd-rw dvd dvd-r dvd-ram
                configuration: ansiversion=5 status=nodisc
        *-serial
             description: SMBus
             product: 6 Series/C200 Series Chipset Family SMBus Controller
             vendor: Intel Corporation
             physical id: 1f.3
             bus info: pci@0000:00:1f.3
             version: 04
             width: 64 bits
             clock: 33MHz
             configuration: driver=i801_smbus latency=0
             resources: irq:18 memory:f0704000-f07040ff ioport:efa0(size=32)
     *-pnp00:00
          product: PnP device PNP0c02
          physical id: 2
          capabilities: pnp
          configuration: driver=system
     *-pnp00:01
          product: PnP device PNP0b00
          physical id: 3
          capabilities: pnp
          configuration: driver=rtc_cmos
     *-pnp00:02
          product: PnP device INT3f0d
          vendor: Interphase Corporation
          physical id: 4
          capabilities: pnp
          configuration: driver=system
     *-pnp00:03
          product: PnP device PNP0303
          physical id: 5
          capabilities: pnp
          configuration: driver=i8042 kbd
     *-pnp00:04
          product: PnP device SYN1b45
          vendor: Synaptics Inc
          physical id: 6
          capabilities: pnp
          configuration: driver=i8042 aux
     *-pnp00:05
          product: PnP device PNP0c02
          physical id: 7
          capabilities: pnp
          configuration: driver=system
     *-pnp00:06
          product: PnP device PNP0c01
          physical id: 8
          capabilities: pnp
          configuration: driver=system
  *-network
       description: Ethernet interface
       physical id: 1
       bus info: usb@1:1.2
       logical name: enp0s26u1u2
       serial: [REMOVED]
       capabilities: ethernet physical
       configuration: broadcast=yes driver=rndis_host driverversion=22-Aug-2005 firmware=RNDIS device ip=[REMOVED] link=yes multicast=yes
