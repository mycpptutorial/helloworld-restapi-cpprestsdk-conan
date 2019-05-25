from conans import ConanFile, CMake, tools


class CpprestsdkConan(ConanFile):
    name = "helloworld-restapi-cpprestsdk-conan"
    version = "1.0.0"
    license = "MIT"
    author = "Nasim Kabiliravi <conanrepos@gmail.com>"
    url = "https://github.com/mycpptutorial/helloworld-restapi-cpprestsdk-conan"
    description = "The C++ REST SDK is a Microsoft project for cloud-based client-server communication in native code using a modern asynchronous C++ API design. This project aims to help C++ developers connect to and interact with services."
    topics = ("C++ REST SDK", "microservice", "restapi", "cpp", "C++ tutorial")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    exports = "*"

    def requirements(self):
        self.requires("OpenSSL/1.0.2o@conan/stable")
        self.requires("zlib/1.2.11@conan/stable")
        self.requires("boost/1.69.0@conan/stable")
        self.requires("cpprestsdk/2.10.13@conanrepos/stable")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="src")
        cmake.build()

    def imports(self):
        self.copy("*.*", "include/openssl", "include/openssl")
        self.copy("*.*", "include/boost", "include/boost")
        self.copy("zconf.h", "include/zlib", "include")
        self.copy("zlib.h", "include/zlib", "include")
        self.copy("bzlib.h", "include/zlib", "include")
        self.copy("*.*", "include/pplx", "include/pplx")
        self.copy("*.*", "include/cpprest", "include/cpprest")
        self.copy("*.dll", "bin", "lib")
        self.copy("*.dylib", "bin", "lib")
        self.copy("*.so", "bin", "lib")
        self.copy("*.a", "lib", "lib")

    def package(self):
        self.copy("*.hpp", dst="include", src="src/foundation/include")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["HelloWorldRestApiWithCppRestSDK"]
