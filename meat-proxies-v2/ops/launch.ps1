param([string]$Script, [string]$PidFile)
$p = Start-Process -FilePath 'C:\Program Files\Git\bin\bash.exe' -ArgumentList '-lc', $Script -WindowStyle Hidden -PassThru
Set-Content -Path $PidFile -Value $p.Id
"launched pid $($p.Id)"
