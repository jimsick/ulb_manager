<template>
	<section ref="section1">
		<!--工具条-->
		<el-col :span="24" class="toolbar" style="padding-bottom: 0px;">
			<el-form :inline="true" :model="filters">
				<el-form-item>
					<el-input v-model="filters.search" placeholder="关键字"></el-input>
				</el-form-item>
				<el-form-item>
					<el-button type="primary" v-on:click="getBusList(1, filters.search)">查询</el-button>
				</el-form-item>
        <el-form-item>
					<el-button v-on:click="reset">重置</el-button>
				</el-form-item>
				<el-form-item>
					<el-button type="success" @click="handleAdd">新增</el-button>
				</el-form-item>
			</el-form>
		</el-col>

		<!--列表-->
		<el-table
      :data="bus_list"
      height="100em"
      highlight-current-row
      v-loading="listLoading"
      style="width: 100%;"
      :height="tableHeight"
      :max-height="tableHeight"
      ref="table"
    >
			<el-table-column type="selection" width="55">
			</el-table-column>
			<el-table-column type="index" width="60">
			</el-table-column>
			<el-table-column prop="bus_id" label="车辆注册信息" width="120">
			</el-table-column>
			<el-table-column prop="company" label="公交公司名称" width="150">
			</el-table-column>
      <el-table-column prop="bus_license_plate" label="车牌号" width="150">
			</el-table-column>
      <el-table-column prop="bus_line" label="线路号" width="150">
			</el-table-column>
			<el-table-column prop="bus_state" label="当前状态" width="180" :formatter="formatterStatus">
			</el-table-column>
      <el-table-column prop="bus_locate" label="当前定位" min-width="180">
			</el-table-column>
			<el-table-column label="操作" width="200">
				<template slot-scope="scope">
					<el-button type="warning" size="small" @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
					<el-button type="danger" size="small" @click="handleDel(scope.$index, scope.row)">删除</el-button>
				</template>
			</el-table-column>
		</el-table>
    <el-pagination
      @size-change="handleSizeChange"
      @current-change="handleCurrentChange"
      @prev-click="handleCurrentChange"
      @next-click="handleCurrentChange"
      :current-page.sync="currentPage"
      :page-size="10"
      layout="prev, pager, next, jumper"
      :total=total>
    </el-pagination>
    </el-pagination>
    </el-pagination>
		<!--工具条-->
		<el-col :span="24" class="toolbar">
			<!--<el-button type="danger" @click="batchRemove" :disabled="this.sels.length===0">批量删除</el-button>-->
			<!--<el-pagination layout="prev, pager, next" @current-change="handleCurrentChange" :page-size="20" :total="total" style="float:right;">-->
			<!--</el-pagination>-->
		</el-col>

		<!--编辑界面-->
		<el-dialog title="编辑" :visible.sync="editFormVisible" :close-on-click-modal="false">
			<el-form :model="editForm" label-width="80px" :rules="editFormRules" ref="editForm">
				<el-form-item label="姓名" prop="name">
					<el-input v-model="editForm.appmanname" auto-complete="off"></el-input>
				</el-form-item>
			</el-form>
			<div slot="footer" class="dialog-footer">
				<el-button @click.native="editFormVisible = false">取消</el-button>
				<el-button type="primary" @click.native="editSubmit" :loading="editLoading">提交</el-button>
			</div>
		</el-dialog>



		<!--新增界面-->
		<el-dialog title="新增" v-model="addFormVisible" :close-on-click-modal="false">
			<el-form :model="addForm" label-width="80px" :rules="addFormRules" ref="addForm">
				<el-form-item label="姓名" prop="name">
					<el-input v-model="addForm.name" auto-complete="off"></el-input>
				</el-form-item>
				<el-form-item label="性别">
					<el-radio-group v-model="addForm.sex">
						<el-radio class="radio" :label="1">男</el-radio>
						<el-radio class="radio" :label="0">女</el-radio>
					</el-radio-group>
				</el-form-item>
				<el-form-item label="年龄">
					<el-input-number v-model="addForm.age" :min="0" :max="200"></el-input-number>
				</el-form-item>
				<el-form-item label="生日">
					<el-date-picker type="date" placeholder="选择日期" v-model="addForm.birth"></el-date-picker>
				</el-form-item>
				<el-form-item label="地址">
					<el-input type="textarea" v-model="addForm.addr"></el-input>
				</el-form-item>
			</el-form>
			<div slot="footer" class="dialog-footer">
				<el-button @click.native="addFormVisible = false">取消</el-button>
				<el-button type="primary" @click.native="addSubmit" :loading="addLoading">提交</el-button>
			</div>
		</el-dialog>
	</section>
</template>

