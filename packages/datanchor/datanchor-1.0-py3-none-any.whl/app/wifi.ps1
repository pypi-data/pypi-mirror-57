# Clear all variables
$State = '' 
$SSID = '' 
$BSSID = '' 

#Run netsh command to get wirelss profile info
$output = netsh.exe wlan show interfaces

# State
$State_line = $output | Select-String -Pattern 'State'
$State = ($State_line -split ":")[-1].Trim()

if ($State -eq 'connected') {

    # SSID
    $SSID_line = $output | Select-String 'SSID'| select -First 1
    $SSID = ($SSID_line -split ":")[-1].Trim()

    $ssid_obj = '"' + "SSID_LOOKUP" + '"' + ":" + '"' + $SSID + '"' + ','

    # BSSID
    $BSSID_line = $output | Select-String -Pattern 'BSSID'
    $BSSID = ($BSSID_line -split ":", 2)[-1].Trim()

    $bssid_obj = '"' + "BSSID_LOOKUP" + '"' + ":" + '"' + $BSSID + '"'
}

Write-Output "{ $ssid_obj $bssid_obj }"