# SFR Ned Migration utility :
[![forthebadge](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxODQuODciIGhlaWdodD0iMzUiIHZpZXdCb3g9IjAgMCAxODQuODcgMzUiPjxyZWN0IGNsYXNzPSJzdmdfX3JlY3QiIHg9IjAiIHk9IjAiIHdpZHRoPSIxMDguMDUiIGhlaWdodD0iMzUiIGZpbGw9IiMzMUM0RjMiLz48cmVjdCBjbGFzcz0ic3ZnX19yZWN0IiB4PSIxMDYuMDUiIHk9IjAiIHdpZHRoPSI3OC44MiIgaGVpZ2h0PSIzNSIgZmlsbD0iIzM4OUFENSIvPjxwYXRoIGNsYXNzPSJzdmdfX3RleHQiIGQ9Ik0xNy4zMyAyMkwxNC4yMiAyMkwxNC4yMiAxMy40N0wxNy4xNCAxMy40N1ExOC41OSAxMy40NyAxOS4zNCAxNC4wNVEyMC4xMCAxNC42MyAyMC4xMCAxNS43OEwyMC4xMCAxNS43OFEyMC4xMCAxNi4zNiAxOS43OCAxNi44M1ExOS40NyAxNy4zMCAxOC44NiAxNy41NkwxOC44NiAxNy41NlExOS41NSAxNy43NSAxOS45MyAxOC4yNlEyMC4zMSAxOC43OCAyMC4zMSAxOS41MUwyMC4zMSAxOS41MVEyMC4zMSAyMC43MSAxOS41MyAyMS4zNlExOC43NiAyMiAxNy4zMyAyMkwxNy4zMyAyMlpNMTUuNzAgMTguMTVMMTUuNzAgMjAuODJMMTcuMzUgMjAuODJRMTguMDQgMjAuODIgMTguNDQgMjAuNDdRMTguODMgMjAuMTMgMTguODMgMTkuNTFMMTguODMgMTkuNTFRMTguODMgMTguMTggMTcuNDcgMTguMTVMMTcuNDcgMTguMTVMMTUuNzAgMTguMTVaTTE1LjcwIDE0LjY2TDE1LjcwIDE3LjA2TDE3LjE1IDE3LjA2UTE3Ljg0IDE3LjA2IDE4LjIzIDE2Ljc1UTE4LjYyIDE2LjQzIDE4LjYyIDE1Ljg2TDE4LjYyIDE1Ljg2UTE4LjYyIDE1LjIzIDE4LjI2IDE0Ljk1UTE3LjkwIDE0LjY2IDE3LjE0IDE0LjY2TDE3LjE0IDE0LjY2TDE1LjcwIDE0LjY2Wk0yNC42NCAxOS4xNkwyNC42NCAxOS4xNkwyNC42NCAxMy40N0wyNi4xMiAxMy40N0wyNi4xMiAxOS4xOFEyNi4xMiAyMC4wMyAyNi41NSAyMC40OFEyNi45OCAyMC45MyAyNy44MyAyMC45M0wyNy44MyAyMC45M1EyOS41NCAyMC45MyAyOS41NCAxOS4xM0wyOS41NCAxOS4xM0wyOS41NCAxMy40N0wzMS4wMiAxMy40N0wzMS4wMiAxOS4xN1EzMS4wMiAyMC41MyAzMC4xNSAyMS4zMlEyOS4yOCAyMi4xMiAyNy44MyAyMi4xMkwyNy44MyAyMi4xMlEyNi4zNiAyMi4xMiAyNS41MCAyMS4zM1EyNC42NCAyMC41NSAyNC42NCAxOS4xNlpNMzcuMTUgMjJMMzUuNjcgMjJMMzUuNjcgMTMuNDdMMzcuMTUgMTMuNDdMMzcuMTUgMjJaTTQ3LjMyIDIyTDQxLjk2IDIyTDQxLjk2IDEzLjQ3TDQzLjQ0IDEzLjQ3TDQzLjQ0IDIwLjgyTDQ3LjMyIDIwLjgyTDQ3LjMyIDIyWk01My4xMiAxNC42Nkw1MC40OSAxNC42Nkw1MC40OSAxMy40N0w1Ny4yNSAxMy40N0w1Ny4yNSAxNC42Nkw1NC41OSAxNC42Nkw1NC41OSAyMkw1My4xMiAyMkw1My4xMiAxNC42NlpNNjguNDcgMjJMNjYuOTkgMjJMNjYuOTkgMTMuNDdMNzIuNDEgMTMuNDdMNzIuNDEgMTQuNjZMNjguNDcgMTQuNjZMNjguNDcgMTcuMjBMNzEuOTAgMTcuMjBMNzEuOTAgMTguMzhMNjguNDcgMTguMzhMNjguNDcgMjJaTTc2LjMwIDE4LjAwTDc2LjMwIDE4LjAwTDc2LjMwIDE3LjUyUTc2LjMwIDE2LjI4IDc2Ljc0IDE1LjMyUTc3LjE4IDE0LjM3IDc3Ljk5IDEzLjg2UTc4Ljc5IDEzLjM1IDc5Ljg0IDEzLjM1UTgwLjg4IDEzLjM1IDgxLjY4IDEzLjg1UTgyLjQ5IDE0LjM1IDgyLjkzIDE1LjI5UTgzLjM3IDE2LjIzIDgzLjM4IDE3LjQ4TDgzLjM4IDE3LjQ4TDgzLjM4IDE3Ljk2UTgzLjM4IDE5LjIxIDgyLjk0IDIwLjE2UTgyLjUxIDIxLjEwIDgxLjcwIDIxLjYxUTgwLjkwIDIyLjEyIDc5Ljg1IDIyLjEyTDc5Ljg1IDIyLjEyUTc4LjgxIDIyLjEyIDc4LjAwIDIxLjYxUTc3LjE5IDIxLjEwIDc2Ljc1IDIwLjE3UTc2LjMwIDE5LjIzIDc2LjMwIDE4LjAwWk03Ny43OCAxNy40Nkw3Ny43OCAxNy45NlE3Ny43OCAxOS4zNiA3OC4zMyAyMC4xM1E3OC44OCAyMC45MCA3OS44NSAyMC45MEw3OS44NSAyMC45MFE4MC44MyAyMC45MCA4MS4zNiAyMC4xNVE4MS44OSAxOS40MCA4MS44OSAxNy45Nkw4MS44OSAxNy45Nkw4MS44OSAxNy41MVE4MS44OSAxNi4wOSA4MS4zNiAxNS4zNFE4MC44MiAxNC41OCA3OS44NCAxNC41OEw3OS44NCAxNC41OFE3OC44OCAxNC41OCA3OC4zMyAxNS4zM1E3Ny43OSAxNi4wOSA3Ny43OCAxNy40Nkw3Ny43OCAxNy40NlpNODkuMzIgMjJMODcuODQgMjJMODcuODQgMTMuNDdMOTAuODQgMTMuNDdROTIuMzIgMTMuNDcgOTMuMTIgMTQuMTNROTMuOTIgMTQuNzkgOTMuOTIgMTYuMDVMOTMuOTIgMTYuMDVROTMuOTIgMTYuOTAgOTMuNTEgMTcuNDhROTMuMTAgMTguMDYgOTIuMzYgMTguMzdMOTIuMzYgMTguMzdMOTQuMjcgMjEuOTJMOTQuMjcgMjJMOTIuNjkgMjJMOTAuOTcgMTguNzFMODkuMzIgMTguNzFMODkuMzIgMjJaTTg5LjMyIDE0LjY2TDg5LjMyIDE3LjUyTDkwLjg1IDE3LjUyUTkxLjYwIDE3LjUyIDkyLjAyIDE3LjE1UTkyLjQ0IDE2Ljc3IDkyLjQ0IDE2LjExTDkyLjQ0IDE2LjExUTkyLjQ0IDE1LjQzIDkyLjA1IDE1LjA1UTkxLjY2IDE0LjY4IDkwLjg5IDE0LjY2TDkwLjg5IDE0LjY2TDg5LjMyIDE0LjY2WiIgZmlsbD0iI0ZGRkZGRiIvPjxwYXRoIGNsYXNzPSJzdmdfX3RleHQiIGQ9Ik0xMTkuODEgMTcuODBMMTE5LjgxIDE3LjgwUTExOS44MSAxNi41NCAxMjAuNDEgMTUuNTRRMTIxLjAxIDE0LjU1IDEyMi4wNiAxMy45OVExMjMuMTEgMTMuNDMgMTI0LjQzIDEzLjQzTDEyNC40MyAxMy40M1ExMjUuNTggMTMuNDMgMTI2LjUwIDEzLjg0UTEyNy40MyAxNC4yNSAxMjguMDQgMTUuMDJMMTI4LjA0IDE1LjAyTDEyNi41MyAxNi4zOVExMjUuNzIgMTUuNDAgMTI0LjU1IDE1LjQwTDEyNC41NSAxNS40MFExMjMuODYgMTUuNDAgMTIzLjMzIDE1LjcwUTEyMi44MCAxNiAxMjIuNTAgMTYuNTRRMTIyLjIxIDE3LjA5IDEyMi4yMSAxNy44MEwxMjIuMjEgMTcuODBRMTIyLjIxIDE4LjUxIDEyMi41MCAxOS4wNVExMjIuODAgMTkuNjAgMTIzLjMzIDE5LjkwUTEyMy44NiAyMC4yMCAxMjQuNTUgMjAuMjBMMTI0LjU1IDIwLjIwUTEyNS43MiAyMC4yMCAxMjYuNTMgMTkuMjJMMTI2LjUzIDE5LjIyTDEyOC4wNCAyMC41OFExMjcuNDMgMjEuMzUgMTI2LjUxIDIxLjc2UTEyNS41OCAyMi4xNyAxMjQuNDMgMjIuMTdMMTI0LjQzIDIyLjE3UTEyMy4xMSAyMi4xNyAxMjIuMDYgMjEuNjFRMTIxLjAxIDIxLjA1IDEyMC40MSAyMC4wNVExMTkuODEgMTkuMDYgMTE5LjgxIDE3LjgwWk0xMzQuOTYgMjJMMTMyLjU4IDIyTDEzMi41OCAxMy42MEwxMzQuOTYgMTMuNjBMMTM0Ljk2IDIyWk0xMzkuNTQgMjEuMjRMMTM5LjU0IDIxLjI0TDE0MC4zMiAxOS40OVExNDAuODkgMTkuODYgMTQxLjYzIDIwLjA5UTE0Mi4zNyAyMC4zMiAxNDMuMTAgMjAuMzJMMTQzLjEwIDIwLjMyUTE0NC40NiAyMC4zMiAxNDQuNDcgMTkuNjRMMTQ0LjQ3IDE5LjY0UTE0NC40NyAxOS4yOCAxNDQuMDggMTkuMTFRMTQzLjY5IDE4LjkzIDE0Mi44MiAxOC43NEwxNDIuODIgMTguNzRRMTQxLjg3IDE4LjUzIDE0MS4yMyAxOC4zMFExNDAuNjAgMTguMDYgMTQwLjE1IDE3LjU1UTEzOS42OSAxNy4wMyAxMzkuNjkgMTYuMTZMMTM5LjY5IDE2LjE2UTEzOS42OSAxNS4zOSAxNDAuMTEgMTQuNzdRMTQwLjUzIDE0LjE1IDE0MS4zNiAxMy43OVExNDIuMjAgMTMuNDMgMTQzLjQxIDEzLjQzTDE0My40MSAxMy40M1ExNDQuMjMgMTMuNDMgMTQ1LjA0IDEzLjYyUTE0NS44NCAxMy44MCAxNDYuNDYgMTQuMTdMMTQ2LjQ2IDE0LjE3TDE0NS43MyAxNS45M1ExNDQuNTMgMTUuMjggMTQzLjM5IDE1LjI4TDE0My4zOSAxNS4yOFExNDIuNjkgMTUuMjggMTQyLjM2IDE1LjQ5UTE0Mi4wNCAxNS43MCAxNDIuMDQgMTYuMDRMMTQyLjA0IDE2LjA0UTE0Mi4wNCAxNi4zNyAxNDIuNDIgMTYuNTRRMTQyLjgxIDE2LjcxIDE0My42NiAxNi44OUwxNDMuNjYgMTYuODlRMTQ0LjYyIDE3LjEwIDE0NS4yNSAxNy4zM1ExNDUuODggMTcuNTYgMTQ2LjM0IDE4LjA3UTE0Ni44MCAxOC41OCAxNDYuODAgMTkuNDZMMTQ2LjgwIDE5LjQ2UTE0Ni44MCAyMC4yMSAxNDYuMzkgMjAuODNRMTQ1Ljk3IDIxLjQ0IDE0NS4xMyAyMS44MFExNDQuMjggMjIuMTcgMTQzLjA4IDIyLjE3TDE0My4wOCAyMi4xN1ExNDIuMDYgMjIuMTcgMTQxLjEwIDIxLjkyUTE0MC4xNCAyMS42NyAxMzkuNTQgMjEuMjRaTTE1MC45NSAxNy44MEwxNTAuOTUgMTcuODBRMTUwLjk1IDE2LjU0IDE1MS41NSAxNS41NFExNTIuMTUgMTQuNTUgMTUzLjIwIDEzLjk5UTE1NC4yNSAxMy40MyAxNTUuNTcgMTMuNDNMMTU1LjU3IDEzLjQzUTE1Ni43MiAxMy40MyAxNTcuNjUgMTMuODRRMTU4LjU3IDE0LjI1IDE1OS4xOSAxNS4wMkwxNTkuMTkgMTUuMDJMMTU3LjY3IDE2LjM5UTE1Ni44NiAxNS40MCAxNTUuNjkgMTUuNDBMMTU1LjY5IDE1LjQwUTE1NS4wMSAxNS40MCAxNTQuNDcgMTUuNzBRMTUzLjk0IDE2IDE1My42NSAxNi41NFExNTMuMzUgMTcuMDkgMTUzLjM1IDE3LjgwTDE1My4zNSAxNy44MFExNTMuMzUgMTguNTEgMTUzLjY1IDE5LjA1UTE1My45NCAxOS42MCAxNTQuNDcgMTkuOTBRMTU1LjAxIDIwLjIwIDE1NS42OSAyMC4yMEwxNTUuNjkgMjAuMjBRMTU2Ljg2IDIwLjIwIDE1Ny42NyAxOS4yMkwxNTcuNjcgMTkuMjJMMTU5LjE5IDIwLjU4UTE1OC41OCAyMS4zNSAxNTcuNjUgMjEuNzZRMTU2LjcyIDIyLjE3IDE1NS41NyAyMi4xN0wxNTUuNTcgMjIuMTdRMTU0LjI1IDIyLjE3IDE1My4yMCAyMS42MVExNTIuMTUgMjEuMDUgMTUxLjU1IDIwLjA1UTE1MC45NSAxOS4wNiAxNTAuOTUgMTcuODBaTTE2My4yOSAxNy44MEwxNjMuMjkgMTcuODBRMTYzLjI5IDE2LjU1IDE2My45MCAxNS41NVExNjQuNTAgMTQuNTYgMTY1LjU2IDE0LjAwUTE2Ni42MyAxMy40MyAxNjcuOTYgMTMuNDNMMTY3Ljk2IDEzLjQzUTE2OS4yOSAxMy40MyAxNzAuMzUgMTQuMDBRMTcxLjQxIDE0LjU2IDE3Mi4wMiAxNS41NVExNzIuNjMgMTYuNTUgMTcyLjYzIDE3LjgwTDE3Mi42MyAxNy44MFExNzIuNjMgMTkuMDUgMTcyLjAyIDIwLjA0UTE3MS40MSAyMS4wNCAxNzAuMzUgMjEuNjBRMTY5LjI5IDIyLjE3IDE2Ny45NiAyMi4xN0wxNjcuOTYgMjIuMTdRMTY2LjYzIDIyLjE3IDE2NS41NiAyMS42MFExNjQuNTAgMjEuMDQgMTYzLjkwIDIwLjA0UTE2My4yOSAxOS4wNSAxNjMuMjkgMTcuODBaTTE2NS42OSAxNy44MEwxNjUuNjkgMTcuODBRMTY1LjY5IDE4LjUxIDE2NS45OSAxOS4wNVExNjYuMjkgMTkuNjAgMTY2LjgxIDE5LjkwUTE2Ny4zMiAyMC4yMCAxNjcuOTYgMjAuMjBMMTY3Ljk2IDIwLjIwUTE2OC42MCAyMC4yMCAxNjkuMTEgMTkuOTBRMTY5LjYzIDE5LjYwIDE2OS45MyAxOS4wNVExNzAuMjIgMTguNTEgMTcwLjIyIDE3LjgwTDE3MC4yMiAxNy44MFExNzAuMjIgMTcuMDkgMTY5LjkzIDE2LjU0UTE2OS42MyAxNiAxNjkuMTEgMTUuNzBRMTY4LjYwIDE1LjQwIDE2Ny45NiAxNS40MEwxNjcuOTYgMTUuNDBRMTY3LjMyIDE1LjQwIDE2Ni44MSAxNS43MFExNjYuMjkgMTYgMTY1Ljk5IDE2LjU0UTE2NS42OSAxNy4wOSAxNjUuNjkgMTcuODBaIiBmaWxsPSIjRkZGRkZGIiB4PSIxMTkuMDUiLz48L3N2Zz4=)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
---
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


    usage: ned_migration.py [-h] [--dry-run] [--no-networking] --new-ned-id
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
```
* ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ *

[*] Ned Migration for:
        [!] Device SEGW-VAL3-1
        [!] dry-run: False
        [!] no-networking: True

* ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ *

[*] The Device SEGW-VAL3-1 is onboarded

* ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ *

[*] Ned version alu-sr-cli-8.17 is loaded

* ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ *

[*] Info:
        [!] Current ned-id alu-sr-cli-8.13
        [!] Target ned-id: alu-sr-cli-8.17


* ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ *

[*]Running Ned Migration for the device SEGW-VAL3-1 in dry-run mode

        [!] Modified Paths : The path that has been modified.

                Path: /devices/device[name='SEGW-VAL3-1']/config/alu:system/security/snmp/community
                Info: list key has changed
                Path: /devices/device[name='SEGW-VAL3-1']/config/alu:router/policy-options/policy-statement/entry/from/protocol/protocol
                Info: leaf/leaf-list type has changed
                Path: /devices/device[name='SEGW-VAL3-1']/config/alu:router/interface/bfd/type
                Info: leaf/leaf-list type has changed
                Path: /devices/device[name='SEGW-VAL3-1']/config/alu:router/interface/ipv6/urpf-check
                Info: node type has changed from non-presence container to presence container
                Path: /devices/device[name='SEGW-VAL3-1']/config/alu:service/vprn/interface/ipv6/urpf-check
                Info: node type has changed from non-presence container to presence container
                Path: /devices/device[name='SEGW-VAL3-1']/config/alu:service/ies/interface/ipv6/urpf-check
                Info: node type has changed from non-presence container to presence container
                Path: /devices/device[name='SEGW-VAL3-1']/config/alu:qos/sap-ingress/dscp/id
                Info: leaf/leaf-list type has changed
                Path: /devices/device[name='SEGW-VAL3-1']/config/alu:qos/sap-ingress/dscp
                Info: list key has changed; leaf 'id' has changed type
        [!] Affected services : The service instances/points that touches the migrated device SEGW-VAL3-1

                [1]/configure_ipsecgw[num_ipsecgw='28'][device='SEGW-VAL3-1'] 

        [!] Affected services with changes: the service instances/pointsthat are affected by the data model 
                 changes on the migrated device. that touches the migrated device SEGW-VAL3-1


* ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ *

[?] There are 1 affected instances by this Ned Migration on SEGW-VAL3-1
[?] There are 0 affected instances with changes by this Ned Migration on SEGW-VAL3-1
[?] Would you like to continue with the Ned migration?
(y/n/CANCEL)
y

* ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ *

[*] Running Ned Migration for the device SEGW-VAL3-1
[*] Ned Migration completed successfully for the device SEGW-VAL3-1
[*] Writing migration report into file migration-12-21-2021-11:32:08.json 

* ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ *
[                                                         ] 100 %
```

## ned-migration-device.log:
```
<INFO> 19-Dec-2021::15:51:09.181 NED Migration : Starting...
<INFO> 19-Dec-2021::15:51:09.181 NED Migration : Ned Migration Utility v1.2
<INFO> 19-Dec-2021::15:51:09.181 NED Migration : Reading devices list file...
<INFO> 19-Dec-2021::15:51:09.181 NED Migration : Ned Migration for:Device SEGW-ABG2-1;dry-run: False;no-networking: True;
<INFO> 19-Dec-2021::15:51:09.189 NED Migration : Maapi transaction started
<INFO> 19-Dec-2021::15:51:09.215 NED Migration : The Device SEGW-ABG2-1 is onboarded
<INFO> 19-Dec-2021::15:51:09.216 NED Migration : Ned version alu-sr-cli-8.17 is loaded
<INFO> 19-Dec-2021::15:51:09.220 NED Migration : Neds status: Current ned-id alu-sr-cli-8.17; Target ned-id: alu-sr-cli-8.17;
<WARNING> 19-Dec-2021::15:51:09.220 NED Migration : The device SEGW-ABG2-1 is already with the ned-id alu-sr-cli-8.17
<WARNING> 19-Dec-2021::15:51:09.221 NED Migration : Skipping Ned migration for the device SEGW-ABG2-1
<INFO> 19-Dec-2021::15:51:09.221 NED Migration : Maapi transction Closed
<INFO> 19-Dec-2021::15:51:09.221 NED Migration : Ned Migration for:Device rtwr;dry-run: False;no-networking: True;
<INFO> 19-Dec-2021::15:51:09.223 NED Migration : Maapi transaction started
<ERROR> 19-Dec-2021::15:51:09.238 NED Migration : The Device rtwr is NOT onboarded
<INFO> 19-Dec-2021::15:51:09.238 NED Migration : Maapi transction Closed
<INFO> 19-Dec-2021::15:51:09.238 NED Migration : Ned Migration for:Device SEGW-ABG2-2;dry-run: False;no-networking: True;
<INFO> 19-Dec-2021::15:51:09.241 NED Migration : Maapi transaction started
<INFO> 19-Dec-2021::15:51:09.255 NED Migration : The Device SEGW-ABG2-2 is onboarded
<INFO> 19-Dec-2021::15:51:09.256 NED Migration : Ned version alu-sr-cli-8.17 is loaded
<INFO> 19-Dec-2021::15:51:09.259 NED Migration : Neds status: Current ned-id alu-sr-cli-8.13; Target ned-id: alu-sr-cli-8.17;
<INFO> 19-Dec-2021::15:51:09.259 NED Migration : Running Ned Migration for the device SEGW-ABG2-2 in dry-run mode
<WARNING> 19-Dec-2021::15:51:10.50 NED Migration : Modified Paths : The path that has been modified
<WARNING> 19-Dec-2021::15:51:10.50 NED Migration : Path: /devices/device[name='SEGW-ABG2-2']/config/alu:system/security/snmp/community ; Info: list key has changed
<WARNING> 19-Dec-2021::15:51:10.50 NED Migration : Path: /devices/device[name='SEGW-ABG2-2']/config/alu:router/policy-options/policy-statement/entry/from/protocol/protocol ; Info: leaf/leaf-list type has changed
<WARNING> 19-Dec-2021::15:51:10.50 NED Migration : Path: /devices/device[name='SEGW-ABG2-2']/config/alu:router/interface/bfd/type ; Info: leaf/leaf-list type has changed
<WARNING> 19-Dec-2021::15:51:10.50 NED Migration : Path: /devices/device[name='SEGW-ABG2-2']/config/alu:router/interface/ipv6/urpf-check ; Info: node type has changed from non-presence container to presence container
<WARNING> 19-Dec-2021::15:51:10.50 NED Migration : Path: /devices/device[name='SEGW-ABG2-2']/config/alu:service/vprn/interface/ipv6/urpf-check ; Info: node type has changed from non-presence container to presence container
<WARNING> 19-Dec-2021::15:51:10.50 NED Migration : Path: /devices/device[name='SEGW-ABG2-2']/config/alu:service/ies/interface/ipv6/urpf-check ; Info: node type has changed from non-presence container to presence container
<WARNING> 19-Dec-2021::15:51:10.51 NED Migration : Path: /devices/device[name='SEGW-ABG2-2']/config/alu:qos/sap-ingress/dscp/id ; Info: leaf/leaf-list type has changed
<WARNING> 19-Dec-2021::15:51:10.51 NED Migration : Path: /devices/device[name='SEGW-ABG2-2']/config/alu:qos/sap-ingress/dscp ; Info: list key has changed; leaf 'id' has changed type
<INFO> 19-Dec-2021::15:51:10.51 NED Migration : Running Ned Migration for the device SEGW-ABG2-2
<INFO> 19-Dec-2021::15:51:10.51 NED Migration : Ned Migration completed successfully for the device SEGW-ABG2-2
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
<CRITICAL> 19-Dec-2021::15:51:56.521 NED Migration : 1 : /configure_ipsecgw[num_ipsecgw='161'][device='SEGW-LIL2-2']
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
    "SEGW-ABG2-2": {
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
                "/devices/device[name='SEGW-ABG2-2']/config/alu:system/security/snmp/community": "list key has changed",
                "/devices/device[name='SEGW-ABG2-2']/config/alu:router/policy-options/policy-statement/entry/from/protocol/protocol": "leaf/leaf-list type has changed",
                "/devices/device[name='SEGW-ABG2-2']/config/alu:router/interface/bfd/type": "leaf/leaf-list type has changed",
                "/devices/device[name='SEGW-ABG2-2']/config/alu:router/interface/ipv6/urpf-check": "node type has changed from non-presence container to presence container",
                "/devices/device[name='SEGW-ABG2-2']/config/alu:service/vprn/interface/ipv6/urpf-check": "node type has changed from non-presence container to presence container",
                "/devices/device[name='SEGW-ABG2-2']/config/alu:service/ies/interface/ipv6/urpf-check": "node type has changed from non-presence container to presence container",
                "/devices/device[name='SEGW-ABG2-2']/config/alu:qos/sap-ingress/dscp/id": "leaf/leaf-list type has changed",
                "/devices/device[name='SEGW-ABG2-2']/config/alu:qos/sap-ingress/dscp": "list key has changed; leaf 'id' has changed type"
            }
        }
    },
    "SEGW-VAL3-1": {
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
                "/devices/device[name='SEGW-VAL3-1']/config/alu:system/security/snmp/community": "list key has changed",
                "/devices/device[name='SEGW-VAL3-1']/config/alu:router/policy-options/policy-statement/entry/from/protocol/protocol": "leaf/leaf-list type has changed",
                "/devices/device[name='SEGW-VAL3-1']/config/alu:router/interface/bfd/type": "leaf/leaf-list type has changed",
                "/devices/device[name='SEGW-VAL3-1']/config/alu:router/interface/ipv6/urpf-check": "node type has changed from non-presence container to presence container",
                "/devices/device[name='SEGW-VAL3-1']/config/alu:service/vprn/interface/ipv6/urpf-check": "node type has changed from non-presence container to presence container",
                "/devices/device[name='SEGW-VAL3-1']/config/alu:service/ies/interface/ipv6/urpf-check": "node type has changed from non-presence container to presence container",
                "/devices/device[name='SEGW-VAL3-1']/config/alu:qos/sap-ingress/dscp/id": "leaf/leaf-list type has changed",
                "/devices/device[name='SEGW-VAL3-1']/config/alu:qos/sap-ingress/dscp": "list key has changed; leaf 'id' has changed type"
            },
            "affected-services": {
                "1": "/configure_ipsecgw[num_ipsecgw='28'][device='SEGW-VAL3-1']"
            },
            "affected-services-with-changes": {}
        }
    }
}
```
