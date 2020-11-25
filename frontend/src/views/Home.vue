<template>
  <div id="home" class="home">
    <b-jumbotron style="margin-bottom: 30px">
      <template #header>Migration Advisor</template>
      <template #lead>
        Tell us a Java library you want to replace, we recommend the most suitable migrations
        through an intelligent analysis upon existing GitHub repositories.
      </template>
      <hr class="my-4" />
      <library-search-input
        size="md"
        buttonText="Try it out!"
        placeholder="Enter the Java library (groupId:artifactId) you want to replace here... (e.g. org.json:json)"
      />
      <b-row class="my-1">
        <b-col sm="9">
          Some Examples:
          <b-link to="search/org.json:json"><code>org.json:json</code></b-link
          >,&emsp; <b-link to="search/junit:junit"><code>junit:junit</code></b-link
          >,&emsp; <b-link to="search/log4j:log4j"><code>log4j:log4j</code></b-link
          >,&emsp;
          <b-link to="search/c3p0:c3p0"><code>c3p0:c3p0</code></b-link>
        </b-col>
      </b-row>
    </b-jumbotron>
    <!-- <b-card-group style="margin-bottom: 30px">
      <b-card>
        <animated-number :number="21358" /><br />
        GitHub Repositories Analyzed
      </b-card>
      <b-card>
        <animated-number :number="185817" /><br />
        Indexed Maven Artifacts
      </b-card>
      <b-card>
        <animated-number :number="1956809" /><br />
        Migration Advisories
      </b-card>
      <b-card>
        <animated-number :number="1384" /><br />
        Confirmed Migration Advisories
      </b-card>
    </b-card-group> -->


  </div>
</template>

<script>
// import LibrarySearchInput from "@/components/LibrarySearchInput.vue";
// import AnimatedNumber from "@/components/AnimatedNumber.vue";

export default {
  name: "Home",
//   components: { LibrarySearchInput, AnimatedNumber },
  data: () => ({
    fromLib: "",
  }),
};
</script>
