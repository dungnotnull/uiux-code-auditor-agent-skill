<template>
  <div class="dashboard-container">
    <SidebarNavigation :active-tab="activeTab" @navigate="setActiveTab" />

    <main class="dashboard-main">
      <div class="kpi-row">
        <div class="kpi-card" v-for="kpi in kpis" :key="kpi.id">
          <span class="kpi-label">{{ kpi.label }}</span>
          <span class="kpi-value">{{ kpi.value }}</span>
          <span class="kpi-change" :class="kpi.trend">{{ kpi.changeText }}</span>
        </div>
      </div>

      <div class="charts-row">
        <div class="chart-container">
          <h3>Revenue Trend</h3>
          <RevenueChart :data="revenueData" />
        </div>
        <div class="chart-container">
          <h3>User Activity</h3>
          <ActivityChart :data="activityData" />
        </div>
        <div class="chart-container">
          <h3>Conversion Rate</h3>
          <ConversionChart :data="conversionData" />
        </div>
        <div class="chart-container">
          <h3>Engagement Score</h3>
          <EngagementChart :data="engagementData" />
        </div>
      </div>

      <div class="data-section">
        <div class="filter-bar">
          <input v-model="searchQuery" placeholder="Search users..." class="filter-input">
          <select v-model="selectedStatus" class="filter-select">
            <option value="">All Status</option>
            <option value="active">Active</option>
            <option value="inactive">Inactive</option>
          </select>
          <select v-model="selectedPlan" class="filter-select">
            <option value="">All Plans</option>
            <option value="free">Free</option>
            <option value="pro">Pro</option>
            <option value="enterprise">Enterprise</option>
          </select>
          <button class="btn-export" @click="exportData">Export CSV</button>
        </div>

        <table class="data-table">
          <thead>
            <tr>
              <th>Name</th>
              <th>Email</th>
              <th>Plan</th>
              <th>Status</th>
              <th>Last Active</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="user in filteredUsers" :key="user.id">
              <td>{{ user.name }}</td>
              <td>{{ user.email }}</td>
              <td>{{ user.plan }}</td>
              <td><span class="status-badge" :class="user.status">{{ user.status }}</span></td>
              <td>{{ user.lastActive }}</td>
              <td>
                <button @click="viewUser(user.id)" class="btn-icon">
                  <Icon name="eye" />
                </button>
                <button @click="editUser(user.id)" class="btn-icon">
                  <Icon name="pencil" />
                </button>
                <button @click="deleteUser(user.id)" class="btn-icon btn-danger">
                  <Icon name="trash" />
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import SidebarNavigation from './SidebarNavigation.vue';
import RevenueChart from './charts/RevenueChart.vue';
import ActivityChart from './charts/ActivityChart.vue';
import ConversionChart from './charts/ConversionChart.vue';
import EngagementChart from './charts/EngagementChart.vue';
import Icon from './Icon.vue';
import { fetchDashboardData, fetchUsers, deleteUser as apiDeleteUser } from '../api/dashboard';

const activeTab = ref('overview');
const kpis = ref([]);
const revenueData = ref([]);
const activityData = ref([]);
const conversionData = ref([]);
const engagementData = ref([]);
const users = ref([]);
const searchQuery = ref('');
const selectedStatus = ref('');
const selectedPlan = ref('');
const isLoading = ref(true);

const filteredUsers = computed(() => {
  return users.value.filter(user => {
    const matchesSearch = user.name.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
      user.email.toLowerCase().includes(searchQuery.value.toLowerCase());
    const matchesStatus = !selectedStatus.value || user.status === selectedStatus.value;
    const matchesPlan = !selectedPlan.value || user.plan === selectedPlan.value;
    return matchesSearch && matchesStatus && matchesPlan;
  });
});

const setActiveTab = (tab) => {
  activeTab.value = tab;
};

const viewUser = (id) => {
  // Navigate to user detail
};

const editUser = (id) => {
  // Navigate to user edit
};

const deleteUser = async (id) => {
  await apiDeleteUser(id);
  users.value = users.value.filter(u => u.id !== id);
};

const exportData = () => {
  // Export logic
};

onMounted(async () => {
  try {
    const data = await fetchDashboardData();
    kpis.value = data.kpis;
    revenueData.value = data.revenue;
    activityData.value = data.activity;
    conversionData.value = data.conversion;
    engagementData.value = data.engagement;
    users.value = await fetchUsers();
  } catch (error) {
    console.error(error);
  } finally {
    isLoading.value = false;
  }
});
</script>

<style lang="scss" scoped>
$primary: #4F46E5;
$success: #10B981;
$danger: #EF4444;
$warning: #F59E0B;
$gray-50: #F9FAFB;
$gray-100: #F3F4F6;
$gray-200: #E5E7EB;
$gray-500: #6B7280;
$gray-700: #374151;
$gray-900: #111827;

.dashboard-container {
  display: flex;
  min-height: 100vh;
}

.dashboard-main {
  flex: 1;
  padding: 24px;
  background: $gray-50;
}

.kpi-row {
  display: flex;
  gap: 16px;
  margin-bottom: 24px;
}

.kpi-card {
  flex: 1;
  background: white;
  border-radius: 8px;
  padding: 20px;
  border: 1px solid $gray-200;
}

.kpi-label {
  display: block;
  font-size: 14px;
  color: $gray-500;
  margin-bottom: 8px;
}

.kpi-value {
  display: block;
  font-size: 32px;
  font-weight: 700;
  color: $gray-900;
}

.kpi-change {
  display: block;
  font-size: 14px;
  margin-top: 4px;

  &.up { color: $success; }
  &.down { color: $danger; }
}

.charts-row {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 16px;
  margin-bottom: 24px;
}

.chart-container {
  background: white;
  border-radius: 8px;
  padding: 20px;
  border: 1px solid $gray-200;

  h3 {
    font-size: 16px;
    color: $gray-700;
    margin-bottom: 16px;
  }
}

.data-section {
  background: white;
  border-radius: 8px;
  padding: 20px;
  border: 1px solid $gray-200;
}

.filter-bar {
  display: flex;
  gap: 12px;
  margin-bottom: 16px;
}

.filter-input {
  padding: 8px 12px;
  border: 1px solid $gray-200;
  border-radius: 6px;
  font-size: 14px;
}

.filter-select {
  padding: 8px 12px;
  border: 1px solid $gray-200;
  border-radius: 6px;
  font-size: 14px;
  background: white;
}

.btn-export {
  padding: 8px 16px;
  background: $primary;
  color: white;
  border: none;
  border-radius: 6px;
  font-size: 14px;
  cursor: pointer;
}

.btn-icon {
  padding: 4px 8px;
  border: none;
  background: transparent;
  cursor: pointer;
  border-radius: 4px;

  &:hover {
    background: $gray-100;
  }
}

.btn-danger {
  color: $danger;
}

.data-table {
  width: 100%;
  border-collapse: collapse;

  th {
    text-align: left;
    padding: 12px 16px;
    border-bottom: 2px solid $gray-200;
    font-size: 12px;
    text-transform: uppercase;
    color: $gray-500;
  }

  td {
    padding: 12px 16px;
    border-bottom: 1px solid $gray-200;
  }
}

.status-badge {
  padding: 4px 8px;
  border-radius: 12px;
  font-size: 12px;
  font-weight: 500;

  &.active {
    background: #D1FAE5;
    color: #065F46;
  }
  &.inactive {
    background: #FEE2E2;
    color: #991B1B;
  }
}
</style>
