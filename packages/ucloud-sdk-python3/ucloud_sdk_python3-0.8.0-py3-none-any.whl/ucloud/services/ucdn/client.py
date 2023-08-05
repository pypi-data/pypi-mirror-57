""" Code is generated by ucloud-model, DO NOT EDIT IT. """

import typing


from ucloud.core.client import Client
from ucloud.services.ucdn.schemas import apis


class UCDNClient(Client):
    def __init__(
        self, config: dict, transport=None, middleware=None, logger=None
    ):
        super(UCDNClient, self).__init__(config, transport, middleware, logger)

    def batch_describe_new_ucdn_domain(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ BatchDescribeNewUcdnDomain - 批量获取加速域名配置

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **ChannelType** (str) - 渠道ucdn、ufile、uvideo
        - **DomainId** (list) - 域名id，创建域名时生成的资源id，默认获取账号下的所有域名信息，n为自然数
        - **Limit** (int) - 返回数据长度，如果制定了Offset，则默认20，否则默认全部，非负整数
        - **Offset** (int) - 数据偏移量，默认0，非负整数
        
        **Response**

        - **Arrearage** (list) - 标识欠费的数组，数组含有下列元素值， 1=国内流量有欠费 2=国外流量有欠费  3=国内带宽有欠费 4=国外带宽有欠费
        - **ChargeType** (int) - 当前计费方式，10=流量付费 20=带宽日峰值  30=按月后付费
        - **DomainSet** (list) - 见 **DomainInfo** 模型定义
        - **LastChargeType** (int) - 表示最后一次切换的计费方式，10=流量付费 20=带宽日峰值  30=按月后付费  40=未选择计费方式
        - **MaxDomainNum** (int) - 最大域名数量，默认20
        - **TotalCount** (int) - 满足条件的域名个数
        - **Vip** (str) - vip标示，yes-是  no-否
        
        **Response Model**
        
        **CacheConf** 
        
        - **CacheBehavior** (int) - 是否缓存，1为缓存，0为不缓存。为0的情况下，CacheTTL和CacheUnit强制不生效
        - **CacheTTL** (int) - 缓存时间
        - **CacheUnit** (str) - 缓存时间的单位。sec（秒），min（分钟），hour（小时），day（天）
        - **Description** (str) - 缓存规则描述
        - **FollowOriginRule** (int) - 是否优先遵循源站头部缓存策略，0为不优先遵循源站，1为优先遵循源站缓存头部。默认为0
        - **HttpCodePattern** (str) - 状态码默认情况只缓存200类状态码，支持正则
        - **IgnoreQueryString** (int) - 是否忽略参数缓存（0为不忽略，1为忽略，默认为0）
        - **PathPattern** (str) - 路径模式，支持正则

        **AccessConf** 
        
        - **IpBlacklist** (str) - 多个ip用逗号隔开

        **DomainInfo** 
        
        - **AccessConf** (dict) - 见 **AccessConf** 模型定义
        - **AreaCode** (str) - 查询带宽区域 cn代表国内 abroad代表海外 不填默认为全部区域
        - **CacheConf** (list) - 见 **CacheConf** 模型定义
        - **CacheHost** (str) - 缓存Host，不同的域名可以配置为同一个CacheHost来实现缓存共享，默认为加速域名
        - **CdnProtocol** (str) - 加速类型http,http|https
        - **CdnType** (str) - 加速域名的业务类型，web代表网站，stream代表视频，download代表下载。
        - **CertName** (str) - 证书名称
        - **Cname** (str) - cdn域名。创建加速域名生成的cdn域名，用于设置CNAME记录
        - **CreateTime** (int) - 域名创建的时间。格式：时间戳
        - **Domain** (str) - 域名，用户创建加速的域名
        - **DomainId** (str) - 域名id，创建域名时生成的id
        - **HttpsStatusAbroad** (str) - 国外https状态 enableing-开启中  fail-开启失败 enable-启用 disable-未启用
        - **HttpsStatusCn** (str) - 国内https状态 enableing-开启中 fail-开启失败 enable-启用 disable-未启用
        - **NullRefer** (bool) - ReferType为白名单时，NullRefer为false代表不允许NULL refer访问，为true代表允许Null refer访问
        - **OriginHost** (str) - 回源Http请求头部Host，默认是加速域名
        - **OriginIp** (list) - 源站ip即cdn服务器回源访问的ip地址。支持多个源站ip，多个源站ip，可表述为如：[1.1.1.1,2.2.2.2]
        - **OriginPort** (int) - 回源端口
        - **OriginProtocol** (str) - 源站协议http，http|https   默认http
        - **ReferList** (list) - Refer列表，支持正则表达式
        - **ReferStatus** (bool) - refer配置开关，true打开，false关闭
        - **ReferType** (int) - 0白名单，1黑名单
        - **Status** (str) - 创建的加速域名的当前的状态。check代表审核中，checkSuccess代表审核通过，checkFail代表审核失败，enable代表加速中，disable代表停止加速，delete代表删除加速 enableing代表正在开启加速，disableing代表正在停止加速中，deleteing代表删除中
        - **Tag** (str) - 业务组，默认为Default
        - **TestUrl** (str) - 测试url，用于域名创建加速时的测试
        - **ValidTime** (int) - 开始分配Cname时间。格式：时间戳

        """
        # build request
        d = {"ProjectId": self.config.project_id}
        req and d.update(req)
        d = apis.BatchDescribeNewUcdnDomainRequestSchema().dumps(d)

        resp = self.invoke("BatchDescribeNewUcdnDomain", d, **kwargs)
        return apis.BatchDescribeNewUcdnDomainResponseSchema().loads(resp)

    def describe_new_ucdn_prefetch_cache_task(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ DescribeNewUcdnPrefetchCacheTask - 获取预取任务状态

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **BeginTime** (int) - 查询的起始时间，格式为Unix Timestamp。如果有EndTime，BeginTime必须赋值
        - **EndTime** (int) - 查询的结束时间，格式为Unix Timestamp。EndTime默认为当前时间，BeginTime默认为当前时间前一天时间。
        - **Limit** (int) - 返回数据长度,默认全部，自然数
        - **Offset** (int) - 数据偏移量，默认为0，自然数
        - **Status** (str) - 需要获取的内容预热的状态，枚举值：success：成功；wait：等待处理；process：正在处理；failure：失败； unknow：未知，默认选择所有状态
        - **TaskId** (list) - 提交任务时返回的任务ID
        
        **Response**

        - **TaskList** (list) - 见 **TaskInfo** 模型定义
        - **TotalCount** (int) - 预热任务的总数
        
        **Response Model**
        
        **UrlProgressInfo** 
        
        - **CreateTime** (int) - 刷新任务创建的时间。格式为Unix Timestamp
        - **FinishTime** (int) - 任务完成时间。格式为Unix Timestamp
        - **Progress** (int) - 刷新进度，单位%
        - **Status** (str) - 刷新任务的当前状态，枚举值：success：成功；wait：排队中；process：处理中；failure：失败； unknow：未知
        - **Url** (str) - 刷新的单条url

        **TaskInfo** 
        
        - **CreateTime** (int) - 刷新任务创建的时间。格式为Unix Timestamp
        - **Status** (str) - 刷新任务的当前状态，枚举值：success：成功；wait：排队中；process：处理中；failure：失败； unknow：未知
        - **TaskId** (str) - 提交任务时返回的任务ID
        - **Type** (str) - file/dir  刷新任务会返回Type，预取任务没有
        - **UrlLists** (list) - 见 **UrlProgressInfo** 模型定义

        """
        # build request
        d = {"ProjectId": self.config.project_id}
        req and d.update(req)
        d = apis.DescribeNewUcdnPrefetchCacheTaskRequestSchema().dumps(d)

        resp = self.invoke("DescribeNewUcdnPrefetchCacheTask", d, **kwargs)
        return apis.DescribeNewUcdnPrefetchCacheTaskResponseSchema().loads(resp)

    def describe_new_ucdn_refresh_cache_task(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ DescribeNewUcdnRefreshCacheTask - 获取域名刷新任务状态

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **BeginTime** (int) - 查询的起始时间，格式为Unix Timestamp。如果有EndTime，BeginTime必须赋值
        - **EndTime** (int) - 查询的结束时间，格式为Unix Timestamp。EndTime默认为当前时间，BeginTime默认为当前时间前一天时间。
        - **Limit** (int) - 返回数据长度,默认全部，自然数
        - **Offset** (int) - 数据偏移量，默认为0，自然数
        - **Status** (str) - 需要获取的内容刷新的状态，枚举值：success：成功；wait：等待处理；process：正在处理；failure：失败； unknow：未知，默认选择所有状态
        - **TaskId** (list) - 提交任务时返回的任务ID
        
        **Response**

        - **TaskList** (list) - 见 **TaskInfo** 模型定义
        - **TotalCount** (int) - 刷新任务的总数
        
        **Response Model**
        
        **UrlProgressInfo** 
        
        - **CreateTime** (int) - 刷新任务创建的时间。格式为Unix Timestamp
        - **FinishTime** (int) - 任务完成时间。格式为Unix Timestamp
        - **Progress** (int) - 刷新进度，单位%
        - **Status** (str) - 刷新任务的当前状态，枚举值：success：成功；wait：排队中；process：处理中；failure：失败； unknow：未知
        - **Url** (str) - 刷新的单条url

        **TaskInfo** 
        
        - **CreateTime** (int) - 刷新任务创建的时间。格式为Unix Timestamp
        - **Status** (str) - 刷新任务的当前状态，枚举值：success：成功；wait：排队中；process：处理中；failure：失败； unknow：未知
        - **TaskId** (str) - 提交任务时返回的任务ID
        - **Type** (str) - file/dir  刷新任务会返回Type，预取任务没有
        - **UrlLists** (list) - 见 **UrlProgressInfo** 模型定义

        """
        # build request
        d = {"ProjectId": self.config.project_id}
        req and d.update(req)
        d = apis.DescribeNewUcdnRefreshCacheTaskRequestSchema().dumps(d)

        resp = self.invoke("DescribeNewUcdnRefreshCacheTask", d, **kwargs)
        return apis.DescribeNewUcdnRefreshCacheTaskResponseSchema().loads(resp)

    def get_new_ucdn_domain_bandwidth(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ GetNewUcdnDomainBandwidth - 获取域名带宽数据

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Type** (int) - (Required) 时间粒度（0表示按照5分钟粒度，1表示按照1小时粒度，2表示按照一天的粒度）
        - **Areacode** (str) - 查询带宽区域 cn代表国内 abroad代表海外 不填默认为全部区域
        - **BeginTime** (int) - 查询的起始时间，格式为Unix Timestamp。如果有EndTime，BeginTime必须赋值。如没有赋值，则返回缺少参 数错误，如果没有EndTime，BeginTime也可以不赋值，EndTime默认当前时间，BeginTime 默认前一天的当前时间。
        - **DomainId** (list) - 域名id，创建域名时生成的id。默认全部域名
        - **EndTime** (int) - 查询的结束时间，格式为Unix Timestamp。EndTime默认为当前时间，BeginTime默认为当前时间前一天时间。
        
        **Response**

        - **BandwidthList** (list) - 见 **BandwidthInfo** 模型定义
        - **Traffic** (str) - 从起始时间到结束时间内的所使用的CDN总流量，单位GB
        
        **Response Model**
        
        **BandwidthInfo** 
        
        - **CdnBandwidth** (str) - 返回值返回指定时间区间内CDN的带宽峰值，单位Mbps（如果请求参数Type为0，则Value是五分钟粒度的带宽值，如果Type为1，则Value是1小时的带宽峰值，如果Type为2，则Value是一天内的带宽峰值）
        - **Time** (int) - 带宽获取的时间点。格式：时间戳

        """
        # build request
        d = {"ProjectId": self.config.project_id}
        req and d.update(req)
        d = apis.GetNewUcdnDomainBandwidthRequestSchema().dumps(d)

        resp = self.invoke("GetNewUcdnDomainBandwidth", d, **kwargs)
        return apis.GetNewUcdnDomainBandwidthResponseSchema().loads(resp)

    def get_new_ucdn_domain_hit_rate(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ GetNewUcdnDomainHitRate - 获取域名命中率

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Type** (int) - (Required) 时间粒度（0表示按照5分钟粒度，1表示按照1小时粒度，2表示按照一天的粒度）
        - **Areacode** (str) - 查询带宽区域 cn代表国内 abroad代表海外，只支持国内
        - **BeginTime** (int) - 查询的起始时间，格式为Unix Timestamp。如果有EndTime，BeginTime必须赋值。如没有赋值，则返回缺少参 数错误，如果没有EndTime，BeginTime也可以不赋值，EndTime默认当前时间，BeginTime 默认前一天的当前时间。
        - **DomainId** (list) - 域名id，创建域名时生成的id。默认全部域名
        - **EndTime** (int) - 查询的结束时间，格式为Unix Timestamp。EndTime默认为当前时间，BeginTime默认为当前时间前一天时间。
        
        **Response**

        - **HitRateList** (list) - 见 **HitRateInfo** 模型定义
        
        **Response Model**
        
        **HitRateInfo** 
        
        - **FlowHitRate** (float) - 流量命中率，单位%
        - **RequestHitRate** (float) - 请求数命中率，单位%
        - **Time** (int) - 带宽获取的时间点。格式：时间戳

        """
        # build request
        d = {"ProjectId": self.config.project_id}
        req and d.update(req)
        d = apis.GetNewUcdnDomainHitRateRequestSchema().dumps(d)

        resp = self.invoke("GetNewUcdnDomainHitRate", d, **kwargs)
        return apis.GetNewUcdnDomainHitRateResponseSchema().loads(resp)

    def get_new_ucdn_domain_http_code(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ GetNewUcdnDomainHttpCode - 获取域名状态码监控

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Type** (int) - (Required) 时间粒度（0表示按照5分钟粒度，1表示按照1小时粒度，2表示按照一天的粒度）
        - **Areacode** (str) - 查询带宽区域 cn代表国内 abroad代表海外，只支持国内
        - **BeginTime** (int) - 查询的起始时间，格式为Unix Timestamp。如果有EndTime，BeginTime必须赋值。如没有赋值，则返回缺少参 数错误，如果没有EndTime，BeginTime也可以不赋值，EndTime默认当前时间，BeginTime 默认前一天的当前时间。
        - **DomainId** (list) - 域名id，创建域名时生成的id。默认全部域名
        - **EndTime** (int) - 查询的结束时间，格式为Unix Timestamp。EndTime默认为当前时间，BeginTime默认为当前时间前一天时间。
        
        **Response**

        - **HttpCodeDetail** (list) - 见 **HttpCodeInfo** 模型定义
        
        **Response Model**
        
        **HttpCodeInfo** 
        
        - **HttpFiveXX** (int) - 5xx数量
        - **HttpFourXX** (int) - 4xx数量
        - **HttpOneXX** (int) - 1xx数量
        - **HttpThreeXX** (int) - 3xx数量
        - **HttpTwoXX** (int) - 2xx数量
        - **Time** (int) - 带宽获取的时间点。格式：时间戳

        """
        # build request
        d = {"ProjectId": self.config.project_id}
        req and d.update(req)
        d = apis.GetNewUcdnDomainHttpCodeRequestSchema().dumps(d)

        resp = self.invoke("GetNewUcdnDomainHttpCode", d, **kwargs)
        return apis.GetNewUcdnDomainHttpCodeResponseSchema().loads(resp)

    def get_new_ucdn_domain_http_code_v2(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ GetNewUcdnDomainHttpCodeV2 - 获取域名详细状态码监控

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **BeginTime** (int) - (Required) 查询的起始时间，格式为Unix Timestamp。
        - **EndTime** (int) - (Required) 查询的结束时间，格式为Unix Timestamp。
        - **Type** (int) - (Required) 时间粒度（0表示按照5分钟粒度，1表示按照1小时粒度，2表示按照一天粒度，3表示按照一分钟粒度）
        - **Areacode** (str) - 查询带宽区域 cn代表国内 abroad代表海外，只支持国内
        - **DomainId** (list) - 域名id，创建域名时生成的id。默认全部域名
        
        **Response**

        - **HttpCodeV2Detail** (list) - 见 **HttpCodeV2Detail** 模型定义
        
        **Response Model**
        
        **HttpCodeV2Detail** 
        
        - **Http100** (int) - http100数量
        - **Http101** (int) - http101数量
        - **Http102** (int) - http102数量
        - **Http200** (int) - http200数量
        - **Http201** (int) - http201数量
        - **Http202** (int) - http202数量
        - **Http203** (int) - http203数量
        - **Http204** (int) - http204数量
        - **Http205** (int) - http205数量
        - **Http206** (int) - http206数量
        - **Http207** (int) - http207数量
        - **Http300** (int) - http300数量
        - **Http301** (int) - http301数量
        - **Http302** (int) - http302数量
        - **Http303** (int) - http303数量
        - **Http304** (int) - http304数量
        - **Http305** (int) - http305数量
        - **Http306** (int) - http306数量
        - **Http307** (int) - http307数量
        - **Http400** (int) - http400数量
        - **Http401** (int) - http401数量
        - **Http402** (int) - http402数量
        - **Http403** (int) - http403数量
        - **Http404** (int) - http404数量
        - **Http405** (int) - http405数量
        - **Http406** (int) - http406数量
        - **Http407** (int) - http407数量
        - **Http408** (int) - http408数量
        - **Http409** (int) - http409数量
        - **Http410** (int) - http410数量
        - **Http411** (int) - http411数量
        - **Http412** (int) - http412数量
        - **Http413** (int) - http413数量
        - **Http414** (int) - http414数量
        - **Http415** (int) - http415数量
        - **Http416** (int) - http416数量
        - **Http417** (int) - http417数量
        - **Http418** (int) - http418数量
        - **Http421** (int) - http421数量
        - **Http422** (int) - http422数量
        - **Http423** (int) - http423数量
        - **Http424** (int) - http424数量
        - **Http425** (int) - http425数量
        - **Http426** (int) - http426数量
        - **Http449** (int) - http449数量
        - **Http451** (int) - http451数量
        - **Http500** (int) - http500数量
        - **Http501** (int) - http501数量
        - **Http502** (int) - http502数量
        - **Http503** (int) - http503数量
        - **Http504** (int) - http504数量
        - **Http505** (int) - http505数量
        - **Http506** (int) - http506数量
        - **Http507** (int) - http507数量
        - **Http509** (int) - http509数量
        - **Http510** (int) - http510数量
        - **Time** (int) - 时间

        """
        # build request
        d = {"ProjectId": self.config.project_id}
        req and d.update(req)
        d = apis.GetNewUcdnDomainHttpCodeV2RequestSchema().dumps(d)

        resp = self.invoke("GetNewUcdnDomainHttpCodeV2", d, **kwargs)
        return apis.GetNewUcdnDomainHttpCodeV2ResponseSchema().loads(resp)

    def get_new_ucdn_domain_request_num(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ GetNewUcdnDomainRequestNum - 获取域名请求数

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Type** (int) - (Required) 时间粒度（0表示按照5分钟粒度，1表示按照1小时粒度，2表示按照一天的粒度）
        - **Areacode** (str) - 查询区域 cn代表国内 abroad代表海外，只支持国内
        - **BeginTime** (int) - 查询的起始时间，格式为Unix Timestamp。如果有EndTime，BeginTime必须赋值。如没有赋值，则返回缺少参 数错误，如果没有EndTime，BeginTime也可以不赋值，EndTime默认当前时间，BeginTime 默认前一天的当前时间。
        - **DomainId** (list) - 域名id，创建域名时生成的id。默认全部域名
        - **EndTime** (int) - 查询的结束时间，格式为Unix Timestamp。EndTime默认为当前时间，BeginTime默认为当前时间前一天时间。
        
        **Response**

        - **RequestList** (list) - 见 **RequestInfo** 模型定义
        
        **Response Model**
        
        **RequestInfo** 
        
        - **CdnRequest** (float) - 返回值返回指定时间区间内的cdn收到的请求次数之和
        - **OriginRequest** (float) - 返回值返回指定时间区间内的cdn回源的请求次数之和
        - **Time** (int) - 带宽获取的时间点。格式：时间戳

        """
        # build request
        d = {"ProjectId": self.config.project_id}
        req and d.update(req)
        d = apis.GetNewUcdnDomainRequestNumRequestSchema().dumps(d)

        resp = self.invoke("GetNewUcdnDomainRequestNum", d, **kwargs)
        return apis.GetNewUcdnDomainRequestNumResponseSchema().loads(resp)

    def get_ucdn_domain_log(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ GetUcdnDomainLog - 获取加速域名原始日志

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **BeginTime** (int) - 查询的起始时间，格式为Unix Timestamp。如果有EndTime，BeginTime必须赋值。
        - **DomainId** (list) - 域名ID，创建加速域名时生成。默认全部域名
        - **EndTime** (int) - 查询的结束时间，格式为Unix Timestamp。EndTime默认为当前时间，BeginTime默认为当前时间前一天时间。
        - **Type** (int) - 查询粒度  0=default(没有粒度) 1=按小时  2=按天
        
        **Response**

        - **LogSet** (list) - 见 **LogSetList** 模型定义
        
        **Response Model**
        
        **LogSetInfo** 
        
        - **AbroadLog** (list) - 国外日志url列表
        - **CnLog** (list) - 国内日志url列表
        - **Time** (int) - 日志时间UnixTime

        **LogSetList** 
        
        - **Domain** (str) - 域名
        - **Logs** (list) - 见 **LogSetInfo** 模型定义

        """
        # build request
        d = {"ProjectId": self.config.project_id}
        req and d.update(req)
        d = apis.GetUcdnDomainLogRequestSchema().dumps(d)

        resp = self.invoke("GetUcdnDomainLog", d, **kwargs)
        return apis.GetUcdnDomainLogResponseSchema().loads(resp)

    def get_ucdn_domain_prefetch_enable(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ GetUcdnDomainPrefetchEnable - 获取域名预取开启状态

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **DomainId** (str) - (Required) 域名ID，创建加速域名时生成。
        
        **Response**

        - **Enable** (int) - 0表示该域名未开启预取，1表示该域名已开启预取
        
        """
        # build request
        d = {"ProjectId": self.config.project_id}
        req and d.update(req)
        d = apis.GetUcdnDomainPrefetchEnableRequestSchema().dumps(d)

        resp = self.invoke("GetUcdnDomainPrefetchEnable", d, **kwargs)
        return apis.GetUcdnDomainPrefetchEnableResponseSchema().loads(resp)

    def get_ucdn_domain_request_num_v2(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ GetUcdnDomainRequestNumV2 - 获取域名请求数

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **BeginTime** (int) - (Required) 查询的起始时间，格式为Unix Timestamp
        - **EndTime** (int) - (Required) 查询的结束时间，格式为Unix Timestamp
        - **Type** (int) - (Required) 时间粒度（0表示按照5分钟粒度，1表示按照1小时粒度，2表示按照一天的粒度, 3=按1分钟）
        - **Areacode** (str) - 查询区域 cn代表国内 abroad代表海外，只支持国内
        - **DomainId** (list) - 域名id，创建域名时生成的id。默认全部域名
        
        **Response**

        - **RequestList** (list) - 见 **RequestInfo** 模型定义
        
        **Response Model**
        
        **RequestInfo** 
        
        - **CdnRequest** (float) - 返回值返回指定时间区间内的cdn收到的请求次数之和
        - **OriginRequest** (float) - 返回值返回指定时间区间内的cdn回源的请求次数之和
        - **Time** (int) - 带宽获取的时间点。格式：时间戳

        """
        # build request
        d = {"ProjectId": self.config.project_id}
        req and d.update(req)
        d = apis.GetUcdnDomainRequestNumV2RequestSchema().dumps(d)

        resp = self.invoke("GetUcdnDomainRequestNumV2", d, **kwargs)
        return apis.GetUcdnDomainRequestNumV2ResponseSchema().loads(resp)

    def get_ucdn_domain_traffic(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ GetUcdnDomainTraffic - 获取加速域名流量使用信息

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Areacode** (str) - 查询流量区域 cn代表国内 abroad代表海外，默认全部区域。
        - **BeginTime** (int) - 查询的起始时间，格式为Unix Timestamp。如果有EndTime，BeginTime必须赋值。
        - **DomainId** (list) - 域名ID，创建加速域名时生成。默认全部域名
        - **EndTime** (int) - 查询的结束时间，格式为Unix Timestamp。EndTime默认为当前时间，BeginTime默认为当前时间前一天时间。
        
        **Response**

        - **TrafficSet** (list) - 见 **UcdnDomainTrafficSet** 模型定义
        
        **Response Model**
        
        **UcdnDomainTrafficSet** 
        
        - **Time** (int) - 流量获取的时间点，格式为Unix Timestamp
        - **Value** (float) - 查询每日流量总值，单位：GB

        """
        # build request
        d = {"ProjectId": self.config.project_id}
        req and d.update(req)
        d = apis.GetUcdnDomainTrafficRequestSchema().dumps(d)

        resp = self.invoke("GetUcdnDomainTraffic", d, **kwargs)
        return apis.GetUcdnDomainTrafficResponseSchema().loads(resp)

    def get_ucdn_pass_bandwidth(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ GetUcdnPassBandwidth - 获取回源带宽数据（cdn回客户源站部分）

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Type** (int) - (Required) 时间粒度（0表示按照5分钟粒度，1表示按照1小时粒度，2表示按照一天的粒度）
        - **Areacode** (str) - 查询带宽区域 cn代表国内 abroad代表海外，只支持国内
        - **BeginTime** (int) - 查询的起始时间，格式为Unix Timestamp。如果有EndTime，BeginTime必须赋值。如没有赋值，则返回缺少参 数错误，如果没有EndTime，BeginTime也可以不赋值，EndTime默认当前时间，BeginTime 默认前一天的当前时间。
        - **DomainId** (list) - 域名id，创建域名时生成的id。默认全部域名
        - **EndTime** (int) - 查询的结束时间，格式为Unix Timestamp。EndTime默认为当前时间，BeginTime默认为当前时间前一天时间。
        
        **Response**

        - **BandwidthDetail** (list) - 见 **BandwidthInfoDetail** 模型定义
        
        **Response Model**
        
        **BandwidthInfoDetail** 
        
        - **Bandwidth** (float) - 返回值带宽值数据。
        - **Time** (int) - 宽获取的时间点。格式：时间戳

        """
        # build request
        d = {"ProjectId": self.config.project_id}
        req and d.update(req)
        d = apis.GetUcdnPassBandwidthRequestSchema().dumps(d)

        resp = self.invoke("GetUcdnPassBandwidth", d, **kwargs)
        return apis.GetUcdnPassBandwidthResponseSchema().loads(resp)

    def get_ucdn_traffic(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ GetUcdnTraffic - 获取流量信息

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        
        **Response**

        - **TrafficSet** (list) - 见 **TrafficSet** 模型定义
        
        **Response Model**
        
        **TrafficSet** 
        
        - **Areacode** (str) - 购买流量的区域, cn: 国内; abroad: 国外
        - **TrafficLeft** (str) - Areacode区域内总剩余流量, 单位GB
        - **TrafficTotal** (str) - Areacode区域内总购买流量, 单位GB
        - **TrafficUsed** (str) - Areacode区域内总使用流量, 单位GB

        """
        # build request
        d = {"ProjectId": self.config.project_id}
        req and d.update(req)
        d = apis.GetUcdnTrafficRequestSchema().dumps(d)

        resp = self.invoke("GetUcdnTraffic", d, **kwargs)
        return apis.GetUcdnTrafficResponseSchema().loads(resp)

    def prefetch_new_ucdn_domain_cache(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ PrefetchNewUcdnDomainCache - 提交预取任务

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **UrlList** (list) - (Required) 预热URL列表，n从自然数0开始。UrlList.n字段必须以”http://域名/”开始。目录要以”/”结尾， 如刷新目录a下所有文件，格式为：http://abc.ucloud.cn/a/；如刷新文件目录a下面img.png文件， 格式为http://abc.ucloud.cn/a/img.png。请正确提交需要刷新的域名
        
        **Response**

        - **TaskId** (str) - 本次提交url对应的任务id
        
        """
        # build request
        d = {"ProjectId": self.config.project_id}
        req and d.update(req)
        d = apis.PrefetchNewUcdnDomainCacheRequestSchema().dumps(d)

        resp = self.invoke("PrefetchNewUcdnDomainCache", d, **kwargs)
        return apis.PrefetchNewUcdnDomainCacheResponseSchema().loads(resp)

    def refresh_new_ucdn_domain_cache(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ RefreshNewUcdnDomainCache - 刷新缓存

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Type** (str) - (Required) 刷新类型，file代表文件刷新，dir 代表路径刷新
        - **UrlList** (list) - (Required) 刷新多个URL列表时，一次最多提交30个。必须以”http://域名/”开始。目录要以”/”结尾， 如刷新目录a下所有文件，格式为：http://abc.ucloud.cn/a/；如刷新文件目录a下面img.png文件， 格式为http://abc.ucloud.cn/a/img.png。请正确提交需要刷新的域名
        
        **Response**

        - **TaskId** (str) - 本次提交url对应的任务id
        
        """
        # build request
        d = {"ProjectId": self.config.project_id}
        req and d.update(req)
        d = apis.RefreshNewUcdnDomainCacheRequestSchema().dumps(d)

        resp = self.invoke("RefreshNewUcdnDomainCache", d, **kwargs)
        return apis.RefreshNewUcdnDomainCacheResponseSchema().loads(resp)

    def switch_ucdn_charge_type(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ SwitchUcdnChargeType - 切换账号计费方式

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **ChargeType** (str) - (Required) 计费方式。traffic代表按流量包计费，bandwidth按带宽付费
        
        **Response**

        
        """
        # build request
        d = {"ProjectId": self.config.project_id}
        req and d.update(req)
        d = apis.SwitchUcdnChargeTypeRequestSchema().dumps(d)

        resp = self.invoke("SwitchUcdnChargeType", d, **kwargs)
        return apis.SwitchUcdnChargeTypeResponseSchema().loads(resp)
