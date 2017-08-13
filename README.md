<a href="https://rbltracker.com" target="_blank"><img src="https://rbltracker.com/portal/static/3.4/images/rbl_logo_front.png"/></a>

[Sign up][rbltracker sign up] for a RBLTracker account and visit our [developer site][rbltracker dev site] for even more details.

# Python Client Library

The official Python binding for your RBLTracker service.

## Prerequisites

Before using this library, you must have:

* A RBLTracker Account, [sign up for a new account][rbltracker sign up] or [login to RBLTracker](https://rbltracker.com/portal/login/)
* A valid RBLTracker account SID and auth token, available from the [RBLTracker Portal](https://rbltracker.com/portal/login/)
* Works with [ 2.6 / 2.7 / 3.2 / 3.3 ]

## Installation

```
pip install rbltracker
```

## Quickstart

### Get a list of hosts on your account

    import rbltracker

    try:
        client = rbltracker.Client('Your Account SID', 'Your Auth Token')

        data = client.hosts.get();

        print(data)

    except rbltracker.RBLTrackerException as err:
        print(err)

## Documentation

Full API documentation is available from the [RBLTracker developer site.][rbltracker dev site]

## Release History

### v1.0.0
* initial release

[rbltracker sign up]:   https://rbltracker.com/portal/signup/
[rbltracker dev site]:  https://rbltracker.com/docs/api/
