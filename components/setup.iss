; -- Inno Setup Script for Tip Calculator Pro Installer --

[Setup]
AppName=Tip Calculator Pro
AppVersion=1.0
DefaultDirName={commonpf}\Tip Calculator Pro
DefaultGroupName=Tip Calculator Pro
OutputBaseFilename=TipCalculatorProSetup
Compression=lzma
SolidCompression=yes

[Files]
Source: "main.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "tip.ico"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\Tip Calculator Pro"; Filename: "{app}\main.exe"; IconFilename: "{app}\tip.ico"
Name: "{userdesktop}\Tip Calculator Pro"; Filename: "{app}\main.exe"; IconFilename: "{app}\tip.ico"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Create a &desktop icon"; GroupDescription: "Additional icons:"

[Registry]
; Add registry entries if needed
Root: HKCU; Subkey: "Software\Tip Calculator Pro"; ValueType: string; ValueData: "Installed"; Flags: uninsdeletevalue
Root: HKCU; Subkey: "Software\Tip Calculator Pro"; Flags: uninsdeletekey

[UninstallDelete]
; Remove files and directories on uninstall
Type: filesandordirs; Name: "{app}"
