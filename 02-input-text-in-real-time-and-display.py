from taipy import Gui

message = "enter a message"

page_content = """
# Getting started with Taipy Gui

Welcome Text : <|{message}|>

<|{message}|input|>

"""
Gui(page_content).run(use_reloader=True)