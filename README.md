# TamagochiApp
Tamagochi that is being fed your hours of work! 
Building your Kivy App for Android
Requirements

You need:

    A reasonably modern Android device with a USB port
    A micro USB cable
    A fast internet connection
    Plenty of disk space
    Lots of RAM
    Patience and a few hours of your time

Also:

    Linux

    Python 2.7

    A few distribution packages for compilers, build tools and libraries (C/Java):

    https://buildozer.readthedocs.io/en/latest/installation.html#targeting-android

Buildozer

https://github.com/kivy/buildozer

Installation:

mkvirtualenv -p python2.7 buildozer
pip install "Cython==0.25"
# Important: install Cython and Kivy in two steps!
pip install "kivy==1.10.0"   # for testing on build host
git clone https://github.com/kivy/buildozer.git
cd buildozer
wget -O buildozer-android-project-properties.diff https://git.io/v914C
patch -p1 -i buildozer-android-project-properties.diff
sudo python setup.py install

For installation pre-requirements, please check:

https://kivy.org/docs/installation/installation-linux.html#installation-in-a-virtual-environment
Building your app

Example project:
https://github.com/mvasilkov/kb/tree/master/1_Clock
Preparing your project

cd <yourapp>
buildozer init
$EDITOR buildozer.spec

    Set at least title, package.name, package.domain, version and author.
    If your app needs additional files besides those with extensions, which get included by default, adapt source.include_exts and/or source.include_patterns.
    If your app needs additional Python packages besides Kivy and those included by Python-for-Android by default, adapt the requirements setting.
    Change orientation if necessary.
    Uncommment icon.filename setting and adjust path to icon file.

Preparing your device

    Enable developer settings (search internet for "<device> enable developer settings").
    Enable USB debugging in the developer settings.
    Connect the device via USB to your build host.

Building the APK

Start:

buildozer android debug deploy run

... then go for lunch.

After a while an APK will have been built. buildozer then installs the APK via adb on the connected Android device and starts it.

The APK is also stored in your project below the bin directory and can be re-installed on the Android device with adb install <APK file>.
Resources

    Create a package for Android
    Kivy homepage and on PyPI
    Kivy Blueprints

