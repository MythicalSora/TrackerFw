function proxyRequest(details) {
    return {
        redirectUrl: 'http://localhost:9999/$route?uri=' + encodeURIComponent(details.url),
        upgradeToSecure: false
    };
}

axios.get('http://localhost:9999/patterns').then(response => {
    browser.webRequest.onBeforeRequest.addListener(
        proxyRequest,
        {
            urls: response.data
        },
        ['blocking']
    );
});