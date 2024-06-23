# Define variables
VERSION := v0.2
PYTHON_SCRIPT := gui.py
BUILD_DIR := build
DIST_DIR := $(BUILD_DIR)\dist
RELEASE_DIR := release
SETUP_SCRIPT := setup.py
EXE_NAME := gui.exe  # Change this to the name of your generated executable by cx_Freeze
ZIP_FILE := release_$(VERSION).zip

# Default target
all: build move zip

# Build the executable with cx_Freeze
build:
	@echo "Building the executable with cx_Freeze..."
	python -m cx_Freeze --script $(PYTHON_SCRIPT) --build-exe=$(DIST_DIR)

# Move the executable and other required files to the release directory
move:
	@echo "Creating the release directory..."
	@if not exist $(RELEASE_DIR) mkdir $(RELEASE_DIR) 
	@echo "Moving files to the release directory..."
	@xcopy /s /i /y /q "$(DIST_DIR)\*" $(RELEASE_DIR)\ 
	@xcopy /s /y /q fonts $(RELEASE_DIR)\fonts\ 
	@xcopy /s /y /q samples $(RELEASE_DIR)\samples\ 
	@copy /y $(PYTHON_SCRIPT) $(RELEASE_DIR)\ 
	@copy /y LICENSE.txt $(RELEASE_DIR)\ 
	@copy /y README.md $(RELEASE_DIR)\ 
	@copy /y requirements.txt $(RELEASE_DIR)\ 
	@copy /y Capper.exe $(RELEASE_DIR)\ 

# Zip the contents of the release directory
zip:
	@echo "Creating a zip archive of the release directory..."
	@7z.exe a -tzip $(ZIP_FILE) -w $(RELEASE_DIR)\.

# Clean up 
clean:
	@echo "Cleaning up..."
	@if exist $(DIST_DIR) rmdir /s /q $(DIST_DIR)
	@if exist $(RELEASE_DIR) rmdir /s /q $(RELEASE_DIR)\  

# Add a convenient way to rebuild
rebuild: clean all

.PHONY: all build move zip clean rebuild