from conans import ConanFile
"""
Conan package recipe for the FibLib library.

This Conan recipe defines the package information and build instructions for the FibLib library, 
which is a library to calculate Fibonacci numbers.

Class Attributes:
    name (str): The name of the package.
    version (str): The version of the package.
    description (str): A brief description of the package.
    settings (tuple): The settings for which the package is built (os, compiler, build_type, arch).
    exports_sources (str): The pattern to specify which source files to export.

Methods:
    package(self):
        Copies the header files and static library files to the package folder.

    package_info(self):
        Sets the library information for consumers of the package.

    deploy(self):
        Copies the header files and static library files to the deployment folder.

Usage:
    1. Define the source files in the `src` directory.
    2. Uncomment the `build` method if you need to build the library using CMake.
    3. Customize the `package` and `deploy` methods as needed to include other types of files (e.g., .lib, .dll, .so, .dylib).
    4. Use the `conan create` command to create the package.
"""

class FibLibConan(ConanFile):
    name = "fib"
    version = "1.1"
    # license = "MIT"
    # author = "Your Name <your.email@example.com>"
    # url = "https://github.com/yourusername/fiblib"
    description = "A library to calculate Fibonacci numbers"
    # topics = ("fibonacci", "math", "example")
    settings = "os", "compiler", "build_type", "arch"
    # generators = "cmake"
    exports_sources = ["bin/*", "include/*", "lib/*", "src/*.h"]

    def build(self):
        pass
        # cmake = CMake(self)
        # cmake.configure(source_folder="src")
        # cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="src")
        # self.copy("*.lib", dst="lib", keep_path=False)
        # self.copy("*.dll", dst="bin", keep_path=False)
        # self.copy("*.so", dst="lib", keep_path=False)
        # self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["fib"]

    # def deploy(self):
    #     self.copy("*.h", dst="include", src="include")
    #     # self.copy("*.lib", dst="lib", src="lib")
    #     # self.copy("*.dll", dst="bin", src="bin")
    #     # self.copy("*.so", dst="lib", src="lib")
    #     # self.copy("*.dylib", dst="lib", src="lib")
    #     self.copy("*.a", dst="lib", src="lib")