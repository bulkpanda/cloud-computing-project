import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Scenario1 from 'C:/Users/msmmj/OneDrive/Documents/Development/cloud-computing-project/frontend/src/views/Scenario1.vue'
import Scenario2 from 'C:/Users/msmmj/OneDrive/Documents/Development/cloud-computing-project/frontend/src/views/Scenario2.vue'
import Scenario3 from 'C:/Users/msmmj/OneDrive/Documents/Development/cloud-computing-project/frontend/src/views/Scenario3.vue'
const router = createRouter({
	history: createWebHistory(),
	routes: [
		{
			path: '/',
			component: Home
		},
		{
			path: '/scenario1',
			component: Scenario1
		},
		{
			path: '/scenario2',
			component: Scenario2
		},
		{
			path: '/scenario3',
			component: Scenario3
		}
	],
})

export default router