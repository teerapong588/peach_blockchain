import os

def initialize_flask_server_debugger_if_needed():
    if os.environ.get("DEBUGGER", "True") == "True":
        import multiprocessing

        if multiprocessing.current_process().pid > 1:
            import debugpy

            DEBUG_PORT = int(os.environ.get("DEBUG_PORT", "10001"))

            debugpy.listen(("0.0.0.0", DEBUG_PORT))
            print("⏳ VS Code debugger can now be attached, press F5 in VS Code ⏳", flush=True)
            debugpy.wait_for_client()
            print("🎉 VS Code debugger attached, enjoy debugging 🎉", flush=True)