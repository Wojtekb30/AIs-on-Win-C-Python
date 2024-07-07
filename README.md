# AIs-on-Win-C-Python
Make Win+C useful again, make it open AIs.

First, "compile" it into .exe with PyInstaller (or download the executable I made).

You can then run the .exe manually or put it in autostart folder. It will not open any window (if you use my .exe or use --windowed PyInstaller argument).

Once it detects that you pressed Win+C, it kills Cortana and opens ChatGPT and DuckDuckGo AIs in your default web browser.

Made for Windows 10, on Windows 11 you may need to remove waiting for Cortana.exe to open from the source code.

I will likely create C++ version too.
