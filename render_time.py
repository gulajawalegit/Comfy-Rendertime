import time

class RenderTime_Start:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "trigger": ("*",),  # Menerima input apa pun sebagai pemicu
            }
        }

    RETURN_TYPES = ("RENDER_START_TIME",)
    FUNCTION = "start"
    CATEGORY = "utils/timer"
    OUTPUT_NODE = False

    def start(self, trigger):
        start_time = time.time()
        return (start_time,)


class RenderTime_End:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "start_time": ("RENDER_START_TIME",),
                "trigger": ("*",),  # Biasanya sambungkan output akhir (misal: VHS_FILENAMES)
            }
        }

    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("render_time_seconds",)
    FUNCTION = "end"
    CATEGORY = "utils/timer"
    OUTPUT_NODE = False

    def end(self, start_time, trigger):
        end_time = time.time()
        duration = max(0.0, end_time - start_time)
        print(f"✅ Render selesai dalam {duration:.2f} detik")
        return (duration,)


# Pendaftaran node untuk ComfyUI
NODE_CLASS_MAPPINGS = {
    "RenderTime_Start": RenderTime_Start,
    "RenderTime_End": RenderTime_End,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "RenderTime_Start": "⏱️ Render Time (Start)",
    "RenderTime_End": "⏱️ Render Time (End)",
}
