find_package(pybind11 CONFIG REQUIRED)

pybind11_add_module(hello_py wrapper.cpp)

if (MSVC AND MSVC_VERSION GREATER_EQUAL 1914)
  target_compile_options(hello_py PUBLIC "/Zc:__cplusplus")
endif()

target_link_libraries(hello_py PRIVATE hello)

set(PYTHON_PKG_DIR ${CMAKE_BINARY_DIR}/python_package)

install(FILES ${CMAKE_CURRENT_SOURCE_DIR}/setup.py DESTINATION ${PYTHON_PKG_DIR})
install(FILES ${CMAKE_CURRENT_SOURCE_DIR}/__init__.py DESTINATION ${PYTHON_PKG_DIR}/hello_py)
install(TARGETS hello DESTINATION ${PYTHON_PKG_DIR}/hello_py)
install(TARGETS hello_py DESTINATION ${PYTHON_PKG_DIR}/hello_py)