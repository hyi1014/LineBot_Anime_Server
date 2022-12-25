from transitions.extensions import GraphMachine

import utils
from utils import *

states =[
    "menu",
    "help",
    "update",
    "set_web",
    "web_acg",
    "web_anime1",
    "set_date",
    "set_name",
    "set_update_name",
    "set_keyword",
]
transitions = [
    #src is menu
    {
        "trigger": "advance",
        "source": "menu",
        "dest": "help",
        "conditions": "is_going_to_help",
    },
    {
        "trigger": "advance",
        "source": "menu",
        "dest": "update",
        "conditions": "is_going_to_update",
    },
    {
        "trigger": "advance",
        "source": "menu",
        "dest": "set_web",
        "conditions": "is_going_to_set_web",
    },
    #src is help
    {
        "trigger": "advance",
        "source": "help",
        "dest": "help",
        "conditions": "is_going_to_help",
    },
    {
        "trigger": "advance",
        "source": "help",
        "dest": "menu",
        "conditions": "is_going_to_menu",
    },
    #src is update
    {
        "trigger": "advance",
        "source": "update",
        "dest": "update",
        "conditions": "is_going_to_update",
    },
    {
        "trigger": "advance",
        "source": "update",
        "dest": "set_update_name",
        "conditions": "is_going_to_set_update_name",
    },
    #src is set_update_name
    {
        "trigger": "advance",
        "source": "set_update_name",
        "dest": "set_update_name",
        "conditions": "is_going_to_set_update_name",
    },
    {
        "trigger": "advance",
        "source": "set_update_name",
        "dest": "menu",
        "conditions": "is_going_to_menu",
    },
    #src is set_web
    {
        "trigger": "advance",
        "source": "set_web",
        "dest": "web_acg",
        "conditions": "is_going_to_web_acg",
    },
    {
        "trigger": "advance",
        "source": "set_web",
        "dest": "web_anime1",
        "conditions": "is_going_to_web_anime1",
    },
    {
        "trigger": "advance",
        "source": "set_web",
        "dest": "menu",
        "conditions": "is_going_to_menu"    
    },
    #src is web_acg
    {
        "trigger": "advance",
        "source": "web_acg",
        "dest": "set_date",
        "conditions": "is_going_to_set_date",
    },
    #src is web_anime1
    {
        "trigger": "advance",
        "source": "web_anime1",
        "dest": "set_name",
        "conditions": "is_going_to_set_name",
    },
    #src is set_date
    {
        "trigger": "advance",
        "source": "set_date",
        "dest": "set_date",
        "conditions": "is_going_to_set_date",
    },
    {
        "trigger": "advance",
        "source": "set_date",
        "dest": "set_name",
        "conditions": "is_going_to_set_name",
    },
    {
        "trigger": "advance",
        "source": "set_date",
        "dest": "set_keyword",
        "conditions": "is_going_to_set_keyword",
    },
    {
        "trigger": "advance",
        "source": "set_date",
        "dest": "web_acg",
        "conditions": "is_going_to_web_acg",
    },
    #src is set_name
    {
        "trigger": "advance",
        "source": "set_name",
        "dest": "set_name",
        "conditions": "is_going_to_set_name",
    },
    {
        "trigger": "advance",
        "source": "set_name",
        "dest": "menu",
        "conditions": "is_going_to_menu",
    },
    #src is set_keyword
    {
        "trigger": "advance",
        "source": "set_keyword",
        "dest": "set_keyword",
        "conditions": "is_going_to_set_keyword",
    },
    {
        "trigger": "advance",
        "source": "set_keyword",
        "dest": "menu",
        "conditions": "is_going_to_menu",
    }
]

