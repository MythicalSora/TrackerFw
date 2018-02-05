var beforeListener;
var trackers = {};

function proxyRequest(details) {
    console.log('> proxy: ' + details.url);

    if (!trackers[details.tabId]) {
        trackers[details.tabId] = 0;
    }

    trackers[details.tabId]++;

    browser.runtime.sendMessage({
        type: 'update-tracker-count',
        tab_id: details.tabId,
        count: trackers[details.tabId]
    });

    browser.browserAction.setBadgeText({
        text: trackers[details.tabId].toString(),
        tabId: details.tabId
    });

    return {
        redirectUrl: 'https://localhost:9999/$route?uri=' + encodeURIComponent(details.url),
        upgradeToSecure: false
    };
}

function loadPatterns(callback) {
    if (!callback) {
        callback = () => {};
    }

    axios.get('https://localhost:9999/patterns').then(response => {
        if (beforeListener) {
            browser.webRequest.onBeforeRequest.removeListener(beforeListener);
        }

        beforeListener = proxyRequest;

        browser.webRequest.onBeforeRequest.addListener(
            beforeListener,
            {
                urls: response.data
            },
            ['blocking']
        );

        callback(null, response.data);
    }).catch(function(e) {
        callback(e, null);
    });
}

browser.runtime.onMessage.addListener(message => {
    console.log('> got message: ' + message.type);

    switch (message.type) {
        case 'reload':
            loadPatterns((e, data) => {
                console.log('> load-patterns', data);
        
                browser.notifications.create('trackerfw.notify', {
                    'type': 'basic',
                    'iconUrl': browser.extension.getURL('icons/TrackerFW-48.png'),
                    'title': 'TrackerFw',
                    'message': e === null ? 'Loaded ' + data.length + ' patterns' : 'No patterns loaded'
                });
            });
            break;

        case 'send-tracker-count':
            browser.runtime.sendMessage({
                tab_id: message.tab_id,
                type: 'update-tracker-count',
                count: trackers[message.tab_id]
            });
            break;
    }
});

browser.webNavigation.onBeforeNavigate.addListener(details => {
    trackers[details.tabId] = 0;
});

browser.browserAction.setBadgeBackgroundColor({
    color: '#444'
});

loadPatterns((e, data) => {
    console.log('> load-patterns', data);
});