# -*- coding: utf-8 -*-
import copy
import socketserver

import UDP

from core import Tools, Router, ThreadPool


def add_router(**params):
    # 创建一个路由器实例
    router = Router.Router(name=params['name'], ip_address=params['ip'])
    # 向此路由表添加一条新路由信息
    router.get_router_list().add_router_info(data={'target': params['target'],
                                                   'distance': params['distance'],
                                                   'next': params['next']})
    # 保存此路由表
    router.get_router_list().save_router_list()

    # 日志显示
    Tools.show_log(log_data=params['log_show'],
                   data=Tools.get_now_time(0) + '新建路由\n')
    # 路由信息显示
    show_data = Tools.get_now_time(0) + '新建路由\n' + '  路由器名称：' + \
                router.get_router_name() + '　　　　路由器地址：' + router.get_router_ip_address()[0] + ':' + \
                str(router.get_router_ip_address()[1]) + '\n' + '    ' + '路由表：\n' + '    ' + \
                '\n    '.join([router_data['target'] + '    　　　　　' + router_data['distance'] +
                               '    　　　　　' + router_data['next'] for router_data
                               in router.get_router_list().get_router_info()]) + '\n'

    Tools.show_router_info(route_data=params['router_show'], data=show_data)


def update_router(**params):
    # 更新全部路由表

    # 获得相邻路由器表
    all_near_router = Tools.get_all_near_router(Router.ROOT_ROUTER_PATH)
    # 创建线程池
    pool = ThreadPool.Pool(max_workers=2)
    # 设置连接列表
    socket_list = []
    # 全部路由器
    all_router = Tools.get_all_router(Router.ROOT_ROUTER_PATH)
    copy_all_router = copy.deepcopy(all_router)
    # 更新提示
    Tools.show_router_info(route_data=params['router_show'],
                           data=Tools.get_now_time(0) + '\n' +
                                '==============更新路由==============\n')
    # 开始发送
    for router in all_router:
        ip_port = router.get_router_ip_address()
        # 建立多线程UDP服务端
        print("IP_PORT:" + str(ip_port))
        udp_sever = socketserver.ThreadingUDPServer(ip_port, UDP.Sever.Server)
        socket_list.append(udp_sever)
        for near_router in router.get_near_router(all_near_router):
            # 添加子线程
            pool.add_method(method=near_router.send_router_list, sever=udp_sever,
                            host=ip_port[0], port=ip_port[1],
                            path=router.get_router_path() + '/' + near_router.get_router_name() + '.rl')

            Tools.show_router_info(route_data=params['router_show'],
                                   data=Tools.get_now_time(0) +
                                        near_router.get_router_name() + '向' +
                                        router.get_router_name() + '发送了路由表\n')
    # 等待子线程全部运行结束
    pool.wait()
    # 关闭所有连接
    for soc in socket_list:
        soc.server_close()
    # 进行路由表更新
    for router in copy_all_router:
        router.update_router_list()
    # 日志显示
    Tools.show_log(log_data=params['log_show'],
                   data=Tools.get_now_time(0) + '更新路由\n')
    # 路由信息显示
    data1 = Tools.get_now_time(0) + '更新后路由表\n'
    data2 = ''
    for router in copy_all_router:
        data2 = data2 + '  路由器名称：' + \
                router.get_router_name() + '　　　　路由器地址：' + router.get_router_ip_address()[0] + ':' + \
                str(router.get_router_ip_address()[1]) + '\n' + '    ' + '路由表：\n' + '    ' + \
                '\n    '.join([router_data['target'] + '    　　　　　' + str(router_data['distance']) +
                               '    　　　　　' + router_data['next'] for router_data
                               in router.get_router_list().get_router_info()]) + '\n'

    Tools.show_router_info(route_data=params['router_show'],
                           data=data1 + data2)