class FSM(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)
    
    def is_going_to_help(self, event):
        msg = event.message.text
        if(self.state == "menu" or self.state == "help"):
            if(msg == "help"):
                show_help_msg(event)
                return True
            if(msg == "show fsm"):
                #print("show fsm")
                #get_fsm("menu").get_graph().draw("fsm.png", prog="dot", format="png")
                image_message = ImageSendMessage(
                    original_content_url='https://img.istreetview.com/?id=+ol1jTEj&url=3cRltBdhUaYc2lJ275Ez4NhqjMmC+vaqAQ4m3zXbsrDDGm94YNcv67oTZnz1/+E7RvOZg3hVx42wEEqRqNsmpMTL4WuaxktUyU9Jag==',
                    preview_image_url='https://img.istreetview.com/?id=+ol1jTEj&url=3cRltBdhUaYc2lJ275Ez4NhqjMmC+vaqAQ4m3zXbsrDDGm94YNcv67oTZnz1/+E7RvOZg3hVx42wEEqRqNsmpMTL4WuaxktUyU9Jag=='
                )
                line_bot_api.reply_message(event.reply_token, image_message)
                return True
            
        return False
    def is_going_to_update(self, event):
        msg = event.message.text
        if(self.state == "menu"):
            if(msg == "update"):
                show_update_msg(event)
                return True
        if(self.state == "update"):
            if(msg == "search"):
                search_update(event)
                return True
        return False
        
    def is_going_to_set_web(self, event):
        msg = event.message.text
        if(self.state == "menu"):
            if(msg == "set web"):
                show_set_web_msg(event)
                return True
        
        return False
    
    def is_going_to_web_acg(self, event):
        msg = event.message.text
        if(self.state == "set_web"):
            if(msg == "acg"):
                show_web_acg_msg(event)
                return True
            
        return False
    
    def is_going_to_set_date(self, event):
        msg = event.message.text
        if(self.state == "web_acg"):
            if(msg == "set date"):
                show_set_date_msg(event)
                return True
        if(self.state == "set_date"):
            if(msg.find("set date")>=0):
                set_date(event)
                return True
            if(msg.find("search")>=0):
                search_name(event)
                return True
            
        return False
    
    def is_going_to_web_anime1(self, event):
        msg = event.message.text
        if(self.state == "set_web"):
            if(msg == "anime1"):
                show_web_anime1_msg(event)
                return True
            
        return False
    
    def is_going_to_set_name(self, event):
        msg = event.message.text
        if(self.state =="set_date" or
           self.state == "web_anime1"):
            if(msg == "set name"):
                show_set_name_msg(event)
                return True
            
        if(self.state == "set_name"):
      
            if(msg.find("add")>=0):
                add_name(event)
                return True
    
            if(msg.find("del")>=0):
                del_name(event)
                print("del name")
                return True
            
            if(msg.find("show")>=0):
                show_name_list(event)
                print("show name list")
                return True 
                         
        return False
    
    def is_going_to_set_keyword(self, event):
        msg = event.message.text
        if(self.state == "set_date"):
            if(msg == "set keyword"):
                show_set_keyword_msg(event)
                return True
        if(self.state == "set_keyword"):
            if(msg.find("add")>=0):
                add_keyword(event)
                return True
            if(msg.find("del")>=0):
                del_keyword(event)
                return True
            if(msg.find("show")>=0):
                show_keyword_list(event)
                return True
        return False
    
    def is_going_to_menu(self, event):
        msg = event.message.text
        if(self.state == "set_name" or 
           self.state == "set_keyword" or 
           self.state == "help"):
            if(msg == "menu" or msg == "exit"):
                return True
        if(self.state == "set_update_name"):
            if(msg == "search"):
                search_update(event)
                return True
            
        if(self.state == "set_name"):
            if(msg == "search"):
                search_name(event)
                return True
        if(self.state == "set_keyword"):
            if(msg == "search"):
                search_keyword(event)
                return True
        return False
    
    def is_going_to_set_update_name(self, event):
        msg = event.message.text
        if(self.state == "update"):
            if(msg == "set name"):
                show_set_name_msg(event)
                return True
        if(self.state == "set_update_name"):
            if(msg.find("add")>=0):
                add_name(event)
                return True
            if(msg.find("del")>=0):
                del_name(event)
                return True
            if(msg.find("show")>=0):
                show_name_list(event)
                return True
    
        return False
def get_fsm(init_state):
    #machine_configs
    machine = FSM(
        states = states,
        transitions = transitions,
        initial = init_state,
        auto_transitions = False,
        show_conditions = True,
    )
    return machine

#get_fsm("menu").get_graph().draw("fsm.png", prog="dot", format="png")
