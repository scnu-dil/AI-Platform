<template>
  <!-- <div class="data-collection query">
    数据集查看
  </div>-->
  <el-main>
    <div class="listbox">
      <el-table
        ref="multipleTable"
        :data="tableData3"
        tooltip-effect="dark"
        border
        @selection-change="handleSelectionChange"
      >
        <el-table-column type="selection" width="55"></el-table-column>
        <el-table-column label="日期">
          <template slot-scope="scope">{{ scope.row.date }}</template>
        </el-table-column>
        <el-table-column prop="modelname" label="数据集名称"></el-table-column>
        <el-table-column prop="uploader" label="上传者" show-overflow-tooltip></el-table-column>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button size="mini" @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
            <el-button size="mini" type="success" @click="outportData(scope.$index, scope.row)">下载</el-button>
          </template>
        </el-table-column>
      </el-table>
      <div class="choosebox" style="margin-top: 20px">
        <!-- <el-button @click="toggleSelection([tableData3[1], tableData3[2]])">切换第二、第三行的选中状态</el-button> -->
        <el-button @click="toggleSelection()">取消选择</el-button>
        <!-- <el-button type="primary" @click="importData">导入</el-button> -->
        <el-button type="primary" @click="outportData">导出</el-button>
      </div>
      <!-- 导入 -->
      <el-dialog
        title="导入"
        :visible.sync="dialogImportVisible"
        :modal-append-to-body="false"
        :close-on-click-modal="false"
        class="dialog-import"
      >
        <div :class="{'import-content': importFlag === 1, 'hide-dialog': importFlag !== 1}">
          <el-upload
            class="upload-demo"
            :action="importUrl"
            :name="name"
            :headers="importHeaders"
            :on-preview="handlePreview"
            :on-remove="handleRemove"
            :before-upload="beforeUpload"
            :on-error="uploadFail"
            :on-success="uploadSuccess"
            :file-list="fileList"
            :with-credentials="withCredentials"
          >
            <!-- 是否支持发送cookie信息 -->
            <el-button size="small" type="primary" :disabled="processing">{{uploadTip}}</el-button>
            <div slot="tip" class="el-upload__tip">上传.xls,.xlsx,.csv类型的文件</div>
          </el-upload>
        </div>
        <div :class="{'import-failure': importFlag === 2, 'hide-dialog': importFlag !== 2}">
          <div class="failure-tips">
            <i class="el-icon-warning"></i>导入失败
          </div>
          <div class="failure-reason">
            <h4>失败原因</h4>
            <ul>
              <li
                v-for="(error,index) in errorResults"
                :key="index"
              >第{{error.rowIdx + 1}}行，错误：{{error.column}},{{error.value}},{{error.errorInfo}}</li>
            </ul>
          </div>
        </div>
      </el-dialog>

      <!-- 导出 -->
    </div>
  </el-main>
</template>

<script>
export default {
  name: "query",
  data() {
    return {
      tableData3: [
        {
          date: "2019-07-19",
          modelname: "Market1501",
          uploader: "Lyndsey"
        },
        {
          date: "2019-07-19",
          modelname: "UCF101",
          uploader: "Lijuce"
        }
      ],
      multipleSelection: [],
      importUrl: "www.baidu.com", //后台接口config.admin_url+'rest/schedule/import/'
      importHeaders: {
        enctype: "multipart/form-data",
        cityCode: ""
      },
      name: "import",
      fileList: [],
      withCredentials: true,
      processing: false,
      uploadTip: "点击上传",
      importFlag: 1,
      dialogImportVisible: false,
      errorResults: []
    };
  },
  methods: {
    toggleSelection(rows) {
      if (rows) {
        rows.forEach(row => {
          this.$refs.multipleTable.toggleRowSelection(row);
        });
      } else {
        this.$refs.multipleTable.clearSelection();
      }
    },
    handleSelectionChange(val) {
      //复选框选择回填函数,val返回一整行的数据
      this.multipleSelection = val;
    },
    importData() {
      this.importFlag = 1;
      this.fileList = [];
      this.uploadTip = "点击上传";
      this.processing = false;
      this.dialogImportVisible = true;
    },
    outportData() {
      scheduleApi.downloadTemplate();
    },
    handlePreview(file) {
      //可以通过 file.response 拿到服务端返回数据
    },
    handleRemove(file, fileList) {
      //文件移除
    },
    handleEdit(index, row) {
      console.log(index, row);
    },
    handleDelete(index, row) {
      console.log(index, row);
    },
    beforeUpload(file) {
      //上传前配置
      // this.importHeaders.cityCode = "上海"; //可以配置请求头
      let excelfileExtend = ".xls,.xlsx,.csv"; //设置文件格式
      let fileExtend = file.name
        .substring(file.name.lastIndexOf("."))
        .toLowerCase();
      if (excelfileExtend.indexOf(fileExtend) <= -1) {
        this.$message.error("文件格式错误");
        return false;
      }
      this.uploadTip = "正在处理中...";
      this.processing = true;
    },
    //上传错误
    uploadFail(err, file, fileList) {
      this.uploadTip = "点击上传";
      this.processing = false;
      this.$message.error(err);
    },
    //上传成功
    uploadSuccess(response, file, fileList) {
      this.uploadTip = "点击上传";
      this.processing = false;
      if (response.status === -1) {
        this.errorResults = response.data;
        if (this.errorResults) {
          this.importFlag = 2;
        } else {
          this.dialogImportVisible = false;
          this.$message.error(response.errorMsg);
        }
      } else {
        this.importFlag = 3;
        this.dialogImportVisible = false;
        this.$message.info("导入成功");
        this.doSearch();
      }
    },
    //下载模板
    download() {
      //调用后台模板方法,和导出类似
      scheduleApi.downloadTemplate();
    }
  }
};
</script>
<style scoped>
.el-main {
  background-color: #e9eef3;
  color: #333;
  text-align: center;
  line-height: 5em;
  height: 700px;
  margin: -20px;
}
body > .el-container {
  margin-bottom: 2.5em;
}
.hide-dialog {
  display: none;
}
.main[data-v-0376c496] {
  height: 100vh - 60px;
  width: 100%;
  overflow: auto;
}
.el-table {
  height: 400px;
}
.listbox {
  width: 80%;
  height: 450px;
  padding: 50px 100px 50px 100px;
}
/* .choosebox {
  width: 80%;
  height: 100px;
} */
</style>