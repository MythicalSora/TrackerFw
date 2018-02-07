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

        <div class="tracker-list" v-show="count > 0">
            <div v-for="tracker in trackers" :key="tracker.name" class="tracker">
                <i class="fas fa-chevron-right"></i>
                {{ tracker.name }}
            </div>
        </div>

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
        count() {
            return this.trackers.length;
        }
    },

    created() {
        browser.tabs.query({
            active: true
        }).then(tabs => {
            this.tab_id = tabs[0].id;

            console.log('< asking to sent trackers for', this.tab_id);

            browser.runtime.sendMessage({
                type: 'sendTrackers',
                tab_id: this.tab_id
            });
        });

        browser.runtime.onMessage.addListener(message => {
            switch (message.type) {
                case 'trackerList':
                    if (message.tab_id == this.tab_id) {
                        this.trackers = message.trackers;
                    }
                    break;
            }
        });
    },

    data() {
        return {
            trackers: [],
            tab_id: null
        };
    }
}
</script>

<style>

</style>
