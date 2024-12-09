
Project Title: Cisco Packet Tracer Static Routing Configuration

Description:
In this project we statically configure the network conection.
It involves setting up two routers and one host on each router to simulate a simple network topology. 
Static routes are configured to enable communication between the two networks.

#Steps to Configure and Verify Two Router Connections in Cisco Packet Tracer :
step-1 : First, open the cisco packet tracer desktop and select the devices given below:
Host devices: Two PCs 
Swithes: Two 2960-24TT swithes
Routers: Two 2911 Model routers
Cable : copper straight-Through cable

Ip addressing:
click on the PC device go to desktop and then select IP configuring fill the below details:
PC1 (network one):
Ipv4 : 192.168.10.2
default gateway: 192.168.10.1
subnetmask : 255.255.255.0
Pc2 (network two): 
Ipv4 : 192.168.20.2
default gateway: 192.168.20.1
subnetmask : 255.255.255.0

step-2: Router configuration 
1. Click on router one go to CLI and then change user mode to privalage mode by giving "enable" command
2. Then go to configuration mode by giving "configure terminal"
3. Configure the interface g0/1 which is connected to network one.
   (ip address 192.168.10.1 255.255.255.0)
4. No shutdown the terminal.
  (no shutdown)
5.click on router two do the configuration similarly.
  (ip address 192.168.20.1 255.255.255.0)
6.Again click on router one configure the router network similarly router two
  router one:(ip address 10.0.0.2 255.255.255.0)
  router one:(ip address 10.0.0.1 255.255.255.0)
7.Now, give the static routing

Step 5: After configuring all of the devices we need to assign the routes to the routers.

To assign static routes to the particular router:
router one : "ip router 192.168.20.0 255.255.255.0 10.0.0.2
router two : "ip router 192.168.10.0 255.255.255.0 10.0.0.1

step-6: Verifying the network by pinging the IP address of any PC. We will use the ping command to do so.
1. First, click on PC1 then Go to the command prompt
2. give the ping command. (ping <destination ip address>)

