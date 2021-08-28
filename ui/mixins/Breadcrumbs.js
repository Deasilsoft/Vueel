import Vueel from "./Vueel";

export default {
    mixins: [
        Vueel
    ],
    data() {
        return {
            breadcrumbs: [],
        };
    },
    methods: {
        async addBreadcrumb(name) {
            const route = this.$router.options.routes.find(route => route.name === name);

            this.breadcrumbs.push({
                text: await this.T("app." + route.name),
                to: route.path,
            });
        },
        clearBreadcrumbs() {
            this.breadcrumbs = [];
        }
    }
};
