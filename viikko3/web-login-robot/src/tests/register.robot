*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset Application And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  kalle
    Set Register Password  kalle123  kalle123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  k
    Set Register Password  kalle123  kalle123
    Submit Credentials
    Register Should Fail With Message  Username too short

Register With Valid Username And Too Short Password
    Set Username  kalle
    Set Register Password  kal123  kal123
    Submit Credentials
    Register Should Fail With Message  Invalid password

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle
    Set Register Password  kalle123  123kalle
    Submit Credentials
    Register Should Fail With Message  Passwords do not match

Login After Successful Registration
    Set Username  kalle
    Set Register Password  kalle123  kalle123
    Submit Credentials
    Register Should Succeed
    
    Go To Login Page
    Set Username  kalle
    Set Password  kalle123
    Submit Login Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  k
    Set Register Password  kle123  123kal
    Submit Credentials

    Go To Login Page
    Set Username  k
    Set Password  kle123
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password

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

Set Register Password
    [Arguments]  ${password}  ${confirmation}
    Input Password  password  ${password}
    Input Password  password_confirmation  ${confirmation}