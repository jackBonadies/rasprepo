installing raspian in headless mode

touch ssh
vim wpa_supplicant.conf
then 
country=US
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev 
update_config=1

network={
       ssid="YourNetworkSSID"
       psk="Your Network's Passphrase"
       key_mgmt=WPA-PSK
    }

/etc/dhcpcd.conf edited for static ip
generate public key on rasppi and add it to github.com
then change remote to git+ssh://url
