import Vue from 'vue'
import Router from 'vue-router'
import searchPage from '@/components/searchPage'
import result from '@/components/result'
import popitem from '@/components/popitem'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'searchPage',
      component: searchPage
    },
    {
      path: '/result',
      name: 'result',
      component: result
    },
    {
      path: '/popitem',
      name: 'popitem',
      component: popitem
    }
  ]
})
