cmake_minimum_required(VERSION 3.0)

project(HelloWorldRestApiWithCppRestSDK)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

set(HEADER_SEARCH_PATH "./src/foundation/include")

add_executable(${PROJECT_NAME} ./src/main.cpp
                               ./src/microsvc_controller.cpp
                               ./src/foundation/network_utils.cpp
                               ./src/foundation/basic_controller.cpp)

include_directories(${HEADER_SEARCH_PATH})

target_link_libraries(${PROJECT_NAME} ${CONAN_LIBS})
