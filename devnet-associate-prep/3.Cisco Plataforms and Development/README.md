# Describe the capabilities of Cisco network management platforms and APIs (Meraki, Cisco DNA Center, ACI, Cisco SD-WAN, and NSO)

# Meraki (Management for small business)

Sandbox: https://devnetsandbox.cisco.com/RM/Diagram/Index/a9487767-deef-4855-b3e3-880e7f39eadc?diagramType=Topology

- Cloud Platform
- Report back to controller in the Cloud
- No configuration directly in Meraki device
- Easy s2s VPN
- One login to manage all the equipment

- Dashboard API
- Scanning API 
- Captive Portal API: Guest connection to Wifi
- Webhooks

Organizations > Networks > Devices

## Dashboard API
    - Check Enable access, get key.
    - API key query param : X-Cisco-Meraki-API-Key
    - endpoint : https://dashboard.meraki.com/api/v0/organizations
    - RESTFul API
    - HTTPs

# ACI (Management for datacenters)

## Nexus

    Sandbox: https://devnetsandbox.cisco.com/RM/Diagram/Index/dae38dd8-e8ee-4d7c-a21c-6036bed7a804?diagramType=Topology

    - For datacenters
    - Runs Linux -> NX-OS
    - NX-API custom API no NETCONF, RESTCONF
        - NX-API CLI (OLD)
            - Accessed over HTTP/HTTPs
            - Not RESTFul API
            - Only POST
            - Enabling NX-API:
                - "feature nxapi"
        - NX-API REST (NEW)
            - Object Model : Management Information tree
            - root layer : sys
            - visore: doc for NX-API REST

- Nexus 9000 series
- VXLAN on IS-IS : Layer 2 information carried in the Layer3 packet from one device to another.
- APIC controllers are servers which are brains of the model

- Universal
    - Tenant Common
        - Networking (Actual physical network conf)
            - VRFs
            - Bridge Domains
            - Subnets
            - External Networks
        - Policy
            - Application Profiles
            - EPGs (End Point Groups):
                Represents same kind of servers
            - Contracts
                Enable connectivity between Devices
            - Filters
    - Tenant A
        - Networking (Actual physical network conf)
            - VRFs
            - Bridge Domains
            - Subnets
            - External Networks
        - Policy
            - Application Profiles
            - EPGs (End Point Groups):
                Represents same kind of servers
            - Contracts
                Enable connectivity between Devices
            - Filters

Sandbox: https://devnetsandbox.cisco.com/RM/Diagram/Index/5a229a7c-95d5-4cfd-a651-5ee9bc1b30e2?diagramType=Topology

- REST API, COBRA SDK, ACI TOOLKIT


# Cisco DNA Center (Management for enterprise)

Reference: https://www.youtube.com/watch?v=hzsmoY2xdjQ

- Catalyst 9000 series
- Automating campuses
- 5 Applications:
    - Design
    - Policy
    - Provision
    - Assurance
    - Platform

Northbound - Intent API
Southbound - Mutivendor SDK (infrastructure)
Eastbound - Cisco devices (Meraki, Stealthwatch)
Westbound - 3rd party solutions

Sandbox: https://devnetsandbox.cisco.com/RM/Diagram/Index/c3c949dc-30af-498b-9d77-4f1c07d835f9?diagramType=Topology

# CISCO SD-WAN

Reference: https://www.cisco.com/c/en_in/solutions/enterprise-networks/sd-wan/demos/walk-through.html#~stickynav=1
           https://www.youtube.com/watch?v=isMnWZqAh0k

vManage: API end point, GUI frontend. Frontend which we configure.
vSmart Controller: Controller: Brains of the operation.
vBond: initiates the bring up process of every vEdge device
vEdge: End Devices

# NSO (Network Service Orchestrator)

- Used to automate network devices
- GUI, REST API, Python API
- Used by Service Providers
- Can be used by legacy equipments

#

# Describe the capabilities of Cisco compute management platforms and APIs (UCS Manager, UCS Director, and Intersight)

# UCS (Unified Computing Server):

# Intersight

Sandbox: https://devnetsandbox.cisco.com/RM/Diagram/Index/a63216d2-e891-4856-9f27-309ca61ec862?diagramType=Topology

- JSON
- Cloud Server
- Similar to Meraki - for compute engines
- REST 
- Supports ucs as well as hyperflex infra

# UCS Manager

Sandbox: https://devnetsandbox.cisco.com/RM/Diagram/Index/3323b7b0-b70b-4b1e-a929-6bdbff3aac8a?diagramType=Topology

- RPC-Based
- XML
- UCSMSDK - Python SDK
- PowerTool - Powershell SDK

# UCS Director

Sandbox: https://devnetsandbox.cisco.com/RM/Diagram/Index/3323b7b0-b70b-4b1e-a929-6bdbff3aac8a?diagramType=Topology

- Running the Data Center
- Regardless of the platform
- REST API
- XML or JSON

#

# Describe the capabilities of Cisco collaboration platforms and APIs (Webex Teams, Webex devices, Cisco Unified Communication Manager including AXL and UDS interfaces, and Finesse)

# Webex Teams

- Like Slack, Microsoft Teams
- Creating teams, rooms, sending messages using python
- Python SDK webexteamssdk

# Webex devices

- REST X-API

# Cisco Unified Communication Manager including AXL and UDS interfaces, and Finesse

- Cisco Unified Communication Manager: VOIP Operations within Cisco Colaboration
- UDS (User Data Service)
    - REST API 
        - XML
- Administrative XML (AXL)
    - Not REST
    - SOAP API
        - SOAP UI
- Cisco Finesse
    - For large call centers
    - UCCX (Unified Contact Center Express)
        - REST API
        - XML
    - Tracking calls
    - https://developer.cisco.com/docs/finesse/#!cisco-finesse-desktop-apis/cisco-finesse-desktop-apis

#

# Describe the capabilities of Cisco security platforms and APIs (Firepower, Umbrella, AMP, ISE, and ThreatGrid)

# Firepower

- Firepower Devices, Firepower Threat Defense, Firepower Management Center
- Threat Centric Policies
    - Login
    - Create Policy
        - Default Policy
        - Policy ID
    - Rules
    - Delete

# Umbrella

- Protection on the go
- For remote machines
- Cloud security Platform

# AMP (Advanced Malware Protection)

- Checks for malware in the network
- Can be installed on FP devices or end devices
- Can be used to produce a list of vulnerable software on user devices using firepower api

# ISE (Identity Service Engine)

- Provides auth serices to the network
- To connect to the network one has to be authenticated by the ISE

# ThreatGrid

- Learn what malware is trying to do
- Separate machine

# 

# Describe the device level APIs and dynamic interfaces for IOS XE and NX-OS

## NX-OS

Sandbox: https://devnetsandbox.cisco.com/RM/Diagram/Index/dae38dd8-e8ee-4d7c-a21c-6036bed7a804?diagramType=Topology

- For datacenters
- Runs Linux -> NX-OS
- NX-API custom API no NETCONF, RESTCONF
    - NX-API CLI (OLD)
        - Accessed over HTTP/HTTPs
        - Not RESTFul API
        - Only POST
        - Enabling NX-API:
            - "feature nxapi"
    - NX-API REST (NEW)
        - Object Model : Management Information tree
        - root layer : sys
        - visore: doc for NX-API REST

## IOS-XE (Covered in 3.8)

YANG
NETCONF
RESTCONF

Default data encoding: XML