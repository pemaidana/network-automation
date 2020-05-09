*** Settings ***

Library        OperatingSystem
Library        pyats.robot.pyATSRobot
Library        vlans_check.py
Library        connectivity_check_v2.py

*** Variables ***

${testbed_1}       testbed.yaml

*** Test Cases ***

T1_Initialize
    [Documentation]    Loading 'testbed'
    use testbed "${testbed_1}"

T1_CommonSetup
    [Documentation]    CommonSetup for vlans_check.py
    run testcase "vlans_check.CommonSetup"

