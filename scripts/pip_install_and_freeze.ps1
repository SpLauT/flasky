param([string] $install)

Write-Output "Trying to install $install";
pip install $install;

Write-Output "Updating requirements file";
pip freeze > .\requirements.txt;