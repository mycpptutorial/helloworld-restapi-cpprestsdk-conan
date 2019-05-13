from conans import ConanFile, CMake, tools


class CpprestsdkConan(ConanFile):
    name = "helloworld-restapi-cpprestsdk-conan"
    version = "1.0.0"
    license = "MIT"
    author = "Nasim Kabiliravi <conanrepos@gmail.com>"
    url = "https://github.com/conan-repos/cpprestsdk"
    description = "The C++ REST SDK is a Microsoft project for cloud-based client-server communication in native code using a modern asynchronous C++ API design. This project aims to help C++ developers connect to and interact with services."
    topics = ("C++ REST SDK", "microservice", "restapi", "cpp")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    def source(self):
        self.run("git clone https://github.com/conan-repos/cpprestsdk.git")
        self.run("cd cpprestsdk && git checkout v2.10.13_conan && git submodule update --init")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="cpprestsdk")
        cmake.build()

        # Explicit way:
        # self.run('cmake %s/hello %s'
        #          % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include", src="hello")
        self.copy("*hello.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["cpprestsdk"]
