""" Code is generated by ucloud-model, DO NOT EDIT IT. """

from ucloud.core.typesystem import schema, fields
from ucloud.services.unet.schemas import models


""" UNet API Schema
"""


"""
API: AllocateEIP

根据提供信息, 申请弹性IP
"""


class AllocateEIPRequestSchema(schema.RequestSchema):
    """ AllocateEIP - 根据提供信息, 申请弹性IP
    """

    fields = {
        "Bandwidth": fields.Int(required=True, dump_to="Bandwidth"),
        "ChargeType": fields.Str(required=False, dump_to="ChargeType"),
        "CouponId": fields.Str(required=False, dump_to="CouponId"),
        "Name": fields.Str(required=False, dump_to="Name"),
        "OperatorName": fields.Str(required=True, dump_to="OperatorName"),
        "PayMode": fields.Str(required=False, dump_to="PayMode"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Quantity": fields.Int(required=False, dump_to="Quantity"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Remark": fields.Str(required=False, dump_to="Remark"),
        "ShareBandwidthId": fields.Str(
            required=False, dump_to="ShareBandwidthId"
        ),
        "Tag": fields.Str(required=False, dump_to="Tag"),
    }


class AllocateEIPResponseSchema(schema.ResponseSchema):
    """ AllocateEIP - 根据提供信息, 申请弹性IP
    """

    fields = {
        "EIPSet": fields.List(
            models.UnetAllocateEIPSetSchema(),
            required=False,
            load_from="EIPSet",
        )
    }


"""
API: AllocateShareBandwidth

开通共享带宽
"""


class AllocateShareBandwidthRequestSchema(schema.RequestSchema):
    """ AllocateShareBandwidth - 开通共享带宽
    """

    fields = {
        "BwType": fields.Str(required=False, dump_to="BwType"),
        "ChargeType": fields.Str(required=True, dump_to="ChargeType"),
        "Name": fields.Str(required=True, dump_to="Name"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Quantity": fields.Int(required=False, dump_to="Quantity"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "ShareBandwidth": fields.Int(required=True, dump_to="ShareBandwidth"),
        "ShareBandwidthGuarantee": fields.Int(
            required=False, dump_to="ShareBandwidthGuarantee"
        ),
    }


class AllocateShareBandwidthResponseSchema(schema.ResponseSchema):
    """ AllocateShareBandwidth - 开通共享带宽
    """

    fields = {
        "ShareBandwidthId": fields.Str(
            required=False, load_from="ShareBandwidthId"
        )
    }


"""
API: AllocateVIP

根据提供信息，申请内网VIP(Virtual IP），多用于高可用程序作为漂移IP。
"""


class AllocateVIPRequestSchema(schema.RequestSchema):
    """ AllocateVIP - 根据提供信息，申请内网VIP(Virtual IP），多用于高可用程序作为漂移IP。
    """

    fields = {
        "BusinessId": fields.Str(required=False, dump_to="BusinessId"),
        "Count": fields.Int(required=False, dump_to="Count"),
        "Ip": fields.Str(required=False, dump_to="Ip"),
        "Name": fields.Str(required=False, dump_to="Name"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Remark": fields.Str(required=False, dump_to="Remark"),
        "SubnetId": fields.Str(required=True, dump_to="SubnetId"),
        "Tag": fields.Str(required=False, dump_to="Tag"),
        "VPCId": fields.Str(required=True, dump_to="VPCId"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class AllocateVIPResponseSchema(schema.ResponseSchema):
    """ AllocateVIP - 根据提供信息，申请内网VIP(Virtual IP），多用于高可用程序作为漂移IP。
    """

    fields = {
        "DataSet": fields.List(
            fields.Str(), required=False, load_from="DataSet"
        ),
        "VIPSet": fields.List(
            models.VIPSetSchema(), required=False, load_from="VIPSet"
        ),
    }


"""
API: AssociateEIPWithShareBandwidth

将EIP加入共享带宽
"""


class AssociateEIPWithShareBandwidthRequestSchema(schema.RequestSchema):
    """ AssociateEIPWithShareBandwidth - 将EIP加入共享带宽
    """

    fields = {
        "EIPIds": fields.List(fields.Str()),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "ShareBandwidthId": fields.Str(
            required=True, dump_to="ShareBandwidthId"
        ),
    }


class AssociateEIPWithShareBandwidthResponseSchema(schema.ResponseSchema):
    """ AssociateEIPWithShareBandwidth - 将EIP加入共享带宽
    """

    fields = {}


"""
API: BindEIP

将尚未使用的弹性IP绑定到指定的资源
"""


class BindEIPRequestSchema(schema.RequestSchema):
    """ BindEIP - 将尚未使用的弹性IP绑定到指定的资源
    """

    fields = {
        "EIPId": fields.Str(required=True, dump_to="EIPId"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "ResourceId": fields.Str(required=True, dump_to="ResourceId"),
        "ResourceType": fields.Str(required=True, dump_to="ResourceType"),
    }


class BindEIPResponseSchema(schema.ResponseSchema):
    """ BindEIP - 将尚未使用的弹性IP绑定到指定的资源
    """

    fields = {}


"""
API: CreateBandwidthPackage

为非共享带宽模式下, 已绑定资源实例的带宽计费弹性IP附加临时带宽包
"""


class CreateBandwidthPackageRequestSchema(schema.RequestSchema):
    """ CreateBandwidthPackage - 为非共享带宽模式下, 已绑定资源实例的带宽计费弹性IP附加临时带宽包
    """

    fields = {
        "Bandwidth": fields.Int(required=True, dump_to="Bandwidth"),
        "CouponId": fields.Str(required=False, dump_to="CouponId"),
        "EIPId": fields.Str(required=True, dump_to="EIPId"),
        "EnableTime": fields.Int(required=False, dump_to="EnableTime"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "TimeRange": fields.Int(required=True, dump_to="TimeRange"),
    }


class CreateBandwidthPackageResponseSchema(schema.ResponseSchema):
    """ CreateBandwidthPackage - 为非共享带宽模式下, 已绑定资源实例的带宽计费弹性IP附加临时带宽包
    """

    fields = {
        "BandwidthPackageId": fields.Str(
            required=False, load_from="BandwidthPackageId"
        )
    }


"""
API: CreateFirewall

创建防火墙
"""


class CreateFirewallRequestSchema(schema.RequestSchema):
    """ CreateFirewall - 创建防火墙
    """

    fields = {
        "Name": fields.Str(required=True, dump_to="Name"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Remark": fields.Str(required=False, dump_to="Remark"),
        "Rule": fields.List(fields.Str()),
        "Tag": fields.Str(required=False, dump_to="Tag"),
    }


class CreateFirewallResponseSchema(schema.ResponseSchema):
    """ CreateFirewall - 创建防火墙
    """

    fields = {"FWId": fields.Str(required=False, load_from="FWId")}


"""
API: DeleteBandwidthPackage

删除弹性IP上已附加带宽包
"""


class DeleteBandwidthPackageRequestSchema(schema.RequestSchema):
    """ DeleteBandwidthPackage - 删除弹性IP上已附加带宽包
    """

    fields = {
        "BandwidthPackageId": fields.Str(
            required=True, dump_to="BandwidthPackageId"
        ),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
    }


class DeleteBandwidthPackageResponseSchema(schema.ResponseSchema):
    """ DeleteBandwidthPackage - 删除弹性IP上已附加带宽包
    """

    fields = {}


"""
API: DeleteFirewall

删除防火墙
"""


class DeleteFirewallRequestSchema(schema.RequestSchema):
    """ DeleteFirewall - 删除防火墙
    """

    fields = {
        "FWId": fields.Str(required=True, dump_to="FWId"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
    }


class DeleteFirewallResponseSchema(schema.ResponseSchema):
    """ DeleteFirewall - 删除防火墙
    """

    fields = {}


"""
API: DescribeBandwidthPackage

获取某地域下的带宽包信息
"""


class DescribeBandwidthPackageRequestSchema(schema.RequestSchema):
    """ DescribeBandwidthPackage - 获取某地域下的带宽包信息
    """

    fields = {
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "Offset": fields.Int(required=False, dump_to="Offset"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
    }


class DescribeBandwidthPackageResponseSchema(schema.ResponseSchema):
    """ DescribeBandwidthPackage - 获取某地域下的带宽包信息
    """

    fields = {
        "DataSets": fields.List(
            models.UnetBandwidthPackageSetSchema(),
            required=False,
            load_from="DataSets",
        ),
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
    }


"""
API: DescribeBandwidthUsage

获取带宽用量信息
"""


class DescribeBandwidthUsageRequestSchema(schema.RequestSchema):
    """ DescribeBandwidthUsage - 获取带宽用量信息
    """

    fields = {
        "EIPIds": fields.List(fields.Str()),
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "OffSet": fields.Int(required=False, dump_to="OffSet"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
    }


class DescribeBandwidthUsageResponseSchema(schema.ResponseSchema):
    """ DescribeBandwidthUsage - 获取带宽用量信息
    """

    fields = {
        "EIPSet": fields.List(
            models.UnetBandwidthUsageEIPSetSchema(),
            required=False,
            load_from="EIPSet",
        ),
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
    }


"""
API: DescribeEIP

获取弹性IP信息
"""


class DescribeEIPRequestSchema(schema.RequestSchema):
    """ DescribeEIP - 获取弹性IP信息
    """

    fields = {
        "EIPIds": fields.List(fields.Str()),
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "Offset": fields.Int(required=False, dump_to="Offset"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
    }


class DescribeEIPResponseSchema(schema.ResponseSchema):
    """ DescribeEIP - 获取弹性IP信息
    """

    fields = {
        "EIPSet": fields.List(
            models.UnetEIPSetSchema(), required=False, load_from="EIPSet"
        ),
        "TotalBandwidth": fields.Int(
            required=False, load_from="TotalBandwidth"
        ),
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
    }


"""
API: DescribeFirewall

获取防火墙组信息
"""


class DescribeFirewallRequestSchema(schema.RequestSchema):
    """ DescribeFirewall - 获取防火墙组信息
    """

    fields = {
        "FWId": fields.Str(required=False, dump_to="FWId"),
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "Offset": fields.Int(required=False, dump_to="Offset"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "ResourceId": fields.Str(required=False, dump_to="ResourceId"),
        "ResourceType": fields.Str(required=False, dump_to="ResourceType"),
    }


class DescribeFirewallResponseSchema(schema.ResponseSchema):
    """ DescribeFirewall - 获取防火墙组信息
    """

    fields = {
        "DataSet": fields.List(
            models.FirewallDataSetSchema(), required=False, load_from="DataSet"
        ),
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
    }


"""
API: DescribeFirewallResource

获取防火墙组所绑定资源的外网IP
"""


class DescribeFirewallResourceRequestSchema(schema.RequestSchema):
    """ DescribeFirewallResource - 获取防火墙组所绑定资源的外网IP
    """

    fields = {
        "FWId": fields.Str(required=True, dump_to="FWId"),
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "Offset": fields.Int(required=False, dump_to="Offset"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
    }


class DescribeFirewallResourceResponseSchema(schema.ResponseSchema):
    """ DescribeFirewallResource - 获取防火墙组所绑定资源的外网IP
    """

    fields = {
        "ResourceSet": fields.List(
            models.ResourceSetSchema(), required=False, load_from="ResourceSet"
        ),
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
    }


"""
API: DescribeShareBandwidth

获取共享带宽信息
"""


class DescribeShareBandwidthRequestSchema(schema.RequestSchema):
    """ DescribeShareBandwidth - 获取共享带宽信息
    """

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "ShareBandwidthIds": fields.List(fields.Str()),
    }


class DescribeShareBandwidthResponseSchema(schema.ResponseSchema):
    """ DescribeShareBandwidth - 获取共享带宽信息
    """

    fields = {
        "DataSet": fields.List(
            models.UnetShareBandwidthSetSchema(),
            required=False,
            load_from="DataSet",
        ),
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
    }


"""
API: DescribeVIP

获取内网VIP详细信息
"""


class DescribeVIPRequestSchema(schema.RequestSchema):
    """ DescribeVIP - 获取内网VIP详细信息
    """

    fields = {
        "BusinessId": fields.Str(required=False, dump_to="BusinessId"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "SubnetId": fields.Str(required=False, dump_to="SubnetId"),
        "Tag": fields.Str(required=False, dump_to="Tag"),
        "VPCId": fields.Str(required=False, dump_to="VPCId"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class DescribeVIPResponseSchema(schema.ResponseSchema):
    """ DescribeVIP - 获取内网VIP详细信息
    """

    fields = {
        "DataSet": fields.List(
            fields.Str(), required=False, load_from="DataSet"
        ),
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
        "VIPSet": fields.List(
            models.VIPDetailSetSchema(), required=False, load_from="VIPSet"
        ),
    }


"""
API: DisassociateEIPWithShareBandwidth

将EIP移出共享带宽
"""


class DisassociateEIPWithShareBandwidthRequestSchema(schema.RequestSchema):
    """ DisassociateEIPWithShareBandwidth - 将EIP移出共享带宽
    """

    fields = {
        "Bandwidth": fields.Int(required=True, dump_to="Bandwidth"),
        "EIPIds": fields.List(fields.Str()),
        "PayMode": fields.Str(required=False, dump_to="PayMode"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "ShareBandwidthId": fields.Str(
            required=True, dump_to="ShareBandwidthId"
        ),
    }


class DisassociateEIPWithShareBandwidthResponseSchema(schema.ResponseSchema):
    """ DisassociateEIPWithShareBandwidth - 将EIP移出共享带宽
    """

    fields = {}


"""
API: GetEIPPayMode

获取弹性IP计费模式
"""


class GetEIPPayModeRequestSchema(schema.RequestSchema):
    """ GetEIPPayMode - 获取弹性IP计费模式
    """

    fields = {
        "EIPId": fields.List(fields.Str()),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
    }


class GetEIPPayModeResponseSchema(schema.ResponseSchema):
    """ GetEIPPayMode - 获取弹性IP计费模式
    """

    fields = {
        "EIPPayMode": fields.List(
            models.EIPPayModeSetSchema(), required=False, load_from="EIPPayMode"
        )
    }


"""
API: GetEIPPrice

获取弹性IP价格
"""


class GetEIPPriceRequestSchema(schema.RequestSchema):
    """ GetEIPPrice - 获取弹性IP价格
    """

    fields = {
        "Bandwidth": fields.Int(required=True, dump_to="Bandwidth"),
        "ChargeType": fields.Str(required=False, dump_to="ChargeType"),
        "OperatorName": fields.Str(required=True, dump_to="OperatorName"),
        "PayMode": fields.Str(required=False, dump_to="PayMode"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Quantity": fields.Int(required=False, dump_to="Quantity"),
        "Region": fields.Str(required=True, dump_to="Region"),
    }


class GetEIPPriceResponseSchema(schema.ResponseSchema):
    """ GetEIPPrice - 获取弹性IP价格
    """

    fields = {
        "PriceSet": fields.List(
            models.EIPPriceDetailSetSchema(),
            required=False,
            load_from="PriceSet",
        )
    }


"""
API: GetEIPUpgradePrice

获取弹性IP带宽改动价格
"""


class GetEIPUpgradePriceRequestSchema(schema.RequestSchema):
    """ GetEIPUpgradePrice - 获取弹性IP带宽改动价格
    """

    fields = {
        "Bandwidth": fields.Int(required=True, dump_to="Bandwidth"),
        "EIPId": fields.Str(required=True, dump_to="EIPId"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
    }


class GetEIPUpgradePriceResponseSchema(schema.ResponseSchema):
    """ GetEIPUpgradePrice - 获取弹性IP带宽改动价格
    """

    fields = {"Price": fields.Float(required=False, load_from="Price")}


"""
API: GrantFirewall

将防火墙应用到资源上
"""


class GrantFirewallRequestSchema(schema.RequestSchema):
    """ GrantFirewall - 将防火墙应用到资源上
    """

    fields = {
        "FWId": fields.Str(required=True, dump_to="FWId"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "ResourceId": fields.Str(required=True, dump_to="ResourceId"),
        "ResourceType": fields.Str(required=True, dump_to="ResourceType"),
    }


class GrantFirewallResponseSchema(schema.ResponseSchema):
    """ GrantFirewall - 将防火墙应用到资源上
    """

    fields = {}


"""
API: ModifyEIPBandwidth

调整弹性IP的外网带宽
"""


class ModifyEIPBandwidthRequestSchema(schema.RequestSchema):
    """ ModifyEIPBandwidth - 调整弹性IP的外网带宽
    """

    fields = {
        "Bandwidth": fields.Int(required=True, dump_to="Bandwidth"),
        "EIPId": fields.Str(required=True, dump_to="EIPId"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
    }


class ModifyEIPBandwidthResponseSchema(schema.ResponseSchema):
    """ ModifyEIPBandwidth - 调整弹性IP的外网带宽
    """

    fields = {}


"""
API: ModifyEIPWeight

修改弹性IP的外网出口权重
"""


class ModifyEIPWeightRequestSchema(schema.RequestSchema):
    """ ModifyEIPWeight - 修改弹性IP的外网出口权重
    """

    fields = {
        "EIPId": fields.Str(required=True, dump_to="EIPId"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Weight": fields.Int(required=True, dump_to="Weight"),
    }


class ModifyEIPWeightResponseSchema(schema.ResponseSchema):
    """ ModifyEIPWeight - 修改弹性IP的外网出口权重
    """

    fields = {}


"""
API: ReleaseEIP

释放弹性IP资源, 所释放弹性IP必须为非绑定状态.
"""


class ReleaseEIPRequestSchema(schema.RequestSchema):
    """ ReleaseEIP - 释放弹性IP资源, 所释放弹性IP必须为非绑定状态.
    """

    fields = {
        "EIPId": fields.Str(required=True, dump_to="EIPId"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
    }


class ReleaseEIPResponseSchema(schema.ResponseSchema):
    """ ReleaseEIP - 释放弹性IP资源, 所释放弹性IP必须为非绑定状态.
    """

    fields = {}


"""
API: ReleaseShareBandwidth

关闭共享带宽
"""


class ReleaseShareBandwidthRequestSchema(schema.RequestSchema):
    """ ReleaseShareBandwidth - 关闭共享带宽
    """

    fields = {
        "EIPBandwidth": fields.Int(required=True, dump_to="EIPBandwidth"),
        "PayMode": fields.Str(required=False, dump_to="PayMode"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "ShareBandwidthId": fields.Str(
            required=True, dump_to="ShareBandwidthId"
        ),
    }


class ReleaseShareBandwidthResponseSchema(schema.ResponseSchema):
    """ ReleaseShareBandwidth - 关闭共享带宽
    """

    fields = {}


"""
API: ReleaseVIP

释放VIP资源
"""


class ReleaseVIPRequestSchema(schema.RequestSchema):
    """ ReleaseVIP - 释放VIP资源
    """

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "VIPId": fields.Str(required=True, dump_to="VIPId"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class ReleaseVIPResponseSchema(schema.ResponseSchema):
    """ ReleaseVIP - 释放VIP资源
    """

    fields = {}


"""
API: ResizeShareBandwidth

调整共享带宽的带宽值
"""


class ResizeShareBandwidthRequestSchema(schema.RequestSchema):
    """ ResizeShareBandwidth - 调整共享带宽的带宽值
    """

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "ShareBandwidth": fields.Int(required=True, dump_to="ShareBandwidth"),
        "ShareBandwidthId": fields.Str(
            required=True, dump_to="ShareBandwidthId"
        ),
    }


class ResizeShareBandwidthResponseSchema(schema.ResponseSchema):
    """ ResizeShareBandwidth - 调整共享带宽的带宽值
    """

    fields = {}


"""
API: SetEIPPayMode

设置弹性IP计费模式, 切换时会涉及付费/退费.
"""


class SetEIPPayModeRequestSchema(schema.RequestSchema):
    """ SetEIPPayMode - 设置弹性IP计费模式, 切换时会涉及付费/退费.
    """

    fields = {
        "Bandwidth": fields.Int(required=True, dump_to="Bandwidth"),
        "EIPId": fields.Str(required=True, dump_to="EIPId"),
        "PayMode": fields.Str(required=True, dump_to="PayMode"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
    }


class SetEIPPayModeResponseSchema(schema.ResponseSchema):
    """ SetEIPPayMode - 设置弹性IP计费模式, 切换时会涉及付费/退费.
    """

    fields = {}


"""
API: UnBindEIP

将弹性IP从资源上解绑
"""


class UnBindEIPRequestSchema(schema.RequestSchema):
    """ UnBindEIP - 将弹性IP从资源上解绑
    """

    fields = {
        "EIPId": fields.Str(required=True, dump_to="EIPId"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "ResourceId": fields.Str(required=True, dump_to="ResourceId"),
        "ResourceType": fields.Str(required=True, dump_to="ResourceType"),
    }


class UnBindEIPResponseSchema(schema.ResponseSchema):
    """ UnBindEIP - 将弹性IP从资源上解绑
    """

    fields = {}


"""
API: UpdateEIPAttribute

更新弹性IP名称，业务组，备注等属性字段
"""


class UpdateEIPAttributeRequestSchema(schema.RequestSchema):
    """ UpdateEIPAttribute - 更新弹性IP名称，业务组，备注等属性字段
    """

    fields = {
        "EIPId": fields.Str(required=True, dump_to="EIPId"),
        "Name": fields.Str(required=False, dump_to="Name"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Remark": fields.Str(required=False, dump_to="Remark"),
        "Tag": fields.Str(required=False, dump_to="Tag"),
    }


class UpdateEIPAttributeResponseSchema(schema.ResponseSchema):
    """ UpdateEIPAttribute - 更新弹性IP名称，业务组，备注等属性字段
    """

    fields = {}


"""
API: UpdateFirewall

更新防火墙规则
"""


class UpdateFirewallRequestSchema(schema.RequestSchema):
    """ UpdateFirewall - 更新防火墙规则
    """

    fields = {
        "FWId": fields.Str(required=True, dump_to="FWId"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Rule": fields.List(fields.Str()),
    }


class UpdateFirewallResponseSchema(schema.ResponseSchema):
    """ UpdateFirewall - 更新防火墙规则
    """

    fields = {"FWId": fields.Str(required=False, load_from="FWId")}


"""
API: UpdateFirewallAttribute

更新防火墙规则
"""


class UpdateFirewallAttributeRequestSchema(schema.RequestSchema):
    """ UpdateFirewallAttribute - 更新防火墙规则
    """

    fields = {
        "FWId": fields.Str(required=True, dump_to="FWId"),
        "Name": fields.Str(required=False, dump_to="Name"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Remark": fields.Str(required=False, dump_to="Remark"),
        "Tag": fields.Str(required=False, dump_to="Tag"),
    }


class UpdateFirewallAttributeResponseSchema(schema.ResponseSchema):
    """ UpdateFirewallAttribute - 更新防火墙规则
    """

    fields = {}
