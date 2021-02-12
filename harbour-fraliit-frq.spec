Name:          harbour-fraliit-frq
Version:       0.1.0
Release:       2
Summary:       FrançaisQ
Requires:      sailfish-version >= 2.1.0, harbour-fraliit-common >= 0.1.0-1
Group:         System/Tools
Vendor:        fravaccaro
Distribution:  SailfishOS
Packager:      fravaccaro <fravaccaro@jollacommunity.it>
URL:           www.jollacommunity.it
License:       GPLv3

%description
Qwerty French keyboard with arrows and numbers.

%files
/usr/share/maliit/plugins/com/jolla/layouts/frq.conf
/usr/share/maliit/plugins/com/jolla/layouts/frq.qml
/usr/share/maliit/plugins/com/jolla/layouts/frq_arw.conf
/usr/share/maliit/plugins/com/jolla/layouts/frq_arw.qml
/usr/share/maliit/plugins/com/jolla/layouts/frq_123.conf
/usr/share/maliit/plugins/com/jolla/layouts/frq_123.qml

%post
systemctl-user restart maliit-server.service

%postun
if [ $1 = 0 ]; then
    // Do stuff specific to uninstalls
rm /usr/share/maliit/plugins/com/jolla/layouts/frq.conf
rm /usr/share/maliit/plugins/com/jolla/layouts/frq.qml
rm /usr/share/maliit/plugins/com/jolla/layouts/frq_arw.conf
rm /usr/share/maliit/plugins/com/jolla/layouts/frq_arw.qml
rm /usr/share/maliit/plugins/com/jolla/layouts/frq_123.conf
rm /usr/share/maliit/plugins/com/jolla/layouts/frq_123.qml
systemctl-user restart maliit-server.service
else
if [ $1 = 1 ]; then
    // Do stuff specific to upgrades
echo "Upgrading"
systemctl-user restart maliit-server.service
fi
fi

%changelog
* Sat Jun 9 2018 0.1.0-1
- First build.
