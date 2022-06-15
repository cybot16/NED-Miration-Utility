#!/usr/bin/env python3
#
# author : Abdellah Sabry <absabry@cisco.com>
#
# Ned Migration utility to facilitate the  ned migration process for multiple devices in one go.
#
# This is a utility that takes as an input a list of devices and a ned-id to migrate to and executes the following:
# 1 - Reads devices list file and loops over the device list
# 2 - Checks if the device is onboarded
# 3 - Checks if the NED is loaded
# 4 - Checks if the device is already onboarded
# 5 - Executes ned migration in a dry-run mode
# 6 - Shows the modified paths and their info
# 7 - Shows the affected services if there are any
# 8 - Gives the user the following options if there are affected services:
#     a - Execute the ned migration
#     b - Skipping the current device ned migration
#     c - Exiting the whole program
# 9 - If there are no affected services or the user choses option 'a'. Ned migration action is executed.
# 10 - The script continues to the next device
# 11 - This utility generates two sets of files :
#     a - NED migration log file : ned-migration-devices.log
#     b - NED migration JSON report : migration-datetime.json
#
# There are options that the user can chose to run the ned migration over the device list:
# 1 {--dry-run}: The utility only simulates the ned migration and shows the modified paths 
#                 and affected services
# 2 {--no-networking}: The utility runs the ned migration action in no-networking mode.
#                 i.e  the action uses the device configuration in CDB and doesn't connect 
#                 and read the configuration from the device
# 3 {--verbose} : The utility uses this option by default to show the affected services and
#                 doesn't give the user the possibility to activate/deactivate this option
#                 to avoid running ned migrations without checking the affected services
#
# Other arguments:
# {--new-ned-id} : the target ned id of the ned migration
# {--file} : devices list file where the devices are newline-delimited:
# device1
# device2
# ...
# deviceN

import ncs
import _ncs
import ncs.application
import argparse
import logging
import sys
from argparse import RawTextHelpFormatter
import time
import math
import sys
import builtins
import json
from datetime import datetime
from dataclasses import dataclass

__version__ = "1.3"

FIGLET = f"""
 ______  _______ _____      ______  _                       _             
|  ___ \(_______|____ \    |  ___ \(_)                 _   (_)            
| |   | |_____   _   \ \   | | _ | |_  ____  ____ ____| |_  _  ___  ____  
| |   | |  ___) | |   | |  | || || | |/ _  |/ ___) _  |  _)| |/ _ \|  _ \ 
| |   | | |_____| |__/ /   | || || | ( ( | | |  ( ( | | |__| | |_| | | | |
|_|   |_|_______)_____/    |_||_||_|_|\_|| |_|   \_||_|\___)_|\___/|_| |_|
                                     (_____|                              
                 _     _      _ _ _           
                | |   | |_   (_) (_)_         
                | |   | | |_  _| |_| |_ _   _ 
                | |   | |  _)| | | |  _) | | |
                | |___| | |__| | | | |_| |_| |
                 \______|\___)_|_|_|\___)__  |
                                       (____/ v{__version__}

Ned Migration utility to facilitate the  ned migration process for multiple devices in one go.

This is a utility that takes as an input a list of devices and a ned-id to migrate to and executes the following:
1 - Reads devices list file and loops over the device list
2 - Checks if the device is onboarded
3 - Checks if the NED is loaded
4 - Checks if the device is already onboarded
5 - Executes ned migration in a dry-run mode
6 - Shows the modified paths and their info
7 - Shows the affected services if there are any
8 - Gives the user the following options if there are affected services:
    a - Execute the ned migration
    b - Skipping the current device ned migration
    c - Exiting the whole program
9 - If there are no affected services or the user choses option 'a'. Ned migration action is executed.
10 - The script continues to the next device
11 - This utility generates two sets of files :
    a - NED migration log file : ned-migration-devices.log
    b - NED migration JSON report : migration-datetime.json
"""

