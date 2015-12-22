Name:           ros-jade-polar-scan-matcher
Version:        0.3.1
Release:        0%{?dist}
Summary:        ROS polar_scan_matcher package

Group:          Development/Libraries
License:        GPL
URL:            http://ros.org/wiki/polar_scan_matcher
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-geometry-msgs
Requires:       ros-jade-roscpp
Requires:       ros-jade-sensor-msgs
Requires:       ros-jade-tf
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-geometry-msgs
BuildRequires:  ros-jade-roscpp
BuildRequires:  ros-jade-sensor-msgs
BuildRequires:  ros-jade-tf

%description
A wrapper around Polar Scan Matcher by Albert Diosi and Lindsay Kleeman, used
for laser scan registration.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Mon Dec 21 2015 Ivan Dryanovski <ccnyroboticslab@gmail.com> - 0.3.1-0
- Autogenerated by Bloom

* Sat Oct 17 2015 Ivan Dryanovski <ccnyroboticslab@gmail.com> - 0.2.1-0
- Autogenerated by Bloom
