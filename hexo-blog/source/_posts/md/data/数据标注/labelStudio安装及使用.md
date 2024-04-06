---
title: labelStudio安装及使用
cover: false
typora-root-url: labelStudio安装及使用
abbrlink: 41627
---



# 配置

- txt文本设置不按行读取

  data导入选择第三个，tag修改配置项

  ```diff
  - <Text name="text" value="$text"/>
  + <Text name="text" value="$text" valueType="url"/>
  ```

- 图片框选标注支持添加描述

  ```bash
  <View>
    <Image name="image" value="$image"/>
    <RectangleLabels name="label" toName="image">
      <Label value="Question" background="green"/>
      <Label value="Car" background="blue"/>
    </RectangleLabels>
    <Header value="Describe object"/>
    <TextArea name="answer" toName="image" editable="true" perRegion="true" required="true"/>
  </View>
  ```
  
  

