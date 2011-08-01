# Minimum required version
cmake_minimum_required(VERSION 2.6)

# Define the project name.
project ( Mantid )

# Add the path to our custom 'find' modules
set ( CMAKE_MODULE_PATH "${CMAKE_SOURCE_DIR}/Build/CMake")

# Find Python
find_package( PythonLibs )

# Generate the library target
set ( BUILD_SHARED_LIBS On )

# Send libraries to common place
set ( CMAKE_RUNTIME_OUTPUT_DIRECTORY ${PROJECT_BINARY_DIR}/bin )
set ( CMAKE_LIBRARY_OUTPUT_DIRECTORY ${PROJECT_BINARY_DIR}/bin )

################################################################################
# Subprojects
################################################################################
add_subdirectory ( mantidplotlib ) 
add_subdirectory ( python )

