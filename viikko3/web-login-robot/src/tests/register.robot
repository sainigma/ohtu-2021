*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset Application And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  kalle
    Set Password  kalle123
    Set PasswordConfirmation  kalle123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  k
    Set Password  kalle123
    Set PasswordConfirmation  kalle123
    Submit Credentials
    Register Should Fail With Message  Username too short

Register With Valid Username And Too Short Password
    Set Username  kalle
    Set Password  kal123
    Set PasswordConfirmation  kal123
    Submit Credentials
    Register Should Fail With Message  Invalid password

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle
    Set Password  kalle123
    Set PasswordConfirmation  123kalle
    Submit Credentials
    Register Should Fail With Message  Passwords do not match

*** Keywords ***

Reset Application And Go To Register Page
    Reset Application
    Go To Register Page

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set PasswordConfirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}