<script>
	import util from '../../common/js/util'
	// import { getBusList, updateList } from '../../config/api';

	export default {
		data() {
			return {
			  // 分页
				total: 0,
				page: 1,
        // 查询
        filters:{
				  search:"",
        },
        // 表格高度
        tableHeight: window.innerHeught,
        currentPage: 1,
				bus_list: [],
				listLoading: false,
				sels: [],//列表选中列
				editFormVisible: false,//编辑界面是否显示
				editLoading: false,
				editFormRules: {  //验证规则
					appmanname: [
						{ required: true, message: '请输入姓名', trigger: 'blur' }
					]
				},
				//编辑界面数据
				editForm: {
					id: 0,
					appmanname: '',
				},
				addFormVisible: false,//新增界面是否显示
				addLoading: false,  // 新增loading
				addFormRules: {  // 新增规则
					name: [
						{ required: true, message: '请输入姓名', trigger: 'blur' }
					]
				},
				//新增界面数据
				addForm: {
					id: 0,
					appmanname: '',
				}

			}
		},
		methods: {
      // ==========分页start==========
      handleSizeChange(val) {
        console.log(`每页 ${val} 条`);
      },
      handleCurrentChange(val) {
		    this.currentPage = val
        this.getBusList(this.currentPage, this.filters.search)
      },
      // ==========分页end==========
		  reset() {
		    this.search = ""
        this.getBusList(1, this.filters.search)
      },
      formatterStatus: function(row, column) {
        if(row.bus_state){
          return '正常'
        }
        return '报警'
      },
			//获取用户列表
			getBusList: function(currentPage, search) {
				let para = {
					page: currentPage,
					search: search
				};
				this.listLoading = true;
				this.$fetch('api/bus/bus/',para).then((res) => {
				  if(!res.hasOwnProperty('code')){
            this.bus_list = res.results;
            this.total = res.count;
            this.listLoading = false;
					}
					//NProgress.done();
				}).catch((err) => {
				  this.listLoading = false;
				  this.$message({
            showClose: true,
            message: err.data.detail,
            type: 'error'
          });
				});
			},
			//删除
			BusDel: function (index, row) {
				this.$confirm('确认删除该记录吗?', '提示', {
					type: 'warning'
				}).then(() => {
					this.listLoading = true;
					let para = {};
					del(`api/bus/bus/${row.id}/`,para).then((res) => {
						this.listLoading = false;
						this.$message({
							message: '删除成功',
							type: 'success'
						});
						this.getUsers();
					});
				}).catch(() => {
				});
			},
			// //显示编辑界面
			handleEdit: function (index, row) {
				this.editFormVisible = true;
				this.editForm = Object.assign({}, util.removeProperty(row));
				console.log(JSON.stringify(row)+ "==========" +JSON.stringify(this.editForm))
			},
			//显示新增界面
			handleAdd: function () {
			  this.addFormVisible = true;
			 	this.addForm = {
			 		name: '',
			 		sex: -1,
			 		age: 0,
			 		birth: '',
			 		addr: ''
			 	};
			 },
			//编辑
			editSubmit: function () {
				this.$refs.editForm.validate((valid) => {
					if (valid) {
						this.$confirm('确认提交吗？', '提示', {}).then(() => {
							this.editLoading = true;
							let para = Object.assign({}, this.editForm);
							// 时间规则验证
              this.$put(`api/bus/bus/${para.id}/`,para)
                  .then(res => {
                    if(res.results.code == 200){
                      this.editLoading = false;
                      this.$message({
                        message: '更新成功',
                        type: 'success'
                      });
                      this.$refs['editForm'].resetFields();
                      this.editFormVisible = false;
                      this.getBusList();
                    }else{
                      this.$message({
                        message: '更新失败',
                        type: 'error'
                      });
                    }
                  })
                  .catch(err => {
                      this.$message({
                        message: '提交失败',
                        type: 'error'
                      });
                  })
						});
					}
				});
			},
			// //新增
			saveBus: function () {
				this.$refs.addForm.validate((valid) => {
					if (valid) {
						this.$confirm('确认提交吗？', '提示', {}).then(() => {
							this.addLoading = true;
							//NProgress.start();
							let para = Object.assign({}, this.addForm);
							// para.birth = (!para.birth || para.birth == '') ? '' : util.formatDate.format(new Date(para.birth), 'yyyy-MM-dd');
							this.$post('api/bus/bus/',para).then((res) => {
							  if(res.results.code == 200) {
                  this.addLoading = false;
                  //NProgress.done();
                  this.$message({
                    message: '提交成功',
                    type: 'success'
                  });
                  this.$refs['addForm'].resetFields();
                  this.addFormVisible = false;
                  this.getUsers();
                }else{
							    this.$message({
                    message: '提交失败',
                    type: 'success'
                  });
                }
							});
						});
					}
				});
			},
			selsChange: function (sels) {
				this.sels = sels;
			},
		},
		mounted() {
			this.getBusList();
			this.$nextTick(() => {
        let self = this;
        this.tableHeight = this.$refs.table.offsetHeight

            // 通过捕获系统的onresize事件触发去改变原有的高度
        // window.onresize = function() {
        //     self.tableHeight = self.$refs.table.offsetHeight
        // }
    })
		}
	}

</script>

<style scoped>
</style>
