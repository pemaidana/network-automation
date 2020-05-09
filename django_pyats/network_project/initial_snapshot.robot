# Take snapshot of the operational state of the device
# and save the output to a file

*** Settings ***
# Importing test libraries, resource files and variable files.
Library        ats.robot.pyATSRobot
Library        genie.libs.robot.GenieRobot


*** Variables ***
# Define the pyATS testbed file to use for this run
${testbed}     ../testbed.yaml 

*** Test Cases ***
# Creating test cases from available keywords.

Connect
    # Initializes the pyATS/Genie Testbed
    use genie testbed "${testbed}"

    # Connect to both devices
    connect to device "SW_CORE_1"

Profile the devices
    Profile the system for "config;interface;platform;routing;vlan" on devices "SW_CORE_1" as "./good_snapshot"
