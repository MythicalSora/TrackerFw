var beforeListener;

function proxyRequest(details) {
    console.log('> proxy: ' + details.url);

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

function showNotification(tab) {
    loadPatterns((e, data) => {
        console.log('> load-patterns', data);

        browser.notifications.create('trackerfw.notify', {
            'type': 'basic',
            'iconUrl': browser.extension.getURL('icons/border-48.png'),
            'title': 'TrackerFW',
            'message': e === null ? 'Loaded ' + data.length + ' patterns' : 'No patterns loaded'
        });
    });
}

browser.browserAction.onClicked.addListener(showNotification);

loadPatterns((e, data) => {
    console.log('> load-patterns', data);
});