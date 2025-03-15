import torch
import numpy as np
from comfy.sample import prepare_noise

class ShowKSamplerNoise:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "seed": ("INT", {"default": 0, "tooltip": "Seed for noise"}),
                "width": ("INT", {"default": 512, "min": 64, "step": 8, "tooltip": "Width in pixels"}),
                "height": ("INT", {"default": 512, "min": 64, "step": 8, "tooltip": "Height in pixels"}),
                "batch_size": ("INT", {"default": 1, "min": 1, "tooltip": "Batch size"}),
                "noise_resolution": (["full", "latent"], {"default": "full",
                                    "tooltip": "generates noise according to KSampler method"})
            }
        }
    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "generate_noise"
    CATEGORY = "HTA"
    DESCRIPTION = ("generates noise according to KSampler method")

    def generate_noise(self, seed, width, height, batch_size, noise_resolution):

        result = torch.zeros((batch_size, height, width, 3), dtype=torch.float32)

        for b in range(batch_size):

            torch.manual_seed(seed + b * 100)
            if noise_resolution == "full":

                r_noise = torch.randn((height, width), dtype=torch.float32)
                torch.manual_seed(seed + b * 100 + 1)
                g_noise = torch.randn((height, width), dtype=torch.float32)
                torch.manual_seed(seed + b * 100 + 2)
                b_noise = torch.randn((height, width), dtype=torch.float32)
            else:

                r_noise = torch.randn((height, width), dtype=torch.float32)
                torch.manual_seed(seed + b * 100 + 1)
                g_noise = torch.randn((height, width), dtype=torch.float32)
                torch.manual_seed(seed + b * 100 + 2)
                b_noise = torch.randn((height, width), dtype=torch.float32)

            def normalize_tensor(tensor):
                min_val = tensor.min()
                max_val = tensor.max()
                return (tensor - min_val) / (max_val - min_val + 1e-5)

            r_norm = normalize_tensor(r_noise)
            g_norm = normalize_tensor(g_noise)
            b_norm = normalize_tensor(b_noise)

            result[b, :, :, 0] = r_norm
            result[b, :, :, 1] = g_norm
            result[b, :, :, 2] = b_norm

        return (result,)

NODE_CLASS_MAPPINGS = {"ShowKSamplerNoise": ShowKSamplerNoise}
NODE_DISPLAY_NAME_MAPPINGS = {"ShowKSamplerNoise": "Show KSampler Noise"}
