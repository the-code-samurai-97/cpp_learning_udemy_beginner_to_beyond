# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/sibi/cpp_learning_udemy_beginner_to_beyond/constants

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/sibi/cpp_learning_udemy_beginner_to_beyond/constants/build

# Include any dependencies generated for this target.
include CMakeFiles/app_lib_const.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/app_lib_const.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/app_lib_const.dir/flags.make

CMakeFiles/app_lib_const.dir/src/constants.cpp.o: CMakeFiles/app_lib_const.dir/flags.make
CMakeFiles/app_lib_const.dir/src/constants.cpp.o: ../src/constants.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/sibi/cpp_learning_udemy_beginner_to_beyond/constants/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/app_lib_const.dir/src/constants.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/app_lib_const.dir/src/constants.cpp.o -c /home/sibi/cpp_learning_udemy_beginner_to_beyond/constants/src/constants.cpp

CMakeFiles/app_lib_const.dir/src/constants.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/app_lib_const.dir/src/constants.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/sibi/cpp_learning_udemy_beginner_to_beyond/constants/src/constants.cpp > CMakeFiles/app_lib_const.dir/src/constants.cpp.i

CMakeFiles/app_lib_const.dir/src/constants.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/app_lib_const.dir/src/constants.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/sibi/cpp_learning_udemy_beginner_to_beyond/constants/src/constants.cpp -o CMakeFiles/app_lib_const.dir/src/constants.cpp.s

# Object files for target app_lib_const
app_lib_const_OBJECTS = \
"CMakeFiles/app_lib_const.dir/src/constants.cpp.o"

# External object files for target app_lib_const
app_lib_const_EXTERNAL_OBJECTS =

libapp_lib_const.a: CMakeFiles/app_lib_const.dir/src/constants.cpp.o
libapp_lib_const.a: CMakeFiles/app_lib_const.dir/build.make
libapp_lib_const.a: CMakeFiles/app_lib_const.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/sibi/cpp_learning_udemy_beginner_to_beyond/constants/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX static library libapp_lib_const.a"
	$(CMAKE_COMMAND) -P CMakeFiles/app_lib_const.dir/cmake_clean_target.cmake
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/app_lib_const.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/app_lib_const.dir/build: libapp_lib_const.a

.PHONY : CMakeFiles/app_lib_const.dir/build

CMakeFiles/app_lib_const.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/app_lib_const.dir/cmake_clean.cmake
.PHONY : CMakeFiles/app_lib_const.dir/clean

CMakeFiles/app_lib_const.dir/depend:
	cd /home/sibi/cpp_learning_udemy_beginner_to_beyond/constants/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/sibi/cpp_learning_udemy_beginner_to_beyond/constants /home/sibi/cpp_learning_udemy_beginner_to_beyond/constants /home/sibi/cpp_learning_udemy_beginner_to_beyond/constants/build /home/sibi/cpp_learning_udemy_beginner_to_beyond/constants/build /home/sibi/cpp_learning_udemy_beginner_to_beyond/constants/build/CMakeFiles/app_lib_const.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/app_lib_const.dir/depend

