<template>
    <div class="container">
        <h1>
            TrackerFw

            <div v-show="count !== null" class="align-right">
                <i class="fas fa-chart-area"></i>
                <small>
                    <strong>{{ count }}</strong>
                </small>
            </div>
        </h1>

        <p v-show="count == 0">
            Can't fetch list of blocked trackers
        </p>

        <p v-show="count > 0">
            Tracker details are not currently shown
        </p>

        <ul>
            <li>
                <a @click.prevent="runAction('toggle')" href="" class="btn" title="toggle">
                    <i class="fas fa-pause"></i>
                </a>
            </li>

            <li>
                <a @click.prevent="runAction('reload')" href="" class="btn" title="reload">
                    <i class="fas fa-sync"></i>
                </a>
            </li>
        </ul>
    </div>
</template>

<script>
export default {
    methods: {
        runAction(action) {
            browser.runtime.sendMessage({
                type: action,
            });
        }
    },

    computed: {
    },

    created() {
        browser.tabs.query({
            active: true
        }).then(tabs => {
            this.tab_id = tabs[0].id;

            browser.runtime.sendMessage({
                type: 'send-tracker-count',
                tab_id: this.tab_id
            });
        });

        browser.runtime.onMessage.addListener(message => {
            switch (message.type) {
                case 'update-tracker-count':
                    if (message.tab_id == this.tab_id) {
                        this.count = message.count;
                    }
                    break;
            }
        });
    },

    data() {
        return {
            count: null,
            tab_id: null
        };
    }
}
</script>

<style>

</style>
