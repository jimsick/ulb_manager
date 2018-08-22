<template>
    <el-table :data="tableData" style="width: 100%">
        <el-table-column prop="date" label="日期" width="180"></el-table-column>
        <el-table-column prop="date" label="日期" width="180"></el-table-column>
        <el-table-column prop="date" label="日期" width="180"></el-table-column>
    </el-table>
</template>

<script>
export default {
  name: 'BusInfo',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  },
  created() {

  },
  methods: {

  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
{#<style scoped>#}
{##}
{#</style>#}
