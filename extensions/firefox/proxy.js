/**
 * Classes
 */
class WebsocketClient {
    constructor() {
        this.uri = 'wss://localhost:9999/$subscribe';
        this.events = [];
    }

    on(event, listener) {
        this.events.push({
            name: event,
            listener: listener
        });
    }

    emit(eventName, data) {
        this.events.forEach(event => {
            if (event.name !== eventName) {
                return;
            }

            event.listener(data);
        });
    }

    connect() {
        this.ws = new WebSocket(this.uri);
        this.bindEvents();
    }

    bindEvents() {
        let reconnectTimer,
            reconnect = () => {
                try {
                    this.ws.close();
                } catch(e) {}

                if (reconnectTimer) {
                    clearTimeout(reconnectTimer);
                }

                reconnectTimer = setTimeout(() => {
                    this.ws = null;
                    this.connect();
                }, 1000);
            };


        this.ws.onopen = () => {
            
        };

        this.ws.onmessage = (event) => {
            let data = JSON.parse(event.data);

            this.emit(data.type, data.data);
        };

        this.ws.onerror = () => {
            reconnect();
        };

        this.ws.onclose = () => {
            reconnect();
        };
    }
}


/**
 * Event handlers
 */
function proxyRequest(details) {
    return {
        redirectUrl: 'https://localhost:9999/$route?uri=' + encodeURIComponent(details.url) + '&tab_id=' + details.tabId,
        upgradeToSecure: false
    };
}


/**
 * Global variables
 */
var beforeListener;
var trackers = {};
var websocket = new WebsocketClient();


/**
 * Bind events
 */
browser.runtime.onMessage.addListener(message => {
    switch (message.type) {
        case 'reload':
            break;

        case 'sendTrackers':
            browser.runtime.sendMessage({
                type: 'trackerList',
                tab_id: message.tab_id,
                trackers: trackers[message.tab_id]
            });
            break;
    }
});

browser.webNavigation.onBeforeNavigate.addListener(details => {
    trackers[details.tabId] = [];
});

browser.browserAction.setBadgeBackgroundColor({
    color: '#444'
});


/**
 * Bind websocket events
 */
websocket.on('trackerFound', (details) => {
    trackers[details.tab_id].push(details);

    browser.browserAction.setBadgeText({
        text: trackers[details.tab_id].length.toString(),
        tabId: details.tabId
    });

    browser.runtime.sendMessage({
        type: 'trackerList',
        tab_id: details.tab_id,
        trackers: trackers[details.tabId]
    });
});

websocket.on('patternList', (patterns) => {
    if (beforeListener) {
        browser.webRequest.onBeforeRequest.removeListener(beforeListener);
    }
    
    beforeListener = proxyRequest;
    
    browser.webRequest.onBeforeRequest.addListener(
        beforeListener,
        {
            urls: patterns
        },
        ['blocking']
    );
});

websocket.connect();
