cmake_minimum_required(VERSION 2.8)
add_compile_options(-std=c++11)

project(stitcher)

find_package( OpenCV 3.4.3 REQUIRED )
include_directories( ${OpenCV_INCLUDE_DIRS} )

#specify your source files here
add_executable(${PROJECT_NAME} "stitcher.cpp")


target_link_libraries(${PROJECT_NAME} ${OpenCV_LIBS} )