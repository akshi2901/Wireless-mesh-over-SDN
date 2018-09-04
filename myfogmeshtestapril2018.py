#!/usr/bin/python

'Shabir Ali: Wireless Fog-Mesh'

from mininet.node import RemoteController
from mininet.log import setLogLevel, info
from mininet.wifi.node import OVSKernelAP
from mininet.wifi.link import wmediumd
from mininet.wifi.cli import CLI_wifi
from mininet.wifi.net import Mininet_wifi

def topology():
    "Create a network."
    net = Mininet_wifi(controller=RemoteController, accessPoint=OVSKernelAP,
                  link=wmediumd, enable_interference=True)

    print "*** Creating nodes"
    sta1 = net.addStation('sta1', mac='00:00:00:00:00:02', position='50,50,0', ip='10.0.0.1/16', range=80)
    sta2 = net.addStation('sta2', mac='00:00:00:00:00:03', position='150,50,0', ip='10.0.0.2/16', range=80)
    sta3 = net.addStation('sta3', mac='00:00:00:00:00:04', position='250,300,0', ip='10.0.0.3/16', range=80)    
    sta4 = net.addStation('sta4', mac='00:00:00:00:00:05', position='350,200,0', ip='10.0.0.4/16', range=80)
    #sta5 = net.addStation('sta5', mac='00:00:00:00:00:06', position='150,50,0', ip='10.0.0.5/16', range=80)
    #sta6 = net.addStation('sta6', mac='00:00:00:00:00:07', position='150,150,0', ip='10.0.0.6/16', range=80) 
    #sta7 = net.addStation('sta7', mac='00:00:00:00:00:08', position='150,250,0', ip='10.0.0.7/16', range=80)
    #sta17 = net.addStation('sta17', mac='00:00:00:00:00:18', position='150,200,0', ip='10.0.0.17/16', range=80)
    #sta8 = net.addStation('sta8', mac='00:00:00:00:00:09', position='150,350,0', ip='10.0.0.8/16', range=80)
    #sta9 = net.addStation('sta9', mac='00:00:00:00:00:10', position='250,50,0', ip='10.0.0.9/16', range=80)    
    #sta10 = net.addStation('sta10', mac='00:00:00:00:00:11', position='250,150,0', ip='10.0.0.10/16', range=80)
    #sta11 = net.addStation('sta11', mac='00:00:00:00:00:12', position='250,250,0', ip='10.0.0.11/16', range=80)
    #sta12 = net.addStation('sta12', mac='00:00:00:00:00:13', position='250,350,0', ip='10.0.0.12/16', range=80)
    #sta13 = net.addStation('sta13', mac='00:00:00:00:00:14', position='350,50,0', ip='10.0.0.13/16', range=80)
    #sta14 = net.addStation('sta14', mac='00:00:00:00:00:15', position='350,150,0', ip='10.0.0.14/16', range=80)
    #sta15 = net.addStation('sta15', mac='00:00:00:00:00:16', position='350,250,0', ip='10.0.0.15/16', range=80)
    #sta16 = net.addStation('sta16', mac='00:00:00:00:00:17', position='350,350,0', ip='10.0.0.16/16', range=80)
    
    ap1 = net.addAccessPoint('ap1', wlans=2, type='mesh', ssid="ssid1,", position='100,100,0', mode="g", channel="1")
    ap2 = net.addAccessPoint('ap2', wlans=2, type='mesh', ssid="ssid2,", position='300,250,0', mode='g', channel='1')
    mr1 = net.addStation('mr1', wlans=2, type='mesh', ssid="ssid3,", mode="g", channel="1", position='200,100,0')
    mr2 = net.addStation('mr2', wlans=2, type='mesh', ssid="ssid4,", mode="g", channel="1", position='250,200,0')


    #ap3 = net.addAccessPoint('ap3', wlans=2, type='mesh', ssid='ssid5,', position='200,120,0', mode="g", channel="1")
    #ap4 = net.addAccessPoint('ap4', wlans=2, type='mesh', ssid='ssid6,', position='250,210,0', mode='g', channel='5')
    #ap5 = net.addAccessPoint('ap5', wlans=2, type='mesh', ssid='ssid5,', position='200,200,0', mode='g', channel='5')
    #ap6 = net.addAccessPoint('ap6', wlans=2, type='mesh', ssid='ssid6,', position='200,300,0', mode='g', channel='5')
    #ap7 = net.addAccessPoint('ap7', wlans=2, type='mesh', ssid='ssid7,', position='300,100,0', mode='g', channel='11')
    #ap8 = net.addAccessPoint('ap8', wlans=2, type='mesh', ssid='ssid8,', position='300,200,0', mode='g', channel='11')
    #ap9 = net.addAccessPoint('ap9', wlans=2, type='mesh', ssid='ssid9,', position='300,300,0', mode='g', channel='11')

    
    
    #ap1.setMAC('40:00:00:00:00:18', ap9.params['mac'][0])
    #ap1.setRange(110,ap1.params['wlan'][1])
    #ap2.setRange(110,ap2.params['wlan'][0])
    #ap3.setRange(110,ap3.params['wlan'][0])
    #ap4.setRange(110,ap4.params['wlan'][0])
    #ap5.setRange(110,ap5.params['wlan'][0])
    #ap6.setRange(110,ap6.params['wlan'][0])
    #ap7.setRange(110,ap7.params['wlan'][0])
    #ap8.setRange(110,ap8.params['wlan'][0])
    #ap9.setRange(110,ap9.params['wlan'][0])
    
    c0 = net.addController('c0', controller=RemoteController, ip='172.31.132.232', port=6653)
    
    print "***configuring propagation model"
    net.propagationModel(model="logDistance", exp=3.6)
   
    print "*** Configuring wifi nodes"
    net.configureWifiNodes()

    print "*** Associating Stations"
    net.addMesh(ap1, intf='ap1-wlan2', ssid='mesh-ssid', channel=1)
    net.addMesh(ap2, intf='ap2-wlan2', ssid='mesh-ssid', channel=1)
    net.addMesh(mr1, intf='mr1-wlan0', ssid='mesh-ssid', channel=1)
    net.addMesh(mr2, intf='mr2-wlan0', ssid='mesh-ssid', channel=1)
    #net.addMesh(ap3, intf='ap3-wlan2', ssid='mesh-ssid', channel=1)
    #net.addMesh(ap4, intf='ap4-wlan2', ssid='mesh-ssid', channel=1)
    #net.addLink(ap5, intf='ap5-wlan2', cls=mesh, ssid='mesh-ssid', channel=5)
    #net.addLink(ap6, intf='ap6-wlan2', cls=mesh, ssid='mesh-ssid', channel=5)
    #net.addLink(ap7, intf='ap7-wlan2', cls=mesh, ssid='mesh-ssid', channel=5)
    #net.addLink(ap8, intf='ap8-wlan2', cls=mesh, ssid='mesh-ssid', channel=5)
    #net.addLink(ap9, intf='ap9-wlan2', cls=mesh, ssid='mesh-ssid', channel=5)
       
    print """plotting graph"""
    net.plotGraph(max_x=400, max_y=400)
    
    #"""association control"""
    net.associationControl('ssf')

    print """Seed"""
    net.seed(1)

    """ *** Available models:
    
                RandomWalk, TruncatedLevyWalk, RandomDirection, RandomWayPoint, GaussMarkov
    *** Association Control (AC) - mechanism that optimizes the use of the APs:
                llf (Least-Loaded-First)
                ssf (Strongest-Signal-First)"""
    #net.startMobility(time=0, model='RandomWayPoint', max_x=120, max_y=120, min_v=0.3, max_v=0.5)
    print "*** Starting network"
    net.build()
    c0.start()
    ap1.start([c0])
    ap2.start([c0])
    #ap3.start([c0])
    #ap4.start([c0])
    #ap5.start([c0])
    #ap6.start([c0])
    #ap7.start([c0])
    #ap8.start([c0])
    #ap9.start([c0])
    #ap1.cmd(" ifconfig ap1-mp2 10.0.0.51")
    #ap2.cmd(" ifconfig ap2-mp2 10.0.0.52")
    #ap3.cmd(" ifconfig ap3-wlan1 172.31.0.3/16")
    #ap4.cmd(" ifconfig ap4-wlan1 172.31.0.4/16")
    #ap5.cmd(" ifconfig ap5-wlan1 172.31.0.5/16")
    #ap6.cmd(" ifconfig ap6-wlan1 172.31.0.6/16")
    #ap7.cmd(" ifconfig ap7-wlan1 172.31.0.7/16")
    #ap8.cmd(" ifconfig ap8-wlan1 172.31.0.8/16")
    #ap9.cmd(" ifconfig ap9-wlan1 172.31.0.9/16")
    #ap1.cmd(" iw dev ap1-wlan1 interface add mon0 type monitor")
  #  ap1.cmd("ifconfig mon0 up")
    
    info("*** Running CLI\n")
    CLI_wifi(net)
    
    print "*** Stopping network"
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    topology()
