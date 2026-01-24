# Network IP Address

## What is an IP Address?

IP address, or Internet Protocol address, is a **unique string of numbers assigned to each device** connected to a computer network that **uses Internet Protocol** for communication.

It **serves as an identifier** that **allows devices to send and receive data over the network**, ensuring that this data reaches the correct destination.

## Components of IP Address

IP address comprises of two parts:

1) `Network ID`
    - Network portion of IP address
    - Tells routers what network the host belongs to and thus where to route data that is destined for that host
    - All hosts on the same physical network share the same network ID

2) `Host ID`
    - Tells routers the specific device that the data should be delivered to

Both network ID and host ID must be unique for proper routing.

### Rules for Assigning Network ID

- **Loopback restriction**:
    - A network ID must not start with `127`, as this range belongs to Class A and is reserved for loopback functions
- **All-zeros restriction**:
    - A network ID with all bits set to 0 represents the local network, is not routed, and therefore, is not used for general network identification
- **All-ones restriction**:
    - A network ID with all bits set to 1 is reserved for broadcast purposes and cannot be assigned to a network

### Rules for Assigning Host ID

- **Uniqueness**:
    - Each host ID must be unique within the same network
- **All-zeros restriction**:
    - A host ID with all bits set to 0 is not allowed, as it represents the network address
- **All-ones restriction**:
    - A host ID with all bits set to 1 is not allowed, as it is reserved for broadcast address used to reach all hosts in the network

## Classful IP Addressing

Address classes are used to **determine the network ID and host ID** on the IP address, using the 32-bit IP address space differently, providing more or fewer bits for the network part (network ID) of the address.

`Class A` :

- First octet value range : 0 to 127
    - The MSB (Most significant bit) of first octet is always `0`, and the remaining 7 bits are used to identify the network
- Network ID range: `0.` to `127.`
- Public IP range : `1.0.0.0` to `126.255.255.255`
- Private IP range : `10.0.0.0` to `10.255.255.255`
- Special IP range : `127.0.0.1` to `172.255.255.255`
- Network bits : First **8** bits
    - Number of usable networks : 126 (2<sup>(8-1)</sup> - 2)
        - `(8-1)` , because only 7 bits are used in 8 network bits
        - `-2` , because each network cannot use end with `.0.0.0` or `.255.255.255`
- Host bits: Remaining **24** bits
    - Number of usable hosts : 16,777,214 (2<sup>24</sup> - 2)
        - `-2` , because 2 addresses are reserved (Network ID and Broadcast address)
- Subnet Mask : `255.0.0.0` (8 bits)
- Broadcast Address : `XXX.255.255.255`
- Use : Large networks
- Example : Government organizations

`Class B` :

- First octet value range : 128 to 191
    - The first 2 bits of the first octet are always `10`, and the remaining 14 bits are used to determine the network ID
- Network ID range : `128.0` to `191.255`
- Public IP range : `128.0.0.0` to `191.255.255.255`
- Private IP range : `172.16.0.0` to `172.31.255.255`
- Network bits : First **16** bits
    - Number of usable networks : 16,382 (2<sup>(16-2)</sup> - 2)
        - `(16-2)` , because only 14 bits are used in 16 network bits
        - `-2` , because each network cannot use end with `.0.0` or `.255.255`
- Host bits: Remaining **16** bits
    - Number of usable hosts : 65,534 (2<sup>16</sup> - 2)
        - `-2` , because 2 addresses are reserved (Network ID and Broadcast address)
- Subnet Mask : `255.255.0.0` (16 bits)
- Broadcast Address : `XXX.XXX.255.255`
- Use : Medium-sized networks
- Example : Universities

`Class C` :

- First octet value range : 192 to 233
    - The first 3 bits of the first octet are always `110`, and the remaining 21 bits are used to determine the network ID
