# Prints free dedicated VRAM in GB on the RX 9070 XT, '.'-decimal (locale-safe for bash/awk).
#
# total: true dedicated VRAM from the driver registry (HardwareInformation.qwMemorySize, a
#        64-bit accurate value). Win32_VideoController.AdapterRAM is a 32-bit field capped at
#        4 GB on >4 GB cards, so it is useless here.
# used:  \GPU Adapter Memory(*)\Dedicated Usage, MAX across adapter instances — the per-ADAPTER
#        aggregate (one number for the whole card). The previous version summed
#        \GPU Process Memory(*)\Dedicated Usage over ~47 per-process/per-LUID instances, which
#        double-counted ~3.5x: it reported 11.5 GB used / 4.5 GB free when the card actually had
#        ~3.2 GB used / ~12.7 GB free, which would make gpu_guard wait forever for the 1.5B/3B runs.

$total = 0
Get-ChildItem 'HKLM:\SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}' -ErrorAction SilentlyContinue | ForEach-Object {
    $p = Get-ItemProperty $_.PSPath -ErrorAction SilentlyContinue
    $m = $p.'HardwareInformation.qwMemorySize'
    if ($m -and ($m -gt $total)) { $total = [double]$m }
}
$totalGB = if ($total -gt 0) { $total / 1GB } else { 16 }

$used = ((Get-Counter "\GPU Adapter Memory(*)\Dedicated Usage" -ErrorAction SilentlyContinue).CounterSamples |
         Measure-Object CookedValue -Maximum).Maximum
if (-not $used) { $used = 0 }

$freeGB = [math]::Round($totalGB - ($used / 1GB), 1)
Write-Output ($freeGB.ToString([System.Globalization.CultureInfo]::InvariantCulture))
