#! /usr/bin/env python

# Programs that are runnable.
ns3_runnable_programs = ['src/aodv/examples/ns3-dev-aodv-debug', 'src/bridge/examples/ns3-dev-csma-bridge-debug', 'src/bridge/examples/ns3-dev-csma-bridge-one-hop-debug', 'src/buildings/examples/ns3-dev-buildings-pathloss-profiler-debug', 'src/config-store/examples/ns3-dev-config-store-save-debug', 'src/core/examples/ns3-dev-main-callback-debug', 'src/core/examples/ns3-dev-sample-simulator-debug', 'src/core/examples/ns3-dev-main-ptr-debug', 'src/core/examples/ns3-dev-main-random-variable-debug', 'src/core/examples/ns3-dev-main-random-variable-stream-debug', 'src/core/examples/ns3-dev-sample-random-variable-debug', 'src/core/examples/ns3-dev-sample-random-variable-stream-debug', 'src/core/examples/ns3-dev-main-test-sync-debug', 'src/csma/examples/ns3-dev-csma-one-subnet-debug', 'src/csma/examples/ns3-dev-csma-broadcast-debug', 'src/csma/examples/ns3-dev-csma-packet-socket-debug', 'src/csma/examples/ns3-dev-csma-multicast-debug', 'src/csma/examples/ns3-dev-csma-raw-ip-socket-debug', 'src/csma/examples/ns3-dev-csma-ping-debug', 'src/csma-layout/examples/ns3-dev-csma-star-debug', 'src/dsdv/examples/ns3-dev-dsdv-manet-debug', 'src/dsr/examples/ns3-dev-dsr-debug', 'src/emu/examples/ns3-dev-emu-udp-echo-debug', 'src/emu/examples/ns3-dev-emu-ping-debug', 'src/energy/examples/ns3-dev-li-ion-energy-source-debug', 'src/internet/examples/ns3-dev-main-simple-debug', 'src/lte/examples/ns3-dev-lena-cqi-threshold-debug', 'src/lte/examples/ns3-dev-lena-dual-stripe-debug', 'src/lte/examples/ns3-dev-lena-fading-debug', 'src/lte/examples/ns3-dev-lena-intercell-interference-debug', 'src/lte/examples/ns3-dev-lena-pathloss-traces-debug', 'src/lte/examples/ns3-dev-lena-profiling-debug', 'src/lte/examples/ns3-dev-lena-rem-debug', 'src/lte/examples/ns3-dev-lena-rem-sector-antenna-debug', 'src/lte/examples/ns3-dev-lena-rlc-traces-debug', 'src/lte/examples/ns3-dev-lena-simple-debug', 'src/lte/examples/ns3-dev-lena-simple-epc-debug', 'src/mesh/examples/ns3-dev-mesh-debug', 'src/mobility/examples/ns3-dev-main-grid-topology-debug', 'src/mobility/examples/ns3-dev-main-random-topology-debug', 'src/mobility/examples/ns3-dev-main-random-walk-debug', 'src/mobility/examples/ns3-dev-mobility-trace-example-debug', 'src/mobility/examples/ns3-dev-ns2-mobility-trace-debug', 'src/mobility/examples/ns3-dev-bonnmotion-ns2-example-debug', 'src/mpi/examples/ns3-dev-simple-distributed-debug', 'src/mpi/examples/ns3-dev-third-distributed-debug', 'src/mpi/examples/ns3-dev-nms-p2p-nix-distributed-debug', 'src/ndnSIM/examples/ns3-dev-ndn-simple-debug', 'src/ndnSIM/examples/ns3-dev-ndn-grid-debug', 'src/ndnSIM/examples/ns3-dev-ndn-zipf-mandelbrot-debug', 'src/ndnSIM/examples/ns3-dev-ndn-simple-with-content-freshness-debug', 'src/ndnSIM/examples/ns3-dev-ndn-simple-with-custom-app-debug', 'src/ndnSIM/examples/ns3-dev-ndn-grid-topo-plugin-debug', 'src/ndnSIM/examples/ns3-dev-ndn-congestion-topo-plugin-debug', 'src/ndnSIM/examples/ns3-dev-ndn-congestion-alt-topo-plugin-debug', 'src/ndnSIM/examples/ns3-dev-ndn-tree-tracers-debug', 'src/ndnSIM/examples/ns3-dev-ndn-tree-cs-tracers-debug', 'src/ndnSIM/examples/ns3-dev-ndn-tree-app-delay-tracer-debug', 'src/ndnSIM/examples/ns3-dev-ndn-tree-with-l2tracer-debug', 'src/ndnSIM/examples/ns3-dev-ndn-simple-pit-policies-debug', 'src/ndnSIM/examples/ns3-dev-ndn-simple-with-different-sizes-content-store-debug', 'src/ndnSIM/examples/ns3-dev-ndn-simple-with-cs-lfu-debug', 'src/ndnSIM/examples/ns3-dev-ndn-simple-with-pcap-debug', 'src/ndnSIM/examples/ns3-dev-ndn-simple-with-pit-operation-stats-debug', 'src/ndnSIM/tools/ns3-dev-rocketfuel-maps-cch-to-annotaded-debug', 'src/netanim/examples/ns3-dev-dumbbell-animation-debug', 'src/netanim/examples/ns3-dev-grid-animation-debug', 'src/netanim/examples/ns3-dev-star-animation-debug', 'src/netanim/examples/ns3-dev-wireless-animation-debug', 'src/netanim/examples/ns3-dev-uan-animation-debug', 'src/netanim/examples/ns3-dev-dynamic_linknode-debug', 'src/network/examples/ns3-dev-main-packet-header-debug', 'src/network/examples/ns3-dev-main-packet-tag-debug', 'src/network/examples/ns3-dev-red-tests-debug', 'src/network/examples/ns3-dev-droptail_vs_red-debug', 'src/nix-vector-routing/examples/ns3-dev-nix-simple-debug', 'src/nix-vector-routing/examples/ns3-dev-nms-p2p-nix-debug', 'src/olsr/examples/ns3-dev-simple-point-to-point-olsr-debug', 'src/olsr/examples/ns3-dev-olsr-hna-debug', 'src/point-to-point/examples/ns3-dev-main-attribute-value-debug', 'src/propagation/examples/ns3-dev-main-propagation-loss-debug', 'src/propagation/examples/ns3-dev-jakes-propagation-model-example-debug', 'src/spectrum/examples/ns3-dev-adhoc-aloha-ideal-phy-debug', 'src/spectrum/examples/ns3-dev-adhoc-aloha-ideal-phy-matrix-propagation-loss-model-debug', 'src/spectrum/examples/ns3-dev-adhoc-aloha-ideal-phy-with-microwave-oven-debug', 'src/tap-bridge/examples/ns3-dev-tap-csma-debug', 'src/tap-bridge/examples/ns3-dev-tap-csma-virtual-machine-debug', 'src/tap-bridge/examples/ns3-dev-tap-wifi-virtual-machine-debug', 'src/tap-bridge/examples/ns3-dev-tap-wifi-dumbbell-debug', 'src/tools/examples/ns3-dev-gnuplot-example-debug', 'src/topology-read/examples/ns3-dev-topology-read-debug', 'src/uan/examples/ns3-dev-uan-cw-example-debug', 'src/uan/examples/ns3-dev-uan-rc-example-debug', 'src/virtual-net-device/examples/ns3-dev-virtual-net-device-debug', 'src/wifi/examples/ns3-dev-wifi-phy-test-debug', 'src/wimax/examples/ns3-dev-wimax-ipv4-debug', 'src/wimax/examples/ns3-dev-wimax-multicast-debug', 'src/wimax/examples/ns3-dev-wimax-simple-debug', 'examples/udp/ns3-dev-udp-echo-debug', 'examples/tutorial/ns3-dev-hello-simulator-debug', 'examples/tutorial/ns3-dev-first-debug', 'examples/tutorial/ns3-dev-second-debug', 'examples/tutorial/ns3-dev-third-debug', 'examples/tutorial/ns3-dev-fourth-debug', 'examples/tutorial/ns3-dev-fifth-debug', 'examples/tutorial/ns3-dev-sixth-debug', 'examples/error-model/ns3-dev-simple-error-model-debug', 'examples/ipv6/ns3-dev-icmpv6-redirect-debug', 'examples/ipv6/ns3-dev-ping6-debug', 'examples/ipv6/ns3-dev-radvd-debug', 'examples/ipv6/ns3-dev-radvd-two-prefix-debug', 'examples/ipv6/ns3-dev-test-ipv6-debug', 'examples/ipv6/ns3-dev-fragmentation-ipv6-debug', 'examples/ipv6/ns3-dev-loose-routing-ipv6-debug', 'examples/tcp/ns3-dev-tcp-large-transfer-debug', 'examples/tcp/ns3-dev-tcp-nsc-lfn-debug', 'examples/tcp/ns3-dev-tcp-nsc-zoo-debug', 'examples/tcp/ns3-dev-tcp-star-server-debug', 'examples/tcp/ns3-dev-star-debug', 'examples/tcp/ns3-dev-tcp-bulk-send-debug', 'examples/realtime/ns3-dev-realtime-udp-echo-debug', 'examples/stats/ns3-dev-wifi-example-sim-debug', 'examples/socket/ns3-dev-socket-bound-static-routing-debug', 'examples/socket/ns3-dev-socket-bound-tcp-static-routing-debug', 'examples/socket/ns3-dev-socket-options-ipv4-debug', 'examples/socket/ns3-dev-socket-options-ipv6-debug', 'examples/routing/ns3-dev-dynamic-global-routing-debug', 'examples/routing/ns3-dev-static-routing-slash32-debug', 'examples/routing/ns3-dev-global-routing-slash32-debug', 'examples/routing/ns3-dev-global-injection-slash32-debug', 'examples/routing/ns3-dev-simple-global-routing-debug', 'examples/routing/ns3-dev-simple-alternate-routing-debug', 'examples/routing/ns3-dev-mixed-global-routing-debug', 'examples/routing/ns3-dev-simple-routing-ping6-debug', 'examples/routing/ns3-dev-manet-routing-compare-debug', 'examples/naming/ns3-dev-object-names-debug', 'examples/matrix-topology/ns3-dev-matrix-topology-debug', 'examples/udp-client-server/ns3-dev-udp-client-server-debug', 'examples/udp-client-server/ns3-dev-udp-trace-client-server-debug', 'examples/wireless/ns3-dev-mixed-wireless-debug', 'examples/wireless/ns3-dev-wifi-adhoc-debug', 'examples/wireless/ns3-dev-wifi-clear-channel-cmu-debug', 'examples/wireless/ns3-dev-wifi-ap-debug', 'examples/wireless/ns3-dev-wifi-wired-bridging-debug', 'examples/wireless/ns3-dev-simple-wifi-frame-aggregation-debug', 'examples/wireless/ns3-dev-multirate-debug', 'examples/wireless/ns3-dev-wifi-simple-adhoc-debug', 'examples/wireless/ns3-dev-wifi-simple-adhoc-grid-debug', 'examples/wireless/ns3-dev-wifi-simple-infra-debug', 'examples/wireless/ns3-dev-wifi-simple-interference-debug', 'examples/wireless/ns3-dev-wifi-blockack-debug', 'examples/wireless/ns3-dev-ofdm-validation-debug', 'examples/wireless/ns3-dev-wifi-hidden-terminal-debug', 'examples/energy/ns3-dev-energy-model-example-debug', 'scratch/ns3-dev-ndncc-bcube-large-scale-sharing-debug', 'scratch/ns3-dev-ndncc-tcp-fattree-large-scale-debug', 'scratch/ns3-dev-ndncc-bcube-large-scale-debug', 'scratch/ns3-dev-ndncc-tcp-bcube-debug', 'scratch/ns3-dev-ndncc-fattree-large-scale-sharing-debug', 'scratch/ns3-dev-ndncc-multihop-tcp-fairness-debug', 'scratch/ns3-dev-scratch-simulator-debug', 'scratch/ns3-dev-ndncc-local-debug', 'scratch/ns3-dev-ndncc-multipath-tcp-fairness-debug', 'scratch/subdir/ns3-dev-subdir-debug', 'scratch/ns3-dev-ndncc-multipath-fairness-debug', 'scratch/ns3-dev-ndncc-failure-simple-debug', 'scratch/ns3-dev-ndncc-tcp-bcube-large-scale-debug', 'scratch/ns3-dev-ndncc-multihoming-debug', 'scratch/ns3-dev-ndncc-fattree-large-scale-debug', 'scratch/ns3-dev-ndncc-bcube-debug', 'scratch/ns3-dev-ndncc-multihop-simple-debug', 'scratch/ns3-dev-ndncc-tcp-local-debug', 'scratch/ns3-dev-ndncc-simple-debug', 'scratch/ns3-dev-ndncc-multihop-fairness-debug', 'scratch/ns3-dev-ndncc-multipath-fairness-sharing-debug', 'scratch/ns3-dev-ndncc-multihop-fairness-sharing-debug']

# Scripts that are runnable.
ns3_runnable_scripts = ['csma-bridge.py', 'sample-simulator.py', 'wifi-olsr-flowmon.py', 'tap-csma-virtual-machine.py', 'tap-wifi-virtual-machine.py', 'first.py', 'realtime-udp-echo.py', 'simple-routing-ping6.py', 'mixed-wireless.py', 'wifi-ap.py']
