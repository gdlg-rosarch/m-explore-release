# Script generated with Bloom
pkgdesc="ROS - Lightweight frontier-based exploration."
url='http://wiki.ros.org/explore_lite'

pkgname='ros-lunar-explore-lite'
pkgver='2.1.1_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-lunar-actionlib'
'ros-lunar-actionlib-msgs'
'ros-lunar-catkin'
'ros-lunar-costmap-2d'
'ros-lunar-geometry-msgs'
'ros-lunar-map-msgs'
'ros-lunar-move-base-msgs'
'ros-lunar-nav-msgs'
'ros-lunar-roscpp'
'ros-lunar-roslaunch'
'ros-lunar-std-msgs'
'ros-lunar-tf'
'ros-lunar-visualization-msgs'
)

depends=('ros-lunar-actionlib'
'ros-lunar-actionlib-msgs'
'ros-lunar-costmap-2d'
'ros-lunar-geometry-msgs'
'ros-lunar-map-msgs'
'ros-lunar-move-base-msgs'
'ros-lunar-nav-msgs'
'ros-lunar-roscpp'
'ros-lunar-std-msgs'
'ros-lunar-tf'
'ros-lunar-visualization-msgs'
)

conflicts=()
replaces=()

_dir=explore_lite
source=()
md5sums=()

prepare() {
    cp -R $startdir/explore_lite $srcdir/explore_lite
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/lunar/setup.bash ] && source /opt/ros/lunar/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/lunar \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

