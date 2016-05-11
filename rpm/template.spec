Name:           ros-jade-explore-lite
Version:        1.0.0
Release:        0%{?dist}
Summary:        ROS explore_lite package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/explore_lite
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-actionlib
Requires:       ros-jade-actionlib-msgs
Requires:       ros-jade-costmap-2d
Requires:       ros-jade-navfn
Requires:       ros-jade-roscpp
Requires:       ros-jade-tf
BuildRequires:  ros-jade-actionlib
BuildRequires:  ros-jade-actionlib-msgs
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-costmap-2d
BuildRequires:  ros-jade-geometry-msgs
BuildRequires:  ros-jade-map-msgs
BuildRequires:  ros-jade-move-base-msgs
BuildRequires:  ros-jade-nav-msgs
BuildRequires:  ros-jade-navfn
BuildRequires:  ros-jade-roscpp
BuildRequires:  ros-jade-roslaunch
BuildRequires:  ros-jade-std-msgs
BuildRequires:  ros-jade-tf
BuildRequires:  ros-jade-visualization-msgs

%description
Lightweight frontier-based exploration.

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
        -DCMAKE_INSTALL_LIBDIR="lib" \
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
* Wed May 11 2016 Jiri Horner <laeqten@gmail.com> - 1.0.0-0
- Autogenerated by Bloom

