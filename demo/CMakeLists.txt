add_executable(example example.cpp)
target_link_libraries(example hello)

if (MSVC AND MSVC_VERSION GREATER_EQUAL 1914)
  target_compile_options(example PUBLIC "/Zc:__cplusplus")
endif()
