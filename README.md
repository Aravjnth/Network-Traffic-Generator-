Network Traffic Generator

## Overview

The Network Traffic Generator is a Python-based tool designed to simulate network traffic for testing and analysis purposes. This tool allows users to generate various types of network traffic, including TCP, UDP, and ICMP, to evaluate the performance and security of network devices and applications.

## Features

- Generate different types of network traffic (TCP, UDP, ICMP).
- Customizable packet size, rate, and duration.
- Support for IPv4 and IPv6.
- Easy-to-use command-line interface.
- Logging and reporting of generated traffic.

## Requirements

- Python 3.x
- `scapy` library for packet crafting

## Installation

1. Clone the repository:
    ```bash
    https://github.com/Aravjnth/Network-Traffic-Generator-.git
    cd network-traffic-generator
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the tool with the desired options to generate network traffic:
    ```bash
    python generate_traffic.py -t <traffic-type> -d <destination-ip> -p <port> -s <packet-size> -r <rate> -u <duration>
    ```

    Replace `<traffic-type>`, `<destination-ip>`, `<port>`, `<packet-size>`, `<rate>`, and `<duration>` with the actual values.

### Example

Generate UDP traffic to 192.168.1.1 on port 80 with a packet size of 100 bytes, at a rate of 10 packets per second, for a duration of 60 seconds:

```bash
python generate_traffic.py -t udp -d 192.168.1.1 -p 80 -s 100 -r 10 -u 60
```

## Options

- `-t, --type`: Type of traffic to generate (tcp, udp, icmp).
- `-d, --destination`: Destination IP address.
- `-p, --port`: Destination port (required for TCP/UDP).
- `-s, --size`: Packet size in bytes.
- `-r, --rate`: Packet rate (packets per second).
- `-u, --duration`: Duration of traffic generation in seconds.
- `-i, --interface`: (Optional) Network interface to use.

## Legal Disclaimer

This tool is intended for educational purposes only. Unauthorized use of this tool to generate traffic against targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state, and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, feel free to contact me at www.linkedin.com/in/aravinth-aj.