- Network ID range : `192.0.0` to `233.255.255`
- Public IP range : `192.0.0.0` to `233.255.255.255`
- Private IP range : `192.168.0.0` to `192.168.255.255`
- Network bits : First **24** bits
    - Number of usable networks : 2,097,150 (2<sup>(24-3)</sup> - 2)
        - `(24-3)` , because only 21 bits are used in 24 network bits
        - `-2` , because each network cannot use end with `.0` or `.255`
- Host bits: Remaining **8** bits
    - Number of usable hosts : 254 (2<sup>8</sup> - 2)
        - `-2` , because 2 addresses are reserved (Network ID and Broadcast address)
- Subnet Mask : `255.255.255.0` (24 bits)
- Broadcast Address : `XXX.XXX.XXX.255`
- Use : Small networks
- Example : Home and small businesses

`Class D` :

- First octet value range : 224 to 239
    - The first 4 bits of the first octet are always `1110`, and the remaining 28 bits are used to represent the multicast group address that interested hosts can join
- Range : `224.0.0.0` to `239.255.255.255`
- Do not have network ID and host ID divisions
- No subnet mask is defined
- Use : Multicast communication
- Example : Video streaming

`Class E` :

- First octect value range : 240 to 255
    - The first 4 bits of the first octet are always `1111`
- Range : `240.0.0.0` to `255.255.255.255`
- Do not have network ID and host ID divisions
- No subnet mask is defined
- Use : Experimental and research
- Not used for public networking

### Range of Special IP Addresses

- `169.254.0.0` to `169.254.255.255`:
    - Used as **link-local addresess** when a device cannot obtain an IP address from a DHCP server
- `172.0.0.0` to `127.255.255.255` (`172.0.0.0/8`):
    - Reserved for **loopback addresses**, used to test network functionality on the local machine
- `0.0.0.0` to `0.255.255.255` (`0.0.0.0/8`):
    - Represents the **current network** and is used during initialization before a device is assigned a valid IP address

## Classless Inter-Domain Routing (`CIDR`)

Classless Addressing or CLDR was introduced in 1993 to replace classful addressing.

CIDR is a method of IP address allocation and routing that allows more efficient use of IP addresses.
- Unlike [traditional class-based addressing](#classful-ip-addressing), CIDR allocates IP addresses based on a network prefix rather than a fixed class (A,B, or C)

### CIDR Notation

```
<IP_address>/<Prefix_Length>
```

- `<IP_address>` : Can be IPv4 or IPv6 address
- `<Prefix_Length>` : Number of bits in the network prefix
    - For IPv4 address, the range is 0 to 32 (Total: 32 bits)
    - For IPv6 address, the range is 0 to 128 (Total: 128 bits)
    - Specifies the number of consective bits from the left that are fixed for the network portion, as noted by `1`'s in the subnet mask

<br>

**Implementation Example:**

Let's say given `192.168.1.0/24`:
- `/24` means first 24 bits are the network part
- Number of host bits = 8 (32 - 24) 
    - NOTE: IPv4 has 32 bits in total
- Subnet Mask : `255.255.255.0`
    - Subnet Mask in bits: 11111111 11111111 11111111 00000000<sub>2<sub>
- Available total IP addresses : 256 (2<sup>8</sup>)
    - Total usable IP addresses : 254 (256 -2 [because `192.168.1.0` & `192.168.1.255` are not usable])
- Available IP ranges : `192.168.1.0` to `192.168.1.255`
    - Available usable IP ranges: `192.168.1.1` to `192.168.1.254`

### Why CIDR?

Classful addressing wastes IP addresses.

For example (in IPv4 classful addressing):

| Class | IPs Available | Hosts | Example Wastage |
|:---:|:---:|:---:|:---:|
| A | 2<sup>24</sup> | 2<sup>24</sup> - 2 | Too large for small orgs |
| B | 2<sup>16</sup> | 2<sup>16</sup> - 2 | Wastes 49,150 hosts for 214 needed |
| C | 2<sup>8</sup> | 2<sup>8</sup> - 2 | Small networks only |

<br>

**Problem:** Organizations often need a number of hosts that do not match class sizes, leading to wastage

**Solution:** CIDR allows **flexible block allocation** matching exact requirements

## Types of IP Address

IP addresses can be classified in several ways based on their structure, purpose, and the type of network they are used in.

### Based on `Addressing Scheme` (IPv4 vs IPv6)

1) **IPv4**

    - The most common form of IP address

    - Consists of four sets of numbers separated by dots, where each set of numbers can range from 0 to 255

        - This format can support over 4 billion unique addresses

        - IPv4 address is broken down into 4 octets as shown in the sample diagram below, where each octet represents 8 bits or a byte, can take a value from 0 to 255 [2<sup>8</sup> = 256 combinations]

        <img src="./images/IPv4_Address_Format.png" alt="IPv4 Address Format">
    
    - Each part of the IP address can indicate various aspects of the network configuration, from the network itself to the specific device within that network

        - For most cases, the network part of the address is represented by the first one to three octets, while the remaining section identifies the host (device)

