#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
接受robot的消息通知服务
"""
from harix.rdk.proto.robot_mind import robot_mind_pb2, robot_mind_pb2_grpc
from harix.rdk.proto.common import common_pb2


class RobotMindService(robot_mind_pb2_grpc.RobotMindServiceServicer):

    def __init__(self, callback):
        """
        初始化方法

        :param callback: 反馈函数
        """
        self.callback = callback

    def EnableSkill(self, request, context):
        print("call EnableSkill")
        header = {
            "tenant_id": request.common_req_info.tenant_id,
            "user_id": request.common_req_info.user_id,
            "robot_id": request.common_req_info.robot_id,
            "robot_type": request.common_req_info.robot_type,
            "service_code": request.common_req_info.service_code,
            "seq": request.common_req_info.seq
        }

        common_resp_info = common_pb2.CommonRspInfo(
            err_code=0
        )
        return robot_mind_pb2.ActionRequest(
            common_rsp_info=common_resp_info
        )


    def HandleAction(self, request, context):

        header = {
            "tenant_id": request.common_req_info.tenant_id,
            "user_id": request.common_req_info.user_id,
            "robot_id": request.common_req_info.robot_id,
            "robot_type": request.common_req_info.robot_type,
            "service_code": request.common_req_info.service_code,
            "seq": request.common_req_info.seq
        }

        self.callback(header, request.id, request.param)

        common_resp_info = common_pb2.CommonRspInfo(
            err_code=0
        )
        return robot_mind_pb2.ActionRequest(
            common_rsp_info=common_resp_info
        )

