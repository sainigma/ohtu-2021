*** Settings ***
Resource  resource.robot

*** Test Cases ***
Register With Valid Username And Password
    Input New Command And Create User  kalle  kalle321
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input New Command And Create User  kalle  kalle123
    Input New Command And Create User  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input New Command And Create User  k  kalle123
    Output Should Contain  Username too short

Register With Valid Username And Too Short Password
    Input New Command And Create User  kalle  k
    Output Should Contain  Invalid password

Register With Valid Username And Long Enough Password Containing Only Letters
    Input New Command And Create User  kalle  password
    Output Should Contain  Invalid password

*** Keywords ***
Input New Command And Create User
    [Arguments]  ${username}  ${password}
    Input New Command
    Input Credentials  ${username}  ${password}