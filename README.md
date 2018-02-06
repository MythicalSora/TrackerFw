# ![Logo](extensions/firefox/icons/TrackerFW-48.png) TrackerFw - <small>Intelligent Firewall for trackers</small>

**Note: This open-source project is stable but not ready for production usage**

## What?
TrackerFW is a software firewall for trackers. It includes a browser plugin which routes all traffic that invades the user its privacy to a local python server. Instead of only cancelling all bad traffic we want to make sure most (if not all) websites keep working but just don't invade your privacy.

TrackerFW **is not** an ad-blocker but a tracker-blocker. It's often used in combination with uBlock Origin.

## Why?
I was using Ghostery, uBlock, Anti Tracker Protection (Firefox) and a lot of other plugins to block trackers but over time this has a couple of disadvantages:

- Multiple plugins try to block the same traffic
- Websites broke because scripts couldn't load
- Websites could see if trackers were being blocked

With this open-source project I'm trying to solve all these problems.

## How?
The browser plugin fetches a list of URL patterns from a locally installed Python server. When a request matches one of the routes the traffic is sent through the Python server which will take further action. Apart from a static file of patterns and actions it also includes some more 'intelligent' block methods.

## Features
### Currently working
- List of URL patterns to block traffic or serve another Javascript file so that the website things the tracker is working
- Firefox browser plugin (will be ported to Google Chrome as well)
- Python aiohttp basic webserver including SSL support
- Bit.ly auto-fetcher which uses the BitLy API to fetch the final URL
- Click tracking redirector which redirects to the final URL without going through a click tracker such as google.nl/url..

### Upcoming
- Auto-update static tracker list
- Create ArchLinux, Debian, Fedora packages
- Port Firefox extension to Google Chrome
- Auto-install SSL certificate for local webserver
- Auto remove URL parts that invade privacy (UTM codes etc.)
- Add A LOT of trackers

## Python
The webserver is written in Python, you need at least python 3.5 or higher.
We will **never** support Python 2.
