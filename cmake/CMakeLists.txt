cmake_minimum_required(VERSION 3.0)

project(main)

include_directories(.)

find_package(PythonInterp 3 REQUIRED)

add_custom_command(
	WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}/A
       	COMMAND ${PYTHON_EXECUTABLE} preparing.py
	DEPENDS A/preparing.py
	OUTPUT ${CMAKE_SOURCE_DIR}/A/index.h)

add_subdirectory(B)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -Wall")

add_executable(main C/main.cpp C/main.h A/index.h)

target_include_directories(main PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})

target_link_libraries(main mylib)