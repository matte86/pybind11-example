set(HEADERS
  ${PROJECT_SOURCE_DIR}/include/hello.h
)

set(SOURCES
  ${PROJECT_SOURCE_DIR}/src/hello.cpp
)

# The type of the library will be determined by value of BUILD_SHARED_LIBS (set by conan)
add_library(hello ${HEADERS} ${SOURCES})
target_link_libraries(hello ${CONAN_LIBS})

