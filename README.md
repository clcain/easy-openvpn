# easy-openvpn

Make managing your OpenVPN servers on Debian just a bit easier. Supports automated server setup and key management.

**This project is under active development. This message will be removed when easy-openvpn is ready for production use.**

## Dependencies

Before you can use easy-openvpn, ensure you have the following packages installed:

```
sudo apt-get install -y openvpn python3
```

## Usage

Once you have installed the required dependencies, simply clone this repo and run `./install.sh`. You will then be able to access easy-openvpn as `ovpn`.

Tested with Debian 11 and OpenVPN 2.4+.
