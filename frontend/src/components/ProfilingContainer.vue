<template>
  <div>
    <el-menu
      :default-active="activeIndex"
      class="el-menu-demo"
      mode="horizontal"
      @select="handleSelect"
    >
      <el-menu-item index="1">LookUp</el-menu-item>
      <el-submenu index="2">
        <template #title>Code Summary </template>
        <el-menu-item index="2-1">Development History</el-menu-item>
        <el-menu-item index="2-2">Contribution preference</el-menu-item>
        <el-menu-item index="2-3">Code Quality</el-menu-item>
        <!-- <el-submenu index="2-4">
          <template #title>选项4</template>
          <el-menu-item index="2-4-1">选项1</el-menu-item>
          <el-menu-item index="2-4-2">选项2</el-menu-item>
          <el-menu-item index="2-4-3">选项3</el-menu-item>
        </el-submenu> -->
      </el-submenu>
      <el-submenu index="3">
        <template #title>Social Ability</template>
        <el-menu-item index="3-1">Social Relationship</el-menu-item>
        <el-menu-item index="3-2">Social Graph</el-menu-item>
      </el-submenu>
      <el-menu-item index="4" disabled>Notification</el-menu-item>
    </el-menu>
  </div>
</template>

<script>
// import ActiveCode from "./activity/ActiveCode";
// import CommitStatistics from "./activity/CommitStatistics";
// import CommunityResponse from "./activity/CommunityResponse";
// import ProjectProgress from "./activity/ProjectProgress";
// import CodeDefect from "./code/CodeDefect";
// import CodeStatistics from "./code/CodeStatistics";
// import DocumentCheckList from "./document/DocumentCheckList";
// import MemberActivity from "./member/MemberActivity";
// import MemberContribution from "./member/MemberContribution";
// import MemberRemain from "./member/MemberRemain";
// import HotCurve from "./popularity/HotCurve";
// import StarCurve from "./popularity/StarCurve";
export default {
  name: "ProfilingContainer",


};
</script>

<style></style>
