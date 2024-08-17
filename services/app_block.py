from services.logger_helper import log_info_message, log_warning_message, log_error_message
import os
import subprocess


APP_FOLDER = "/Applications"



def block_mac_app(app_name:str):
    change_mac_executable(app_name=app_name, chmod='-x')



def unblock_mac_app(app_name:str):
    change_mac_executable(app_name=app_name, chmod='+x')



def change_mac_executable(app_name: str, chmod:str):
    app_name = app_name.strip()
    app_bundle_path = search_app_bundle_path(app_name=app_name)
    if not app_bundle_path:
        return None
    binary_path = search_app_binary_path(app_bundle_path=app_bundle_path, app_name=app_name)
    if binary_path:
        change_mode_for_binary(binary_path=binary_path, chmod=chmod)
    else:
        log_error_message(f"Failed to change executable mode at {binary_path}")


def change_mode_for_binary(binary_path:str, chmod:str):
    try:
        subprocess.run(["sudo", "chmod", chmod, binary_path])
        log_info_message(f"Successfuly changed mode for binary path {binary_path} with {chmod}")
    except Exception as e:
        log_error_message(f"Failed to change mode for binary {binary_path} with chmod {chmod}: {e}")


def search_app_binary_path(app_bundle_path: str, app_name: str):
    if not app_bundle_path:
        log_error_message("App bundle path is null. Couldn't search for the binary of the app.")
        return None
    
    macos_dir = os.path.join(app_bundle_path, "Contents", "MacOS")
    if not os.path.exists(macos_dir):
        log_error_message(f"MacOS directory not found in {app_bundle_path}")
        return None

    binary_path = os.path.join(macos_dir, app_name)
    if os.path.exists(binary_path):
        return binary_path

    # if not found list all files in the macos directory and return the first executable
    for file in os.listdir(macos_dir):
        file_path = os.path.join(macos_dir, file)
        if os.path.isfile(file_path) and os.access(file_path, os.X_OK):
            return file_path

def search_app_bundle_path(app_name: str):
    app_bundle_path = os.path.join(APP_FOLDER, f"{app_name}.app")
    if not os.path.exists(app_bundle_path):
        log_error_message(f"App '{app_name}' not found in {APP_FOLDER}. Tried to find {app_bundle_path} bundle.")
        return None
    return app_bundle_path