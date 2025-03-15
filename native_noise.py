import torch
import numpy as np

class HtaNativeNoise:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "seed": ("INT", {"default": 0, "tooltip": "Seed for noise"}),
                "width": ("INT", {"default": 512, "min": 64, "step": 8, "tooltip": "Width in pixels"}),
                "height": ("INT", {"default": 512, "min": 64, "step": 8, "tooltip": "Height in pixels"})
            }
        }
    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "generate_noise"
    CATEGORY = "HTA"
    DESCRIPTION = "Generates noise directly at the specified resolution for visualization purposes."

    def generate_noise(self, seed, width, height):
        # Create a result tensor that is expected as an image in format (1, H, W, 3)
        result = torch.zeros((1, height, width, 3), dtype=torch.float32)

        # Set the seed and generate noise
        torch.manual_seed(seed)
        r_noise = torch.randn((height, width), dtype=torch.float32)
        torch.manual_seed(seed + 1)
        g_noise = torch.randn((height, width), dtype=torch.float32)
        torch.manual_seed(seed + 2)
        b_noise = torch.randn((height, width), dtype=torch.float32)

        # Function to normalize a tensor to [0,1]
        def normalize_tensor(tensor):
            min_val = tensor.min()
            max_val = tensor.max()
            return (tensor - min_val) / (max_val - min_val + 1e-5)

        r_norm = normalize_tensor(r_noise)
        g_norm = normalize_tensor(g_noise)
        b_norm = normalize_tensor(b_noise)

        result[0, :, :, 0] = r_norm
        result[0, :, :, 1] = g_norm
        result[0, :, :, 2] = b_norm

        # Debug: Output the shape
        print("Generated noise tensor shape:", result.shape)

        return (result,)

NODE_CLASS_MAPPINGS = {"HtaNativeNoise": HtaNativeNoise}
NODE_DISPLAY_NAME_MAPPINGS = {"HtaNativeNoise": "Native Noise"}
