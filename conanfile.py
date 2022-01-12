from conans import ConanFile, CMake, RunEnvironment, tools
import sys


class Pybind11ExampleConan(ConanFile):
    name = "hello-pybind11"
    version = "0.0.1"
    description = "a pybind11 example"
    settings = ('os', 'compiler', 'build_type', 'arch')
    options = {
        "shared": [True, False]
    }
    default_options = {
        "shared": True
    }
    generators = "cmake", "cmake_find_package", "cmake_find_package_multi"

    def configure(self):
        print("Conan: python path: %s" % sys.executable)
        print("Conan: python version: %s" % sys.version)

    def requirements(self):
        self.requires("pybind11/2.8.1")

    def build(self):
        env_build = RunEnvironment(self)
        with tools.environment_append(env_build.vars):
            cmake = CMake(self, set_cmake_flags=True)
            cmake.verbose = False
            cmake.definitions["PYTHON_EXECUTABLE"] = sys.executable
            cmake.configure()
            cmake.build()
            cmake.install()

    def imports(self):
        self.copy('*.dll', src='bin', dst='bin')
        self.copy('*.dll', src='bin', dst='dll_deps')
        self.copy('*.dylib*', src='lib', dst='lib')
        self.copy('*.so*', src='lib', dst='lib')

    def package(self):
        self.copy(pattern="*.h", dst="include", src="include")
        self.copy(pattern="*.lib", dst="lib", keep_path=False)
        self.copy(pattern="*.dll", dst="bin", keep_path=False)
        self.copy(pattern="*.dylib", dst="lib", keep_path=False)
        self.copy(pattern="*.so*", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["hello"]
