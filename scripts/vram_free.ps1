# Prints free VRAM in GB on the 16 GB RX 9070 XT (total - sum of per-process dedicated usage).
# Used by run_sweep.sh as a pre-step guard (require >= 12 GB free before any GPU step).
$used = ((Get-Counter "\GPU Process Memory(*)\Dedicated Usage" -ErrorAction SilentlyContinue).CounterSamples |
         Measure-Object CookedValue -Sum).Sum
$totalGB = 16
$freeGB = [math]::Round($totalGB - ($used / 1GB), 1)
# force '.' decimal (system locale may be French -> ','), so awk/bash parse it
Write-Output ($freeGB.ToString([System.Globalization.CultureInfo]::InvariantCulture))
