*** Settings ***
Documentation     Test Position
Test Template     HelloPosition
Library           PositionLibrary.py

*** Test Cases ***      startingPositionX   startingPositionY 
SuperSimpleDefault      4                   4

*** Keywords ***
HelloPosition
    [Arguments]  ${startingPositionX}  ${startingPositionY}
    Initialize position     ${startingPositionX}  ${startingPositionY}
    Starting X coordinate should be    ${startingPositionX}
    Starting Y coordinate should be    ${startingPositionY}
