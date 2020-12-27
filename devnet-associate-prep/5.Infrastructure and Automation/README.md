# Infrastructure and Automation

# Model Driven Programmability

<div class='img-mdp-stack' align="center">
    <h2>MDP Stack</h2> 
    <img src="https://developer.cisco.com/learning/posts/files/why-mdp/assets/images/standard_device_interface.jpg" alt="Docker" width="300">
</div>


# Yang data model

YANG data models are available and being developed that represent a "Network Service" to describe a network construct that spans across an entire network.

A YANG data model that can be used for communication between customers and network operators and to deliver a Layer 3 Provider Provisioned VPN service.

<div class='img-mdp-stack' align="center">
    <img src="https://developer.cisco.com/learning/posts/files/why-mdp/assets/images/yang_models1.jpg" alt="Docker" width="300">
</div>


# Roles of network Simulation and test tools 

Virl (Virtual Internet Routing Lab)
- Network simulation tool

pyATS
- Python testing library
- With genie used for network testing

# Infrastructure as a Code

- Rather than configuring devices itself through cli and/or GUI, systems and networks are deployed by code and scripts.

# Automation tools

Ansible:
    - Master only. No client software needed.

Puppet:
    - Master-Agent architecture. Client software needed.

Chef:
    - Master-Agent architecture. Also requires workstation. 

# Workflow being automated by an Ansible playbook

ansible.cfg & hosts -> /etc/ansible/

hosts ->
    - Define hosts
    - eg:
        [nsox]
        172.16.30.101
    - childrens:
        [childgroup2]
        host1
        host2
        
        [childgroup1]
        host2
        host3
        
        [parent1:children]
        childgroup1
        childgroup2

group_vars
    - dir for groups
    - yaml structure

host_vars
    - dir for hosts
    - yaml structure

How to run playbooks
    - ansible-playbook

# Unified Diff

diff first.txt second.txt -u

------ OUTPUT ------

--- first.txt   2020-12-27 00:04:03.057673600 -0300
+++ second.txt  2020-12-27 00:03:57.857377500 -0300
@@ -1,4 +1,5 @@
 hello my name is natan
-this is a file
-bla bla bla
+this is not a file
+bla bla Bla
+extra line
 another line
\ No newline at end of file

# Principles and benefits of a code review process

Good code reviews are the bar that all of us should strive for. They cover common and easy to follow best practices that any team can get started with, while ensuring high-quality and helpful reviews for the long term.

Better code reviews are where engineers keep improving how they do code reviews. These code reviews look at the code change in the context of the codebase, of who is requesting it and in what situation. These reviews adjust their approach based on the context and situation. The goal not only being a high-quality review, but also to help the developers and teams requesting the review to be more productive.