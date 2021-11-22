*** Settings ***
Resource  resource.robot
Test Setup  Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  petteri  punakuono2
    Output Should Contain  New user registered
Register With Already Taken Username And Valid Password
    Input Credentials  petteri  punakuono2
    Output Should Contain  New user registered
    Input New Command
    Input Credentials  petteri  punakuono2
    Output Should Contain  User with username petteri already exists
Register With Too Short Username And Valid Password
    Input Credentials  Li  puheenjohtaja2
    Output Should Contain  Username is not valid
Register With Valid Username And Too Short Password
    Input Credentials  petteri  puna
    Output Should Contain  Password is too short
Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  petteri  punakuono
    Output Should Contain  Password is not valid

*** Keywords ***
Input New Command
    Input  new