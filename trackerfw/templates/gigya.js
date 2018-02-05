gigya = {
    isGigya: true
};

gigya.__initialized = true;
gigya.env = 'prod';
gigya.gaeDomain = 'chat.gigya.com';
gigya.defaultApiDomain = 'gigya.com';
gigya.dataCenter = 'eu1';
gigya.build = {
    version: '8.1.0',
    time: 'Monday 1970-01-01 00:00:00'
};

if (typeof gigya.partnerSettings == 'undefined') {
    gigya.partnerSettings = {
        "authMode": "cookie",
        "baseDomains": "",
        "ssoKey": "NONEXISTING_KEY"
    };
    gigya.partnerSettings.plugins = {
        "connectWithoutLoginBehavior": "loginExistingUser",
        "defaultRegScreenSet": "RegistrationLogin",
        "defaultMobileRegScreenSet": "RegistrationLogin",
        "sessionExpiration": -2,
        "rememberSessionExpiration": -2,
        "apiDomain": "eu1.gigya.com"
    };
}

gigya.providersConfig = {};
gigya.abTesting = null;
gigya.samlConfig = null;
gigya.accounts = {
    addEventHandlers: function() {},
    getAccountInfo: function() {},
    verifyLogin: function() {}
};
gigya.external = {
    facebook: {}
};
gigya._ = {
    apiAdapters: {
        mobile: {
            MobileAdapter: function() {}
        }
    }
};