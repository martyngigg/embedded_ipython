# Minimum required version
cmake_minimum_required(VERSION 2.6)

# Define the project name.
project ( EmbeddedIPython )

if ( NOT CMAKE_CONFIGURATION_TYPES )
  if ( NOT CMAKE_BUILD_TYPE )
    message ( STATUS "No build type selected, default to Release." )
    set( CMAKE_BUILD_TYPE Release CACHE STRING "Choose the type of build." FORCE )
    # Set the possible values of build type for cmake-gui
    set_property(CACHE CMAKE_BUILD_TYPE PROPERTY STRINGS "Debug" "Release"
      "MinSizeRel" "RelWithDebInfo")
  else ()
    message ( STATUS "Build type is " ${CMAKE_BUILD_TYPE} )
  endif ()
endif()

# Add the path to our custom 'find' modules
set ( CMAKE_MODULE_PATH "${CMAKE_SOURCE_DIR}/Build/CMake")

# Find Python
if ( WIN32 )
  set ( THIRD_PARTY "C:/MantidProject/svn/trunk/Code/Third_Party" )
  set ( CMAKE_INCLUDE_PATH "${THIRD_PARTY}/include" )

  if ( CMAKE_CL_64 )
    message ( STATUS "64 bit compiler found" )
    set ( CMAKE_LIBRARY_PATH "${THIRD_PARTY}/lib/win64" )
    set ( BOOST_LIBRARYDIR "${THIRD_PARTY}/lib/win64" )
  else()
    message ( STATUS "32 bit compiler found" )
    set ( CMAKE_LIBRARY_PATH "${THIRD_PARTY}/lib/win32" )
    set ( BOOST_LIBRARYDIR  "${THIRD_PARTY}/lib/win32" )
  endif()
  ###########################################################################
  # On Windows we want to bundle Python. The necessary libraries are in
  # Third_Party/lib/win{BITNESS}/Python27
  ###########################################################################
  ## Set the variables that FindPythonLibs would set
  set ( PYTHON_INCLUDE_DIRS "${CMAKE_INCLUDE_PATH}/Python27" "${CMAKE_INCLUDE_PATH}/Python27/Include" )
  set ( PYTHON_LIBRARIES "${CMAKE_LIBRARY_PATH}/Python27/python27.lib" )
  set ( PYTHON_DEBUG_LIBRARY "${CMAKE_LIBRARY_PATH}/Python27/python27_d.lib" )
  set ( PYTHON_DEBUG_LIBRARIES ${PYTHON_DEBUG_LIBRARY} )
  ## Add debug library into libraries variable
  set ( PYTHON_LIBRARIES optimized ${PYTHON_LIBRARIES} debug ${PYTHON_DEBUG_LIBRARIES} )
  ## The executable
  set ( PYTHON_EXECUTABLE "${CMAKE_LIBRARY_PATH}/Python27/python.exe" )
  ## Add the include directory
  include_directories ( ${PYTHON_INCLUDE_DIRS} )
else () # Other systems
  find_package( PythonLibs )
endif()

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

# TODO: Copy the images folder
