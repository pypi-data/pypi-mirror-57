# 图像识别工具-limcv

## 功能
   * 用于自动化测试中，定位icon图片在手机中App截图中的位置，从而进一步针对位置进行点击、输入、滑动操作。
   * 因为是基于图片做的控件定位，所以此工具适用于Android、iOS、小程序、H5自动化测试的应用。
   * 支持多个目标的识别。

## 安装

* `pip3 install limcv`

## 使用说明

* 使用代码

```python
import limcv
res = limcv.find(im_source_path, im_search_path)
print(res)
```

* 输出

```python
[{'result': (996, 584), 'rectangle': ((835, 408), (835, 760), (1158, 760), (1158, 408)), 'confidence': 1.0},
 {'result': (998, 1654), 'rectangle': ((837, 1478), (837, 1830), (1160, 1830), (1160, 1478)), 'confidence': 1.0}]
```

参数 | 解释
:-: | :-:
`result` | 目标中间点
`rectangle` | 矩形位置四个点坐标，分别为左上、右上、右下、左下
`confidence`| 置信度


## 感谢

limcv是基于[aircv](https://github.com/AirtestProject/Airtest/tree/master/airtest/aircv)改造，增加了对多分辨率识别的支持。

## TODO
1. 增加图片比对，用于兼容性测试中，检测App的显示效果是否符合预期。
