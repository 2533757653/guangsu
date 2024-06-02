class ProductionOrder:   #需求类
    def __init__(self, order_number, quantity, start_date, end_date, material):
        self.order_number = order_number
        self.quantity = quantity
        self.start_date = start_date
        self.end_date = end_date
        self.material = material

class ProcessRoute:  #生产工艺类
    def __init__(self, material_code, resource_name, resource_quantity, setup_time):
        self.material_code = material_code
        self.resource_name = resource_name
        self.resource_quantity = resource_quantity
        self.setup_time = setup_time

class ResourceCalendar:   #资源类
    def __init__(self, resource_name, resource_quantity):
        self.resource_name = resource_name
        self.resource_quantity = resource_quantity

#这边会面临一个问题，那就是每个工艺包含多个生产冲程
    
    
def generate_gantt_chart(production_orders, process_routes, resource_calendars):
    # 将资源按照优先级排序（假设资源越多，优先级越高）
    resource_calendars.sort(key=lambda x: x.resource_quantity, reverse=True)
    
    # 初始化甘特图字典
    gantt_chart = {}
    
    for order in production_orders:
        # 获取生产工单相关的工艺路线
        relevant_process_routes = [route for route in process_routes if route.material_code == order.material]
        
        # 初始化当前工单的开始时间为工单的开始时间
        current_time = order.start_date
        
        # 为当前工单查找可用资源
        for resource_calendar in resource_calendars:
            # 查找当前资源对应的工艺路线
            relevant_process_route = next((route for route in relevant_process_routes if route.resource_name == resource_calendar.resource_name), None)
            
            if relevant_process_route:
                # 计算当前工艺路线的结束时间
                setup_time = relevant_process_route.setup_time
                resource_quantity = min(resource_calendar.resource_quantity, relevant_process_route.resource_quantity)
                process_time = order.quantity / resource_quantity
                
                # 如果资源足够，则安排工序
                if current_time + setup_time <= order.end_date:
                    gantt_chart[order.order_number] = (current_time, current_time + setup_time)
                    current_time += setup_time
                    current_time += process_time
                    
                    # 更新资源日历
                    resource_calendar.resource_quantity -= resource_quantity
                    break  # 安排了工序后，跳出当前资源的循环
    
    return gantt_chart

# 使用示例
production_orders = [...]  # 假设这是你的生产工单列表
process_routes = [...]  # 假设这是你的工艺路线列表
resource_calendars = [...]  # 假设这是你的资源日历列表

gantt_chart = generate_gantt_chart(production_orders, process_routes, resource_calendars)
print(gantt_chart)
