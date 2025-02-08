from conans import ConanFile, tools

class FibConan(ConanFile):
    name = "fib"
    version = "1.0"
    license = "MIT"
    # author = "Your Name <your.email@example.com>"
    # url = "https://github.com/yourusername/fib"
    description = "A simple Fibonacci library"
    topics = ("fibonacci", "math", "example")
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    
    def source(self):
        # Download the source archive
        tools.get("https://example.com/fib-1.0.tar.gz")
    
    def build(self):
        # No build step required for header-only library
        pass
    
    def package(self):
        # Copy the header file to the package
        self.copy("fib.h", dst="lib", src="fib-1.0")
        # Copy the archive file to the package
        self.copy("libfib.a", dst="lib", src="fib-1.0")
    
    def package_info(self):
        # Specify the include path for consumers
        self.cpp_info.includedirs = ["lib"]