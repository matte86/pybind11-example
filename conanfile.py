from conan import ConanFile
from conan.tools.cmake import CMakeDeps, CMake
import sys


class Pybind11ExampleConan(ConanFile):
    name = "hello-pybind11"
    version = "0.0.1"
    description = "a pybind11 example"

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    generators = "CMakeToolchain"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def configure(self):
        print("Conan: python path: %s" % sys.executable)
        print("Conan: python version: %s" % sys.version)

    def requirements(self):
        self.requires("pybind11/2.10.1")

    def generate(self):
        cmake = CMakeDeps(self)
        cmake.generate()

    def build(self):
        cmake = CMake(self)
        cmake.verbose = True
        cmake.configure()
        cmake.build()
        cmake.install()
