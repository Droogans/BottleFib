BottleFib
=========

Fibonacci sequence generator as a webservice in Bottle Python.


To Set Up
---------

Get `pip`, if you don't already have it.

    sudo apt-get install python-setuptools
    sudo easy-install pip
    sudo pip install virtualenv

`virtualenv` is the virtual environment manager for Python. This creates a "source" for you to keep this project isolated from your main environments.

To use it in this project:

    cd ~/py/
    git clone git@github.com:Droogans/BottleFib.git BottleFib
    virtualenv -p python3.1 ~/py/env/BottleFib --no-site-packages
    source ~/py/env/BottleFib/bin/activate
    (BottleFib)user@machine ~/py/BottleFib $

Next, get the needed installs to run this project:

    pip install -r requirements.txt --no-index --find-links file:///tmp/packages

And then ensure that you `.pth` files put this on your environment's PYTHONPATH:

    echo ~/py/BottleFib > ~/py/env/BottleFib/lib/python3.1/site-packages/BottleFib.pth

Next, run the tests:

    python services/fibonacci_service_test.py
    python services/lib/fibonacci_test.py

Finally, run the app:

    python services/fibonacci_service.py

You can reach the app on [your localhost](http://127.0.0.1:8080/fib/), once the server has started.

Future-Proofing
---------------

- Services are in their own folder, with a lib supporting each.
- `prime_service.py` could be added, with a matching `lib` helper, and a test.
- `requirements.txt` ensures an even experience between contributers.
- Python 3.1 was chosen for its forward-facing feature set (unicode support being the biggest for a website)
- A good README with instruction to use a virutal environment when developing a new project.

Improvements
------------

- JSON-centric configuration and better logging.
- `lxml` for anything other than simple xml file creation/parsing.
- A "run one and done" test suite (ala `unittest discover`). 
- Memoizing/pickling the fibonacci sequence to memory for large numbers.