2) **IPv6**

    - Created to deal with shortage of IPv4 addresses

    - Use 128 bits instead of 32, offering a vastly greater number of possible addresses

    - These addresses are expressed as 8 groups of four hexademical digits, where each group representing 16 bits and seperated by colon (`:`)

For more detailed information on the comparison, may refer to this <a href="https://www.geeksforgeeks.org/computer-networks/differences-between-ipv4-and-ipv6/">article</a>.

### Based on `Usage` (Public VS Private)

1) **Public IP Addresses**

    - Assigned to every device that directly accesses the internet

    - Unique across the entire internet

    - Key characteristics and uses of public IP addresses:

        - **Uniqueness:** 
        
            - Each public IP address is globally unique 
            - No two devices on the internet can have the same public IP address at the same time.

        - **Accessibility:**

            - Devices with a public IP address can be accessed directly from anywhere on the internet, assuming no firewall or security settings block the address

        - **Assigned by ISPs:**

            - Public IP addresses are assigned by Internet Service Providers (ISPs)

            - When you connect to the internet through an ISP, your device or router receives a public IP address

        - **Types:**

            - Public IP addresses can be static (permanently assigned to a device) or dynamic (temporary assigned and can change over time)

2) **Private IP Addresses**

    - Used within private networks (such as home networks, office networks, etc) and are not routable on the internet

    - Devices with private IP addresses cannot directly communicate with devices on the internet without a translating mechanism like a router performing Network Address Translation (NAT)

    - Key features of private IP addresses:

        - **Not globally unique:**

            - Private IP addresses are only required to be unique within their own network

            - Different private networks can use the same range of IP addresses without conflict

        - **Local communication:**

            - These addresses are used for communication between devices within the same network

            - They cannot be used to communicate directly with devices on the internet

        - **Defined ranges:**

            - The Internet Assigned Numbers Authority (IANA) has reserved specific IP address ranges for private use:

                - **IPv4:**

                    - 10.0.0.0 to 10.255.255.255 [Class A]
                    - 172.16.0.0 to 172.31.255.255 [Class B]
                    - 192.168.0.0 to 192.168.255.255 [Class C]

                - **IPv6:**

                    - Addresses starting with FD or FC

### Based on `Assignment Method` (Static VS Dynamic)

1) **Static IP Addresses**

    - Permanently assigned to a device, typically important for servers or devices that need a constant address

    - Reliable for network services that require regular access such as websites, remote management

2) **Dynamic IP Addresses**

    - Temporarily assigned from a pool of available addresses by the Dynamic Host Configuration Protocol (DHCP)

    - Cost-effective and efficient for providers, perfect for consumer devices that do not require permanent addresses

For more information on the comparison, please refer to this <a href="https://www.geeksforgeeks.org/computer-networks/difference-between-static-and-dynamic-ip-address/">article</a>

## Appendix

Reference link:

- <a href="https://www.geeksforgeeks.org/computer-science-fundamentals/what-is-an-ip-address/">What is an IP Address?</a>