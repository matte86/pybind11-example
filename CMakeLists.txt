cmake_minimum_required(VERSION 3.14)

# Set the project name
set(PROJECT_NAME "hello")
set(${PROJECT_NAME}_VERSION 0.0.1)
project(${PROJECT_NAME} VERSION ${${PROJECT_NAME}_VERSION})

# Initialise conan stuff
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(KEEP_RPATHS)

set(CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS YES CACHE BOOL "Export all symbols")
set(CMAKE_VS_INCLUDE_INSTALL_TO_DEFAULT_BUILD 1)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/${CMAKE_INSTALL_BINDIR}")
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/${CMAKE_INSTALL_LIBDIR}")
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/${CMAKE_INSTALL_LIBDIR}")
set(CMAKE_PREFIX_PATH "${PROJECT_BINARY_DIR}")

if (MSVC)
  set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} /ignore:4099")
  set(CMAKE_SHARED_LINKER_FLAGS "${CMAKE_SHARED_LINKER_FLAGS} /ignore:4099")
  set(CMAKE_STATIC_LINKER_FLAGS "${CMAKE_STATIC_LINKER_FLAGS} /ignore:4099")
  add_compile_options("/Zc:__cplusplus")
endif()

# Set @rpaths for libraries to link against
if(APPLE)
  SET(CMAKE_SKIP_BUILD_RPATH FALSE)
  SET(CMAKE_BUILD_WITH_INSTALL_RPATH TRUE)
  SET(CMAKE_INSTALL_RPATH "${CMAKE_LIBRARY_OUTPUT_DIRECTORY};@executable_path/;@executable_path/../lib")
  SET(CMAKE_INSTALL_RPATH_USE_LINK_PATH TRUE)
endif()

include_directories(
  ${PROJECT_NAME} PUBLIC
  "${PROJECT_BINARY_DIR}"
  include
)

# Add sub directory
add_subdirectory(src)
add_subdirectory(demo)
add_subdirectory(python)
