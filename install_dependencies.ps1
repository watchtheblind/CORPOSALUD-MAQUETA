# Script to install Tesseract and Poppler for Payroll-OCR-Automation
# Run as Administrator for best results

Function Install-Dependencies {
    Write-Host "--- Checking System Dependencies ---" -ForegroundColor Cyan

    # 1. Check Tesseract
    $tesseract = Get-Command tesseract -ErrorAction SilentlyContinue
    if ($null -eq $tesseract) {
        Write-Host "[!] Tesseract not found. Installing via Winget..." -ForegroundColor Yellow
        # Install Tesseract OCR
        winget install UB-Mannheim.TesseractOCR --accept-source-agreements --accept-package-agreements
        Write-Host "[+] Tesseract installation triggered. Please complete the wizard if it appears." -ForegroundColor Green
    } else {
        Write-Host "[V] Tesseract is already installed at: $($tesseract.Source)" -ForegroundColor Green
    }

    # 2. Check Poppler (Usually distributed as binaries, so we check PATH)
    $poppler = Get-Command pdftocairo -ErrorAction SilentlyContinue
    if ($null -eq $poppler) {
        Write-Host "[!] Poppler not found in PATH." -ForegroundColor Yellow
        Write-Host "[i] Downloading Poppler binaries..." -ForegroundColor Cyan

        $url = "https://github.com/oschwartz10612/poppler-windows/releases/download/v24.02.0-0/Release-24.02.0-0.zip"
        $zipPath = "$env:TEMP\poppler.zip"
        $destPath = "C:\poppler"

        if (!(Test-Path $destPath)) { New-Item -ItemType Directory -Path $destPath }

        Invoke-WebRequest -Uri $url -OutFile $zipPath
        Expand-Archive -Path $zipPath -DestinationPath $destPath -Force

        # Add to User PATH
        $binPath = "$destPath\Library\bin"
        Write-Host "[+] Adding Poppler to PATH: $binPath" -ForegroundColor Green
        $oldPath = [Environment]::GetEnvironmentVariable("Path", "User")
        if ($oldPath -notlike "*poppler*") {
            [Environment]::SetEnvironmentVariable("Path", "$oldPath;$binPath", "User")
            $env:Path += ";$binPath"
        }
    } else {
        Write-Host "[V] Poppler is already in PATH." -ForegroundColor Green
    }

    # 3. Download Spanish Language Pack (spa.traineddata)
    $tessDataPath = "C:\Program Files\Tesseract-OCR\tessdata\spa.traineddata"
    if (!(Test-Path $tessDataPath)) {
        Write-Host "[i] Downloading Spanish language pack..." -ForegroundColor Cyan
        $spaUrl = "https://github.com/tesseract-ocr/tessdata/raw/main/spa.traineddata"

        try {
            Invoke-WebRequest -Uri $spaUrl -OutFile $tessDataPath -ErrorAction Stop
            Write-Host "[V] Spanish language pack installed." -ForegroundColor Green
        } catch {
            Write-Host "[!] Could not download language pack automatically. Please run PowerShell as Admin." -ForegroundColor Red
        }
    }

    Write-Host "--- Setup Complete! Please restart your Terminal/PyCharm ---" -ForegroundColor Cyan
}

Install-Dependencies