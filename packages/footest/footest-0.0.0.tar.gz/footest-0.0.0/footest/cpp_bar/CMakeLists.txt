#-------------------------------------------------------------------------------
# Build C++ module footest.bar
#   > cd _build
# For a clean build:
#   > rm -rf * 
# Configure:
#   > cmake ..
# build and install the .so file:
#   > make install
#-------------------------------------------------------------------------------
cmake_minimum_required(VERSION 2.8.12)
project(bar CXX)

find_package(pybind11 CONFIG REQUIRED)
pybind11_add_module(bar bar.cpp)

install(FILES       "_build/bar${PYTHON_MODULE_EXTENSION}"
        DESTINATION "${CMAKE_CURRENT_SOURCE_DIR}/.."
       )
