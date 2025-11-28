#!/usr/bin/env python3
"""T1.09: PCAP Parser (Latency & Microburst Analysis)

Analyze captured market data packets for latency and microbursts.

Problem:
    Given a PCAP file of multicast market data:
    - Ethernet frames with UDP payload
    - Multiple length-prefixed messages per packet
    - Message format:
      - Bytes 0-3: sequence number (uint32, big-endian)
      - Bytes 4-7: reserved
      - Bytes 8-13: exchange timestamp (48-bit nanoseconds since midnight)
      - Bytes 14+: message payload

    Tasks:
    1. Parse PCAP using scapy or dpkt
    2. For each message:
       - Extract exchange_ts_ns from payload
       - Get recv_ts_ns from pcap record header
       - Compute latency = recv_ts_ns - exchange_ts_ns
    3. Produce latency statistics:
       - p50, p90, p99, max
       - Histogram (10µs bins)
    4. Microburst analysis:
       - Rolling 1ms windows with message counts
       - Top 20 burst windows
    5. Detect packet loss via sequence number gaps

Edge Cases:
    - Out-of-order packets
    - Timestamp wrap at midnight
    - VLAN tags in frames
    - Corrupted/short packets

Complexity:
    Time: O(n log n) for sorting/statistics
    Space: O(n) for message list
"""

from pathlib import Path
from typing import BinaryIO


def analyze_pcap(
    pcap_file: str | BinaryIO,
    clock_skew_ns: int = 0
) -> dict:
    """Analyze PCAP for latency and microbursts.

    Args:
        pcap_file: Path to PCAP file or binary file object
        clock_skew_ns: Clock skew correction in nanoseconds

    Returns:
        Dict with latency stats, histogram, bursts, and packet loss info
    """
    # TODO - you fill in here.
    # Note: You'll need to install scapy or dpkt:
    #   pip install scapy
    # or
    #   pip install dpkt
    return {
        'message_count': 0,
        'latency': {
            'p50_us': 0.0,
            'p90_us': 0.0,
            'p99_us': 0.0,
            'max_us': 0.0,
            'histogram': []  # [(bin_start_us, count), ...]
        },
        'microbursts': {
            'top_windows': []  # [(window_start_ns, message_count), ...]
        },
        'packet_loss': {
            'total_gaps': 0,
            'missing_sequences': []
        }
    }


if __name__ == '__main__':
    import sys
    sys.path.insert(0, str(Path(__file__).parent))
    from test_framework import run_tests

    def test_wrapper(pcap_filename: str) -> dict:
        path = Path(__file__).parent / 'test_data' / pcap_filename
        return analyze_pcap(str(path))

    exit(run_tests('pcap_latency_tests.json', test_wrapper))
