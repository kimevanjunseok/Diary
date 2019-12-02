import Vue from "vue";
import Router from "vue-router";

Vue.use(Router);

const router = new Router({
	mode: "history",
    base: process.env.BASE_URL,
    routes: [
        {
          path: "/",
          name: "MainPage",
          component: () => import("./views/MainPage"),
          meta: { requiresAuth: true }
        },
        {
          path: "/WritePage",
          name: "WritePage",
          component: () => import("./views/WritePage"),
          meta: { requiresAuth: true }
        },
        {
          path: "/UpdatePage/:id",
          name: "UpdatePage",
          component: () => import("./views/UpdatePage"),
          meta: { requiresAuth: true }
        },
    ]
})
export default router;