@dataclass
class signs:
    OK = '[\033[92m*\033[0m]'
    INFO = '\t[\033[95m!\033[0m]'
    EXIT = '[\033[91m+\033[0m]'
    ERROR = '[\033[91mX\033[0m]'
    WARNING = '\033[93m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    RED = '\033[91m'
    OKBLUE = '\033[96m'

class ProgressConsole:
    def __init__(self, size, width=80, output=sys.stdout):
        self.size = size
        self.width = width
        self.current = 0
        self.output = output
        self._bar_size = width - 4 - int(math.log10(size))
        self._bar_step = self._bar_size / self.size

    def print(self, *message):
        self._clear()
        builtins.print(*message, file=self.output)
        self._display()

    def increment(self, step=1):
        self.current = min(self.current + step, self.size) 
        self._display()

    def _clear(self):
        self.output.write('\r')
        self.output.write(' ' * self.width)
        self.output.write('\r')

    def _display(self):
        bar = '\033[0;37m\033[0;37m\033[7m \033[27m\033[0;0m\033[0;0m' * (int(round(self._bar_step * self.current)-2))
        blank = ' ' * (self._bar_size - len(bar)-2)
        self.output.write(f"\r|{bar}{blank}|{min(int(((self.current)/(self.size))*100),100)}%")

logging.basicConfig(
    filename = "ned-migration-devices.log",
    level=logging.INFO,
    format='<%(levelname)s> %(asctime)s.%(msecs)d NED Migration : %(message)s',
    datefmt='%d-%b-%Y::%H:%M:%S'
)

def parser(args):
    parser = argparse.ArgumentParser(description="""
    Ned Migration utility to facilitate the  ned migration process for multiple devices in one go.

    This is a utility that takes as an input a list of devices and a ned-id to migrate to and executes the following:
    1 - Reads devices list file and loops over the device list
    2 - Checks if the device is onboarded
    3 - Checks if the NED is loaded
    4 - Checks if the device is already onboarded
    5 - Executes ned migration in a dry-run mode
    6 - Shows the modified paths and their info
    7 - Shows the affected services if there are any
    8 - Gives the user the following options if there are affected services:
        a - Execute the ned migration
        b - Skipping the current device ned migration
        c - Exiting the whole program
    9 - If there are no affected services or the user choses option 'a'. Ned migration action is executed.
    10 - The script continues to the next device
    11 - This utility generates two sets of files :
        a - NED migration log file : ned-migration-devices.log
        b - NED migration JSON report : migration-datetime.json
    
    There are options that the user can chose to run the ned migration over the device list:
    1 {--dry-run}: The utility only simulates the ned migration and shows the modified paths 
                    and affected services
    2 {--no-networking}: The utility runs the ned migration action in no-networking mode.
                    i.e  the action uses the device configuration in CDB and doesn't connect 
                    and read the configuration from the device
    3 {--verbose} : The utility uses this option by default to show the affected services and
                    doesn't give the user the possibility to activate/deactivate this option
                    to avoid running ned migrations without checking the affected services

    Other arguments:
    {--new-ned-id} : the target ned id of the ned migration
    {--file} : devices list file where the devices are newline-delimited:
    device1
    device2
    ...
    deviceN

    """,
                    formatter_class=RawTextHelpFormatter)
    parser.add_argument('--dry-run', '-d', action='store_true',
                    help='Perform the Ned Migration using dry-run option to only simulate the output of the operation.')
    parser.add_argument('--no-networking', action='store_true',
                    help='Perform the Ned Migration using the no-networking option to use the device configuration in CDB.')
    parser.add_argument('--new-ned-id',  required=True, type=str,
                    help='Perform the Ned Migration using the new-ned-id provided in the input')
    parser.add_argument('--file', '-f', required=True, type=str,
                    help='Path of the file containing the list of devices to perform NED migration on.\n\
                    The devices are newline-delimited')
    parser.add_argument('--version', action='version', version='%(prog)s' + __version__)
    try:
        args = parser.parse_args(sys.argv[1:])
        return args.dry_run, args.no_networking, args.new_ned_id, args.file
    except argparse.ArgumentError:
        parser.print_help(sys.stderr)
        sys.exit(2)

def display_seperator():
    print(signs.OKBLUE+"\n* ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ *\n"+signs.ENDC)

def confirm_startup():
    # Validating starting ned migration utility

    confirm = input(signs.OKBLUE+'Would you like to start the Ned migration?\n'
                        'Y/n (Continue/Quit)\n'+signs.ENDC)
    logging.info("Running user validation to start ned migration Y/n (Continue/Quit)")

    if confirm in ['y','Y']:
        # Starting Ned Migration
        logging.info("User Input : 'YES' :: chosing to start the utility")
        logging.info("Let's go...")

    elif confirm in ['n','N']:
        # Canceling and exiting the program
        print(signs.OK+" Exiting...")
        logging.info("User Input :  'CANCEL' : chosing to cancel ned migration and exist program")
        logging.info("Exiting...")
        return sys.exit()

    else:
        print(f"{signs.ERROR} {confirm} is not a valid input\n")
        logging.error(f"{confirm} is not a valid input")
        confirm_startup()

def confirm_migration():
    # Giving the option to the user to chose if they want to execute NED migration
    # even if there are affected services
    # If no is the repsonse, we move to the next device
    # They can also Cancel and exit all the ned migration script
    print(signs.RED +'[?] Would you like to continue with this Ned migration for this device? (y/n/CANCEL)\n'+signs.ENDC)
    confirm = input("\t")
    logging.info("Running user validation to continue with ned migration y/n/CANCEL")

    if confirm in ['y','Y']:
        # Confirming Ned migration for this device
        logging.info("User Input : 'YES' :: chosing to continue with the ned migration for this device")
        logging.info("Let's go...")
        return True

    elif confirm in ['n','N']:
        # Skipping Ned migration for this device
        logging.info("User Input :  'NO' : chosing to skip the ned migration for this device")
        logging.info("Skipping...")
        return False

    elif confirm in ['c','C', 'CANCEL']:
        # Canceling and exiting the program
        print(signs.OK+" Exiting...")
        logging.info("User Input :  'CANCEL' : chosing to cancel ned migration and exist program")
        logging.info("Exiting...")

        # Writing migration report into file before exiting 
        write_json("migration", migration_report)

        return sys.exit()
    else:
        print(f"{signs.ERROR} {confirm} is not a valid input\n")
        logging.error(f"{confirm} is not a valid input")
        confirm_migration()

def write_json(filename, data):
    #write json output on the fs
    now = datetime.now()
    date_time = now.strftime("%m-%d-%Y-%H:%M:%S")
    filename = f'{filename}-{date_time}.json'

    with open(filename, 'w') as f:
        json.dump(data, f, indent = 4)
    print(f"{signs.OK} Writing migration report into file {filename}") 
    display_seperator()

    logging.info(f"Writing migration report into file {filename}") 

def check_already_migrated(device, new_ned_id):
    # Checking if the device is already migration to avoid getting errors
    ned_id = ncs.application.get_ned_id(device)
    return new_ned_id in ned_id 

def check_ned_package(root, new_ned_id):
    nedNotLoaded = False
    # Checking if the ned is loaded to avoid getting errors
    if new_ned_id in root.packages.package:
        if root.packages.package[new_ned_id].oper_status.up:
            # Displaying/logging new ned is  loaded to NSO
            print(f"{signs.OK} Ned version {new_ned_id} is loaded")
            logging.info(f"Ned version {new_ned_id} is loaded")
            display_seperator()
        else:
            nedNotLoaded = True
    else:
        nedNotLoaded = True

    if nedNotLoaded:
        # Displaying/logging new ned is not loaded to NSO
        print(f"{signs.ERROR} Ned version {new_ned_id} is "+signs.RED+"NOT"+signs.ENDC+" loaded")
        display_seperator()
        logging.error(f"Ned version {new_ned_id} is NOT loaded")

        # Exist with status 1
        sys.exit(1)

def check_device_exists(root, device):
    # Checking if device is onboarded to avoid getting errors

    if device in root.devices.device:

        # Display/ Logging device is onboarded
        print(f"{signs.OK} The Device {device} is onboarded")
        display_seperator()
        logging.info(f"The Device {device} is onboarded")

        # Return True if device is onboarded
        return True
    else:
        # Display/ Logging device is not onboarded
        print(f"{signs.ERROR} The Device {device} is "+signs.RED+"NOT"+signs.ENDC+" onboarded")
        display_seperator()
        logging.error(f"The Device {device} is NOT onboarded")

        #Return False if device is not onboarded
        return False

def display_affected_services(device, device_migrate_result, with_changes):
    # Using the display_affected_service function to display both:
    # affected-services and affected-services-with-changes
    # the with_changes argument differentiate between these options

    if with_changes:
        # Getting the list of services with changes
        affected_services_list = device_migrate_result.affected_services_with_changes.as_list()
        affect_services_list_index = "affected-services-with-changes"

        # Displaying and logging affected services with changes by the ned migration action
        print(f"{signs.INFO} Affected services with changes: the service instances/points" \
                         "that are affected by the data model \n\t\t changes on the migrated device." \
                    f" that touches the migrated device  {signs.OKBLUE}{device}{signs.ENDC}\n")
        logging.warning("Affected services with changes: the service instances/points" \
                        "that are affected by the data model changes on the migrated device." \
                        f" that touches the migrated device {device}")
    else : 
        # Getting the list of services 
        affected_services_list = device_migrate_result.affected_services.as_list()
        affect_services_list_index = "affected-services"

        # Displaying/ logging affected services by the ned migration action
        print(f"{signs.INFO} Affected services : The service instances/points" \
                        f" that touches the migrated device  {signs.OKBLUE}{device}{signs.ENDC}")
        logging.warning("Affected services : The service instances/points" \
                        f" that touches the migrated device {device}")


    # Updating migration report: creating affected-services list
    migration_report[device]["dry-run"][affect_services_list_index] = {}

    # Enumerating affected-services
    for instance_num, service in enumerate(affected_services_list):

        # Printing/Logging affected-services and their numbers
        print(f"\t\t[{signs.RED}{instance_num+1}{signs.ENDC}] : {signs.BOLD}{service}{signs.ENDC}")
        logging.critical(f"{instance_num+1} : {service}")

        # Updating migration report
        migration_report[device]["dry-run"][affect_services_list_index][instance_num+1] = service

    #returning number of affected-services
    return len(affected_services_list)

def execute_migration(root, device, new_ned_id, no_networking, dry_run):
    try:
        # Preparing ned-migration  action inputs
        device_migrate_input = root.devices.device[device].migrate.get_input()
        device_migrate_input.new_ned_id = new_ned_id

        # Always in verbose mode to display affected services
        device_migrate_input.verbose.create()

        # Dry-run mode
        if dry_run:
            device_migrate_input.dry_run.create()

        # No-networking if the user wants to use the device model in CDB 
        # instead of direct communication with the device
        if no_networking:
            device_migrate_input.no_networking.create()
        
        # Executing ned migration action
        device_migrate_result = root.devices.device[device].migrate(device_migrate_input)

        if not dry_run:

            # Display info
            display_seperator()
            print(f"{signs.OK} Ned Migration completed for the device: {signs.OKBLUE}{device}{signs.ENDC}\n")
            display_seperator()

            # Logging info
            logging.info(f"Ned Migration completed for the device: {device}")

            # Updating migration report
            migration_report[device]["status"] = 'Ned Migrated'

        return device_migrate_result

    except Exception as e:
        # Display the error if the action execution fails
        print(f"{signs.ERROR} Error while trying to run ned migrate with flags dry-run {dry_run} ; no-networking {no_networking} for {device}\n")
        print(f"{signs.ERROR} Error: {e}")

        # Logging Exception
        logging.exception(f"Error while trying to run ned migrate with flags : dry-run {dry_run}; no-networking {no_networking} for {device} : {e} ")

        # Updating migration report
        migration_report[device]["status"] = 'Error When Migration'


def ned_migrate(root, device, new_ned_id, dry_run, no_networking):
    
    # Display and logging info
    print(f"{signs.OK} Running Ned Migration for the device {signs.OKBLUE}{device} in dry-run{signs.ENDC} mode\n")
    logging.info(f"Running Ned Migration for the device {device} in dry-run mode")

    # Running the ned migration action in dry-run mode
    device_migrate_dr_result = execute_migration(root, device, new_ned_id, no_networking, dry_run=True)

    # Updating migration report
    migration_report[device]["status"] = 'simulated'
    migration_report[device]["dry-run"] = {}

    # Display modified paths if there are any
    if device_migrate_dr_result:
        if device_migrate_dr_result.modified_path:

            #Printing and logging info
            print(signs.INFO+" Modified Paths : The path that has been modified.\n")
            logging.warning("Modified Paths : The path that has been modified")

            # Updating migration report, adding modified-paths lists
            migration_report[device]["dry-run"]["modified-paths"] = {}
            migration_report[device]["dry-run"]["modified-paths"]["deleted"]={}

            # Looping over the modified paths
            for entry in device_migrate_dr_result.modified_path:

                # Checking if there is a deleted part of the model
                # and storing it in a seperate list "deleted"
                if "deleted" in  entry.info:

                    # Printing/Logging deleted paths
                    print(f"\t\t{signs.RED}Path: {entry.path}{signs.ENDC}")
                    print(f"\t\t{signs.RED}Info: {entry.info}{signs.ENDC}")
                    logging.critical(f"Path: {entry.path} ; Info: {entry.info}")

                    # updating migration report info with deleted paths
                    migration_report[device]["dry-run"]["modified-paths"]["deleted"][entry.path] = entry.info
                else:
                    # Printing/Logging modified paths
                    print(f"\t\t{signs.BOLD}Path: {entry.path}{signs.ENDC}")
                    print(f"\t\t{signs.BOLD}Info: {entry.info}{signs.ENDC}")
                    logging.warning(f"Path: {entry.path} ; Info: {entry.info}")

                # Updating migration report info with modified paths
                migration_report[device]["dry-run"]["modified-paths"][entry.path] = entry.info

        proceedMigration = False
        # Checking if there will be {affected services} and or {affected services with changes} by the NED migration
        if device_migrate_dr_result.affected_services.as_list() or device_migrate_dr_result.affected_services_with_changes.as_list():
            
            # Displaying affected services and affected services with changes
            number_affected_services = display_affected_services(device, device_migrate_dr_result, with_changes = False)
            number_affected_services_with_changes = display_affected_services(device, device_migrate_dr_result, with_changes = True)

            # Displaying the number of affected service instances
            display_seperator()
            print(f"{signs.WARNING}[?] There are {number_affected_services}" \
                f" affected instances by this Ned Migration on {device}{signs.ENDC}")
            print(f"{signs.WARNING}[?] There are {number_affected_services_with_changes}" \
                f" affected instances with changes by this Ned Migration on {device}{signs.ENDC}")
                
            # Logging the number of affected service instances
            logging.info(f"There are {number_affected_services} affected instances by this Ned Migration on {device}")
            logging.info(f"There are {number_affected_services_with_changes} affected instances with changes by this Ned Migration on {device}")
            
            # Giving the user the option to chose how to proceed with this migration knowing that there are affected services
            if not dry_run:
                if confirm_migration():
                    # In case of user validation, proceeding the executing ned migration
                    proceedMigration = True
        else:
            # In case of user no affected services and no dry-run, proceeding automatically with ned migration
            if not dry_run:
                proceedMigration = True

        if proceedMigration:

            #Display/ Logging starting Ned migration for the current device
            display_seperator()
            print(f"{signs.OK} Running Ned Migration for the device {signs.OKBLUE}{device}{signs.ENDC}\n")
            logging.info(f"Running Ned Migration for the device {device}")

            # Execute ned migration
            execute_migration(root, device, new_ned_id, no_networking, dry_run=False)

            # Updating Migration report status to "Ned Migrated"
            migration_report[device]["status"] = 'Ned Migrated'


if __name__ == "__main__":

    #Calling the parser function to get the args from input
    dry_run, no_networking, new_ned_id, devices_list_file= parser(sys.argv)
    
    #Welcome Banner & Logging
    print(FIGLET)
    confirm_startup()
    display_seperator()
    print(f"{signs.OK} Device Migration Script")
    print(f"{signs.OK} Starting...")
    logging.info("Starting...")
    logging.info(f"Ned Migration Utility v{__version__}")
    logging.info(f"Options used : dry-run {dry_run} no-networking {no_networking} new-ned-id {new_ned_id}  device-list-file {devices_list_file}")
    # Reading the devices_list input file
    try:
        devices_list = open(devices_list_file, "r").readlines()
        print(f"{signs.OK} Reading devices list file...")
        logging.info("Reading devices list file...")
        display_seperator()
    except Exception as e:
        print(f"{signs.ERROR} Error while reading file...")
        print(f"{signs.ERROR} {e}")
        logging.exception(f"Error while reading file...{e}")
        sys.exit(1)

    # Creating migration report
    migration_report= {}

    # Progress bar
    progress_bar = ProgressConsole(len(devices_list))
    print = progress_bar.print

    #Starting Maapi Session
    with ncs.maapi.Maapi() as m:
        with ncs.maapi.Session(m, 'admin', 'system'):
            with m.start_read_trans() as t:

                #Getting root object
                root = ncs.maagic.get_root(t)
                #Checking ned package is loaded on NSO
                check_ned_package(root, new_ned_id)
            
                #Looping over the device list and performing NED migration 
                for device in devices_list:
                    # Getting rid of \n
                    device = device.strip()


                
                    # Structuring Migration Report
                    migration_report[device] = {}
                    migration_report[device]["options"] = {}
                    migration_report[device]["info"] = {}
                    migration_report[device]["info"]["new-ned-id"] = new_ned_id
                    migration_report[device]["prerequisites"] = {}
                    migration_report[device]["prerequisites"]["device-onboarded"] = False
                    migration_report[device]["prerequisites"]["ned-loaded"] = True
                    migration_report[device]["prerequisites"]["device-not-already-migrated"] = False
                    
                    # Displaying device info and options
                    print(f"{signs.OK} Ned Migration for:\n" \
                         f"{signs.INFO} Device {device}\n" \
                         f"{signs.INFO} dry-run: {dry_run}\n" \
                         f"{signs.INFO} no-networking: {no_networking}")
                    display_seperator()

                    logging.info(f"Ned Migration for:" \
                        f"Device {device};" \
                        f"dry-run: {dry_run};" \
                        f"no-networking: {no_networking};")

                    # Recording info into the report
                    migration_report[device]["options"]["dry-run"] = dry_run
                    migration_report[device]["options"]["no-networking"] = no_networking
                    migration_report[device]["options"]["verbose"] = True

                    #Checking device is onboarded in NSO:
                    if not check_device_exists(root, device):
                        continue
                    #Getting device object
                    device_obj = root.devices.device[device]
                    migration_report[device]["prerequisites"]["device-onboarded"] = True
                    migration_report[device]["status"] = 'Not Migrated'
                    


                    # Log the old ned id and displaying/logging it
                    ned_id = ncs.application.get_ned_id(device_obj).split(":")[0]
                    migration_report[device]["info"]["old-ned-id"] = ned_id
                    print(f"{signs.OK} Info:\n" \
                        f"{signs.INFO} Current ned-id {ned_id}\n" \
                        f"{signs.INFO} Target ned-id: {new_ned_id}\n")
                    display_seperator()
                    logging.info(f"Neds status:" \
                        f" Current ned-id {ned_id};" \
                        f" Target ned-id: {new_ned_id};")

                    #Checking if the device is already migrated:
                    #If it's already with the new ned-id skip to the next device
                    #Else run ned_migrate() function
                    if check_already_migrated(device_obj, new_ned_id):

                        #Printing info
                        print(f"{signs.EXIT} The device {device} is already with the ned-id {new_ned_id}")
                        print(f"{signs.INFO} Skipping Ned migration for this device")
                        display_seperator()

                        # Logging warning 
                        logging.warning(f"The device {device} is already with the ned-id {new_ned_id}")
                        logging.warning(f"Skipping Ned migration for the device {device}")

                        # Updating migration report status
                        #migration_report[device]["status"] = 'Ned Migrated'
                        migration_report[device]["status"] = 'Device is already using the target NED'
                    else:
                        # Updating migration report prerequisites
                        migration_report[device]["prerequisites"]["device-not-already-migrated"] = True

                        # All prerequisites are checked, Calling ned_migrate() function
                        ned_migrate(root, device, new_ned_id, dry_run , no_networking)
                        

                    progress_bar.increment()
    #Logging info
    logging.info("Transaction Closed")       
    # Writing migration report into a file
    write_json("migration", migration_report)
