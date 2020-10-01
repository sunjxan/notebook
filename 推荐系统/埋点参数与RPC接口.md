### 用户行为

##### 1. 获取物品列表（曝光 exposure）

服务器返回列表时，写入日志

##### 2. 阅读物品信息（阅读 read）

用户离开物品时，写入日志，如果停留在某物品时间过长，则取消写入

##### 3. 用户操作事件

用户操作某物品时，写入日志

- 点击（click）
- 收藏（collect）
- 分享（share）
- ......

### 埋点参数

根据曝光返回物品列表的数据，构造埋点参数：

```json
{
    userId: '',
    action: 'exposure|read|click|collect|share',
    timestamp: '',
    // 物品该次曝光所使用的算法策略
    algorithm: '',
    itemId: '',
    // 获取物品列表时使用
    // itemIds: [],
    // 阅读物品时间，阅读事件时使用
    // readTime: ''
}
```

### RPC接口

##### 推荐场景

- 一般推荐（channelRecommend: channelId = 0）  用户 => 物品列表
- 频道内推荐（channelRecommend）  用户 + 物品类别 => 物品列表
- 相似物品推荐（similarRecommend）  用户 + 物品 => 物品列表

##### proto文件（items_recommend.proto）

```
syntax = "proto3";

message ItemsRequest {
    string userId = 1;
    string channelId = 2;
    string itemId = 3;
    // 获取物品的数量
    int32 count = 4;
    // 获取物品的起始位置
    int32 offset = 5;
}

message ItemsReply {
    // 返回的物品列表
    repeated string itemIds = 1;
    // 物品列表该次曝光所使用的算法策略
    string algorithm = 2;
}

service ItemsRecommend {
    rpc channelRecommend(ItemsRequest) returns (ItemsReply) {}
    rpc similarRecommend(ItemsRequest) returns (ItemsReply) {}
}
```

