Name:           ros-kinetic-multirobot-map-merge
Version:        2.0.0
Release:        1%{?dist}
Summary:        ROS multirobot_map_merge package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/multirobot_map_merge
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-geometry-msgs
Requires:       ros-kinetic-map-msgs
Requires:       ros-kinetic-nav-msgs
Requires:       ros-kinetic-opencv3
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-tf2-geometry-msgs
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-geometry-msgs
BuildRequires:  ros-kinetic-map-msgs
BuildRequires:  ros-kinetic-nav-msgs
BuildRequires:  ros-kinetic-opencv3
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-roslaunch
BuildRequires:  ros-kinetic-rosunit
BuildRequires:  ros-kinetic-tf2-geometry-msgs

%description
Merging multiple maps without knowledge of initial positions of robots.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Sun Mar 26 2017 Jiri Horner <laeqten@gmail.com> - 2.0.0-1
- Autogenerated by Bloom

* Sun Mar 26 2017 Jiri Horner <laeqten@gmail.com> - 2.0.0-0
- Autogenerated by Bloom

