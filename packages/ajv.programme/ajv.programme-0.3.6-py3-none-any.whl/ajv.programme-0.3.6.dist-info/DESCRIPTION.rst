programme
=========

programme is a program that writes programmes.

This isn't really intended for general use. It's something I put
together so someone I know could make nice-ish music-recital programmes,
without having to manually futz with word processor layouts.  But if you
run across it on pypi, you're welcome to use it.

Quick Start
-----------

Install Python 3, ``pip``, and ``programme`` itself, if they're not
already present. The commands will differ by OS; this example is for
Mint, Ubuntu, and other Debian-based systems:

::

    sudo apt install python3-pip
    pip3 install ajv.programme

Now generate a blank performer file, as follows:

::

    programme --init > performers.tsv


Open ``performers.tsv`` in your spreadsheet program of choice. It may
prompt you for import settings; the only relevant one is the delimiter,
which should be a tab.

Fill in the columns on the spreadsheet. Anything left blank will be
ignored. Save when done. Then:

::

    programme performers.tsv output.html

That's it. Open output.html and you should get something usable. If you
specified images in the tsv file, and if those files are present in the
same directory, they'll be included in the output as portraits.

You can run ``programme --help`` to see additional options.


