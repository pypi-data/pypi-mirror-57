""" Code is generated by ucloud-model, DO NOT EDIT IT. """

from ucloud.core.typesystem import schema, fields
from ucloud.services.pathx.schemas import models


""" PathX API Schema
"""


"""
API: CreateGlobalSSHInstance

创建GlobalSSH实例
"""


class CreateGlobalSSHInstanceRequestSchema(schema.RequestSchema):
    """ CreateGlobalSSHInstance - 创建GlobalSSH实例
    """

    fields = {
        "Area": fields.Str(required=True, dump_to="Area"),
        "AreaCode": fields.Str(required=True, dump_to="AreaCode"),
        "ChargeType": fields.Str(required=False, dump_to="ChargeType"),
        "CouponId": fields.Str(required=False, dump_to="CouponId"),
        "Port": fields.Int(required=True, dump_to="Port"),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "Quantity": fields.Int(required=False, dump_to="Quantity"),
        "Remark": fields.Str(required=False, dump_to="Remark"),
        "TargetIP": fields.Str(required=True, dump_to="TargetIP"),
    }


class CreateGlobalSSHInstanceResponseSchema(schema.ResponseSchema):
    """ CreateGlobalSSHInstance - 创建GlobalSSH实例
    """

    fields = {
        "AcceleratingDomain": fields.Str(
            required=False, load_from="AcceleratingDomain"
        ),
        "InstanceId": fields.Str(required=True, load_from="InstanceId"),
        "Message": fields.Str(required=False, load_from="Message"),
    }


"""
API: DeleteGlobalSSHInstance

删除GlobalSSH实例
"""


class DeleteGlobalSSHInstanceRequestSchema(schema.RequestSchema):
    """ DeleteGlobalSSHInstance - 删除GlobalSSH实例
    """

    fields = {
        "InstanceId": fields.Str(required=True, dump_to="InstanceId"),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
    }


class DeleteGlobalSSHInstanceResponseSchema(schema.ResponseSchema):
    """ DeleteGlobalSSHInstance - 删除GlobalSSH实例
    """

    fields = {"Message": fields.Str(required=False, load_from="Message")}


"""
API: DescribeGlobalSSHArea

获取GlobalSSH覆盖的地区列表 用于控制显示哪些机房地域可以使用SSH特性
"""


class DescribeGlobalSSHAreaRequestSchema(schema.RequestSchema):
    """ DescribeGlobalSSHArea - 获取GlobalSSH覆盖的地区列表 用于控制显示哪些机房地域可以使用SSH特性
    """

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=False, dump_to="Region"),
    }


class DescribeGlobalSSHAreaResponseSchema(schema.ResponseSchema):
    """ DescribeGlobalSSHArea - 获取GlobalSSH覆盖的地区列表 用于控制显示哪些机房地域可以使用SSH特性
    """

    fields = {
        "AreaSet": fields.List(
            models.GlobalSSHAreaSchema(), required=False, load_from="AreaSet"
        ),
        "Message": fields.Str(required=False, load_from="Message"),
    }


"""
API: DescribeGlobalSSHInstance

获取GlobalSSH实例列表（传实例ID获取单个实例信息，不传获取项目下全部实例）
"""


class DescribeGlobalSSHInstanceRequestSchema(schema.RequestSchema):
    """ DescribeGlobalSSHInstance - 获取GlobalSSH实例列表（传实例ID获取单个实例信息，不传获取项目下全部实例）
    """

    fields = {
        "InstanceId": fields.Str(required=False, dump_to="InstanceId"),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
    }


class DescribeGlobalSSHInstanceResponseSchema(schema.ResponseSchema):
    """ DescribeGlobalSSHInstance - 获取GlobalSSH实例列表（传实例ID获取单个实例信息，不传获取项目下全部实例）
    """

    fields = {
        "InstanceSet": fields.List(
            models.GlobalSSHInfoSchema(),
            required=False,
            load_from="InstanceSet",
        )
    }


"""
API: ModifyGlobalSSHPort

修改GlobalSSH端口
"""


class ModifyGlobalSSHPortRequestSchema(schema.RequestSchema):
    """ ModifyGlobalSSHPort - 修改GlobalSSH端口
    """

    fields = {
        "InstanceId": fields.Str(required=True, dump_to="InstanceId"),
        "Port": fields.Int(required=True, dump_to="Port"),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
    }


class ModifyGlobalSSHPortResponseSchema(schema.ResponseSchema):
    """ ModifyGlobalSSHPort - 修改GlobalSSH端口
    """

    fields = {"Message": fields.Str(required=False, load_from="Message")}


"""
API: ModifyGlobalSSHRemark

修改GlobalSSH备注
"""


class ModifyGlobalSSHRemarkRequestSchema(schema.RequestSchema):
    """ ModifyGlobalSSHRemark - 修改GlobalSSH备注
    """

    fields = {
        "InstanceId": fields.Str(required=True, dump_to="InstanceId"),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "Remark": fields.Str(required=False, dump_to="Remark"),
    }


class ModifyGlobalSSHRemarkResponseSchema(schema.ResponseSchema):
    """ ModifyGlobalSSHRemark - 修改GlobalSSH备注
    """

    fields = {"Message": fields.Str(required=False, load_from="Message")}
