# Asks for each API key (hidden as you paste), then runs the agent.
function Read-Key($label) {
    $secure = Read-Host "Paste your $label key, then press Enter" -AsSecureString
    $plain = [Runtime.InteropServices.Marshal]::PtrToStringAuto(
        [Runtime.InteropServices.Marshal]::SecureStringToBSTR($secure))
    return $plain.Trim().Trim('"')
}

if (-not $env:ANTHROPIC_API_KEY) { $env:ANTHROPIC_API_KEY = Read-Key "Anthropic (sk-ant-...)" }
if (-not $env:TAVILY_API_KEY)    { $env:TAVILY_API_KEY    = Read-Key "Tavily (tvly-...)" }

python "$PSScriptRoot\video_editing_agent.py" @args
