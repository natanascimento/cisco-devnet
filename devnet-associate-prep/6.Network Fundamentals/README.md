# Network Fundamentals

# Describe the purpose and usage of MAC addresses and VLANs

## MAC Addresses:

- Layer two identifiers
- 12 hexadecimals
- OUI and Unique identifiers 
- Sending frames 

## VLAN:

- Breaks the broadcast domain
- Layer 2 feature

# Describe the purpose and usage of IP addresses, routes, subnet mask / prefix, and gateways

## IP addresses

- Layer 3 identifier

## Routes

- Gain information of distant networks

## Subnet mask / prefix

- Identifies a network
- Network and Host network

## Gateways

- where to transfer the packets
- Default routes

# Describe the function of common networking components (such as switches, routers, firewalls, and load balancers)

## Switches:
    - L2 Switching
## Routers:
    - L3 Routing
## Firewalls:
    - Default is to block all packets
    - Types:
        - Packet Filtering (L2, L3, L4)
        - Stateful Filtering
        - New Gen Fire Wall (L5)
## Load balancers:
    - Balance data load between servers/devices

# Interpret a basic network topology diagram with elements such as switches, routers, firewalls, load balancers, and port values

## Management Plane:
- Managing network devices
- SNMP, NETCONF, SSHn

## Data Plane:
- Actually do forwarding

## Control Plane:
- How to forward 
- Routing protocols
- MAC address table

# Describe the functionality of these IP Services: DHCP, DNS, NAT, SNMP, NTP

## DHCP (Dynammic Host Configuration Protocol):
    - Handing out IPs to the devices in the network
    - Uses UDP
    - Port 67: Used by the server
    - Port 68: Used by the client
## DNS (Domain Name Server):
    - Conversion of domain name to IP addresses
    - Used UDP
    - Port 53
    - Records:
        - A: Known as a DNS host record, stores a hostname and its corresponding IPv4 address
        - AAAA: Stores a hostname and its corresponding IPv6 address.
        - CNAME: Can be used to alias a hostname to another hostname. When a DNS client requests a record that contains a CNAME, which points to another hostname.
        - MX Records: Specifies an SMTP email server for the domain, used to route outgoing emails to an email server.
        - NS Records: Specifies that a DNS Zone.
## NAT (Network Address Translation):
    - Converts local IPs to routable public IP addresses
## SNMP (Simple Network Management protocol):
    - Used for management of network devices
    - Port: 161
## NTP (Network Time Protocol): 
    - Used for clock sync b/w systems
    - Stratum levels
    - Uses UDP
    - Port 123

# Recognize common protocol port values (such as, SSH, Telnet, HTTP, HTTPS, and NETCONF)

SSH: 22
Telnet: 23
HTTP: 80
HTTPS: 443
NETCONF: 830

# Recognize common protocol port values (such as, SSH, Telnet, HTTP, HTTPS, and NETCONF)

NAT problem, Transport Port blocked, proxy, and VPN
Firewalls, IPS, ACLs
MTUs
Loopback Interfaces
Insecure Protocols (HTTP, Telnet)