/// <reference types="vite/client" />

declare module "*.vue" {
    import type { DefineComponent, ComponentOptions } from "vue";
    const component: DefineComponent<{}, {}, any>;
    const componentOptions: ComponentOptions;
    export default { component, componentOptions };
}