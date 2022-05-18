# easy-openvpn

Make managing your OpenVPN servers on Debian just a bit easier. Supports automated server setup and key management.

## Dependencies

Before you can use easy-openvpn, run the following:

```
sudo apt-get install -y easy-rsa git openvpn python3
```

## Usage

Once you have installed the required dependencies, simply clone this repo and run `./install.sh`. You will then be able to access easy-openvpn as `ovpn`.