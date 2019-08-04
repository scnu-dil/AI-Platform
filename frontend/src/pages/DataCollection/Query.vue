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
            <!-- <el-button size="mini" @click="handleEdit(scope.$index, scope.row)">编辑</el-button> -->
            <el-button size="mini" type="success" @click="outportData(scope.$index, scope.row)">下载</el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
  </el-main>
</template>

<script>
import axios from 'axios';

export default {
  name: "query",
  data() {
    return {
      tableData3: [
        {
          date: "2019-07-19",
          modelname: "test",
          uploader: "Lyndsey"
        }
      ]
    };
  },
  methods: {
  // 下载文件
  download (data) {
  if (!data) {
    return
  }
  // 标签‘a’，触发下载功能
  let url = window.URL.createObjectURL(new Blob([data]))
  let link = document.createElement('a')
  link.style.display = 'none'
  link.href = url         
  link.setAttribute('download', 'file.csv')

  document.body.appendChild(link)
  link.click()
  },
  outportData(){
    axios.get("http://127.0.0.1:5000/download/file",
    {params: {}})
    .then(response => {
      //this.download(response.data)
      let blob = new Blob([response.data])
      //let filename=response.headers['Content-Disposition'];
      let url = window.URL.createObjectURL(blob)
      let link = document.createElement('a')
      //link.style.display = 'none'
      link.href = url
      link.download = 'test.csv'
      
      document.body.appendChild(link)
      link.click()
      document.body.removeChild(link)
      window.URL.revokeObjectURL(url)
    })
    .catch(error => {
      console.log(error)
    })
  }
/*  toggleSelection(rows) {
      if (rows) {
        rows.forEach(row => {
          this.$refs.multipleTable.toggleRowSelection(row);
        });
      } else {
        this.$refs.multipleTable.clearSelection();
      }
    },
    outportData() {
      scheduleApi.downloadTemplate();
    },
    handlePreview(file) {
      //可以通过 file.response 拿到服务端返回数据
    },
    handleRemove(file, fileList) {
      //文件移除
    }*/
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