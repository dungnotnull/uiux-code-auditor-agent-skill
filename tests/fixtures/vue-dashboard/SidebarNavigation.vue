<template>
  <aside class="sidebar" :class="{ collapsed: isCollapsed }">
    <button class="sidebar-toggle" @click="toggleSidebar">
      <Icon :name="isCollapsed ? 'chevron-right' : 'chevron-left'" />
    </button>
    <nav class="sidebar-nav">
      <ul>
        <li v-for="item in menuItems" :key="item.id">
          <a
            :href="item.path"
            :class="{ active: activeTab === item.id }"
            @click.prevent="navigate(item.id)"
          >
            <Icon :name="item.icon" />
            <span v-if="!isCollapsed">{{ item.label }}</span>
          </a>
        </li>
      </ul>
    </nav>
  </aside>
</template>

<script setup>
import { ref } from 'vue';
import Icon from './Icon.vue';

const props = defineProps({
  activeTab: { type: String, default: 'overview' }
});

const emit = defineEmits(['navigate']);

const isCollapsed = ref(false);

const menuItems = [
  { id: 'overview', label: 'Overview', icon: 'home', path: '/dashboard' },
  { id: 'analytics', label: 'Analytics', icon: 'chart', path: '/dashboard/analytics' },
  { id: 'users', label: 'Users', icon: 'users', path: '/dashboard/users' },
  { id: 'settings', label: 'Settings', icon: 'cog', path: '/dashboard/settings' },
];

const toggleSidebar = () => {
  isCollapsed.value = !isCollapsed.value;
};

const navigate = (id) => {
  emit('navigate', id);
};
</script>

<style lang="scss" scoped>
$primary: #4F46E5;
$gray-100: #F3F4F6;
$gray-200: #E5E7EB;
$gray-500: #6B7280;
$gray-700: #374151;
$gray-900: #111827;

.sidebar {
  width: 240px;
  background: white;
  border-right: 1px solid $gray-200;
  padding: 16px 0;
  transition: width 0.2s ease;

  &.collapsed {
    width: 64px;
  }
}

.sidebar-toggle {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  padding: 8px;
  border: none;
  background: transparent;
  cursor: pointer;
  color: $gray-500;

  &:hover {
    background: $gray-100;
  }
}

.sidebar-nav {
  ul {
    list-style: none;
    padding: 0;
    margin: 0;
  }

  a {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 10px 16px;
    color: $gray-700;
    text-decoration: none;
    font-size: 14px;
    border-radius: 6px;
    margin: 2px 8px;

    &:hover {
      background: $gray-100;
    }

    &.active {
      background: #EEF2FF;
      color: $primary;
      font-weight: 600;
    }
  }
}
</style>
