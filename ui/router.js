import Vue from "vue";
import VueRouter from "vue-router";

Vue.use(VueRouter);

export default new VueRouter({
    linkActiveClass: "",
    linkExactActiveClass: "active",
    routes: [
        {
            path: "/",
            name: "vueel",
            navigation: {
                show: false
            },
            breadcrumbs: ["vueel"],
            redirect: "/home"
        },
        {
            path: "/home",
            name: "home",
            navigation: {
                show: true,
                order: 1
            },
            breadcrumbs: ["vueel", "home"],
            component: () => import("./views/Home.vue")
        },
        {
            path: "/about",
            name: "about",
            navigation: {
                show: true,
                order: 2
            },
            breadcrumbs: ["vueel", "about"],
            component: () => import("./views/About.vue")
        }
    ]
});
