cmake_minimum_required(VERSION 3.0)

project(HelloWorldRestApiWithCppRestSDK)

# Configure compiler options ...
if(CMAKE_CXX_COMPILER_ID MATCHES "Clang")

    message("-- configuring clang options")
    set(CMAKE_CXX_FLAGS "-arch x86_64 -std=c++11 -stdlib=libc++ -DBOOST_LOG_DYN_LINK -Wno-deprecated-declarations -fvisibility=hidden")

elseif(CMAKE_CXX_COMPILER_ID MATCHES "GNU")

    message("-- configuring gcc options")

    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=gnu++11 -DBOOST_LOG_DYN_LINK")

endif()

add_executable(${PROJECT_NAME} main.cpp
                               microsvc_controller.cpp
                               foundation/network_utils.cpp
                               foundation/basic_controller.cpp)

set(HEADER_SEARCH_PATHS "foundation/include" "../build/include")

include_directories(${HEADER_SEARCH_PATHS})

file(GLOB_RECURSE SHARED_LIBRARIES "../build/bin/*.dylib")
file(GLOB_RECURSE STATIC_LIBRARIES "../build/lib/*.a")

if (APPLE)
    target_link_libraries(${PROJECT_NAME} "-framework CoreFoundation")
    target_link_libraries(${PROJECT_NAME} "-framework Security")
    target_link_libraries(${PROJECT_NAME} ${SHARED_LIBRARIES} ${STATIC_LIBRARIES})
    set_target_properties(${PROJECT_NAME} PROPERTIES LINK_FLAGS "-W1, -F/Library/Frameworks")
else()
    target_link_libraries(${PROJECT_NAME} ${SHARED_LIBRARIES} ${STATIC_LIBRARIES})
endif()
