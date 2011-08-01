# Regenerate this structure in the target directory

# Widgets
add_subdirectory( widgets )

# The files to copy
set ( PY_FILES 
  mantidplot.py 
)

set ( DEST_DIR ${CMAKE_LIBRARY_OUTPUT_DIRECTORY}/${CMAKE_CFG_INTDIR} )

# Now us
set ( PYTHON_INSTALL_FILES "" )
foreach ( PYFILE ${PY_FILES} )
  add_custom_command ( 
    OUTPUT ${DEST_DIR}/${PYFILE}
    DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/${PYFILE}
    COMMAND ${CMAKE_COMMAND} ARGS -E copy_if_different 
    ${CMAKE_CURRENT_SOURCE_DIR}/${PYFILE}
    ${DEST_DIR}/${PYFILE}
    )
set ( PYTHON_INSTALL_FILES ${PYTHON_INSTALL_FILES} ${DEST_DIR}/${PYFILE} )
endforeach ( PYFILE )

# "Dummy" target
add_custom_target ( mantidplot ALL 
  SOURCES ${PY_FILES} 
  DEPENDS ${PYTHON_INSTALL_FILES}
  )
