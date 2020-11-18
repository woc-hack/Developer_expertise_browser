<template>
  <div id="app">
    <!-- type='flex' 启动flex布局-->
    <!-- center:居中，start左对齐，end右对齐， -->
    <el-col :span="10"></el-col>
    <el-row id="project-head" type="flex" justify="center" class="bg-white">
      <el-col :span="8">
        <div class="el-icon-share"></div>
        OSSLAB/ Developer Expertise Browser
      </el-col> 
    </el-row>
    <profiling-container></profiling-container>
  </div>
</template>

<script>
import ProfilingContainer from "./components/ProfilingContainer.vue";

export default {
  name: "App",
  components: {
    ProfilingContainer,
  },
  data() {
    return {
      activeIndex: "1",
    };
  },
  methods: {
    handleSelect(key, keyPath) {
      console.log(key, keyPath);
    },

  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
#project-head {
  margin-bottom: 20px;
  font-size: 28px;
}
.bg-white {
  background: #ffffff;
}
</style>
