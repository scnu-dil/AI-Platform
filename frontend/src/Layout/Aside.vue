<template>
  <div class="menu-group" :class="{expand: !collapse}">
    <el-menu unique-opened :collapse="collapse" class="el-menu">
      <template v-for="(group, groupIndex) in menuGroup">

        <template v-if="group.children">
          <el-submenu :key="groupIndex" :index="groupIndex + ''" :disabeld="group.disabeld">
            <template slot="title">
              <i v-if="group.icon" :class="group.icon"/>
              <span slot="title">{{group.label}}</span>
            </template>
            <template v-for="(child, childIndex) in group.children">

              <template v-if="child.children">
                 <el-submenu :key="`${groupIndex}-${childIndex}`" :index="`${groupIndex}-${childIndex}`" :disabled="child.disabeld">
                  <template slot="title">
                    <i v-if="child.icon" :class="child.icon"/>
                    <span slot="title">{{child.label}}</span>
                  </template>
                  <el-menu-item
                    v-for="(item, itemIndex) in child.children"
                    :key="`${groupIndex}-${childIndex}-${itemIndex}`"
                    :index="`${groupIndex}-${childIndex}-${itemIndex}`"
                    :disabled="item.disabeld"
                    @click="handleNavClick(item)">
                    <i v-if="item.icon" :class="item.icon"/>
                    <span slot="title">{{item.label}}</span>
                  </el-menu-item>
                 </el-submenu>
              </template>
              <template v-else>
                <el-menu-item
                  :key="`${groupIndex}-${childIndex}`"
                  :index="`${groupIndex}-${childIndex}`"
                  :disabled="child.disabled"
                  @click="handleNavClick(child)">
                  <i v-if="child.icon" :class="child.icon"/>
                  <span slot="title">{{child.label}}</span>
                </el-menu-item>
              </template>
            </template>
          </el-submenu>
        </template>

        <template v-else>
          <el-menu-item
            :key="`${groupIndex}`"
            :index="`${groupIndex} + ''`"
            @click="handleNavClick(group)"
            :disabled="group.disabled">
            <i v-if="group.icon" :class="group.icon"/>
            <span slot="title">{{group.label}}</span>
          </el-menu-item>
        </template>
      </template>
      <span class="collapse" @click="switchCollapse"><i :class="collapse ? 'el-icon-s-unfold' : 'el-icon-s-fold'" /></span>
    </el-menu>
  </div>
</template>

<script>
import { menuGroup } from '@/config/menus'
export default {
  name: 'menu-group',

  props: {
    collapse: Boolean
  },

  data () {
    this.menuGroup = menuGroup
    return {

    }
  },

  methods: {
    handleNavClick (item) {
      console.log(item)
      item.name && this.$router.push({ name: item.name })
    },

    switchCollapse () {
      this.$emit('collaspeChange', this.collapse)
    }
  }
}
</script>

<style>
.collapse {
  position: absolute;
  bottom: 10px;
  display: inline-block;
  left: 0;
  right: 0;
  margin: auto;
  text-align: center;
  padding: 5px;
  font-size: 18px;
  color: #909399;
  cursor: pointer;
}
.menu-group {
  height: 100%;
  transition: width .3s;
}
.el-menu {
  height: 100%;
}
.expand {
  min-width: 200px;
}
</style>
