from transitions.extensions import GraphMachine

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
        "dest": "set_name",
        "conditions": "is_going_to_set_name",
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
        "dest": "menu",
        "conditions": "is_going_to_menu",
    },
    #src is set_keyword
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
                #get_fsm("menu").get_graph().draw("fsm.png", prog="dot", format="png")
                return True
            
        return False
    def is_going_to_update(self, event):
        msg = event.message.text
        if(self.state == "menu"):
            if(msg == "update"):
                show_update_msg(event)
                return True
            
        return False
        
    def is_going_to_set_web(self, event):
        msg = event.message.text
        if(self.state == "menu"):
            if(msg == "set web"):
                #print("go to set web")
                #show_web_msg(event)
                return True
        
        return False
    
    def is_going_to_web_acg(self, event):
        msg = event.message.text
        if(self.state == "set_web"):
            if(msg == "acg"):
                print("go to web acg")
                #show_date_msg(event)
                return True
            
        return False
    
    def is_going_to_set_date(self, event):
        msg = event.message.text
        if(self.state == "web_acg"):
            if(msg == "set date"):
                print("go to set date")
                #show_date_msg(event)
                return True
            
        return False
    
    def is_going_to_web_anime1(self, event):
        msg = event.message.text
        if(self.state == "set_web"):
            if(msg == "anime1"):
                print("go to web anime1")
                return True
                #show_name_msg(event)
            if(msg == "show"):
                print("list anime1")
                return True
        return False
    
    def is_going_to_set_name(self, event):
        msg = event.message.text
        if(self.state == "web_anime1" or 
           self.state == "set_date" or
           self.state == "set_name" or
           self.state == "set_keyword" or
           self.state == "update"):
            if(msg == "set name"):
                print("go to set name")
                #show_name_msg(event)
                return True
            if(msg == "add"):
                print("add")
                return
            if(msg == "del"):
                print("del")
                return
        return False
    
    def is_going_to_set_keyword(self, event):
        msg = event.message.text
        if(self.state == "set_date"):
            if(msg == "set keyword"):
                print("go to set keyword")
                return True
            if(msg == "add"):
                print("add")
                return True
            if(msg == "del"):
                print("del")
                #show_keyword_msg(event)
                return True
        return False
    
    def is_going_to_menu(self, event):
        msg = event.message.text
        if(self.state == "set_name" or 
           self.state == "set_keyword" or 
           self.state == "help"):
            if(msg == "menu" or msg == "exit"):
                print("go to menu")
                return True
            if(msg == "search"):
                print("search")
                #show_menu_msg(event)
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

