import Vue from 'vue'
import App from './App.vue'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import ECharts from 'vue-echarts'
import 'echarts/'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
// import store from './store'
// import router from './router'

Vue.config.productionTip = false

Vue.use(BootstrapVue) // Install BootstrapVue
Vue.use(IconsPlugin) // Optionally install the BootstrapVue icon components plugin
Vue.component('v-chart', ECharts)

new Vue({
  // store,
  // router,
  render: h => h(App)
}).$mount('#app')
