# Include Qt 
find_package ( Qt4 COMPONENTS QtCore QtGui REQUIRED )
include ( UseQt4 )

# sip
find_package ( SIP REQUIRED )
# PyQt4
find_package ( PyQt4 REQUIRED )
separate_arguments ( PYQT4_SIP_FLAGS )

# Set the src cpp files
set ( SRC_FILES 
  mainwindow.cpp 
)

# Header files
set ( HDR_FILES
  mainwindow.h
)

# Headers known to sip
set ( SIP_HDRS
  mainwindow.h
)

# Spec file for sip
set ( SIP_SPEC ${CMAKE_CURRENT_SOURCE_DIR}/mantidplotlib.sip )
# Generated source file
set ( SIP_SRC sipmantidplotlibpart0.cpp )


# Generate sip files
add_custom_command ( OUTPUT ${SIP_SRC}
                     COMMAND ${SIP_EXECUTABLE}
                          -I ${PYQT4_SIP_DIR} ${PYQT4_SIP_FLAGS}
                          -c ${CMAKE_CURRENT_BINARY_DIR} -j1 -w 
                          ${SIP_SPEC}
                     DEPENDS ${SIP_SPEC} ${SIP_HDRS}
                     COMMENT "Generating python bindings using sip"
)

set ( SRC_FILES ${SRC_FILES} ${SIP_SRC} )

# Needed for sip generated files to find includes here
include_directories ( ${CMAKE_CURRENT_SOURCE_DIR} )
include_directories ( ${PYTHON_INCLUDE_PATH} )

# Generate moc_ files
qt4_wrap_cpp ( MOCCED_FILES ${HDR_FILES} )

set ( CMAKE_SHARED_LIBRARY_PREFIX )
# Add the target for this directory
add_library ( mantidplotlib ${SRC_FILES} ${INC_FILES} ${MOCCED_FILES} )
if ( WIN32 )
  set_target_properties ( mantidplotlib PROPERTIES SUFFIX .pyd )
elseif ( APPLE )
# and in .so on the Mac
  set_target_properties ( mantidplotlib PROPERTIES SUFFIX .so )
endif ()

# Additonal libraries
target_link_libraries ( mantidplotlib ${QT_LIBRARIES} ${PYTHON_LIBRARIES} )
