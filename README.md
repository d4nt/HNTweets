# Introduction
This is the code for the HNTweets bot, which powers the @HNTweets twitter
account (http://twitter.com/HNTweets)

The project consists of a main script 'HNTweets.py', and a script to clear down the
database 'cleanup.py'. Both of which can be invoked with no arguments, for example:

    python HNTweets.py

The script will import the 'settings' module, i.e. it relies on having a
settings.py file in the same directory. The 'settings.py.dummy' file is included
which contains all the declarations of the real file, but none of the sensitive
information. To run the HNTweets.py script, you should first rename
settings.py.dummy to settings.py:

    mv settings.py.dummy settings.py

And then populate the missing fields with a valid bit.ly and Twitter security
information.

The setting DEBUG_MODE can be set to true to prevent the acutal posting of
messages to Twitter.

## Requirements
This code requires:

* sqlite3
* tweepy

The file requirements.txt contains the output of pip freeze -l and can be used to install any non-standard libaries like so:

    pip install -r requirements.txt

# License
This code is licensed under the Simplified BSD License

Copyright 2009 Daniel Thompson. All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

   1. Redistributions of source code must retain the above copyright notice,
      this list of conditions and the following disclaimer.

   2. Redistributions in binary form must reproduce the above copyright notice,
      this list of conditions and the following disclaimer in the documentation
      and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY DANIEL THOMPSON "AS IS" AND ANY EXPRESS OR IMPLIED
WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT
SHALL DANIEL THOMPSON OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

The views and conclusions contained in the software and documentation are those
of the authors and should not be interpreted as representing official policies,
either expressed or implied, of Daniel Thompson.
