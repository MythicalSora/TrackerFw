function _googleTagProxy() {
    return {
        addService: function() {
            return _googleTagProxy();
        },
        setTargeting: function() {
            return _googleTagProxy();
        },
        enableSyncRendering: function() {
            return _googleTagProxy();
        },
        enableSingleRequest: function() {
            return _googleTagProxy();
        }
    };
};

window.googletag = {
    defineSlot: _googleTagProxy,
    display: _googleTagProxy,
    pubads: _googleTagProxy,
    enableServices: _googleTagProxy
};