param([string] $install)

Write-Output "Trying to install $install";
pip install $install;

Write-Output "Updating requirements file";
Write-Output (pip freeze) > .\requirements.txt;