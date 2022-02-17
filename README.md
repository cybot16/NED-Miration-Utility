# NED Migration Utility

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

The NMU(NED Migration Utility) is tool that demystifies the NED migration process, and makes it safe for NSO operators to run NED migrations on a list of devices in a batch fashion. Thus gaining operationnal time while avoiding side effects.

NED migrations usually need to be ran over a number of devices that needs to be migrated, and every device has its own conditions and states that  may affect the services that are configured on it.

The NMU gives the possibility to the users to run migrations in a safe manner, it can migrate devices that do not have special conditions automatically, and gives the user the possibility to deal seperatly with caveats.
The NMU generates reports that contain all the affected services, device state, migrated paths and much more. 

---
## Prerequisites
- The NCS minimum version is v5.2
- Python minimum version is v.3.6
- Local and System NCS installs are compliant
---
## Getting started :
Cloning the github repository :
```
git clone https://github.com/cybot16/NED-Miration-Utility.git
```
Running the helper :
```
./ned_migration.py -h
```

## Usage :

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
                                           (____/ v1.2


    usage: ./ned_migration.py [-h] [--dry-run] [--no-networking] --new-ned-id
                            NEW_NED_ID --file FILE

    Ned Migration utility to facilitate the  ned migration process for multiple devices in one go.

    This is a utility that takes as an input a list of devices and a ned-id to migrate to and executes the following:
    1 - Reads devices list file and loops over the device list
    2 - Checks if the device is onboarded
    3 - Checks if the NED is loaded
    4 - Checks if the device is already migrated
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

    optional arguments:
      -h, --help            show this help message and exit
      --dry-run, -d         Perform the Ned Migration using dry-run option to only simulate the output of the operation.
      --no-networking       Perform the Ned Migration using the no-networking option to use the device configuration in CDB.
      --new-ned-id NEW_NED_ID
                            Perform the Ned Migration using the new-ned-id provided in the input
      --file FILE, -f FILE  Path of the file containing the list of devices to perform NED migration on.
                                                The devices are newline-delimited
---    

## NED migration example :

This is a NED migration that is executed on the device NETSIM-DEVICE-1

```
* ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ *

[*] Ned Migration for:
        [!] Device NETSIM-DEVICE-1
        [!] dry-run: False
        [!] no-networking: True

* ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ *

[*] The Device NETSIM-DEVICE-1 is onboarded

* ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ *

[*] Ned version alu-sr-cli-8.17 is loaded

* ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ *

[*] Info:
        [!] Current ned-id alu-sr-cli-8.13
        [!] Target ned-id: alu-sr-cli-8.17


* ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ *

[*]Running Ned Migration for the device NETSIM-DEVICE-1 in dry-run mode

        [!] Modified Paths : The path that has been modified.

                Path: /devices/device[name='NETSIM-DEVICE-1']/config/alu:system/security/snmp/community
                Info: list key has changed
                Path: /devices/device[name='NETSIM-DEVICE-1']/config/alu:router/policy-options/policy-statement/entry/from/protocol/protocol
                Info: leaf/leaf-list type has changed
                Path: /devices/device[name='NETSIM-DEVICE-1']/config/alu:router/interface/bfd/type
                Info: leaf/leaf-list type has changed
                Path: /devices/device[name='NETSIM-DEVICE-1']/config/alu:router/interface/ipv6/urpf-check
                Info: node type has changed from non-presence container to presence container
                Path: /devices/device[name='NETSIM-DEVICE-1']/config/alu:service/vprn/interface/ipv6/urpf-check
                Info: node type has changed from non-presence container to presence container
                Path: /devices/device[name='NETSIM-DEVICE-1']/config/alu:service/ies/interface/ipv6/urpf-check
                Info: node type has changed from non-presence container to presence container
                Path: /devices/device[name='NETSIM-DEVICE-1']/config/alu:qos/sap-ingress/dscp/id
                Info: leaf/leaf-list type has changed
                Path: /devices/device[name='NETSIM-DEVICE-1']/config/alu:qos/sap-ingress/dscp
                Info: list key has changed; leaf 'id' has changed type
        [!] Affected services : The service instances/points that touches the migrated device NETSIM-DEVICE-1

                [1]/l3vpn[instance='volvo'][device='NETSIM-DEVICE-1'] 

        [!] Affected services with changes: the service instances/pointsthat are affected by the data model 
                 changes on the migrated device. that touches the migrated device NETSIM-DEVICE-1


* ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ *

[?] There are 1 affected instances by this Ned Migration on NETSIM-DEVICE-1
[?] There are 0 affected instances with changes by this Ned Migration on NETSIM-DEVICE-1
[?] Would you like to continue with the Ned migration?
(y/n/CANCEL)
y

* ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ *

[*] Running Ned Migration for the device NETSIM-DEVICE-1
[*] Ned Migration completed successfully for the device NETSIM-DEVICE-1
[*] Writing migration report into file migration-12-21-2021-11:32:08.json 

* ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ *
[                                                         ] 100 %
```

## ned-migration-device.log:
```
<INFO> 19-Dec-2021::15:51:09.181 NED Migration : Starting...
<INFO> 19-Dec-2021::15:51:09.181 NED Migration : Ned Migration Utility v1.2
<INFO> 19-Dec-2021::15:51:09.181 NED Migration : Reading devices list file...
<INFO> 19-Dec-2021::15:51:09.181 NED Migration : Ned Migration for:Device NETSIM-DEVICE-1;dry-run: False;no-networking: True;
<INFO> 19-Dec-2021::15:51:09.189 NED Migration : Maapi transaction started
<INFO> 19-Dec-2021::15:51:09.215 NED Migration : The Device NETSIM-DEVICE-1 is onboarded
<INFO> 19-Dec-2021::15:51:09.216 NED Migration : Ned version alu-sr-cli-8.17 is loaded
<INFO> 19-Dec-2021::15:51:09.220 NED Migration : Neds status: Current ned-id alu-sr-cli-8.17; Target ned-id: alu-sr-cli-8.17;
<WARNING> 19-Dec-2021::15:51:09.220 NED Migration : The device NETSIM-DEVICE-1 is already with the ned-id alu-sr-cli-8.17
<WARNING> 19-Dec-2021::15:51:09.221 NED Migration : Skipping Ned migration for the device NETSIM-DEVICE-1
<INFO> 19-Dec-2021::15:51:09.221 NED Migration : Maapi transction Closed
<INFO> 19-Dec-2021::15:51:09.221 NED Migration : Ned Migration for:Device rtwr;dry-run: False;no-networking: True;
<INFO> 19-Dec-2021::15:51:09.223 NED Migration : Maapi transaction started
<ERROR> 19-Dec-2021::15:51:09.238 NED Migration : The Device rtwr is NOT onboarded
<INFO> 19-Dec-2021::15:51:09.238 NED Migration : Maapi transction Closed
<INFO> 19-Dec-2021::15:51:09.238 NED Migration : Ned Migration for:Device NETSIM-DEVICE-2;dry-run: False;no-networking: True;
<INFO> 19-Dec-2021::15:51:09.241 NED Migration : Maapi transaction started
<INFO> 19-Dec-2021::15:51:09.255 NED Migration : The Device NETSIM-DEVICE-2 is onboarded
<INFO> 19-Dec-2021::15:51:09.256 NED Migration : Ned version alu-sr-cli-8.17 is loaded
<INFO> 19-Dec-2021::15:51:09.259 NED Migration : Neds status: Current ned-id alu-sr-cli-8.13; Target ned-id: alu-sr-cli-8.17;
<INFO> 19-Dec-2021::15:51:09.259 NED Migration : Running Ned Migration for the device NETSIM-DEVICE-2 in dry-run mode
<WARNING> 19-Dec-2021::15:51:10.50 NED Migration : Modified Paths : The path that has been modified
<WARNING> 19-Dec-2021::15:51:10.50 NED Migration : Path: /devices/device[name='NETSIM-DEVICE-2']/config/alu:system/security/snmp/community ; Info: list key has changed
<WARNING> 19-Dec-2021::15:51:10.50 NED Migration : Path: /devices/device[name='NETSIM-DEVICE-2']/config/alu:router/policy-options/policy-statement/entry/from/protocol/protocol ; Info: leaf/leaf-list type has changed
<WARNING> 19-Dec-2021::15:51:10.50 NED Migration : Path: /devices/device[name='NETSIM-DEVICE-2']/config/alu:router/interface/bfd/type ; Info: leaf/leaf-list type has changed
<WARNING> 19-Dec-2021::15:51:10.50 NED Migration : Path: /devices/device[name='NETSIM-DEVICE-2']/config/alu:router/interface/ipv6/urpf-check ; Info: node type has changed from non-presence container to presence container
<WARNING> 19-Dec-2021::15:51:10.50 NED Migration : Path: /devices/device[name='NETSIM-DEVICE-2']/config/alu:service/vprn/interface/ipv6/urpf-check ; Info: node type has changed from non-presence container to presence container
<WARNING> 19-Dec-2021::15:51:10.50 NED Migration : Path: /devices/device[name='NETSIM-DEVICE-2']/config/alu:service/ies/interface/ipv6/urpf-check ; Info: node type has changed from non-presence container to presence container
<WARNING> 19-Dec-2021::15:51:10.51 NED Migration : Path: /devices/device[name='NETSIM-DEVICE-2']/config/alu:qos/sap-ingress/dscp/id ; Info: leaf/leaf-list type has changed
<WARNING> 19-Dec-2021::15:51:10.51 NED Migration : Path: /devices/device[name='NETSIM-DEVICE-2']/config/alu:qos/sap-ingress/dscp ; Info: list key has changed; leaf 'id' has changed type
<INFO> 19-Dec-2021::15:51:10.51 NED Migration : Running Ned Migration for the device NETSIM-DEVICE-2
<INFO> 19-Dec-2021::15:51:10.51 NED Migration : Ned Migration completed successfully for the device NETSIM-DEVICE-2
<INFO> 19-Dec-2021::15:51:10.51 NED Migration : Maapi transction Closed
<INFO> 19-Dec-2021::15:51:55.856 NED Migration : Ned Migration for:Device SEGW-LIL2-2;dry-run: False;no-networking: True;
<INFO> 19-Dec-2021::15:51:55.860 NED Migration : Maapi transaction started
<INFO> 19-Dec-2021::15:51:55.878 NED Migration : The Device SEGW-LIL2-2 is onboarded
<INFO> 19-Dec-2021::15:51:55.880 NED Migration : Ned version alu-sr-cli-8.17 is loaded
<INFO> 19-Dec-2021::15:51:55.883 NED Migration : Neds status: Current ned-id alu-sr-cli-8.13; Target ned-id: alu-sr-cli-8.17;
<INFO> 19-Dec-2021::15:51:55.884 NED Migration : Running Ned Migration for the device SEGW-LIL2-2 in dry-run mode
<WARNING> 19-Dec-2021::15:51:56.520 NED Migration : Modified Paths : The path that has been modified
<WARNING> 19-Dec-2021::15:51:56.520 NED Migration : Path: /devices/device[name='SEGW-LIL2-2']/config/alu:system/security/snmp/community ; Info: list key has changed
<WARNING> 19-Dec-2021::15:51:56.520 NED Migration : Path: /devices/device[name='SEGW-LIL2-2']/config/alu:router/policy-options/policy-statement/entry/from/protocol/protocol ; Info: leaf/leaf-list type has changed
<WARNING> 19-Dec-2021::15:51:56.520 NED Migration : Path: /devices/device[name='SEGW-LIL2-2']/config/alu:router/interface/bfd/type ; Info: leaf/leaf-list type has changed
<WARNING> 19-Dec-2021::15:51:56.520 NED Migration : Path: /devices/device[name='SEGW-LIL2-2']/config/alu:router/interface/ipv6/urpf-check ; Info: node type has changed from non-presence container to presence container
<WARNING> 19-Dec-2021::15:51:56.520 NED Migration : Path: /devices/device[name='SEGW-LIL2-2']/config/alu:service/vprn/interface/ipv6/urpf-check ; Info: node type has changed from non-presence container to presence container
<WARNING> 19-Dec-2021::15:51:56.521 NED Migration : Path: /devices/device[name='SEGW-LIL2-2']/config/alu:service/ies/interface/ipv6/urpf-check ; Info: node type has changed from non-presence container to presence container
<WARNING> 19-Dec-2021::15:51:56.521 NED Migration : Path: /devices/device[name='SEGW-LIL2-2']/config/alu:qos/sap-ingress/dscp/id ; Info: leaf/leaf-list type has changed
<WARNING> 19-Dec-2021::15:51:56.521 NED Migration : Path: /devices/device[name='SEGW-LIL2-2']/config/alu:qos/sap-ingress/dscp ; Info: list key has changed; leaf 'id' has changed type
<WARNING> 19-Dec-2021::15:51:56.521 NED Migration : Affected services : The service instances/points that touches the migrated device SEGW-LIL2-2
<CRITICAL> 19-Dec-2021::15:51:56.521 NED Migration : 1 : /l3vpn[instance='volvo2'][device='SEGW-LIL2-2']
<WARNING> 19-Dec-2021::15:51:56.521 NED Migration : Affected services with changes: the service instances/pointsthat are affected by the data model changes on the migrated device. that touches the migrated device SEGW-LIL2-2
<INFO> 19-Dec-2021::15:51:56.521 NED Migration : There are 1 affected instances by this Ned Migration on SEGW-LIL2-2
<INFO> 19-Dec-2021::15:51:56.521 NED Migration : There are 0 affected instances by this Ned Migration on SEGW-LIL2-2
<INFO> 19-Dec-2021::15:51:57.332 NED Migration : Running user validation to continue with ned migration y/n/CANCEL
<INFO> 19-Dec-2021::15:51:57.333 NED Migration : User Input :  'CANCEL' : chosing to cancel ned migration and exist program
<INFO> 19-Dec-2021::15:51:57.333 NED Migration : Exiting...
<INFO> 19-Dec-2021::15:51:57.334 NED Migration : Writing migration report into file migration-12-19-2021-15:51:57.json
```
---

## JSON report:
```
{
    "NETSIM-DEVICE-2": {
        "options": {
            "dry-run": false,
            "no-networking": true,
            "verbose": true
        },
        "info": {
            "new-ned-id": "alu-sr-cli-8.17",
            "old-ned-id": "alu-sr-cli-8.13"
        },
        "prerequisites": {
            "device-onboarded": true,
            "ned-loaded": true,
            "device-not-already-migrated": true
        },
        "status": "Ned Migrated",
        "dry-run": {
            "modified-paths": {
                "deleted": {},
                "/devices/device[name='NETSIM-DEVICE-2']/config/alu:system/security/snmp/community": "list key has changed",
                "/devices/device[name='NETSIM-DEVICE-2']/config/alu:router/policy-options/policy-statement/entry/from/protocol/protocol": "leaf/leaf-list type has changed",
                "/devices/device[name='NETSIM-DEVICE-2']/config/alu:router/interface/bfd/type": "leaf/leaf-list type has changed",
                "/devices/device[name='NETSIM-DEVICE-2']/config/alu:router/interface/ipv6/urpf-check": "node type has changed from non-presence container to presence container",
                "/devices/device[name='NETSIM-DEVICE-2']/config/alu:service/vprn/interface/ipv6/urpf-check": "node type has changed from non-presence container to presence container",
                "/devices/device[name='NETSIM-DEVICE-2']/config/alu:service/ies/interface/ipv6/urpf-check": "node type has changed from non-presence container to presence container",
                "/devices/device[name='NETSIM-DEVICE-2']/config/alu:qos/sap-ingress/dscp/id": "leaf/leaf-list type has changed",
                "/devices/device[name='NETSIM-DEVICE-2']/config/alu:qos/sap-ingress/dscp": "list key has changed; leaf 'id' has changed type"
            }
        }
    },
    "NETSIM-DEVICE-1": {
        "options": {
            "dry-run": false,
            "no-networking": true,
            "verbose": true
        },
        "info": {
            "new-ned-id": "alu-sr-cli-8.17",
            "old-ned-id": "alu-sr-cli-8.13"
        },
        "prerequisites": {
            "device-onboarded": true,
            "ned-loaded": true,
            "device-not-already-migrated": true
        },
        "status": "simulated",
        "dry-run": {
            "modified-paths": {
                "deleted": {},
                "/devices/device[name='NETSIM-DEVICE-1']/config/alu:system/security/snmp/community": "list key has changed",
                "/devices/device[name='NETSIM-DEVICE-1']/config/alu:router/policy-options/policy-statement/entry/from/protocol/protocol": "leaf/leaf-list type has changed",
                "/devices/device[name='NETSIM-DEVICE-1']/config/alu:router/interface/bfd/type": "leaf/leaf-list type has changed",
                "/devices/device[name='NETSIM-DEVICE-1']/config/alu:router/interface/ipv6/urpf-check": "node type has changed from non-presence container to presence container",
                "/devices/device[name='NETSIM-DEVICE-1']/config/alu:service/vprn/interface/ipv6/urpf-check": "node type has changed from non-presence container to presence container",
                "/devices/device[name='NETSIM-DEVICE-1']/config/alu:service/ies/interface/ipv6/urpf-check": "node type has changed from non-presence container to presence container",
                "/devices/device[name='NETSIM-DEVICE-1']/config/alu:qos/sap-ingress/dscp/id": "leaf/leaf-list type has changed",
                "/devices/device[name='NETSIM-DEVICE-1']/config/alu:qos/sap-ingress/dscp": "list key has changed; leaf 'id' has changed type"
            },
            "affected-services": {
                "1": "/l3vpn[instance='volvo'][device='NETSIM-DEVICE-1']"
            },
            "affected-services-with-changes": {}
        }
    }
}
```

## Upcoming Web UI:
- Web UI for a better user experience
- Generates statistics of the NED migrations( success/failure)
- Contains other devices management functionnalities
- Support import of devices lists
