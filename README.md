# TrackerFw - <small>Intelligent Firewall for trackers</small>

**Note: This open-source project is stable but not ready for production usage**

## What?
TrackerFW is an intelligent software firewall for trackers. It includes a browser plugin which routes all 'bad' traffic to a local python server. Instead of only cancelling all bad traffic we want to make sure most (if not all) websites keep working but don't invase your privacy.

## Why?
I was using Ghostery, uBlock, Anti Tracker Protection and a lot of other plugins to block trackers but over time this has a couple of disadvantages:

- Multiple plugins try to block the same traffic
- Websites broke because scripts couldn't load
- Websites could see if trackers were being blocked

With this open-source project I'm trying to solve all these problems.

## How?
The browser plugin fetches a list of URL patterns from a locally installed Python server. When a request matches it routes the traffic through the Python server which will take further action. Apart from a static file of patterns and actions it also includes some more intelligent block methods.

## Features
### Currently working
- Firefox browser plugin (will be ported to Google Chrome as well)
- Python aiohttp basic webserver including SSL support
- Bit.ly auto-fetcher which uses the BitLy API to fetch the final URL
- Click tracking redirector which redirects to the final URL without going through a click tracker such as google.nl/url..

### Upcoming
- Auto-update static tracker list
- Create ArchLinux, Debian, Fedora packages
- Port Firefox extension to Google Chrome
- Auto-install SSL certificate for local webserver
- Add A LOT of trackers
