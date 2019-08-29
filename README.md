# Bruteforce password protected zip archives
You can crack a password protected zip archive providing a wordlist. 
The percentage of success depends of course from the dimensions of your wordlist.

# What do I need?
You can run this script anywhere, you just need:
- Terminal (macOS/UNIX-like) / Command Prompt (Windows) / Termux or any other emulator (Android/iOS)
- Python 3.x 

# How do I get it?
You can download the script in .zip format from this page or type from a Terminal of your choice: 

<pre><code>git clone https://github.com/manuelpellegrinet/zip-psw-cracker.git</code></pre>

For this operation you need to have git installed on your system.

# How do I use it?
Navigate to the folder where the file zip-psw-cracker.py has been downloaded or cloned and type from a Terminal of your choice: 

<pre><code>python3 zip-psw-cracker.py -h</code></pre>

<pre><code>
python3 -f <file-you-want-to-crack.zip> -d <wordlist-of-your-choice.txt>
</code></pre>

Usage example:

<pre><code>python3 zip-psw-cracker.py -f path/to/zip/archive.zip -d path/to/wordlist.txt</code></pre>

Use it responsably.
