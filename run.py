#!/usr/bin/env python3

from roop import core

if __name__ == '__main__':
    interface = core.run()  # Ensure core.run() returns the Gradio interface object
    interface.launch(share=True)
