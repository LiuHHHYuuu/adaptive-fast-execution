$content = Get-Content -Raw (Join-Path $PSScriptRoot 'index.html')
if ($content -notmatch '>Submit<') {
    throw 'Expected the button label to be Submit.'
}
if ($content -match '>Save<') {
    throw 'The old Save label is still present.'
}
Write-Output 'PASS: button label is Submit'

