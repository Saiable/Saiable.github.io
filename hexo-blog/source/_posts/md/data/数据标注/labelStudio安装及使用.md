---
title: 'labelStudio安装及使用'
cover: false
typora-root-url: labelStudio安装及使用
---

# docker安装

[Label Studio Documentation — Install and Upgrade Label Studio](https://labelstud.io/guide/install#Install-with-Docker)

根据uid查找用户组

```bash
getent group | awk -F: '$3 == 1001 {print $1}'
```


不用管当前的1001对应的是哪一个用户，直接设置

```bash
chown -R 1001:1001 /data/data13/hh/software/label-studio
```

新建子目录data和files，注意更改权限

```bash
docker run -it -p 26900:8080 --privileged=true -v /data/data13/hh/software/label-studio/data:/label-studio/data --env LABEL_STUDIO_LOCAL_FILES_SERVING_ENABLED=true --env LABEL_STUDIO_LOCAL_FILES_DOCUMENT_ROOT=/data/data13/hh/software/label-studio/files -v /data/data13/hh/software/label-studio/files:/label-studio/files heartexlabs/label-studio:latest label-studio
```

`ctrl+p+q`退出页面



配置数据源

[Label Studio Documentation — Cloud and External Storage Integration](https://labelstud.io/guide/storage?experiment=login_revamp&treatment=sync_cloud_data&server_id=28640883-f80e-4ad4-808a-6a6e279d51f9#Local-storage)

选定好目录后

```bash
sudo docker run -it -p 26900:8080 --privileged=true -v $(pwd)/mydata:/label-studio/data  --env LABEL_STUDIO_LOCAL_FILES_SERVING_ENABLED=true --env LABEL_STUDIO_LOCAL_FILES_DOCUMENT_ROOT=/label-studio/files -v $(pwd)/myfiles:/label-studio/files heartexlabs/label-studio:latest label-studio
```

进入容器后，新建目录

```bash
docker exec -it ID /bin/bash
```

在容器内部新建文件夹后，配置的路径是容器内的路径

![image-20240219110807781](image-20240219110807781.png)

首次成功后，就可以在宿主机中新建目录，而不用进入容器里。并且也不用管权限问题，可以直接读取（`--privileged=true`）

![image-20240219111032207](image-20240219111032207.png)

注意导入单文件时，打开如下设置

![image-20240219111249282](image-20240219111249282.png)

如果导入的是JSON，则不需要（待验证）

问题：
- localstorage相当于是用户自己管理的，如果在这个目录中删除了文件，UI上的文件还在

  ![image-20240219112045491](image-20240219112045491.png)

  ![image-20240219112506936](image-20240219112506936.png)

- LS自己在默认路径下，维护着一份语料

  

# 配置

- txt文本设置不按行读取

  data导入选择第三个，tag修改配置项

  ```diff
  - <Text name="text" value="$text"/>
  + <Text name="text" value="$text" valueType="url"/>
  ```

- 图片框选标注支持添加描述（包含ocr）

  ```xml
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
  
- `html`

# 标注数据迁移指南

labelstudio上传的数据集，默认在`/home/rhino/.local/share/label-studio/media/upload/`路径下，文件夹编号和项目编号一致

导出的`json`文件在`/home/rhino/.local/share/label-studio/export/`路径下



背景：现在不用转换文件名的hash了，找到原始标注的文件夹，配置好路径即可

只要修改下路径即可，原来是如下路径：/data/upload/90

现在需要修改成如下：/data/local-files/?d=0006_06_01/0225a044-sdfsA_19.png

批量替换即可。

file-uplod字段不用删

updated_by、completed_by字段要匹配上现在的（类似用户id）

UI上可以正常显示。

另外的问题：原来的任务中的各个标签，一开始没有保存，去哪里找？

打开sqlite数据库文件，在project这个表里

![1708412102529](file:///data/data13/hh/desktop/tag/dwd/0006_%E8%8B%8F%E7%B2%AE%E5%90%88%E5%90%8C%E5%8D%95%E6%8D%AE_%E9%A3%8E%E6%8E%A7/batch_06_%E8%A1%A8%E6%A0%BC%E8%AF%AD%E4%B9%89%E5%AE%9E%E4%BD%93%E5%85%B3%E7%B3%BB/output/labelstudio_migration_script_3.0/readme/1708412102529.png?lastModify=1708412147)

找到了sqlite文件，后面有时间，我们可不可以直接迁移数据库文件呢？



## 如下废弃

如果是同一服务器部署的labelstudio，导出json后，再新建任务导入json，即使是不同的task，也会自动识别出文件

但是，如果是不同环境的labelstudio，需要使用如下脚本进行迁移

目录结构如下：

![image-20240126112851640](image-20240126112851640.png)

```python
import re
import os

def get_filenanme(path):
    filenames = os.listdir(path)
    return filenames

def replace_filenames(content, old_name, new_name):
    # 使用正则表达式替换所有匹配的 old_name
    updated_content = re.sub(re.escape(old_name), new_name, content)
    return updated_content
def get_suffix(filename):
    split_arr = filename.split('-')
    whole_filename = '-'.join(split_arr[1:]) # 即使原始文件名中包含分隔符，也不会有问题
    return str(whole_filename)
if __name__ == '__main__':
    # 配置项
    new_path = './new_filename' # 存放新文件的文件夹
    old_path = './old_filename' # 存放旧文件的文件夹，需要确保两者中的文件数量，是一致的（只是传了两遍而已）
    replace_json = './suliang_label_studio_corpus.json' # 原始标注语料
    replace_result = './suliang_label_studio_corpus_replace_filename.json'  # 新生成的结果文件名
    # 新建项目后的项目id，按照实际更改
    origin_project_id = '16'
    new_project_id = '89'
    
    repalcement_origin_str1 = '/upload/' + origin_project_id + '/'
    repalcement_new_str1 = '/upload/' + new_project_id + '/'
    repalcement_origin_str2 = '"project": '+ origin_project_id + ',' # 注意空格
    repalcement_new_str2 = '"project": ' + new_project_id + ','
    # print(repalcement_origin_str2)
    # 对两个数组中文件名，按照后缀，进行相同的排序处理
    new_filename_group = get_filenanme(new_path)  # 样例：ohsdoHk_data01.png
    old_filename_group = get_filenanme(old_path)  # 样例：iondoLl_data01.png
    
    new_sorted_array1 = sorted(new_filename_group, key=get_suffix)
    old_sorted_array2 = sorted(old_filename_group, key=get_suffix)
    # print(new_sorted_array1)
    # print(old_sorted_array2)

    with open(replace_json, 'r') as fr:
        content = fr.read()

        # 遍历需要替换的文件名对
        for old_name, new_name in zip(old_sorted_array2, new_sorted_array1):
            # 替换文件名
            content = replace_filenames(content, old_name, new_name)
            # 替换包含id的路径
            content = content.replace(repalcement_origin_str1, repalcement_new_str1)
            # 替换包含project的字段值
            content = content.replace(repalcement_origin_str2, repalcement_new_str2)

    # 将替换后的内容写回文件
    with open(replace_result, 'w') as fw:
        fw.write(content)

```





# 配置存储路径