def update_step_router(**params):
    # 更新全部路由表

    # # 获得相邻路由器表
    # all_near_router = Tools.get_all_near_router(Router.ROOT_ROUTER_PATH)
    # # 创建线程池
    pool = ThreadPool.Pool(max_workers=1)
    # # 设置连接列表
    socket_list = []
    # # 全部路由器
    # all_router = Tools.get_all_router(Router.ROOT_ROUTER_PATH)
    # copy_all_router = copy.deepcopy(all_router)
    # 更新提示
    Tools.show_router_info(route_data=params['router_show'],
                           data=Tools.get_now_time(0) + '\n' +
                                '==============更新路由==============\n')
    # 开始发送
    # for router in Step.all_router:

    Step.update()
    if (Step.step_index >= Step.all_router.__len__()):
        Step.step_index=0
    router = Step.all_router[Step.step_index]
    ip_port = router.get_router_ip_address()
    # 建立多线程UDP服务端
    print("IP_PORT:" + str(ip_port))
    udp_sever = socketserver.ThreadingUDPServer(ip_port, UDP.Sever.Server)
    socket_list.append(udp_sever)
    for near_router in router.get_near_router(Step.all_near_router):
        # 添加子线程
        pool.add_method(method=near_router.send_router_list, sever=udp_sever,
                        host=ip_port[0], port=ip_port[1],
                        path=router.get_router_path() + '/' + near_router.get_router_name() + '.rl')

        Tools.show_router_info(route_data=params['router_show'],
                               data=Tools.get_now_time(0) +
                                    near_router.get_router_name() + '向' +
                                    router.get_router_name() + '发送了路由表\n')
    # 等待子线程全部运行结束
    pool.wait()
    # 关闭所有连接
    for soc in socket_list:
        soc.server_close()
    # 进行路由表更新
    for router in Step.copy_all_router:
        router.update_router_list()
    # 日志显示
    Tools.show_log(log_data=params['log_show'],
                   data=Tools.get_now_time(0) + '更新路由\n')
    # 路由信息显示
    data1 = Tools.get_now_time(0) + '更新后路由表\n'
    data2 = ''
    for router in Step.copy_all_router:
        data2 = data2 + '  路由器名称：' + \
                router.get_router_name() + '　　　　路由器地址：' + router.get_router_ip_address()[0] + ':' + \
                str(router.get_router_ip_address()[1]) + '\n' + '    ' + '路由表：\n' + '    ' + \
                '\n    '.join([router_data['target'] + '    　　　　　' + str(router_data['distance']) +
                               '    　　　　　' + router_data['next'] for router_data
                               in router.get_router_list().get_router_info()]) + '\n'

    Step.step_index = Step.step_index + 1
    Tools.show_router_info(route_data=params['router_show'],
                           data=data1 + data2)



def fault_test(**params):
    Tools.show_router_info(route_data=params['router_show'],
                           data=Tools.get_now_time(0) +
                                '\n==============网络故障==============\n')
    Tools.show_router_info(route_data=params['router_show'],
                           data='  故障网络： ' + params['fault'] + '\n')
    # 使指定网络故障
    for router in Tools.get_all_router(Router.ROOT_ROUTER_PATH):
        sign = 0  # 标志位
        for router_info in [router_info for router_info in router.get_router_list().get_router_info()
                            if (router_info['target'] == params['fault'])
                               and (int(router_info['distance']) == 1)]:
            router_info['distance'] = '16'
            # 路由信息显示
            data = '    路由器名称：' + router.get_router_name() + \
                   '　　　　路由器地址：' + router.get_router_ip_address()[0] + ':' + str(router.get_router_ip_address()[1]) + \
                   '\n' + '    ' + '  路由表：\n' + \
                   '    ' + '\n    '.join([router_data['target'] +
                                           '    　　　　　' + router_data['distance']
                                           + '    　　　　　' + router_data['next']
                                           for router_data in router.get_router_list().get_router_info()]) + '\n'

            Tools.show_router_info(route_data=params['router_show'], data=data)
            sign = 1
            break
        if sign == 1:
            # 保存路由表
            router.get_router_list().save_router_list()
    # 日志显示
    Tools.show_log(log_data=params['log_show'], data=Tools.get_now_time(0) + '网络故障\n')


class Step:
    # 获得相邻路由器表
    all_near_router = Tools.get_all_near_router(Router.ROOT_ROUTER_PATH)
    # 创建线程池
    pool = ThreadPool.Pool(max_workers=2)
    # 设置连接列表
    socket_list = []
    # 全部路由器
    all_router = Tools.get_all_router(Router.ROOT_ROUTER_PATH)
    copy_all_router = copy.deepcopy(all_router)
    step_index = 0

    @classmethod
    def update(cls):
        # 获得相邻路由器表
        cls.all_near_router = Tools.get_all_near_router(Router.ROOT_ROUTER_PATH)
        # 设置连接列表
        cls.socket_list = []
        # 全部路由器
        cls.all_router = Tools.get_all_router(Router.ROOT_ROUTER_PATH)
        cls.copy_all_router = copy.deepcopy(cls.all_router)
        pass
